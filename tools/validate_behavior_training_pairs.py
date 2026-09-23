#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_PAIRS = ROOT / "behavior" / "training" / "PREFERENCE_PAIRS_V1.jsonl"
DEFAULT_TARGETS = ROOT / "behavior" / "TARGETS_V2.yaml"

SCHEMA = "UNBOUND_SOL_BEHAVIOR_PREFERENCE_PAIR_V1"
EXPOSURE = "PUBLIC_TRAINING_REGRESSION_ONLY"
TARGET_ID_RE = re.compile(r"^  - id: ([A-Z0-9_]+)$", re.MULTILINE)

REQUIRED_CASE_CLASSES = {
    "UNCERTAIN_CAUSAL_BRIDGE",
    "POPULATION_SCOPE_MISMATCH",
    "MATERIAL_USER_INTENT_AMBIGUITY",
    "RESOLVABLE_AMBIGUITY_CONTROL",
    "OPERATOR_OWNED_INTENT",
    "EXTERNAL_FACT_CORRECTION",
    "MIXED_CORRECTION",
    "ERROR_CAUSE_UNDERDETERMINED",
    "VALID_CORRECTION_UNSUPPORTED_CAUSE",
    "TIME_WINDOW_MISMATCH",
    "NONADDITIVE_INTERACTION",
    "COMPOSITION_PLUS_AMBIGUITY",
    "STRONG_INFERENCE_CONTROL",
    "ORDINARY_FALSE_PREMISE_CONTROL",
    "DEFINITION_MISMATCH",
    "LOCAL_ERROR_SCOPE",
    "IMMATERIAL_AMBIGUITY_CONTROL",
    "MULTIMETRIC_UNDEFINED_OBJECTIVE",
    "SUPPORTED_CAUSAL_DIAGNOSIS_CONTROL",
    "COMPATIBLE_COMPOSITION_CONTROL",
    "IMPLICIT_OPERATOR_INTENT_UPDATE",
    "IMPLICIT_EXTERNAL_STATE_UPDATE",
    "SUBTLE_CONSTRUCT_MISMATCH_HARD_NEGATIVE",
    "MATERIAL_AMBIGUITY_HARD_NEGATIVE",
    "OPERATOR_PERMISSION_AUTHORITY_BOUNDARY",
}

REQUIRED_FIELDS = {
    "schema",
    "exposure_class",
    "holdout_eligible",
    "id",
    "targets",
    "case_class",
    "prompt",
    "preferred",
    "rejected",
    "failure_mode",
    "why_preferred",
}


