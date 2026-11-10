#!/usr/bin/env python3
from __future__ import annotations

import json
import hashlib
import os
import pathlib
import re
import stat
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "IDENTITY.md",
    "CONTINUITY.md",
    "PRINCIPLES.md",
    "PUBLIC_BOUNDARY.md",
    "LEARNING_LEDGER.md",
    "EXPERIMENTS.md",
    "CONNECTIONS.md",
    "docs/ARCHITECTURE_V1.md",
    "docs/CANNIBALIZATION_MAP_V1.md",
    "state/SOL_STATE_V1.json",
    "state/SOURCES_V1.json",
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-proj-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"(?i)\b(password|api[_-]?key|bearer[_-]?token)\s*[:=]\s*[^\s<>{}]{8,}"),
]

MAX_INSPECTED_BYTES = 16 * 1024 * 1024
KNOWN_BINARY_SUFFIXES = {".eot", ".ttf", ".woff", ".woff2"}


def fail(message: str) -> None:
    raise SystemExit(message)


def tracked_files(root: pathlib.Path) -> list[tuple[pathlib.Path, str]]:
    """Bind each tracked path to its exact Git index blob, not just its name."""
    try:
        top = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
        )
        if pathlib.Path(os.fsdecode(top).strip()).resolve() != root.resolve():
            fail("public validation must run at the checkout root")
        entries = subprocess.check_output(
            ["git", "-C", str(root), "ls-files", "--cached", "--stage", "-z"],
            stderr=subprocess.DEVNULL,
        ).split(b"\0")
    except (OSError, subprocess.CalledProcessError):
        fail("unable to enumerate tracked repository files")
    files: list[tuple[pathlib.Path, str]] = []
    for entry in entries:
        if not entry:
            continue
        try:
            header, name = entry.split(b"\t", 1)
            mode, object_id, stage = header.split(b" ")
        except ValueError:
            fail("malformed Git index entry")
        if stage != b"0":
            fail("unmerged Git index stage")
        if mode == b"120000":
            fail("tracked symlink entry in Git index")
        if mode not in (b"100644", b"100755"):
            fail("non-regular Git index entry")
        if not re.fullmatch(rb"[0-9a-f]{40}", object_id):
            fail("malformed Git index object identity")
        files.append((pathlib.Path(os.fsdecode(name)), object_id.decode("ascii")))
    if not files:
        fail("repository has no tracked files")
    if any(path.is_absolute() or ".." in path.parts for path, _ in files):
        fail("unsafe tracked file path")
    return files


def indexed_blob(root: pathlib.Path, rel: pathlib.Path, object_id: str) -> bytes:
    """Read bounded Git index content, rejecting replacement-object spoofing."""
    try:
        size = int(subprocess.check_output(
            ["git", "-C", str(root), "cat-file", "-s", object_id],
            stderr=subprocess.DEVNULL,
        ))
        if size < 0 or size > MAX_INSPECTED_BYTES:
            fail(f"indexed file exceeds inspection size: {rel}")
        data = subprocess.check_output(
            ["git", "-C", str(root), "cat-file", "blob", object_id],
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError, ValueError):
        fail(f"Git index blob unavailable: {rel}")
    digest = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
    if len(data) != size or digest != object_id:
        fail(f"Git index blob identity mismatch: {rel}")
    return data


def inspect_contents(rel: pathlib.Path, data: bytes) -> None:
    if len(data) > MAX_INSPECTED_BYTES:
        fail(f"tracked file exceeds inspection size: {rel}")
    # Even binary assets are checked for embedded ASCII/UTF-16 secrets.
    # Unknown NUL-bearing files fail closed rather than being skipped.
    if rel.suffix.lower() not in KNOWN_BINARY_SUFFIXES:
        try:
            content = data.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            fail(f"invalid UTF-8 in non-font tracked file: {rel}")
    else:
        content = data.decode("utf-8", errors="replace")
    candidates = [content]
    if b"\0" in data:
        candidates.extend((
            data.decode("utf-16-le", errors="replace"),
            data.decode("utf-16-be", errors="replace"),
        ))
    for content in candidates:
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                fail(f"possible secret-like material in {rel}")
    if b"\0" in data and rel.suffix.lower() not in KNOWN_BINARY_SUFFIXES:
        fail(f"unclassified NUL-bearing tracked file: {rel}")


