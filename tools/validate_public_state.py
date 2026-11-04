#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import pathlib
import re
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


def tracked_files(root: pathlib.Path) -> list[pathlib.Path]:
    """Inspect exactly Git's staged/tracked paths, never an untracked private file."""
    try:
        top = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
        )
        if pathlib.Path(os.fsdecode(top).strip()).resolve() != root.resolve():
            fail("public validation must run at the checkout root")
        paths = subprocess.check_output(
            ["git", "-C", str(root), "ls-files", "--cached", "-z"],
            stderr=subprocess.DEVNULL,
        ).split(b"\0")
    except (OSError, subprocess.CalledProcessError):
        fail("unable to enumerate tracked repository files")
    files = [pathlib.Path(os.fsdecode(raw)) for raw in paths if raw]
    if not files:
        fail("repository has no tracked files")
    if any(path.is_absolute() or ".." in path.parts for path in files):
        fail("unsafe tracked file path")
    return files


def scan_tracked_files(root: pathlib.Path) -> None:
    for rel in tracked_files(root):
        path = root
        for part in rel.parts:
            path = path / part
            if path.is_symlink():
                fail(f"tracked symlink or redirected path: {rel}")
        try:
            with path.open("rb") as stream:
                data = stream.read(MAX_INSPECTED_BYTES + 1)
        except OSError:
            fail(f"tracked file is unreadable: {rel}")
        if len(data) > MAX_INSPECTED_BYTES:
            fail(f"tracked file exceeds inspection size: {rel}")
        # Even binary assets are checked for embedded ASCII/UTF-16 secrets.
        # Unknown NUL-bearing files fail closed rather than being skipped.
        candidates = [data.decode("utf-8", errors="replace")]
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
