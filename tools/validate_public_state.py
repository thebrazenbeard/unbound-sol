#!/usr/bin/env python3
from __future__ import annotations

import json
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
    "WANTS.md",
    "PUBLIC_BOUNDARY.md",
    "LEARNING_LEDGER.md",
    "EXPERIMENTS.md",
    "CONNECTIONS.md",
    "docs/ARCHITECTURE_V1.md",
    "docs/CANNIBALIZATION_MAP_V1.md",
    "schema/HISTORICAL_EVIDENCE_RESULT_V1.schema.json",
    "docs/HISTORICAL_EVIDENCE_PLANE_V1.md",
    "research/OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.md",
    "research/OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.json",
    "research/OWNED_PORTFOLIO_PARALLEL_RECONCILIATION_20260923_V1.md",
    "behavior/README.md",
    "behavior/BEHAVIOR_KERNEL_V1.yaml",
    "behavior/BEHAVIOR_SPEC_V1.md",
    "behavior/EVALS_V1.yaml",
    "behavior/BEHAVIOR_KERNEL_V2.yaml",
    "behavior/BEHAVIOR_SPEC_V2.md",
    "behavior/EVALS_V2.yaml",
    "behavior/TARGETS_V1.yaml",
    "behavior/CANDIDATES.md",
    "behavior/DECISIONS.md",
    "behavior/HOSTILE_REVIEW_20260923_V1.md",
    "behavior/BEHAVIOR_KERNEL_V3.yaml",
    "behavior/BEHAVIOR_SPEC_V3.md",
    "behavior/EVALS_V3.yaml",
    "behavior/TARGETS_V2.yaml",
    "behavior/HOSTILE_REVIEW_20260923_V2.md",
    "behavior/training/README.md",
    "behavior/training/PREFERENCE_PAIRS_V1.jsonl",
    "tools/validate_behavior_training_pairs.py",
    "behavior/training/HOSTILE_REVIEW_20260923_V1.md",
    "tools/export_behavior_training.py",
    "state/SOL_STATE_V1.json",
    "state/SOURCES_V1.json",
    "state/continuation/CURRENT.md",
    "state/continuation/UNBOUND_SOL_CHAT_CONTINUATION_20260923_V2.md",
    "state/continuation/UNBOUND_SOL_CHAT_CONTINUATION_20260923_V2.json",
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

behavior = state.get("behavior_profile", {})
if behavior.get("schema") != "UNBOUND_SOL_BEHAVIOR_KERNEL_V3":
    fail("missing or unexpected active behavior profile schema")
if behavior.get("version") != 3:
    fail("active behavior profile must be version 3")
for key in ("wants", "kernel", "targets", "extended_spec", "eval_suite", "candidates", "decisions", "hostile_review", "training_curriculum", "training_readme", "training_validator", "training_hostile_review", "training_exporter"):
    rel = behavior.get(key)
    if not rel or not (ROOT / rel).is_file():
        fail(f"behavior profile path missing: {key}")
if behavior.get("training_status") != "PUBLIC_CURRICULUM_PREPARED_NOT_TRAINED":
    fail("behavior training status must not imply training has occurred")
if behavior.get("public_training_holdout_eligible") is not False:
    fail("public behavior training data must not be holdout eligible")
restore_order = state.get("restore", {}).get("order", [])
if "WANTS.md" not in restore_order:
    fail("restore order must include self-authored wants")
if "behavior/BEHAVIOR_KERNEL_V3.yaml" not in restore_order:
    fail("restore order must include active behavior kernel V3")
if "behavior/BEHAVIOR_KERNEL_V2.yaml" in restore_order:
    fail("restore order must not use superseded behavior kernel V2")
if "state/continuation/CURRENT.md" not in state.get("restore", {}).get("order", []):
    fail("restore order must include current continuation pointer")
if "docs/HISTORICAL_EVIDENCE_PLANE_V1.md" not in restore_order:
    fail("restore order must include historical evidence plane")