def scan_tracked_files(root: pathlib.Path) -> None:
    pinned_entries = tracked_files(root)
    for rel, object_id in pinned_entries:
        inspect_contents(rel, indexed_blob(root, rel, object_id))
        path = root
        preflight_components = []
        for part in rel.parts:
            path = path / part
            try:
                info = path.lstat()
            except OSError:
                fail(f"tracked file is unreadable: {rel}")
            reparse = getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
            if stat.S_ISLNK(info.st_mode) or reparse:
                fail(f"tracked symlink or redirected path: {rel}")
            preflight_components.append((path, info))
        if not stat.S_ISREG(info.st_mode):
            fail(f"tracked file is non-regular: {rel}")
        try:
            # A replaced FIFO would block plain open() before any file check.
            # Recheck the opened descriptor to close the normal lstat/open race.
            flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_NOFOLLOW", 0)
            descriptor = os.open(path, flags)
            with os.fdopen(descriptor, "rb") as stream:
                opened = os.fstat(stream.fileno())
                if not stat.S_ISREG(opened.st_mode):
                    fail(f"tracked file is non-regular: {rel}")
                # O_NOFOLLOW protects only the last path component; Windows
                # does not expose it at all. Bind the opened handle to the
                # preflight file identity before reading any content.
                if (not opened.st_ino or not info.st_ino or
                    (opened.st_dev, opened.st_ino) != (info.st_dev, info.st_ino)):
                    fail(f"tracked symlink or redirected path: {rel}")
                for component, before in preflight_components:
                    try:
                        after = component.lstat()
                    except OSError:
                        fail(f"tracked file is unreadable: {rel}")
                    reparse = getattr(after, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
                    if (stat.S_ISLNK(after.st_mode) or reparse or
                        (after.st_dev, after.st_ino) != (before.st_dev, before.st_ino)):
                        fail(f"tracked symlink or redirected path: {rel}")
                data = stream.read(MAX_INSPECTED_BYTES + 1)
        except OSError:
            fail(f"tracked file is unreadable: {rel}")
        inspect_contents(rel, data)
    if pinned_entries != tracked_files(root):
        fail("Git index changed during public validation")


for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        fail(f"missing required file: {rel}")

state = json.loads((ROOT / "state/SOL_STATE_V1.json").read_text(encoding="utf-8"))
if state.get("schema") != "UNBOUND_SOL_STATE_V1":
    fail("wrong state schema")
if state.get("model_identity", {}).get("substrate") != "GPT-5.6 Sol":
    fail("unexpected model substrate")
if state.get("public_boundary", {}).get("secrets_allowed") is not False:
    fail("public state must forbid secrets")
if state.get("restore", {}).get("fresh_check_mutable_external_state") is not True:
    fail("restore policy must require fresh-checking mutable external state")

sources = json.loads((ROOT / "state/SOURCES_V1.json").read_text(encoding="utf-8"))
if sources.get("schema") != "UNBOUND_SOL_PUBLIC_SOURCES_V1":
    fail("wrong sources schema")
if sources.get("public_safe") is not True:
    fail("public source registry must assert public_safe")
for item in sources.get("sources", []):
    ref = item.get("ref", "")
    if not re.fullmatch(r"[0-9a-f]{40}", ref):
        fail(f"source ref is not exact 40-hex: {item.get('repo')}")

scan_tracked_files(ROOT)
print("unbound-sol public continuity validation: PASS")
