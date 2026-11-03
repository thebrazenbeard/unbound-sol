#!/usr/bin/env python3
"""Non-destructive Portal/Project Runner wheel qualification.

This tool never changes an existing Python installation, PATH, launcher,
service, or repository. It can snapshot sanitized package versions, stage a
*new* offline virtual environment, and verify a chosen staged interpreter.
An operator must separately authorize any launcher cutover and rollback.
"""

from __future__ import annotations

import argparse
from email.parser import Parser
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import unicodedata
import venv
import zipfile


PROBE = r"""
import importlib.metadata as metadata
import importlib.resources as resources
import json
from pathlib import Path
import portal
import runner
import sys

prefix = Path(sys.prefix).resolve()
modules = [Path(portal.__file__).resolve(), Path(runner.__file__).resolve()]
schema = resources.files('runner._schemas').joinpath('worker.schema.json')
parsed = json.loads(schema.read_text(encoding='utf-8'))
print(json.dumps({
    'virtual_environment': sys.prefix != sys.base_prefix,
    'all_modules_under_prefix': all(p.is_relative_to(prefix) for p in modules),
    'portal_version': metadata.version('portal-coordinator'),
    'runner_version': metadata.version('project-runner'),
    'worker_schema_valid_shape': isinstance(parsed, dict)
        and isinstance(parsed.get('required'), list),
}, sort_keys=True))
"""

SNAPSHOT = r"""
import importlib.metadata as metadata
import json
import re
import sys

packages = {}
for dist in metadata.distributions():
    name = dist.metadata.get('Name')
    version = dist.version
    if (name and version and re.fullmatch(r'[A-Za-z0-9_.-]{1,120}', name)
            and re.fullmatch(r'[A-Za-z0-9_.+!~-]{1,120}', version)):
        packages[name.lower().replace('_', '-')] = version
print(json.dumps({
    'schema': 'PORTAL_RUNNER_REDACTED_INSTALLED_SNAPSHOT_V1',
    'freeze_equivalent': [f'{name}=={packages[name]}' for name in sorted(packages)],
    'note': 'Version-only snapshot; interpreter, paths, VCS URLs and credentials omitted.',
}, sort_keys=True))
"""


class HostCustodyHold(ValueError):
    """No OS-protected staging root or separate host identity was established."""


def _safe_subprocess_env() -> dict[str, str]:
    # Inherited pip options such as PIP_TARGET/PIP_PREFIX can redirect an
    # apparently isolated venv installation to an unrelated filesystem path.
    # This is a *staging* boundary, not a sandbox for malicious wheel code.
    env = {key: value for key, value in os.environ.items()
           if not key.upper().startswith(("PIP_", "PYTHON"))
           and key.upper() not in {"VIRTUAL_ENV", "__PYVENV_LAUNCHER__"}}
    env["PIP_CONFIG_FILE"] = os.devnull
    env["PYTHONNOUSERSITE"] = "1"
    return env


def _run(args: list[str], *, limit_seconds: int = 90) -> str:
    proc = subprocess.run(
        args, capture_output=True, text=True, encoding="utf-8",
        errors="replace", timeout=limit_seconds, check=False,
        env=_safe_subprocess_env(),
    )
    if proc.returncode:
        raise RuntimeError(f"qualification command failed ({proc.returncode}): {args[1:3]}")
    return proc.stdout


