"""Offline, no-host-effect tests for side-by-side Portal/Runner qualification."""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "portal_runner_wheel_qualification",
    ROOT / "tools" / "portal_runner_wheel_qualification.py",
)
assert spec and spec.loader
qual = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qual)


def wheel(path: Path, name: str, payload: bytes = b"test") -> str:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(name, payload)
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PortalRunnerQualificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_exact_pinned_wheels_have_no_application_file_collision(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        portal_hash = wheel(portal, "portal/__init__.py")
        runner_hash = wheel(runner, "runner/__init__.py")
        receipt = qual.validate_wheels(portal, runner, portal_hash, runner_hash)
        self.assertEqual(receipt["portal_sha256"], portal_hash)

    def test_wheel_collision_and_sha_substitution_fail_closed(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        portal_hash = wheel(portal, "runner/schema.py")
        runner_hash = wheel(runner, "runner/schema.py")
        with self.assertRaisesRegex(ValueError, "overwrite"):
            qual.validate_wheels(portal, runner, portal_hash, runner_hash)
        with self.assertRaisesRegex(ValueError, "mismatch"):
            qual.validate_wheels(portal, runner, "0" * 64, runner_hash)

    def test_duplicate_member_in_wheel_is_rejected(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        with zipfile.ZipFile(portal, "w") as archive:
            archive.writestr("portal/__init__.py", b"first")
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                archive.writestr("portal/__init__.py", b"second")
        runner_hash = wheel(runner, "runner/__init__.py")
        with self.assertRaisesRegex(ValueError, "repeats"):
            qual.validate_wheels(portal, runner,
                                 hashlib.sha256(portal.read_bytes()).hexdigest(), runner_hash)

    def test_candidate_must_be_new_absolute_and_not_system_root(self) -> None:
        with self.assertRaisesRegex(ValueError, "absolute"):
            qual.require_unused_candidate(Path("relative-venv"))
        with self.assertRaisesRegex(ValueError, "unused"):
            qual.require_unused_candidate(self.root)
        with self.assertRaisesRegex(ValueError, "root"):
            qual.require_unused_candidate(Path(self.root.anchor))
        self.assertEqual(qual.require_unused_candidate(self.root / "new"),
                         (self.root / "new").resolve())

    def test_probe_rejects_global_editable_binding_and_false_authority(self) -> None:
        python = self.root / "python.exe"
        python.touch()
        fake = {
            "virtual_environment": False,
            "all_modules_under_prefix": False,
            "portal_version": "0.2.0",
            "runner_version": "0.1.0",
            "worker_schema_valid_shape": True,
        }
        with patch.object(qual, "_run", return_value=json.dumps(fake)):
            with self.assertRaisesRegex(ValueError, "HOLD"):
                qual.probe_python(python)
        fake["virtual_environment"] = True
        with patch.object(qual, "_run", return_value=json.dumps(fake)):
            with self.assertRaisesRegex(ValueError, "HOLD"):
                qual.probe_python(python)

    def test_probe_checks_both_cli_entrypoints_and_never_grants_authority(self) -> None:
        # Use the running platform's executable naming to avoid assuming Windows.
        bin_dir = self.root / "bin"
        bin_dir.mkdir()
        python = bin_dir / "python"
        python.touch()
        suffix = ".exe" if qual.sys.platform == "win32" else ""
        for name in ("portal", "project-runner"):
            (bin_dir / (name + suffix)).touch()
        good = {
            "virtual_environment": True,
            "all_modules_under_prefix": True,
            "portal_version": "0.2.0",
            "runner_version": "0.1.0",
            "worker_schema_valid_shape": True,
        }
        with patch.object(qual, "_run", return_value=json.dumps(good)) as run:
            result = qual.probe_python(python)
        self.assertEqual(result["authority"], "NO_HOST_OR_EXECUTION_AUTHORIZATION")
        self.assertEqual(run.call_count, 3)
        self.assertEqual(run.call_args_list[1].args[0][-1], "--help")
        self.assertEqual(run.call_args_list[2].args[0][-1], "--help")

    def test_snapshot_omits_raw_freeze_and_rejects_tokenized_version(self) -> None:
        python = self.root / "python.exe"
        python.touch()
        output = self.root / "private-snapshot.json"
        safe = {
            "schema": "PORTAL_RUNNER_REDACTED_INSTALLED_SNAPSHOT_V1",
            "interpreter": "python",
            "prefix": "prefix",
            "freeze_equivalent": ["portal-coordinator==0.2.0", "project-runner==0.1.0"],
            "note": "version only",
        }
        with patch.object(qual, "_run", return_value=json.dumps(safe)):
            qual.sanitized_snapshot(python, output)
        self.assertEqual(json.loads(output.read_text())["freeze_equivalent"],
                         safe["freeze_equivalent"])
        with self.assertRaisesRegex(ValueError, "unused"):
            qual.sanitized_snapshot(python, output)
        bad = dict(safe)
        bad["freeze_equivalent"] = ["project-runner @ https://example.invalid/repo"]
        fresh = self.root / "fresh.json"
        with patch.object(qual, "_run", return_value=json.dumps(bad)):
            with self.assertRaisesRegex(ValueError, "unsafe"):
                qual.sanitized_snapshot(python, fresh)
        self.assertFalse(fresh.exists())

    def test_stage_never_reuses_existing_target_or_wheelhouse(self) -> None:
        with patch.object(qual, "venv") as virtualenv:
            result = qual.main([
                "stage", "--candidate-dir", str(self.root),
                "--portal-wheel", str(self.root / "missing1.whl"),
                "--runner-wheel", str(self.root / "missing2.whl"),
                "--portal-sha256", "0" * 64,
                "--runner-sha256", "0" * 64,
                "--wheelhouse", str(self.root),
            ])
        self.assertEqual(result, 2)
        virtualenv.EnvBuilder.assert_not_called()


if __name__ == "__main__":
    unittest.main()