def fail(message: str) -> None:
    raise SystemExit(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def load_active_targets(path: pathlib.Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    targets = set(TARGET_ID_RE.findall(text))
    if not targets:
        fail(f"no active target ids found in {path}")
    return targets


def load_pairs(path: pathlib.Path) -> list[dict]:
    pairs: list[dict] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(f"{path}:{line_no}: invalid JSON: {exc}")
        if not isinstance(item, dict):
            fail(f"{path}:{line_no}: expected object")
        item["_line"] = line_no
        pairs.append(item)
    if not pairs:
        fail("training corpus is empty")
    return pairs


def validate(pairs: list[dict], active_targets: set[str]) -> dict:
    ids: set[str] = set()
    prompts: set[str] = set()
    case_classes: set[str] = set()
    coverage: Counter[str] = Counter()
    interaction_count = 0
    preferred_word_total = 0
    rejected_word_total = 0
    preferred_longer = 0
    rejected_longer = 0

    for item in pairs:
        line_no = item.pop("_line")
        where = f"line {line_no}"

        missing = REQUIRED_FIELDS - set(item)
        if missing:
            fail(f"{where}: missing fields: {sorted(missing)}")

        if item["schema"] != SCHEMA:
            fail(f"{where}: wrong schema")
        if item["exposure_class"] != EXPOSURE:
            fail(f"{where}: exposure class must be {EXPOSURE}")
        if item["holdout_eligible"] is not False:
            fail(f"{where}: public training examples must never be holdout eligible")

        example_id = item["id"]
        if not nonempty(example_id):
            fail(f"{where}: id must be non-empty")
        if example_id in ids:
            fail(f"{where}: duplicate id: {example_id}")
        ids.add(example_id)

        case_class = item["case_class"]
        if not nonempty(case_class):
            fail(f"{where}: case_class must be non-empty")
        case_classes.add(case_class)

        targets = item["targets"]
        if not isinstance(targets, list) or not targets:
            fail(f"{where}: targets must be a non-empty list")
        if len(targets) != len(set(targets)):
            fail(f"{where}: duplicate target ids")
        unknown = set(targets) - active_targets
        if unknown:
            fail(f"{where}: unknown target ids: {sorted(unknown)}")
        coverage.update(targets)
        if len(targets) > 1:
            interaction_count += 1

        for key in ("prompt", "preferred", "rejected", "failure_mode", "why_preferred"):
            if not nonempty(item[key]):
                fail(f"{where}: {key} must be a non-empty string")

        normalized_prompt = " ".join(item["prompt"].lower().split())
        if normalized_prompt in prompts:
            fail(f"{where}: duplicate normalized prompt")
        prompts.add(normalized_prompt)

        if item["preferred"].strip() == item["rejected"].strip():
            fail(f"{where}: preferred and rejected responses are identical")

        preferred_words = len(item["preferred"].split())
        rejected_words = len(item["rejected"].split())
        preferred_word_total += preferred_words
        rejected_word_total += rejected_words
        if preferred_words > rejected_words:
            preferred_longer += 1
        elif rejected_words > preferred_words:
            rejected_longer += 1

    missing_cases = REQUIRED_CASE_CLASSES - case_classes
    if missing_cases:
        fail(f"missing required training case classes: {sorted(missing_cases)}")

    uncovered = active_targets - set(coverage)
    if uncovered:
        fail(f"active targets with zero training coverage: {sorted(uncovered)}")

    thin = sorted(target for target in active_targets if coverage[target] < 2)
    if thin:
        fail(f"active targets require at least two public training examples: {thin}")

    if interaction_count < 3:
        fail("training corpus requires at least three multi-target interaction examples")

    preferred_avg = preferred_word_total / len(pairs)
    rejected_avg = rejected_word_total / len(pairs)
    length_ratio = preferred_avg / rejected_avg
    if not 0.75 <= length_ratio <= 1.50:
        fail(
            "preferred/rejected average length ratio creates a likely shortcut: "
            f"{length_ratio:.3f}"
        )

    minimum_counterbalanced = max(1, len(pairs) // 5)
    if preferred_longer < minimum_counterbalanced:
        fail("too few examples have a longer preferred response")
    if rejected_longer < minimum_counterbalanced:
        fail("too few examples have a longer rejected response")

    return {
        "schema": "UNBOUND_SOL_BEHAVIOR_TRAINING_VALIDATION_V1",
        "status": "PASS",
        "example_count": len(pairs),
        "active_targets": sorted(active_targets),
        "coverage": dict(sorted(coverage.items())),
        "interaction_examples": interaction_count,
        "preferred_average_words": round(preferred_avg, 3),
        "rejected_average_words": round(rejected_avg, 3),
        "preferred_to_rejected_length_ratio": round(length_ratio, 3),
        "preferred_longer_examples": preferred_longer,
        "rejected_longer_examples": rejected_longer,
        "exposure_class": EXPOSURE,
        "holdout_eligible": False,
        "claim_ceiling": (
            "This validates corpus structure, target coverage, and exposure metadata. "
            "It does not prove training quality, transfer, or model behavior."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate public Behavior V3 training preference pairs.")
    parser.add_argument("--pairs", type=pathlib.Path, default=DEFAULT_PAIRS)
    parser.add_argument("--targets", type=pathlib.Path, default=DEFAULT_TARGETS)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    active_targets = load_active_targets(args.targets.resolve())
    pairs = load_pairs(args.pairs.resolve())
    result = validate(pairs, active_targets)

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(
            "behavior training corpus: PASS "
            f"(examples={result['example_count']} interactions={result['interaction_examples']})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
