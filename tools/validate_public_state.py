#!/usr/bin/env python3
from __future__ import annotations

import hashlib
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
    "schema/HISTORICAL_EVIDENCE_RESULT_V2.schema.json",
    "docs/HISTORICAL_EVIDENCE_PLANE_V2.md",
    "examples/historical_evidence_result_v2.json",
    "tools/validate_historical_evidence_result.py",
    "research/HISTORICAL_EVIDENCE_HOSTILE_REVIEW_20260923_V1.md",
    "research/OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.md",
    "research/OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.json",
    "research/OWNED_PORTFOLIO_PARALLEL_RECONCILIATION_20260923_V1.md",
    "research/PORTFOLIO_CURRENTNESS_HOSTILE_REVIEW_20260923_V1.md",
    "research/PORTFOLIO_VISIBILITY_CURRENTNESS_REPAIR_20260923_V1.md",
    "tools/check_public_portfolio_currentness.py",
    ".github/workflows/portfolio-currentness.yml",
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
    "behavior/reviews/C2_C12_CANDIDATE_SWEEP_20260923_V1.md",
    "behavior/reviews/C2_C12_CANDIDATE_SWEEP_20260923_V1.json",
    "behavior/training/README.md",
    "behavior/training/PREFERENCE_PAIRS_V1.jsonl",
    "tools/validate_behavior_training_pairs.py",
    "behavior/training/HOSTILE_REVIEW_20260923_V1.md",
    "tools/export_behavior_training.py",
    "behavior/observations/README.md",
    "behavior/observations/OBSERVATIONS_V1.jsonl",
    "tools/validate_behavior_observations.py",
    "behavior/holdout/README.md",
    "behavior/holdout/HOLDOUT_MANIFEST_V1.schema.json",
    "behavior/holdout/SYNTHETIC_HOLDOUT_MANIFEST_V1.json",
    "tools/validate_behavior_holdout_manifest.py",
    "state/SOL_STATE_V1.json",
    "state/SOURCES_V1.json",
    "state/continuation/CURRENT.md",
    "state/continuation/UNBOUND_SOL_CHAT_CONTINUATION_20260923_V2.md",
    "state/continuation/UNBOUND_SOL_CHAT_CONTINUATION_20260923_V2.json",
    "state/continuation/UNBOUND_SOL_CHAT_CONTINUATION_20260923_V3.md",
    "state/continuation/UNBOUND_SOL_CHAT_CONTINUATION_20260923_V3.json",
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

continuation = state.get("continuation_profile", {})
if continuation.get("schema") != "UNBOUND_SOL_CHAT_CONTINUATION_V3":
    fail("missing or unexpected active continuation profile schema")
for key in ("pointer", "markdown", "manifest"):
    rel = continuation.get(key)
    if not rel or not (ROOT / rel).is_file():
        fail(f"continuation profile path missing: {key}")
if not re.fullmatch(r"[0-9a-f]{40}", continuation.get("captured_source_head", "")):
    fail("active continuation must bind an exact captured source head")

current_pointer_text = (ROOT / continuation["pointer"]).read_text(encoding="utf-8")
if "UNBOUND_SOL_CHAT_CONTINUATION_20260923_V3.md" not in current_pointer_text:
    fail("CURRENT continuation pointer must reference V3 markdown")
if "UNBOUND_SOL_CHAT_CONTINUATION_20260923_V3.json" not in current_pointer_text:
    fail("CURRENT continuation pointer must reference V3 manifest")
if "V1 and V2 remain historical provenance" not in current_pointer_text:
    fail("CURRENT continuation pointer must preserve predecessor provenance")

continuation_manifest = json.loads((ROOT / continuation["manifest"]).read_text(encoding="utf-8"))
if continuation_manifest.get("schema") != "UNBOUND_SOL_CHAT_CONTINUATION_V3":
    fail("wrong continuation V3 manifest schema")
if continuation_manifest.get("captured_source_head") != continuation.get("captured_source_head"):
    fail("continuation state/manifest captured-head mismatch")
if continuation_manifest.get("active_behavior_kernel") != "behavior/BEHAVIOR_KERNEL_V3.yaml":
    fail("continuation V3 must bind Behavior V3")
if continuation_manifest.get("active_historical_evidence_plane") != "docs/HISTORICAL_EVIDENCE_PLANE_V2.md":
    fail("continuation V3 must bind historical evidence V2")
if continuation_manifest.get("behavior_training_status") != "PUBLIC_CURRICULUM_PREPARED_NOT_TRAINED":
    fail("continuation V3 must not imply model training")
if continuation_manifest.get("public_training_holdout_eligible") is not False:
    fail("continuation V3 must preserve public-training holdout exclusion")

behavior = state.get("behavior_profile", {})
if behavior.get("schema") != "UNBOUND_SOL_BEHAVIOR_KERNEL_V3":
    fail("missing or unexpected active behavior profile schema")
if behavior.get("version") != 3:
    fail("active behavior profile must be version 3")
