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


def _read_text(root: Path, relative: str) -> str | None:
    path = root / relative
    if path.is_symlink() or not path.is_file():
        return None
    return path.read_text(encoding="utf-8", errors="replace")


def scan(root: Path) -> list[dict[str, str]]:
    """Return evidence, not a host-execution or malware attribution verdict."""
    findings: list[dict[str, str]] = []

    def flag(path: str, rule: str, detail: str) -> None:
        findings.append({"path": path, "rule": rule, "detail": detail})

    for relative in (".vscode/tasks.json", ".vscode/settings.json"):
        content = _read_text(root, relative)
        if content is None:
            continue
        if FOLDER_OPEN.search(content):
            flag(relative, "workspace-folder-open", "Automatic workspace task found")
        if ALLOW_AUTOMATIC.search(content):
            flag(relative, "workspace-auto-allow", "Automatic workspace tasks explicitly enabled")
        for name in SUSPICIOUS_FONT_NAMES:
            if name in content:
                flag(relative, "disguised-asset-reference", f"References {name}")

    package = _read_text(root, "package.json")
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
    if fonts.is_dir() and not fonts.is_symlink():
        for name in sorted(SUSPICIOUS_FONT_NAMES):
            asset = fonts / name
            if asset.is_file() and not asset.is_symlink():
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