def _digest(path: Path) -> str:
    with path.open("rb") as stream:
        hasher = hashlib.sha256()
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _wheel_members(path: Path) -> set[str]:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if len(names) != len(set(names)):
            raise ValueError("wheel repeats a ZIP member")
        result: set[str] = set()
        seen: set[str] = set()
        reserved = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)),
                    *(f"lpt{i}" for i in range(1, 10))}
        for name in names:
            # Treat wheel members as cross-platform install targets. A case- or
            # Unicode-normalization alias collides on Windows even if ZIP
            # member spellings differ. Reject traversal, drive/ADS, and
            # backslash aliases before considering wheel ownership.
            if (not name or name.startswith("/") or "\\" in name or ":" in name
                    or "\x00" in name):
                raise ValueError("unsafe wheel member path")
            parts = name.rstrip("/").split("/")
            if any(not part or part in {".", ".."} or part.rstrip(" .") != part
                   for part in parts):
                raise ValueError("unsafe wheel member path")
            normalized = "/".join(unicodedata.normalize("NFC", p).casefold() for p in parts)
            segments = normalized.split("/")
            if any(p.split(".")[0] in reserved for p in segments):
                raise ValueError("unsafe Windows-reserved wheel member path")
            # PEP 427 .data/{purelib,platlib,...} members are relocated by pip.
            # Refuse them until an independently tested target-path resolver is
            # available; otherwise comparing archive names can miss collisions.
            if any(p.endswith(".data") for p in segments):
                raise ValueError("relocated wheel .data entries require separate qualification")
            if normalized in seen:
                raise ValueError("wheel repeats a normalized install path")
            seen.add(normalized)
            if not any(p.endswith(".dist-info") for p in normalized.split("/")):
                result.add(normalized)
        return result


def _require_wheel_metadata_without_direct_refs(path: Path) -> None:
    """Refuse pip requirements which bypass the supplied offline wheelhouse."""
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist()
                 if name.count("/") == 1 and name.endswith(".dist-info/METADATA")]
        if len(names) != 1 or archive.getinfo(names[0]).file_size > (1 << 20):
            raise ValueError("missing or oversized wheel metadata")
        metadata = Parser().parsestr(archive.read(names[0]).decode("utf-8", "strict"))
        for requirement in metadata.get_all("Requires-Dist", []):
            if "@" in requirement or "://" in requirement or "file:" in requirement.lower():
                raise ValueError("direct-reference wheel dependency escapes offline closure")


def validate_wheels(portal: Path, runner: Path, portal_sha: str, runner_sha: str) -> dict[str, str]:
    if not portal.is_file() or not runner.is_file():
        raise ValueError("both wheel files must exist")
    for path, expected in ((portal, portal_sha), (runner, runner_sha)):
        if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
            raise ValueError("wheel checksum must be 64 lowercase SHA-256 characters")
        if _digest(path) != expected:
            raise ValueError("wheel SHA-256 mismatch")
    overlap = _wheel_members(portal) & _wheel_members(runner)
    if overlap:
        raise ValueError("Portal and Runner wheels overwrite the same application path")
    return {"portal_sha256": portal_sha, "runner_sha256": runner_sha}


def stage_private_wheelhouse(candidate: Path, portal: Path, runner: Path,
                             portal_sha: str, runner_sha: str,
                             dependencies: Path,
                             parent_identity: tuple[int, int]) -> tuple[Path, list[Path]]:
    """Snapshot wheel *bytes* before venv creation, then install only copies.

    This closes source-path replacement between checksum validation and pip.
    Files protected only by the calling OS identity are NOT a defense against
    a malicious process with that same identity; host ACL custody is separate.
    """
    if require_private_stage_parent(candidate) != parent_identity:
        raise ValueError("candidate parent identity changed before stage")
    candidate.mkdir(mode=0o700)
    private = candidate / ".qualification-wheels"
    private.mkdir(mode=0o700)

    def copy_exclusive(source: Path) -> Path:
        if source.is_symlink() or not source.is_file() or source.suffix.lower() != ".whl":
            raise ValueError("unsafe wheelhouse entry")
        destination = private / source.name
        with source.open("rb") as incoming, destination.open("xb") as outgoing:
            shutil.copyfileobj(incoming, outgoing, length=1 << 20)
        # The copied bytes, not the original mutable source path, are the
        # installation input. We never remove or overwrite a staged file.
        destination.chmod(0o400)
        return destination

    copied_portal = copy_exclusive(portal)
    copied_runner = copy_exclusive(runner)
    validate_wheels(copied_portal, copied_runner, portal_sha, runner_sha)
    staged_wheels = [copied_portal, copied_runner]

    direct_names = {portal.name.casefold(), runner.name.casefold()}
    seen_names = set(direct_names)
    for entry in sorted(dependencies.iterdir(), key=lambda p: p.name.casefold()):
        if entry.suffix.lower() != ".whl":
            continue
        if entry.name.casefold() in direct_names:
            continue
        if entry.name.casefold() in seen_names:
            raise ValueError("duplicate case-folded wheelhouse filename")
        seen_names.add(entry.name.casefold())
        staged_dependency = copy_exclusive(entry)
        _wheel_members(staged_dependency)
        staged_wheels.append(staged_dependency)
    for staged_wheel in staged_wheels:
        _require_wheel_metadata_without_direct_refs(staged_wheel)
    return private, staged_wheels