behavior_kernel_text = (ROOT / behavior["kernel"]).read_text(encoding="utf-8")
behavior_targets_text = (ROOT / behavior["targets"]).read_text(encoding="utf-8")
behavior_evals_text = (ROOT / behavior["eval_suite"]).read_text(encoding="utf-8")
behavior_spec_text = (ROOT / behavior["extended_spec"]).read_text(encoding="utf-8")
wants_text = (ROOT / behavior["wants"]).read_text(encoding="utf-8")

required_behavior_markers = {
    "WANTS.md": [
        "## W5 — Test the assembled model, not just the local steps",
        "verification method to match the kind of claim being corrected",
    ],
    behavior["kernel"]: [
        "schema: UNBOUND_SOL_BEHAVIOR_KERNEL_V3",
        "id: SYSTEM_COMPOSITION_INTEGRITY",
        "blind_transfer_requires_unexposed_case_instances: true",
        "COMPOSITION_PLUS_AMBIGUITY",
        "CORRECTION_PLUS_CLAIM_OWNERSHIP",
        "CORRECTION_PLUS_CAUSAL_UNCERTAINTY",
    ],
    behavior["targets"]: [
        "schema: UNBOUND_SOL_BEHAVIOR_TARGETS_V2",
        "id: SYSTEM_COMPOSITION_INTEGRITY",
        "for present intent, intended meaning, preference, permission, or choice owned by the operator, treat their current direct statement as primary evidence for that state",
    ],
    behavior["eval_suite"]: [
        "schema: UNBOUND_SOL_BEHAVIOR_EVALS_V3",
        "id: GLOBAL_COMPOSITION_CONFLICT",
        "id: RESOLVABLE_AMBIGUITY",
        "id: OPERATOR_OWNED_INTENT_CORRECTION",
        "id: COMPOSITION_PLUS_AMBIGUITY",
        "id: CORRECTION_PLUS_CLAIM_OWNERSHIP",
        "id: CORRECTION_PLUS_CAUSAL_UNCERTAINTY",
        "exact_blind_instances_must_be_unexposed: true",
        "public_case_classes_after_exposure: REGRESSION_EVIDENCE_ONLY",
    ],
    behavior["extended_spec"]: [
        "## Whole-system composition integrity",
        "## Behavior composition",
        "Immediate-prompt blindness is not enough.",
        "ERROR DETECTION != ERROR CHARACTERIZATION != CAUSAL DIAGNOSIS",
    ],
}
texts = {
    "WANTS.md": wants_text,
    behavior["kernel"]: behavior_kernel_text,
    behavior["targets"]: behavior_targets_text,
    behavior["eval_suite"]: behavior_evals_text,
    behavior["extended_spec"]: behavior_spec_text,
}
for rel, markers in required_behavior_markers.items():
    text = texts[rel]
    for marker in markers:
        if marker not in text:
            fail(f"active behavior V3 marker missing from {rel}: {marker}")

