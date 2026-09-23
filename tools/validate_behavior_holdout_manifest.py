#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "behavior" / "holdout" / "SYNTHETIC_HOLDOUT_MANIFEST_V1.json"
DEFAULT_TARGETS = ROOT / "behavior" / "TARGETS_V2.yaml"

SCHEMA = "UNBOUND_SOL_BEHAVIOR_HOLDOUT_MANIFEST_V1"
CLAIM_SEMANTICS = "HOLDOUT_CUSTODY_DECLARATION_NOT_PROOF_OF_NONEXPOSURE"
TARGET_ID_RE = re.compile(r"^  - id: ([A-Z0-9_]+)$", re.MULTILINE)
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")

STATUSES = {"FROZEN_UNEXPOSED", "EXPOSED_REGRESSION_ONLY", "INVALIDATED"}
USE_STATES = {"ELIGIBLE_TO_ATTEMPT", "REGRESSION_ONLY", "INVALID"}
BINDING_KINDS = {"MODEL_ARTIFACT_DIGEST", "RUNTIME_REF", "SOURCE_COMMIT", "COMPOSITE_SUBJECT", "OTHER"}
STORAGE_CLASSES = {"PRIVATE_EXTERNAL", "SEALED_EXTERNAL"}
EVIDENCE_KINDS = {"IMMUTABLE_REF", "CONTENT_DIGEST", "SIGNED_RECEIPT", "SEALED_STORE_RECEIPT", "OTHER"}
EXPOSURE_KEYS = {
    "restored_state",
    "training_data",
    "tuning_feedback",
    "prior_evaluation_feedback",
    "candidate_pre_access",
}


class ValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def parse_datetime(value: object, where: str) -> None:
    require(nonempty(value), f"{where}: expected non-empty date-time")
    normalized = value[:-1] + "+00:00" if isinstance(value, str) and value.endswith("Z") else value
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{where}: invalid ISO date-time") from exc
    require(parsed.tzinfo is not None and parsed.utcoffset() is not None, f"{where}: date-time must include offset or Z")