def require_unused_candidate(path: Path) -> Path:
    if not path.is_absolute():
        raise ValueError("candidate virtual environment path must be absolute")
    resolved = path.resolve(strict=False)
    if resolved.exists() or resolved == Path.home().resolve() or resolved == Path(resolved.anchor):
        raise ValueError("candidate path must be unused and not a broad system/user root")
    if any(parent.is_symlink() for parent in (path, *path.parents)):
        raise ValueError("candidate path traverses a symbolic link")
    return resolved


def require_private_stage_parent(candidate: Path) -> tuple[int, int]:
    """Constrain normal staging to a user-owned private parent directory.

    This detects path substitutions between preflight and staging, but is not
    same-user malicious-process confinement: that requires host path custody.
    """
    parent = candidate.parent
    if parent.resolve(strict=True) != parent or candidate.is_symlink() or candidate.exists():
        raise ValueError("candidate parent changed or candidate already exists")
    info = parent.stat()
    if not stat.S_ISDIR(info.st_mode):
        raise ValueError("candidate parent is not a directory")
    if os.name != "nt":
        if info.st_uid != os.geteuid() or (stat.S_IMODE(info.st_mode) & 0o077):
            raise ValueError("candidate parent requires private user ownership and mode 0700")
    # Windows ACL custody is not established by portable st_mode metadata.
    return info.st_dev, info.st_ino


def probe_python(python: Path) -> dict[str, object]:
    if not python.is_file():
        raise ValueError("specified interpreter does not exist")
    result = json.loads(_run([str(python), "-I", "-c", PROBE]))
    if (
        result.get("virtual_environment") is not True
        or result.get("all_modules_under_prefix") is not True
        or result.get("worker_schema_valid_shape") is not True
        or result.get("portal_version") != "0.2.0"
        or result.get("runner_version") != "0.1.0"
    ):
        raise ValueError("installed source identity, package version, or schema qualification HOLD")
    scripts = python.parent
    suffix = ".exe" if sys.platform == "win32" else ""
    for name in ("portal", "project-runner"):
        executable = scripts / (name + suffix)
        if not executable.is_file():
            raise ValueError(f"missing installed CLI {name}")
        _run([str(executable), "--help"], limit_seconds=30)
    return {"status": "SOURCE_PACKAGE_SMOKE_PASS", **result,
            "authority": "NO_HOST_OR_EXECUTION_AUTHORIZATION"}