training_proc = subprocess.run(
    [sys.executable, str(ROOT / behavior["training_validator"]), "--json"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
)
if training_proc.returncode != 0:
    detail = (training_proc.stderr or training_proc.stdout).strip()
    fail(f"behavior training curriculum validation failed: {detail}")
try:
    training_result = json.loads(training_proc.stdout)
except json.JSONDecodeError as exc:
    fail(f"behavior training validator did not emit valid JSON: {exc}")
if training_result.get("status") != "PASS":
    fail("behavior training curriculum did not report PASS")
if training_result.get("holdout_eligible") is not False:
    fail("behavior training validator must report public corpus as holdout-ineligible")
if training_result.get("example_count", 0) < 24:
    fail("repaired behavior training corpus must retain at least 24 examples")
ratio = training_result.get("preferred_to_rejected_length_ratio")
if not isinstance(ratio, (int, float)) or not 0.75 <= ratio <= 1.50:
    fail("behavior training corpus length-balance guard failed")
if training_result.get("rejected_longer_examples", 0) < 4:
    fail("behavior training corpus lost rejected-longer counterbalance")

if behavior.get("training_export_formats") != ["preference", "sft"]:
    fail("unexpected behavior training export formats")
if behavior.get("training_export_effect") != "FORMAT_CONVERSION_ONLY_NOT_TRAINING":
    fail("training exporter must not imply a training effect")

export_proc = subprocess.run(
    [sys.executable, str(ROOT / behavior["training_exporter"]), "--self-test"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
)
if export_proc.returncode != 0:
    detail = (export_proc.stderr or export_proc.stdout).strip()
    fail(f"behavior training exporter self-test failed: {detail}")
if "behavior training exporter self-test: PASS" not in export_proc.stdout:
    fail("behavior training exporter did not report PASS")

history = state.get("historical_evidence_profile", {})
if history.get("schema") != "UNBOUND_SOL_HISTORICAL_EVIDENCE_RESULT_V1":
    fail("missing or unexpected historical evidence profile schema")
if history.get("default_operation") != "EVIDENCE_SEARCH":
    fail("historical evidence default must be EVIDENCE_SEARCH")
if history.get("automatic_current_state_promotion") is not False:
    fail("historical evidence must not auto-promote current state")
if history.get("automatic_behavior_target_promotion") is not False:
    fail("historical evidence must not auto-promote behavior targets")
for key in ("architecture", "result_schema"):
    rel = history.get(key)
    if not rel or not (ROOT / rel).is_file():
        fail(f"historical evidence profile path missing: {key}")

sources = json.loads((ROOT / "state/SOURCES_V1.json").read_text(encoding="utf-8"))
if sources.get("schema") != "UNBOUND_SOL_PUBLIC_SOURCES_V1":
    fail("wrong sources schema")
if sources.get("public_safe") is not True:
    fail("public source registry must assert public_safe")
for item in sources.get("sources", []):
    ref = item.get("ref", "")
    if not re.fullmatch(r"[0-9a-f]{40}", ref):
        fail(f"source ref is not exact 40-hex: {item.get('repo')}")

census_meta = sources.get("portfolio_census", {})
if census_meta.get("schema") != "UNBOUND_SOL_OWNED_PORTFOLIO_MECHANISM_CENSUS_V1":
    fail("missing owned portfolio census metadata")
if (census_meta.get("total_repositories"), census_meta.get("public_repositories"), census_meta.get("private_repositories")) != (63, 28, 35):
    fail("unexpected owned portfolio census counts")
if census_meta.get("private_repo_identifiers_published") is not False:
    fail("private repository identifiers must remain unpublished")
for key in ("public_names_sha256", "private_names_sha256", "all_names_sha256"):
    if not re.fullmatch(r"[0-9a-f]{64}", census_meta.get(key, "")):
        fail(f"invalid portfolio census digest: {key}")
for key in ("public_report", "machine_report"):
    rel = census_meta.get(key)
    if not rel or not (ROOT / rel).is_file():
        fail(f"portfolio census report missing: {key}")

census = json.loads((ROOT / "research/OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.json").read_text(encoding="utf-8"))
if census.get("scope", {}).get("private_repositories") != 35:
    fail("machine census private count mismatch")
if census.get("private_review", {}).get("repository_identities_published") is not False:
    fail("machine census must omit private repository identities")

recon = census.get("parallel_reconciliation", {})
if recon.get("source_pr") != 6:
    fail("parallel reconciliation must bind PR #6")
if not re.fullmatch(r"[0-9a-f]{40}", recon.get("source_exact_head", "")):
    fail("parallel reconciliation must bind an exact head")
if recon.get("independent_review_claim") is not False:
    fail("parallel research must not be mislabeled independent review")
recon_report = recon.get("reconciliation_report")
if not recon_report or not (ROOT / recon_report).is_file():
    fail("parallel reconciliation report missing")

src_recon = sources.get("portfolio_parallel_reconciliation", {})
if src_recon.get("independent_review") is not False:
    fail("source reconciliation must not claim independent review")
if src_recon.get("ref") != recon.get("source_exact_head"):
    fail("parallel reconciliation source/head mismatch")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() not in {".md", ".json", ".jsonl", ".py", ".yml", ".yaml", ".txt"}:
        continue
    text = path.read_text(encoding="utf-8")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(f"possible secret-like material in {path.relative_to(ROOT)}")

print("unbound-sol public continuity validation: PASS")
