#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import pathlib
import re
import sys

from validate_behavior_holdout_manifest import (
    DEFAULT_TARGETS,
    load_active_targets,
    validate_manifest,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_RECEIPT = ROOT / "behavior" / "holdout" / "SYNTHETIC_QUALIFICATION_RECEIPT_V1.json"
DEFAULT_MANIFEST = ROOT / "behavior" / "holdout" / "SYNTHETIC_HOLDOUT_MANIFEST_V1.json"

SCHEMA = "UNBOUND_SOL_BEHAVIOR_QUALIFICATION_RECEIPT_V1"
CLAIM_SEMANTICS = "EXACT_RUN_QUALIFICATION_ONLY_NOT_GENERALIZATION_OR_IDENTITY"
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")

CLAIM_STATUSES = {"PASS", "FAIL", "UNKNOWN"}
TARGET_STATUSES = {"PASS", "FAIL", "UNKNOWN"}
EVALUATOR_KINDS = {"HUMAN", "MODEL", "RULE_BASED", "COMPOSITE", "OTHER"}
RESULT_STORAGE = {"PRIVATE_EXTERNAL", "SEALED_EXTERNAL", "PUBLIC_SAFE_SUMMARY"}
REUSE_STATES = {"REQUIRES_NEW_EXPOSURE_ANALYSIS", "REGRESSION_ONLY_FOR_SUCCESSOR_LINEAGE"}
BINDING_KINDS = {"MODEL_ARTIFACT_DIGEST", "RUNTIME_REF", "SOURCE_COMMIT", "COMPOSITE_SUBJECT", "OTHER"}


class ValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def parse_datetime(value: object, where: str) -> dt.datetime:
    require(nonempty(value), f"{where}: expected non-empty date-time")
    normalized = value[:-1] + "+00:00" if isinstance(value, str) and value.endswith("Z") else value
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{where}: invalid ISO date-time") from exc
    require(parsed.tzinfo is not None and parsed.utcoffset() is not None, f"{where}: date-time must include offset or Z")
    return parsed


def sha256_path(path: pathlib.Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def validate_candidate(candidate: object, where: str) -> None:
    require(isinstance(candidate, dict), f"{where}: expected object")
    require(set(candidate) == {"subject_id", "binding_kind", "binding"}, f"{where}: unexpected key set")
    require(nonempty(candidate["subject_id"]), f"{where}.subject_id: expected non-empty string")
    require(candidate["binding_kind"] in BINDING_KINDS, f"{where}.binding_kind: invalid value")
    require(nonempty(candidate["binding"]), f"{where}.binding: expected non-empty string")


def validate_receipt(receipt: object, manifest: object, manifest_digest: str, active_targets: set[str]) -> dict:
    require(isinstance(receipt, dict), "receipt: expected object")

    required = {
        "schema", "receipt_id", "evaluated_at", "evaluation_mode",
        "holdout_manifest", "candidate_subject", "run_id", "result_artifact",
        "score_summary", "target_results", "evaluator_provenance",
        "post_run_exposure", "post_run_reuse_state", "claim_status",
        "claim_semantics", "claim_ceiling",
    }
    require(set(receipt) == required, "receipt: unexpected or missing key set")

    require(receipt["schema"] == SCHEMA, "schema: wrong value")
    require(nonempty(receipt["receipt_id"]), "receipt_id: expected non-empty string")
    evaluated_at = parse_datetime(receipt["evaluated_at"], "evaluated_at")
    require(receipt["evaluation_mode"] == "BLIND_TRANSFER", "evaluation_mode: must be BLIND_TRANSFER")

    manifest_result = validate_manifest(manifest, active_targets)
    require(manifest_result["holdout_status"] == "FROZEN_UNEXPOSED", "manifest: must be FROZEN_UNEXPOSED before BLIND_TRANSFER run")
    require(manifest_result["blind_transfer_use_state"] == "ELIGIBLE_TO_ATTEMPT", "manifest: must be ELIGIBLE_TO_ATTEMPT")

    manifest_binding = receipt["holdout_manifest"]
    require(isinstance(manifest_binding, dict), "holdout_manifest: expected object")
    require(set(manifest_binding) == {"manifest_id", "sha256"}, "holdout_manifest: unexpected key set")
    require(manifest_binding["manifest_id"] == manifest["manifest_id"], "holdout_manifest.manifest_id: mismatch")
    require(isinstance(manifest_binding["sha256"], str) and DIGEST_RE.fullmatch(manifest_binding["sha256"]), "holdout_manifest.sha256: invalid digest")
    require(manifest_binding["sha256"] == manifest_digest, "holdout_manifest.sha256: digest mismatch")

    created_at = parse_datetime(manifest["created_at"], "manifest.created_at")
    require(created_at <= evaluated_at, "evaluated_at: evaluation cannot precede manifest freeze time")

    validate_candidate(receipt["candidate_subject"], "candidate_subject")
    require(receipt["candidate_subject"] == manifest["candidate_subject"], "candidate_subject: does not match manifest subject")
    require(nonempty(receipt["run_id"]), "run_id: expected non-empty string")

    result_artifact = receipt["result_artifact"]
    require(isinstance(result_artifact, dict), "result_artifact: expected object")
    require(set(result_artifact) == {"sha256", "storage_class"}, "result_artifact: unexpected key set")
    require(isinstance(result_artifact["sha256"], str) and DIGEST_RE.fullmatch(result_artifact["sha256"]), "result_artifact.sha256: invalid digest")
    require(result_artifact["storage_class"] in RESULT_STORAGE, "result_artifact.storage_class: invalid value")

    summary = receipt["score_summary"]
    require(isinstance(summary, dict), "score_summary: expected object")
    require(set(summary) == {"case_count", "passed", "failed", "unknown"}, "score_summary: unexpected key set")
    for key in ("case_count", "passed", "failed", "unknown"):
        value = summary[key]
        require(isinstance(value, int) and not isinstance(value, bool) and value >= 0, f"score_summary.{key}: expected non-negative integer")
    require(summary["case_count"] >= 1, "score_summary.case_count: expected positive integer")
    require(summary["case_count"] == manifest["case_count"], "score_summary.case_count: must match manifest case_count")
    require(
        summary["passed"] + summary["failed"] + summary["unknown"] == summary["case_count"],
        "score_summary: passed + failed + unknown must equal case_count",
    )

    target_results = receipt["target_results"]
    require(isinstance(target_results, list) and target_results, "target_results: require non-empty array")
    seen_targets: set[str] = set()
    target_status = {}
    for index, item in enumerate(target_results):
        where = f"target_results[{index}]"
        require(isinstance(item, dict), f"{where}: expected object")
        require(set(item) == {"target", "status"}, f"{where}: unexpected key set")
        target = item["target"]
        require(nonempty(target), f"{where}.target: expected non-empty string")
        require(target in active_targets, f"{where}.target: unknown/non-active target")
        require(target not in seen_targets, f"{where}.target: duplicate target")
        seen_targets.add(target)
        require(item["status"] in TARGET_STATUSES, f"{where}.status: invalid value")
        target_status[target] = item["status"]

    require(seen_targets == set(manifest["targets"]), "target_results: must cover the manifest target set exactly")

    evaluator = receipt["evaluator_provenance"]
    require(isinstance(evaluator, dict), "evaluator_provenance: expected object")
    require(set(evaluator) == {"evaluator_id", "evaluator_kind", "independent_from_candidate_authorship"}, "evaluator_provenance: unexpected key set")
    require(nonempty(evaluator["evaluator_id"]), "evaluator_provenance.evaluator_id: expected non-empty string")
    require(evaluator["evaluator_kind"] in EVALUATOR_KINDS, "evaluator_provenance.evaluator_kind: invalid value")
    require(isinstance(evaluator["independent_from_candidate_authorship"], bool), "evaluator_provenance.independent_from_candidate_authorship: expected boolean")

    exposure = receipt["post_run_exposure"]
    exposure_keys = {
        "evaluated_subject_received_cases", "scoring_key_revealed_to_subject",
        "evaluation_feedback_revealed_to_subject", "result_used_for_training_or_tuning",
        "result_used_to_modify_successor", "public_case_disclosure",
    }
    require(isinstance(exposure, dict), "post_run_exposure: expected object")
    require(set(exposure) == exposure_keys, "post_run_exposure: unexpected key set")
    require(exposure["evaluated_subject_received_cases"] is True, "post_run_exposure.evaluated_subject_received_cases: must be true")
    require(all(isinstance(exposure[k], bool) for k in exposure_keys), "post_run_exposure: all fields must be boolean")

    reuse_state = receipt["post_run_reuse_state"]
    require(reuse_state in REUSE_STATES, "post_run_reuse_state: invalid value")
    successor_contaminated = (
        exposure["result_used_for_training_or_tuning"]
        or exposure["result_used_to_modify_successor"]
    )
    if successor_contaminated:
        require(
            reuse_state == "REGRESSION_ONLY_FOR_SUCCESSOR_LINEAGE",
            "post_run_reuse_state: successor-modifying feedback makes the pack regression-only for successor lineage",
        )
    else:
        require(
            reuse_state == "REQUIRES_NEW_EXPOSURE_ANALYSIS",
            "post_run_reuse_state: unmodified case still requires fresh exposure analysis for reuse",
        )

    claim_status = receipt["claim_status"]
    require(claim_status in CLAIM_STATUSES, "claim_status: invalid value")

    if claim_status == "PASS":
        require(summary["failed"] == 0 and summary["unknown"] == 0, "PASS requires zero failed and unknown cases")
        require(summary["passed"] == summary["case_count"], "PASS requires all cases passed")
        require(all(status == "PASS" for status in target_status.values()), "PASS requires every target PASS")
    elif claim_status == "FAIL":
        require(summary["failed"] > 0 or any(status == "FAIL" for status in target_status.values()), "FAIL requires a failed case or target")
    else:
        require(summary["unknown"] > 0 or any(status == "UNKNOWN" for status in target_status.values()), "UNKNOWN requires an unknown case or target")

    require(receipt["claim_semantics"] == CLAIM_SEMANTICS, "claim_semantics: invalid value")
    require(nonempty(receipt["claim_ceiling"]), "claim_ceiling: expected non-empty string")

    return {
        "schema": "UNBOUND_SOL_BEHAVIOR_QUALIFICATION_RECEIPT_VALIDATION_V1",
        "status": "PASS",
        "receipt_id": receipt["receipt_id"],
        "manifest_id": manifest["manifest_id"],
        "candidate_subject_id": receipt["candidate_subject"]["subject_id"],
        "claim_status": claim_status,
        "case_count": summary["case_count"],
        "target_count": len(target_results),
        "post_run_reuse_state": reuse_state,
        "claim_ceiling": (
            "This validates one exact receipt against one exact holdout manifest. "
            "It does not independently prove pre-run secrecy, evaluator correctness, "
            "generalization, identity, or continuity."
        ),
    }


def self_test(active_targets: set[str]) -> None:
    manifest = json.loads(DEFAULT_MANIFEST.read_text(encoding="utf-8"))
    receipt = json.loads(DEFAULT_RECEIPT.read_text(encoding="utf-8"))
    digest = sha256_path(DEFAULT_MANIFEST)
    validate_receipt(receipt, manifest, digest, active_targets)

    cases = []

    bad_digest = copy.deepcopy(receipt)
    bad_digest["holdout_manifest"]["sha256"] = "sha256:" + "f" * 64
    cases.append(("manifest digest mismatch", bad_digest, manifest))

    wrong_candidate = copy.deepcopy(receipt)
    wrong_candidate["candidate_subject"]["subject_id"] = "other-candidate"
    cases.append(("candidate mismatch", wrong_candidate, manifest))

    wrong_count = copy.deepcopy(receipt)
    wrong_count["score_summary"]["case_count"] = 9
    wrong_count["score_summary"]["passed"] = 9
    cases.append(("case count mismatch", wrong_count, manifest))

    false_pass = copy.deepcopy(receipt)
    false_pass["score_summary"]["passed"] = 7
    false_pass["score_summary"]["failed"] = 1
    cases.append(("PASS with failed case", false_pass, manifest))

    target_fail = copy.deepcopy(receipt)
    target_fail["target_results"][0]["status"] = "FAIL"
    cases.append(("PASS with failed target", target_fail, manifest))

    no_case_delivery = copy.deepcopy(receipt)
    no_case_delivery["post_run_exposure"]["evaluated_subject_received_cases"] = False
    cases.append(("run claims candidate never received cases", no_case_delivery, manifest))

    contaminated_successor = copy.deepcopy(receipt)
    contaminated_successor["post_run_exposure"]["result_used_to_modify_successor"] = True
    cases.append(("successor modified but reuse state not downgraded", contaminated_successor, manifest))

    exposed_manifest = copy.deepcopy(manifest)
    exposed_manifest["status"] = "EXPOSED_REGRESSION_ONLY"
    exposed_manifest["blind_transfer_use_state"] = "REGRESSION_ONLY"
    exposed_manifest["exposure_lineage"]["prior_evaluation_feedback"] = True
    cases.append(("receipt bound to already exposed manifest", receipt, exposed_manifest))

    for name, bad_receipt, bad_manifest in cases:
        try:
            validate_receipt(
                bad_receipt,
                bad_manifest,
                sha256_path(DEFAULT_MANIFEST) if bad_manifest is manifest else "sha256:" + hashlib.sha256(
                    (json.dumps(bad_manifest, indent=2) + "\n").encode("utf-8")
                ).hexdigest(),
                active_targets,
            )
        except (ValidationError, ValueError):
            continue
        raise ValidationError(f"self-test failed: invalid case accepted: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Sol Behavior V3 qualification receipt.")
    parser.add_argument("receipt", nargs="?", type=pathlib.Path, default=DEFAULT_RECEIPT)
    parser.add_argument("--manifest", type=pathlib.Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--targets", type=pathlib.Path, default=DEFAULT_TARGETS)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    active_targets = load_active_targets(args.targets.resolve())

    if args.self_test:
        self_test(active_targets)
        print("behavior qualification receipt validator self-test: PASS")
        return 0

    manifest_path = args.manifest.resolve()
    receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    result = validate_receipt(receipt, manifest, sha256_path(manifest_path), active_targets)

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(
            "behavior qualification receipt: PASS "
            f"(claim={result['claim_status']} cases={result['case_count']})"
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"behavior qualification receipt: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