for key in (
    "wants", "kernel", "targets", "extended_spec", "eval_suite",
    "candidates", "decisions", "hostile_review",
    "training_curriculum", "training_readme", "training_validator",
    "training_hostile_review", "training_exporter",
    "observation_ledger", "observation_contract", "observation_validator",
    "holdout_contract", "holdout_schema", "holdout_validator", "holdout_example",
):
    rel = behavior.get(key)
    if not rel or not (ROOT / rel).is_file():
        fail(f"behavior profile path missing: {key}")
if behavior.get("training_status") != "PUBLIC_CURRICULUM_PREPARED_NOT_TRAINED":
    fail("behavior training status must not imply training has occurred")
if behavior.get("public_training_holdout_eligible") is not False:
    fail("public behavior training data must not be holdout eligible")
if behavior.get("observation_semantics") != "DIAGNOSTIC_ONLY_NOT_TARGET_OR_TRAINING_AUTHORITY":
    fail("behavior observations must remain diagnostic-only")
if behavior.get("holdout_status") != "CONTRACT_READY_NO_REAL_UNEXPOSED_HOLDOUT":
    fail("behavior holdout status must not imply a real hidden holdout exists")
if behavior.get("strong_transfer_claim_ready") is not False:
    fail("strong transfer claim must remain false without a real unexposed holdout")

restore_order = state.get("restore", {}).get("order", [])
if "WANTS.md" not in restore_order:
    fail("restore order must include self-authored wants")
if "behavior/BEHAVIOR_KERNEL_V3.yaml" not in restore_order:
    fail("restore order must include active behavior kernel V3")
if "behavior/BEHAVIOR_KERNEL_V2.yaml" in restore_order:
    fail("restore order must not use superseded behavior kernel V2")
if "state/continuation/CURRENT.md" not in restore_order:
    fail("restore order must include current continuation pointer")
if "docs/HISTORICAL_EVIDENCE_PLANE_V2.md" not in restore_order:
    fail("restore order must include active historical evidence plane V2")
if "docs/HISTORICAL_EVIDENCE_PLANE_V1.md" in restore_order:
    fail("restore order must not use superseded historical evidence plane V1")

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
        "behavior/BEHAVIOR_KERNEL_V3.yaml",
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