def load_active_targets(path: pathlib.Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    targets = set(TARGET_ID_RE.findall(text))
    require(bool(targets), f"{path}: no active target ids found")
    return targets


def validate_hidden_artifact(value: object, where: str) -> None:
    require(isinstance(value, dict), f"{where}: expected object")
    require(set(value) == {"sha256", "storage_class", "public_content"}, f"{where}: unexpected key set")
    require(isinstance(value["sha256"], str) and DIGEST_RE.fullmatch(value["sha256"]), f"{where}.sha256: invalid digest")
    require(value["storage_class"] in STORAGE_CLASSES, f"{where}.storage_class: invalid value")
    require(value["public_content"] is False, f"{where}.public_content: hidden artifact cannot be public")


def validate_manifest(manifest: object, active_targets: set[str]) -> dict:
    require(isinstance(manifest, dict), "root: expected object")

    required = {
        "schema", "manifest_id", "created_at", "status", "candidate_subject",
        "targets", "case_count", "case_set_artifact", "scoring_key_artifact",
        "exposure_lineage", "custody_evidence", "blind_transfer_use_state",
        "invalidation_reasons", "claim_semantics", "claim_ceiling",
    }
    require(set(manifest) == required, "root: unexpected or missing key set")

    require(manifest["schema"] == SCHEMA, "schema: wrong value")
    require(nonempty(manifest["manifest_id"]), "manifest_id: expected non-empty string")
    parse_datetime(manifest["created_at"], "created_at")

    status = manifest["status"]
    require(status in STATUSES, "status: invalid value")

    candidate = manifest["candidate_subject"]
    require(isinstance(candidate, dict), "candidate_subject: expected object")
    require(set(candidate) == {"subject_id", "binding_kind", "binding"}, "candidate_subject: unexpected key set")
    require(nonempty(candidate["subject_id"]), "candidate_subject.subject_id: expected non-empty string")
    require(candidate["binding_kind"] in BINDING_KINDS, "candidate_subject.binding_kind: invalid value")
    require(nonempty(candidate["binding"]), "candidate_subject.binding: expected non-empty string")

    targets = manifest["targets"]
    require(isinstance(targets, list) and targets, "targets: require non-empty array")
    require(len(targets) == len(set(targets)), "targets: duplicate target id")
    require(all(nonempty(x) for x in targets), "targets: target IDs must be non-empty strings")
    unknown = set(targets) - active_targets
    require(not unknown, f"targets: unknown/non-active target IDs: {sorted(unknown)}")

    count = manifest["case_count"]
    require(isinstance(count, int) and not isinstance(count, bool) and count >= 1, "case_count: expected positive integer")

    validate_hidden_artifact(manifest["case_set_artifact"], "case_set_artifact")
    validate_hidden_artifact(manifest["scoring_key_artifact"], "scoring_key_artifact")
    require(
        manifest["case_set_artifact"]["sha256"] != manifest["scoring_key_artifact"]["sha256"],
        "case and scoring-key artifact digests must differ",
    )

    exposure = manifest["exposure_lineage"]
    require(isinstance(exposure, dict), "exposure_lineage: expected object")
    require(set(exposure) == EXPOSURE_KEYS, "exposure_lineage: unexpected key set")
    require(all(isinstance(exposure[k], bool) for k in EXPOSURE_KEYS), "exposure_lineage: all values must be boolean")
    exposed = [key for key in sorted(EXPOSURE_KEYS) if exposure[key]]

    custody = manifest["custody_evidence"]
    require(isinstance(custody, list) and custody, "custody_evidence: require non-empty array")
    evidence_ids: set[str] = set()
    for index, item in enumerate(custody):
        where = f"custody_evidence[{index}]"
        require(isinstance(item, dict), f"{where}: expected object")
        require(set(item) == {"evidence_id", "evidence_kind", "binding"}, f"{where}: unexpected key set")
        require(nonempty(item["evidence_id"]), f"{where}.evidence_id: expected non-empty string")
        require(item["evidence_id"] not in evidence_ids, f"{where}.evidence_id: duplicate")
        evidence_ids.add(item["evidence_id"])
        require(item["evidence_kind"] in EVIDENCE_KINDS, f"{where}.evidence_kind: invalid value")
        require(nonempty(item["binding"]), f"{where}.binding: expected non-empty string")

    use_state = manifest["blind_transfer_use_state"]
    require(use_state in USE_STATES, "blind_transfer_use_state: invalid value")

    reasons = manifest["invalidation_reasons"]
    require(isinstance(reasons, list), "invalidation_reasons: expected array")
    require(all(nonempty(x) for x in reasons), "invalidation_reasons: entries must be non-empty strings")
    require(len(reasons) == len(set(reasons)), "invalidation_reasons: duplicates")

    if status == "FROZEN_UNEXPOSED":
        require(not exposed, f"FROZEN_UNEXPOSED cannot have exposure flags: {exposed}")
        require(use_state == "ELIGIBLE_TO_ATTEMPT", "FROZEN_UNEXPOSED must be ELIGIBLE_TO_ATTEMPT")
        require(not reasons, "FROZEN_UNEXPOSED cannot carry invalidation reasons")
    elif status == "EXPOSED_REGRESSION_ONLY":
        require(bool(exposed) or bool(reasons), "EXPOSED_REGRESSION_ONLY requires exposure or invalidation reason")
        require(use_state == "REGRESSION_ONLY", "EXPOSED_REGRESSION_ONLY must be REGRESSION_ONLY")
    elif status == "INVALIDATED":
        require(bool(reasons), "INVALIDATED requires at least one invalidation reason")
        require(use_state == "INVALID", "INVALIDATED must be INVALID")

    require(manifest["claim_semantics"] == CLAIM_SEMANTICS, "claim_semantics: invalid value")
    require(nonempty(manifest["claim_ceiling"]), "claim_ceiling: expected non-empty string")

    return {
        "schema": "UNBOUND_SOL_BEHAVIOR_HOLDOUT_VALIDATION_V1",
        "status": "PASS",
        "manifest_id": manifest["manifest_id"],
        "holdout_status": status,
        "blind_transfer_use_state": use_state,
        "target_count": len(targets),
        "case_count": count,
        "exposure_flags_true": exposed,
        "custody_evidence_count": len(custody),
        "claim_ceiling": (
            "This validates manifest consistency only. It does not prove non-exposure, "
            "independent authorship, case quality, scoring correctness, or candidate performance."
        ),
    }


def self_test(active_targets: set[str]) -> None:
    valid = json.loads(DEFAULT_MANIFEST.read_text(encoding="utf-8"))
    validate_manifest(valid, active_targets)

    cases = []

    exposed = json.loads(json.dumps(valid))
    exposed["exposure_lineage"]["training_data"] = True
    cases.append(("unexposed status with training exposure", exposed))

    public_case = json.loads(json.dumps(valid))
    public_case["case_set_artifact"]["public_content"] = True
    cases.append(("public hidden case artifact", public_case))

    no_custody = json.loads(json.dumps(valid))
    no_custody["custody_evidence"] = []
    cases.append(("missing custody evidence", no_custody))

    wrong_use = json.loads(json.dumps(valid))
    wrong_use["blind_transfer_use_state"] = "REGRESSION_ONLY"
    cases.append(("frozen status with regression-only use state", wrong_use))

    bad_target = json.loads(json.dumps(valid))
    bad_target["targets"] = ["NOT_AN_ACTIVE_TARGET"]
    cases.append(("unknown target", bad_target))

    invalid_without_reason = json.loads(json.dumps(valid))
    invalid_without_reason["status"] = "INVALIDATED"
    invalid_without_reason["blind_transfer_use_state"] = "INVALID"
    cases.append(("invalidated without reason", invalid_without_reason))

    for name, candidate in cases:
        try:
            validate_manifest(candidate, active_targets)
        except ValidationError:
            continue
        raise ValidationError(f"self-test failed: invalid case accepted: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Sol Behavior V3 holdout custody manifest.")
    parser.add_argument("path", nargs="?", type=pathlib.Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--targets", type=pathlib.Path, default=DEFAULT_TARGETS)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    active_targets = load_active_targets(args.targets.resolve())

    if args.self_test:
        self_test(active_targets)
        print("behavior holdout manifest validator self-test: PASS")
        return 0

    manifest = json.loads(args.path.read_text(encoding="utf-8"))
    result = validate_manifest(manifest, active_targets)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(
            "behavior holdout manifest: PASS "
            f"(status={result['holdout_status']} cases={result['case_count']})"
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"behavior holdout manifest: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