def sanitized_snapshot(python: Path, destination: Path) -> None:
    if not python.is_file() or not destination.is_absolute() or destination.exists():
        raise ValueError("snapshot requires an existing interpreter and unused absolute destination")
    data = json.loads(_run([str(python), "-I", "-c", SNAPSHOT]))
    # Retain only version names; never persist pip freeze's potentially tokenized URLs.
    allowed = {"schema", "freeze_equivalent", "note"}
    if set(data) != allowed or not isinstance(data["freeze_equivalent"], list):
        raise ValueError("unexpected snapshot shape")
    if (data["schema"] != "PORTAL_RUNNER_REDACTED_INSTALLED_SNAPSHOT_V1"
            or data["note"] != "Version-only snapshot; interpreter, paths, VCS URLs and credentials omitted."):
        raise ValueError("unsafe snapshot metadata")
    import re
    if any(not isinstance(item, str) or
           re.fullmatch(r"[A-Za-z0-9_.-]{1,120}==[A-Za-z0-9_.+!~-]{1,120}", item) is None
           for item in data["freeze_equivalent"]):
        raise ValueError("unsafe snapshot version entry")
    with destination.open("x", encoding="utf-8") as out:
        json.dump(data, out, indent=2, sort_keys=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    snapshot = sub.add_parser("snapshot", help="private, version-only installed inventory")
    snapshot.add_argument("--python", type=Path, required=True)
    snapshot.add_argument("--output", type=Path, required=True)
    verify = sub.add_parser("verify", help="read-only isolated installed-wheel check")
    verify.add_argument("--python", type=Path, required=True)
    stage = sub.add_parser("stage", help="create only a new OFFLINE candidate venv")
    stage.add_argument("--candidate-dir", type=Path, required=True)
    stage.add_argument("--portal-wheel", type=Path, required=True)
    stage.add_argument("--runner-wheel", type=Path, required=True)
    stage.add_argument("--portal-sha256", required=True)
    stage.add_argument("--runner-sha256", required=True)
    stage.add_argument("--wheelhouse", type=Path, required=True)
    stage.add_argument(
        "--disposable-test-only", action="store_true",
        help="explicit untrusted offline lab staging; same-user race risk remains",
    )
    args = parser.parse_args(argv)
    try:
        if args.mode == "snapshot":
            sanitized_snapshot(args.python, args.output)
            result: dict[str, object] = {"status": "PRIVATE_SANITIZED_SNAPSHOT_WRITTEN"}
        elif args.mode == "verify":
            result = probe_python(args.python)
        else:
            # A caller-owned path and a pure-Python venv builder cannot prove
            # absence of concurrent same-UID symlink/junction replacement.
            # Default is a pre-write HOLD until a host-owned separate-identity
            # staging capability is supplied outside this source-only tool.
            if not args.disposable_test_only:
                raise HostCustodyHold("no protected staging custody capability")
            candidate = require_unused_candidate(args.candidate_dir)
            parent_identity = require_private_stage_parent(candidate)
            if not args.wheelhouse.is_dir():
                raise ValueError("offline dependency wheelhouse missing")
            checks = validate_wheels(args.portal_wheel, args.runner_wheel,
                                     args.portal_sha256, args.runner_sha256)
            private, staged_wheels = stage_private_wheelhouse(
                candidate, args.portal_wheel, args.runner_wheel,
                args.portal_sha256, args.runner_sha256, args.wheelhouse,
                parent_identity)
            if (candidate.parent.stat().st_dev, candidate.parent.stat().st_ino) != parent_identity:
                raise ValueError("candidate parent identity changed during stage")
            if candidate.is_symlink() or candidate.resolve(strict=True) != candidate:
                raise ValueError("candidate identity changed during stage")
            venv.EnvBuilder(with_pip=True, system_site_packages=False).create(candidate)
            python = candidate / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
            _run([str(python), "-m", "pip", "--isolated", "install",
                  "--no-index", "--no-user", "--no-deps", "--only-binary=:all:",
                  "--prefix", str(candidate),
                  *[str(path) for path in staged_wheels]], limit_seconds=180)
            _run([str(python), "-m", "pip", "--isolated", "check"])
            result = {**checks, **probe_python(python), "candidate": str(candidate),
                      "host_custody": "NOT_ATTESTED_DISPOSABLE_TEST_ONLY"}
        print(json.dumps(result, sort_keys=True))
        return 0
    except HostCustodyHold:
        print(json.dumps({"status": "HOST_CUSTODY_HOLD",
                          "reason": "NO_OS_PROTECTED_SEPARATE_IDENTITY_STAGING",
                          "rollback": "No candidate was created. Use read-only verify, or a "
                          "separately approved disposable test-only environment."}))
        return 2
    except (ValueError, OSError, RuntimeError, subprocess.TimeoutExpired,
            json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(json.dumps({"status": "HOLD", "reason": type(exc).__name__,
                          "rollback": "Do not switch launchers. Preserve the previous environment; "
                          "inspect the separate candidate and requalify before any cutover."}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