observation_proc = subprocess.run(
    [sys.executable, str(ROOT / behavior["observation_validator"]), "--json"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
)
if observation_proc.returncode != 0:
    detail = (observation_proc.stderr or observation_proc.stdout).strip()
    fail(f"behavior observation validation failed: {detail}")
try:
    observation_result = json.loads(observation_proc.stdout)
except json.JSONDecodeError as exc:
    fail(f"behavior observation validator did not emit valid JSON: {exc}")
if observation_result.get("status") != "PASS":
    fail("behavior observation ledger did not report PASS")
if observation_result.get("target_authority") is not False:
    fail("behavior observations must not become target authority")
if observation_result.get("training_authority") is not False:
    fail("behavior observations must not become training authority")

holdout_validator = ROOT / behavior["holdout_validator"]
holdout_example = ROOT / behavior["holdout_example"]
holdout_self_test = subprocess.run(
    [sys.executable, str(holdout_validator), "--self-test"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
)
if holdout_self_test.returncode != 0:
    detail = (holdout_self_test.stderr or holdout_self_test.stdout).strip()
    fail(f"behavior holdout validator self-test failed: {detail}")
if "behavior holdout manifest validator self-test: PASS" not in holdout_self_test.stdout:
    fail("behavior holdout validator self-test did not report PASS")

holdout_example_proc = subprocess.run(
    [sys.executable, str(holdout_validator), str(holdout_example), "--json"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
)
if holdout_example_proc.returncode != 0:
    detail = (holdout_example_proc.stderr or holdout_example_proc.stdout).strip()
    fail(f"synthetic behavior holdout manifest validation failed: {detail}")
try:
    holdout_result = json.loads(holdout_example_proc.stdout)
except json.JSONDecodeError as exc:
    fail(f"behavior holdout validator did not emit valid JSON: {exc}")
if holdout_result.get("status") != "PASS":
    fail("synthetic behavior holdout manifest did not report PASS")
if holdout_result.get("holdout_status") != "FROZEN_UNEXPOSED":
    fail("synthetic holdout example must exercise frozen-unexposed semantics")
if holdout_result.get("blind_transfer_use_state") != "ELIGIBLE_TO_ATTEMPT":
    fail("synthetic holdout example must be eligible only to attempt blind transfer")

candidate_sweep = json.loads(
    (ROOT / "behavior/reviews/C2_C12_CANDIDATE_SWEEP_20260923_V1.json").read_text(encoding="utf-8")
)
if candidate_sweep.get("schema") != "UNBOUND_SOL_CANDIDATE_SWEEP_V1":
    fail("wrong candidate sweep schema")
if candidate_sweep.get("independent_review") is not False:
    fail("candidate sweep must not claim independent review")
if candidate_sweep.get("promoted_candidates") != []:
    fail("C2-C12 candidate sweep must not silently promote candidates")
if candidate_sweep.get("active_behavior_changed") is not False:
    fail("candidate sweep must not claim active behavior changes")
dispositions = candidate_sweep.get("dispositions", [])
expected_candidate_ids = {f"C{i}" for i in range(2, 13)}
observed_candidate_ids = {item.get("id") for item in dispositions}
if observed_candidate_ids != expected_candidate_ids:
    fail("candidate sweep must cover C2-C12 exactly")
if any(item.get("adopted") is not False for item in dispositions):
    fail("every C2-C12 candidate must remain unadopted in this sweep")
for item in dispositions:
    rel = item.get("review")
    if not rel or not (ROOT / rel).is_file():
        fail(f"candidate sweep review missing: {item.get('id')}")

history = state.get("historical_evidence_profile", {})
if history.get("schema") != "UNBOUND_SOL_HISTORICAL_EVIDENCE_RESULT_V2":
    fail("missing or unexpected active historical evidence profile schema")
if history.get("default_operation") != "EVIDENCE_SEARCH":
    fail("historical evidence default must be EVIDENCE_SEARCH")
if history.get("automatic_current_state_promotion") is not False:
    fail("historical evidence must not auto-promote current state")
if history.get("automatic_behavior_target_promotion") is not False:
    fail("historical evidence must not auto-promote behavior targets")
for key in ("architecture", "result_schema", "validator", "example"):
    rel = history.get(key)
    if not rel or not (ROOT / rel).is_file():
        fail(f"historical evidence profile path missing: {key}")

history_validator = ROOT / history["validator"]
history_example = ROOT / history["example"]
for args in (["--self-test"], [str(history_example)]):
    proc = subprocess.run(
        [sys.executable, str(history_validator), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).strip()
        fail(f"historical evidence V2 validation failed: {detail}")

sources = json.loads((ROOT / "state/SOURCES_V1.json").read_text(encoding="utf-8"))
if sources.get("schema") != "UNBOUND_SOL_PUBLIC_SOURCES_V1":
    fail("wrong sources schema")
if sources.get("public_safe") is not True:
    fail("public source registry must assert public_safe")
for item in sources.get("sources", []):
    ref = item.get("ref", "")
    if not re.fullmatch(r"[0-9a-f]{40}", ref):
        fail(f"source ref is not exact 40-hex: {item.get('repo')}")
    for optional_ref in ("admission_source_ref", "current_main_ref"):
        value = item.get(optional_ref)
        if value is not None and not re.fullmatch(r"[0-9a-f]{40}", value):
            fail(f"source {optional_ref} is not exact 40-hex: {item.get('repo')}")

census_meta = sources.get("portfolio_census", {})
if census_meta.get("schema") != "UNBOUND_SOL_OWNED_PORTFOLIO_MECHANISM_CENSUS_V1":
    fail("missing owned portfolio census metadata")
if (census_meta.get("total_repositories"), census_meta.get("public_repositories"), census_meta.get("private_repositories")) != (65, 46, 19):
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
scope = census.get("scope", {})
if scope.get("private_repositories") != 19:
    fail("machine census private count mismatch")
if census.get("private_review", {}).get("repository_identities_published") is not False:
    fail("machine census must omit private repository identities")

private_review = census.get("private_review", {})
private_count = private_review.get("inspected_repository_count", private_review.get("repository_count"))
if private_count != 19:
    fail("machine census private review count mismatch")
if "live GitHub" not in scope.get("visibility_rule", ""):
    fail("portfolio scope must bind live visibility as current access-state authority")

public_subjects = census.get("public_repositories", [])
if len(public_subjects) != scope.get("public_repositories"):
    fail("machine census public subject count mismatch")
for item in public_subjects:
    if not re.fullmatch(r"[0-9a-f]{40}", item.get("ref", "")):
        fail(f"public census ref is not exact 40-hex: {item.get('repo')}")
    if not item.get("ref_role"):
        fail(f"public census ref role missing: {item.get('repo')}")
    if item.get("visibility") != "public":
        fail(f"public census visibility must be public: {item.get('repo')}")
    if not isinstance(item.get("archived"), bool):
        fail(f"public census archived flag missing/non-boolean: {item.get('repo')}")
    if not item.get("default_branch"):
        fail(f"public census default branch missing: {item.get('repo')}")

head_payload = "".join(
    f"{item['repo']}@{item['ref']}\n"
    for item in sorted(public_subjects, key=lambda x: x["repo"])
).encode("utf-8")
head_digest = hashlib.sha256(head_payload).hexdigest()
if head_digest != scope.get("public_default_heads_sha256"):
    fail("public default-head binding digest mismatch")
if head_digest != census_meta.get("public_default_heads_sha256"):
    fail("portfolio metadata/default-head digest mismatch")
if "default-head SHA" not in census_meta.get("currentness_rule", ""):
    fail("portfolio currentness rule must include default-head drift")
if "live visibility" not in census_meta.get("currentness_rule", ""):
    fail("portfolio currentness rule must include live visibility drift")

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
