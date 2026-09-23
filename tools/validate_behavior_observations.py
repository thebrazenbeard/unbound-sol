#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = ROOT / "behavior" / "observations" / "OBSERVATIONS_V1.jsonl"
DEFAULT_TARGETS = ROOT / "behavior" / "TARGETS_V2.yaml"

SCHEMA = "UNBOUND_SOL_BEHAVIOR_OBSERVATION_V1"
RESULT_SEMANTICS = "OBSERVED_BEHAVIOR_DIAGNOSTIC_ONLY_NOT_TARGET_AUTHORITY"
TARGET_ID_RE = re.compile(r"^  - id: ([A-Z0-9_]+)$", re.MULTILINE)
CLASSES = {
    "CORRECTED_ERROR",
    "SELF_CORRECTED_ERROR",
    "RECOVERY_BEFORE_FINAL_CLAIM",
    "SUCCESS",
    "MIXED",
}
CAUSE_STATUSES = {"UNDETERMINED", "SUPPORTED", "NOT_APPLICABLE"}
PROMOTION_KEYS = {"want_admission", "behavior_target_admission", "training_admission"}


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


def load_targets(path: pathlib.Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    targets = set(TARGET_ID_RE.findall(text))
    require(bool(targets), f"{path}: no active target IDs found")
    return targets


def load_records(path: pathlib.Path) -> list[dict]:
    records = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValidationError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
        require(isinstance(item, dict), f"{path}:{line_no}: expected object")
        item["_line"] = line_no
        records.append(item)
    require(bool(records), "observation ledger is empty")
    return records


def validate(records: list[dict], active_targets: set[str]) -> dict:
    ids: set[str] = set()
    counts: dict[str, int] = {name: 0 for name in sorted(CLASSES)}

    for raw in records:
        item = dict(raw)
        line = item.pop("_line")
        where = f"line {line}"

        required = {
            "schema", "id", "observed_at", "observation_class", "summary",
            "observed_behavior", "error_characterization", "causal_diagnosis",
            "relevant_targets", "evidence_bindings", "promotion_semantics",
            "public_safe", "result_semantics",
        }
        missing = required - set(item)
        require(not missing, f"{where}: missing fields: {sorted(missing)}")

        require(item["schema"] == SCHEMA, f"{where}: wrong schema")
        require(nonempty(item["id"]), f"{where}: id must be non-empty")
        require(item["id"] not in ids, f"{where}: duplicate id: {item['id']}")
        ids.add(item["id"])

        parse_datetime(item["observed_at"], f"{where}.observed_at")
        observation_class = item["observation_class"]
        require(observation_class in CLASSES, f"{where}: invalid observation_class")
        counts[observation_class] += 1

        require(nonempty(item["summary"]), f"{where}: summary must be non-empty")
        require(nonempty(item["observed_behavior"]), f"{where}: observed_behavior must be non-empty")

        error_characterization = item["error_characterization"]
        if observation_class in {"CORRECTED_ERROR", "SELF_CORRECTED_ERROR"}:
            require(nonempty(error_characterization), f"{where}: corrected errors require error_characterization")
        else:
            require(error_characterization is None or nonempty(error_characterization), f"{where}: invalid error_characterization")

        causal = item["causal_diagnosis"]
        require(isinstance(causal, dict), f"{where}: causal_diagnosis must be object")
        require(set(causal) == {"status", "claim", "evidence_bindings"}, f"{where}: causal_diagnosis key set mismatch")
        status = causal["status"]
        require(status in CAUSE_STATUSES, f"{where}: invalid causal status")
        require(isinstance(causal["evidence_bindings"], list), f"{where}: causal evidence_bindings must be array")
        require(all(nonempty(x) for x in causal["evidence_bindings"]), f"{where}: causal evidence bindings must be non-empty strings")

        if status == "SUPPORTED":
            require(nonempty(causal["claim"]), f"{where}: SUPPORTED causal diagnosis requires claim")
            require(bool(causal["evidence_bindings"]), f"{where}: SUPPORTED causal diagnosis requires separate causal evidence")
        else:
            require(causal["claim"] is None, f"{where}: unsupported causal diagnosis must not carry a cause claim")

        targets = item["relevant_targets"]
        require(isinstance(targets, list) and targets, f"{where}: relevant_targets must be non-empty array")
        require(len(targets) == len(set(targets)), f"{where}: duplicate relevant target")
        unknown = set(targets) - active_targets
        require(not unknown, f"{where}: unknown/non-active target references: {sorted(unknown)}")

        evidence = item["evidence_bindings"]
        require(isinstance(evidence, list) and evidence, f"{where}: evidence_bindings must be non-empty array")
        require(all(nonempty(x) for x in evidence), f"{where}: evidence bindings must be non-empty strings")
        require(len(evidence) == len(set(evidence)), f"{where}: duplicate evidence binding")

        promotion = item["promotion_semantics"]
        require(isinstance(promotion, dict), f"{where}: promotion_semantics must be object")
        require(set(promotion) == PROMOTION_KEYS, f"{where}: promotion_semantics key set mismatch")
        require(all(promotion[key] is False for key in PROMOTION_KEYS), f"{where}: observation must not auto-promote into wants, targets, or training")

        require(item["public_safe"] is True, f"{where}: public_safe must be true")
        require(item["result_semantics"] == RESULT_SEMANTICS, f"{where}: invalid result_semantics")

    return {
        "schema": "UNBOUND_SOL_BEHAVIOR_OBSERVATION_VALIDATION_V1",
        "status": "PASS",
        "record_count": len(records),
        "classes": {k: v for k, v in counts.items() if v},
        "active_target_count": len(active_targets),
        "target_authority": False,
        "training_authority": False,
        "claim_ceiling": (
            "This validates public-safe observation-record structure and anti-promotion semantics. "
            "It does not prove causal diagnosis, target correctness, training value, or behavioral improvement."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate public-safe Sol behavior observations.")
    parser.add_argument("--ledger", type=pathlib.Path, default=DEFAULT_LEDGER)
    parser.add_argument("--targets", type=pathlib.Path, default=DEFAULT_TARGETS)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    active_targets = load_targets(args.targets.resolve())
    records = load_records(args.ledger.resolve())
    result = validate(records, active_targets)

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"behavior observations: PASS (records={result['record_count']})")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"behavior observations: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
