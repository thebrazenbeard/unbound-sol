#!/usr/bin/env python3
"""Read-only, fail-closed check for known unsafe repository startup paths.

This scanner never imports code from the inspected repository or executes any
part of it. A clean result only means these *specific* signatures were absent.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FOLDER_OPEN = re.compile(r'["\']runOn["\']\s*:\s*["\']folderOpen["\']', re.I)
ALLOW_AUTOMATIC = re.compile(r'["\']task\.allowAutomaticTasks["\']\s*:\s*true\b', re.I)
KNOWN_NODE_HOOK = re.compile(r'\bnode(?:\.exe)?\s+(?:\./)?api\.js\b', re.I)
SUSPICIOUS_FONT_NAMES = {"fa-solid.lkf", "fa-solid-500.woff2"}
MAX_CONFIG_BYTES = 1_000_000


def _guarded_path(root: Path, relative: str) -> tuple[Path | None, str | None]:
    """Reject symlink traversal instead of accidentally reading outside root."""
    path = root
    for component in Path(relative).parts:
        path = path / component
        if path.is_symlink():
            return None, "symlink"
    return path, None


def _read_text(root: Path, relative: str) -> tuple[str | None, str | None]:
    path, problem = _guarded_path(root, relative)
    if problem or path is None:
        return None, problem
    if not path.is_file():
        return None, None
    if path.stat().st_size > MAX_CONFIG_BYTES:
        return None, "oversized"
    return path.read_text(encoding="utf-8", errors="replace"), None


def scan(root: Path) -> list[dict[str, str]]:
    """Return evidence, not a host-execution or malware attribution verdict."""
    findings: list[dict[str, str]] = []

    def flag(path: str, rule: str, detail: str) -> None:
        findings.append({"path": path, "rule": rule, "detail": detail})

    for relative in (".vscode/tasks.json", ".vscode/settings.json"):
        content, problem = _read_text(root, relative)
        if problem:
            flag(relative, "unscanned-config", f"Cannot inspect {problem} configuration safely")
        if content is None:
            continue
        if FOLDER_OPEN.search(content):
            flag(relative, "workspace-folder-open", "Automatic workspace task found")
        if ALLOW_AUTOMATIC.search(content):
            flag(relative, "workspace-auto-allow", "Automatic workspace tasks explicitly enabled")
        for name in SUSPICIOUS_FONT_NAMES:
            if name in content:
                flag(relative, "disguised-asset-reference", f"References {name}")

    package, problem = _read_text(root, "package.json")
    if problem:
        flag("package.json", "unscanned-config", f"Cannot inspect {problem} package file safely")
    if package is not None:
        try:
            scripts = json.loads(package).get("scripts", {})
        except (ValueError, AttributeError):
            flag("package.json", "invalid-package-json", "Cannot inspect scripts reliably")
        else:
            if not isinstance(scripts, dict):
                flag("package.json", "invalid-scripts", "Scripts must be an object")
            else:
                for name, command in scripts.items():
                    if isinstance(command, str) and KNOWN_NODE_HOOK.search(command):
                        flag("package.json", "known-node-hook", f"Script {name!r} invokes node api.js")

    fonts = root / "public" / "fonts"
    guarded_fonts, problem = _guarded_path(root, "public/fonts")
    if problem:
        flag("public/fonts", "unscanned-assets", "Font directory crosses a symlink")
    elif guarded_fonts is not None and guarded_fonts.is_dir():
        for name in sorted(SUSPICIOUS_FONT_NAMES):
            asset = fonts / name
            if asset.is_symlink():
                flag(str(asset.relative_to(root)), "unscanned-asset", "Suspicious asset path is a symlink")
            elif asset.is_file():
                if asset.suffix == ".lkf":
                    flag(str(asset.relative_to(root)), "disguised-executable-asset", "Known suspicious .lkf path exists")
                else:
                    with asset.open("rb") as handle:
                        magic = handle.read(4)
                    if magic != b"wOF2":
                        flag(str(asset.relative_to(root)), "invalid-woff2-magic", "Purported WOFF2 file lacks wOF2 signature")
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Repository directory to inspect, never execute")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    try:
        findings = scan(root)
    except OSError as exc:
        print(json.dumps({"status": "ERROR", "reason": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({"status": "BLOCK" if findings else "NO_MATCH", "root": str(root), "findings": findings}, indent=2))
    return 2 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
