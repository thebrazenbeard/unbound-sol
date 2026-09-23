#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "IDENTITY.md",
    "CONTINUITY.md",
    "PRINCIPLES.md",
    "WANTS.md",
    "behavior/TARGETS_V1.yaml",
    "behavior/DECISIONS.md",
    "behavior/QUALIFICATION.md",
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

def fail(message: str) -> None:
    raise SystemExit(message)

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

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml", ".txt"}:
        continue
    text = path.read_text(encoding="utf-8")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(f"possible secret-like material in {path.relative_to(ROOT)}")

print("unbound-sol public continuity validation: PASS")
