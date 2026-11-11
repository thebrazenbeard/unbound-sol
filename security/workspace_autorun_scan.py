#!/usr/bin/env python3
"""Read-only, fail-closed check for known unsafe repository startup paths.

This scanner never imports code from the inspected repository or executes any
part of it. A clean result only means these *specific* signatures were absent.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


FOLDER_OPEN = re.compile(r'["\']runOn["\']\s*:\s*["\']folderOpen["\']', re.I)
AUTO_TASK_SETTING = re.compile(
    r'["\']task\.allowAutomaticTasks["\']\s*:\s*(true|false|["\']on["\']|["\']off["\'])', re.I
)
KNOWN_NODE_HOOK = re.compile(r'\bnode(?:\.exe)?\s+(?:\.[\\/])?api\.js\b', re.I)
SUSPICIOUS_FONT_NAMES = {"fa-solid.lkf", "fa-solid-500.woff2", "fa-solid-600.ttf"}
MAX_CONFIG_BYTES = 1_000_000
MAX_TTF_BYTES = 64 * 1024 * 1024
NODE_INTERPRETER = re.compile(r"(?i)(?:^|[\\/\s])node(?:\.exe)?(?:$|\s|[\\/])")
FONT_PROGRAM = re.compile(r"(?i)\.(?:ttf|woff2?|eot|lkf|svg)(?:$|[\s?#])")


def _strip_jsonc(text: str) -> str:
    """Strip JSONC comments and trailing commas outside quoted strings."""
    if text.startswith("\ufeff"):
        text = text[1:]
    output: list[str] = []
    quoted = escaped = False
    index = 0
    while index < len(text):
        ch = text[index]
        next_ch = text[index + 1] if index + 1 < len(text) else ""
        if quoted:
            output.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                quoted = False
            index += 1
        elif ch == '"':
            quoted = True
            output.append(ch)
            index += 1
        elif ch == "/" and next_ch in {"/", "*"}:
            block = next_ch == "*"
            index += 2
            closed = not block
            while index < len(text):
                if block and text[index:index + 2] == "*/":
                    index += 2
                    closed = True
                    break
                if not block and text[index] == "\n":
                    break
                if text[index] == "\n":
                    output.append("\n")
                index += 1
            if not closed:
                raise ValueError("Unclosed JSONC block comment")
        else:
            output.append(ch)
            index += 1

    stripped = "".join(output)
    result: list[str] = []
    next_visible: list[str | None] = [None] * (len(stripped) + 1)
    visible: str | None = None
    for index in range(len(stripped) - 1, -1, -1):
        if not stripped[index].isspace():
            visible = stripped[index]
        next_visible[index] = visible
    quoted = escaped = False
    for index, ch in enumerate(stripped):
        if quoted:
            result.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                quoted = False
            continue
        if ch == '"':
            quoted = True
        elif ch == ",":
            if next_visible[index + 1] in {"}", "]"}:
                continue
        result.append(ch)
    return "".join(result)


def _jsonc_object(text: str) -> dict:
    def no_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
        result: dict = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate workspace key: {key}")
            result[key] = value
        return result

    decoded = json.loads(_strip_jsonc(text), object_pairs_hook=no_duplicate_keys)
    if not isinstance(decoded, dict):
        raise ValueError("Workspace configuration must be an object")
    return decoded


def _walk_objects(node: object):
    if isinstance(node, dict):
        yield node
        for child in node.values():
            yield from _walk_objects(child)
    elif isinstance(node, list):
        for child in node:
            yield from _walk_objects(child)


def _effective_invocations(node: dict):
    if not ("command" in node or "args" in node):
        return
    variants = [node]
    for name in ("windows", "osx", "linux"):
        override = node.get(name)
        if isinstance(override, dict):
            variants.append({**node, **override})
    for variant in variants:
        command = variant.get("command", "")
        args = variant.get("args", [])
        if not isinstance(args, list):
            args = [args]
        yield str(command), " ".join(str(arg) for arg in args)


def _valid_sfnt_ttf(path: Path) -> bool:
    """Inspect an on-disk sfnt directory, never decode or execute its tables."""
    size = path.stat().st_size
    if size < 12 or size > MAX_TTF_BYTES:
        return False
    with path.open("rb") as handle:
        header = handle.read(12)
        if len(header) != 12 or header[:4] not in {b"\x00\x01\x00\x00", b"OTTO", b"true", b"typ1"}:
            return False
        num_tables = int.from_bytes(header[4:6], "big")
        if not 1 <= num_tables <= 256 or 12 + 16 * num_tables > size:
            return False
        power = 1 << (num_tables.bit_length() - 1)
        expected = (power * 16, power.bit_length() - 1, num_tables * 16 - power * 16)
        actual = tuple(int.from_bytes(header[i : i + 2], "big") for i in (6, 8, 10))
        if actual != expected:
            return False
        directory = handle.read(num_tables * 16)
    if len(directory) != num_tables * 16:
        return False
    tags = set()
    last_table_end = 0
    for start in range(0, len(directory), 16):
        record = directory[start : start + 16]
        tag = record[:4]
        offset = int.from_bytes(record[8:12], "big")
        length = int.from_bytes(record[12:16], "big")
        if tag in tags or offset < 12 + len(directory) or length == 0 or offset + length > size:
            return False
        tags.add(tag)
        last_table_end = max(last_table_end, offset + length)
    return {b"head", b"cmap"} <= tags and size - last_table_end <= 3


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


def _workspace_config_paths(root: Path) -> tuple[list[str], list[str], list[str]]:
    """Enumerate nested VS Code config without following symlinked directories.

    Generated dependencies and .git internals are not workspace source files.
    Directory read failures cannot silently produce a clean result.
    """
    configs = {".vscode/tasks.json", ".vscode/settings.json"}
    packages = {"package.json"}
    unreadable: list[str] = []
    excluded = {".git", "node_modules", ".venv", "venv", "__pycache__", ".tox"}

    def on_error(_error: OSError) -> None:
        unreadable.append("directory-enumeration-error")

    for folder, directories, files in os.walk(root, topdown=True, followlinks=False, onerror=on_error):
        parent = Path(folder)
        in_editor_config = parent.name.casefold() == ".vscode"
        for filename in files:
            folded = filename.casefold()
            relative = (parent / filename).relative_to(root).as_posix()
            if (in_editor_config and folded in {"tasks.json", "settings.json"}) or folded.endswith(".code-workspace"):
                configs.add(relative)
            if folded == "package.json":
                packages.add(relative)

        safe_directories = []
        for dirname in directories:
            if dirname.casefold() in excluded:
                continue
            candidate = parent / dirname
            if candidate.is_symlink():
                if dirname.casefold() == ".vscode":
                    configs.add((candidate / "tasks.json").relative_to(root).as_posix())
                else:
                    unreadable.append(candidate.relative_to(root).as_posix())
            else:
                safe_directories.append(dirname)
        directories[:] = safe_directories

    return sorted(configs), sorted(packages), unreadable


def scan(root: Path) -> list[dict[str, str]]:
    """Return evidence, not a host-execution or malware attribution verdict."""
    findings: list[dict[str, str]] = []

    def flag(path: str, rule: str, detail: str) -> None:
        findings.append({"path": path, "rule": rule, "detail": detail})

    config_paths, package_paths, blocked_directories = _workspace_config_paths(root)
    for directory in blocked_directories:
        flag(directory, "unscanned-config", "Cannot safely inspect a directory while locating workspace files")
    for relative in config_paths:
        content, problem = _read_text(root, relative)
        if problem:
            flag(relative, "unscanned-config", f"Cannot inspect {problem} configuration safely")
        if content is None:
            continue
        try:
            decoded = _jsonc_object(content)
        except ValueError:
            flag(relative, "invalid-workspace-jsonc", "Cannot semantically inspect workspace configuration")
            if FOLDER_OPEN.search(content):
                flag(relative, "workspace-folder-open", "Automatic workspace task found")
            if AUTO_TASK_SETTING.search(content):
                flag(relative, "workspace-auto-allow", "Automatic-task setting exists in malformed configuration")
        else:
            if Path(relative).name.casefold() == "settings.json" and Path(relative).parent.name.casefold() == ".vscode" and isinstance(decoded.get("tasks"), (dict, list)):
                flag(relative, "workspace-embedded-tasks", "Settings file embeds workspace tasks")
            for node in _walk_objects(decoded):
                if node.get("runOn") == "folderOpen":
                    flag(relative, "workspace-folder-open", "Automatic workspace task found")
                if "task.allowAutomaticTasks" in node:
                    setting = node["task.allowAutomaticTasks"]
                    if setting is True or setting == "on":
                        flag(relative, "workspace-auto-allow", "Automatic workspace tasks explicitly enabled or attempted")
                    if not isinstance(setting, str) or setting not in {"on", "off"}:
                        flag(relative, "invalid-auto-task-setting", "VS Code expects the string 'on' or 'off'")
                for command, args in _effective_invocations(node):
                    if NODE_INTERPRETER.search(command) and FONT_PROGRAM.search(command + " " + args):
                        flag(relative, "disguised-interpreter-asset", "Node interpreter references a font-like executable path")
        for name in SUSPICIOUS_FONT_NAMES:
            if name in content:
                flag(relative, "disguised-asset-reference", f"References {name}")

    for relative in package_paths:
        package, problem = _read_text(root, relative)
        if problem:
            flag(relative, "unscanned-config", f"Cannot inspect {problem} package file safely")
        if package is None:
            continue
        try:
            manifest = json.loads(package)
            scripts = manifest.get("scripts", {}) if isinstance(manifest, dict) else None
        except ValueError:
            flag(relative, "invalid-package-json", "Cannot inspect scripts reliably")
            continue
        if not isinstance(scripts, dict):
            flag(relative, "invalid-scripts", "Scripts must be an object")
            continue
        for name, command in scripts.items():
            if not isinstance(command, str):
                continue
            if KNOWN_NODE_HOOK.search(command):
                flag(relative, "known-node-hook", f"Script {name!r} invokes node api.js")
            if NODE_INTERPRETER.search(command) and FONT_PROGRAM.search(command):
                flag(relative, "disguised-interpreter-asset", f"Script {name!r} runs a font-like asset using Node")

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
                elif asset.suffix == ".woff2":
                    with asset.open("rb") as handle:
                        magic = handle.read(4)
                    if magic != b"wOF2":
                        flag(str(asset.relative_to(root)), "invalid-woff2-magic", "Purported WOFF2 file lacks wOF2 signature")
        for asset in sorted(fonts.rglob("*")):
            if asset.suffix.casefold() != ".ttf":
                continue
            relative = str(asset.relative_to(root))
            if asset.is_symlink():
                flag(relative, "unscanned-asset", "TTF asset path is a symlink")
            elif asset.is_file():
                try:
                    valid = _valid_sfnt_ttf(asset)
                except OSError:
                    flag(relative, "unscanned-asset", "Cannot read TTF asset safely")
                else:
                    if not valid:
                        flag(relative, "invalid-ttf-structure", "Purported TTF lacks a valid bounded sfnt table directory")
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
