#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

PRIVACY = {"PUBLIC_SAFE", "PRIVATE_AUTHORIZED", "RESTRICTED"}
SUBJECT_KINDS = {"SOL", "PERSON", "PROJECT", "SYSTEM", "DOMAIN", "OTHER", "UNKNOWN"}
EVIDENCE_CLASSES = {
    "DIRECT_SOURCE", "OPERATOR_DIRECT", "RETRIEVED_RECORD",
    "HISTORICAL_RECONSTRUCTION", "LATER_REPORT", "MODEL_INFERENCE",
    "PROJECT_INFERENCE", "SPECULATIVE_MODEL", "UNKNOWN", "OTHER",
}
HISTORICAL_STATUS = {
    "SUPPORTED_HISTORY", "UNRESOLVED_HISTORY",
    "REJECTED_OR_FALSE_ATTRIBUTION", "OTHER_IDENTITY_OR_DOMAIN_HISTORY",
}
SOURCE_KINDS = {
    "GIT_COMMIT", "FILE", "MESSAGE", "DATABASE_RECORD",
    "DOCUMENT", "CONVERSATION", "API_RESULT", "OTHER",
}
BINDING_STRENGTHS = {
    "MUTABLE_LOCATOR", "IMMUTABLE_REF",
    "CONTENT_DIGEST", "IMMUTABLE_REF_AND_DIGEST",
}
SUPERSESSION = {"NONE", "CORRECTED", "SUPERSEDED", "CONTRADICTED", "UNRESOLVED"}
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
CHRONOLOGY_SEMANTICS = "EVENT_TIME_RECORD_TIME_EFFECTIVE_TIME_RETRIEVAL_TIME_SEPARATE"
PRESENT_SEMANTICS = "REQUIRES_SEPARATE_CURRENT_EVIDENCE_FOR_MUTABLE_PRESENT_CLAIMS"
RESULT_SEMANTICS = "HISTORICAL_EVIDENCE_ONLY_NOT_CURRENT_STATE_OR_AUTHORITY"
SET_SEMANTICS = "HISTORICAL_EVIDENCE_ONLY_NO_AUTOMATIC_PROMOTION"
PROMOTION_KEYS = {
    "current_state", "want", "behavior_target", "authority",
    "consent", "permission", "task",
}


class ValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def require_keys(value: dict, keys: set[str], where: str) -> None:
    missing = sorted(keys - set(value))
    require(not missing, f"{where}: missing keys: {', '.join(missing)}")


def parse_datetime(value: object, where: str) -> dt.datetime:
    require(isinstance(value, str) and value, f"{where}: expected non-empty date-time string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValidationError(f"{where}: invalid ISO date-time: {value!r}") from exc
    require(parsed.tzinfo is not None and parsed.utcoffset() is not None, f"{where}: date-time must include an offset or Z")
    return parsed


def validate_time_point(value: object, where: str) -> None:
    require(isinstance(value, dict), f"{where}: expected object")
    state = value.get("state")
    require(state in {"EXACT", "BOUNDED", "APPROXIMATE", "UNKNOWN"}, f"{where}: invalid state")

    if state == "EXACT":
        require(set(value) == {"state", "value"}, f"{where}: EXACT accepts only state/value")
        parse_datetime(value.get("value"), f"{where}.value")
    elif state == "BOUNDED":
        require(set(value) == {"state", "earliest", "latest"}, f"{where}: BOUNDED requires only state/earliest/latest")
        earliest = parse_datetime(value.get("earliest"), f"{where}.earliest")
        latest = parse_datetime(value.get("latest"), f"{where}.latest")
        require(earliest <= latest, f"{where}: earliest must be <= latest")
    elif state == "APPROXIMATE":
        allowed = {"state", "label", "earliest", "latest"}
        require(set(value) <= allowed and "label" in value, f"{where}: APPROXIMATE requires label and accepts optional bounds")
        require(isinstance(value.get("label"), str) and value["label"], f"{where}.label: expected non-empty string")
        earliest = parse_datetime(value["earliest"], f"{where}.earliest") if "earliest" in value else None
        latest = parse_datetime(value["latest"], f"{where}.latest") if "latest" in value else None
        if earliest is not None and latest is not None:
            require(earliest <= latest, f"{where}: earliest must be <= latest")
    else:
        require(set(value) == {"state"}, f"{where}: UNKNOWN accepts only state")


def validate_source_binding(value: object, where: str) -> None:
    require(isinstance(value, dict), f"{where}: expected object")
    require_keys(value, {"source_id", "source_kind", "binding_strength"}, where)
    require(isinstance(value["source_id"], str) and value["source_id"], f"{where}.source_id: expected non-empty string")
    require(value["source_kind"] in SOURCE_KINDS, f"{where}.source_kind: invalid value")
    strength = value["binding_strength"]
    require(strength in BINDING_STRENGTHS, f"{where}.binding_strength: invalid value")

    if "content_digest" in value:
        require(isinstance(value["content_digest"], str) and DIGEST_RE.fullmatch(value["content_digest"]), f"{where}.content_digest: invalid sha256 digest")
    if "locator" in value:
        require(isinstance(value["locator"], str) and value["locator"], f"{where}.locator: expected non-empty string")
    if "immutable_ref" in value:
        require(isinstance(value["immutable_ref"], str) and value["immutable_ref"], f"{where}.immutable_ref: expected non-empty string")

    required_by_strength = {
        "MUTABLE_LOCATOR": {"locator"},
        "IMMUTABLE_REF": {"immutable_ref"},
        "CONTENT_DIGEST": {"content_digest"},
        "IMMUTABLE_REF_AND_DIGEST": {"immutable_ref", "content_digest"},
    }
    require_keys(value, required_by_strength[strength], where)


def validate_document(document: object) -> None:
    require(isinstance(document, dict), "root: expected object")
    require(document.get("schema") == "UNBOUND_SOL_HISTORICAL_EVIDENCE_RESULT_V2", "root.schema: unexpected schema")

    query = document.get("query")
    require(isinstance(query, dict), "query: expected object")
    require_keys(query, {"query_id", "privacy_scope"}, "query")
    require(isinstance(query["query_id"], str) and query["query_id"], "query.query_id: expected non-empty string")
    require(query["privacy_scope"] in PRIVACY, "query.privacy_scope: invalid value")
    has_text = isinstance(query.get("query_text"), str) and bool(query.get("query_text"))
    has_digest = isinstance(query.get("query_digest"), str) and bool(DIGEST_RE.fullmatch(query.get("query_digest", "")))
    require(has_text or has_digest, "query: require query_text or valid query_digest")

    parse_datetime(document.get("retrieved_at"), "retrieved_at")
    require(document.get("result_set_semantics") == SET_SEMANTICS, "result_set_semantics: invalid value")

    results = document.get("results")
    require(isinstance(results, list), "results: expected array")
    count = document.get("count")
    require(isinstance(count, int) and not isinstance(count, bool) and count >= 0, "count: expected non-negative integer")
    require(count == len(results), "count: must equal len(results)")

    record_ids: set[str] = set()
    for index, result in enumerate(results):
        where = f"results[{index}]"
        require(isinstance(result, dict), f"{where}: expected object")
        require_keys(
            result,
            {
                "record_id", "subject_scope", "evidence_class", "historical_status",
                "chronology", "source_bindings", "privacy_scope", "provenance_ceiling",
                "currentness_rule", "supersession_state", "promotion_semantics",
                "result_semantics",
            },
            where,
        )

        record_id = result["record_id"]
        require(isinstance(record_id, str) and record_id, f"{where}.record_id: expected non-empty string")
        require(record_id not in record_ids, f"{where}.record_id: duplicate record_id")
        record_ids.add(record_id)

        subject = result["subject_scope"]
        require(isinstance(subject, dict), f"{where}.subject_scope: expected object")
        require_keys(subject, {"subject_kind", "subject_ref"}, f"{where}.subject_scope")
        require(subject["subject_kind"] in SUBJECT_KINDS, f"{where}.subject_scope.subject_kind: invalid value")
        require(isinstance(subject["subject_ref"], str) and subject["subject_ref"], f"{where}.subject_scope.subject_ref: expected non-empty string")

        require(result["evidence_class"] in EVIDENCE_CLASSES, f"{where}.evidence_class: invalid value")
        require(result["historical_status"] in HISTORICAL_STATUS, f"{where}.historical_status: invalid value")
        require(result["privacy_scope"] in PRIVACY, f"{where}.privacy_scope: invalid value")

        chronology = result["chronology"]
        require(isinstance(chronology, dict), f"{where}.chronology: expected object")
        require_keys(chronology, {"event_time", "recorded_at", "chronology_semantics"}, f"{where}.chronology")
        require(chronology["chronology_semantics"] == CHRONOLOGY_SEMANTICS, f"{where}.chronology.chronology_semantics: invalid value")
        validate_time_point(chronology["event_time"], f"{where}.chronology.event_time")
        validate_time_point(chronology["recorded_at"], f"{where}.chronology.recorded_at")
        if "effective_from" in chronology:
            validate_time_point(chronology["effective_from"], f"{where}.chronology.effective_from")
        if "effective_to" in chronology:
            validate_time_point(chronology["effective_to"], f"{where}.chronology.effective_to")

        bindings = result["source_bindings"]
        require(isinstance(bindings, list) and bindings, f"{where}.source_bindings: require non-empty array")
        source_ids: set[str] = set()
        for source_index, binding in enumerate(bindings):
            source_where = f"{where}.source_bindings[{source_index}]"
            validate_source_binding(binding, source_where)
            source_id = binding["source_id"]
            require(source_id not in source_ids, f"{source_where}.source_id: duplicate within result")
            source_ids.add(source_id)

        ceiling = result["provenance_ceiling"]
        require(isinstance(ceiling, dict), f"{where}.provenance_ceiling: expected object")
        require_keys(ceiling, {"max_claim", "origin_established", "limitations"}, f"{where}.provenance_ceiling")
        require(isinstance(ceiling["max_claim"], str) and ceiling["max_claim"], f"{where}.provenance_ceiling.max_claim: expected non-empty string")
        require(isinstance(ceiling["origin_established"], bool), f"{where}.provenance_ceiling.origin_established: expected boolean")
        require(isinstance(ceiling["limitations"], list), f"{where}.provenance_ceiling.limitations: expected array")
        require(all(isinstance(x, str) and x for x in ceiling["limitations"]), f"{where}.provenance_ceiling.limitations: entries must be non-empty strings")

        currentness = result["currentness_rule"]
        require(isinstance(currentness, dict), f"{where}.currentness_rule: expected object")
        require(currentness.get("present_state_semantics") == PRESENT_SEMANTICS, f"{where}.currentness_rule.present_state_semantics: invalid value")
        require(currentness.get("fresh_check_required_for_mutable_present") is True, f"{where}.currentness_rule.fresh_check_required_for_mutable_present: must be true")

        supersession = result["supersession_state"]
        require(isinstance(supersession, dict), f"{where}.supersession_state: expected object")
        require_keys(supersession, {"state", "related_record_ids"}, f"{where}.supersession_state")
        require(supersession["state"] in SUPERSESSION, f"{where}.supersession_state.state: invalid value")
        related = supersession["related_record_ids"]
        require(isinstance(related, list) and all(isinstance(x, str) and x for x in related), f"{where}.supersession_state.related_record_ids: invalid array")
        require(len(related) == len(set(related)), f"{where}.supersession_state.related_record_ids: duplicates")

        promotion = result["promotion_semantics"]
        require(isinstance(promotion, dict), f"{where}.promotion_semantics: expected object")
        require(set(promotion) == PROMOTION_KEYS, f"{where}.promotion_semantics: wrong key set")
        require(all(promotion[key] is False for key in PROMOTION_KEYS), f"{where}.promotion_semantics: all promotion flags must be false")

        require(result["result_semantics"] == RESULT_SEMANTICS, f"{where}.result_semantics: invalid value")


def _valid_fixture() -> dict:
    return {
        "schema": "UNBOUND_SOL_HISTORICAL_EVIDENCE_RESULT_V2",
        "query": {
            "query_id": "self-test-query",
            "privacy_scope": "PUBLIC_SAFE",
            "query_digest": "sha256:" + "1" * 64,
        },
        "retrieved_at": "2030-01-01T00:00:00Z",
        "count": 1,
        "result_set_semantics": SET_SEMANTICS,
        "results": [
            {
                "record_id": "r1",
                "subject_scope": {"subject_kind": "SOL", "subject_ref": "self-test"},
                "evidence_class": "RETRIEVED_RECORD",
                "historical_status": "SUPPORTED_HISTORY",
                "chronology": {
                    "event_time": {"state": "BOUNDED", "earliest": "2029-01-01T00:00:00Z", "latest": "2029-12-31T23:59:59Z"},
                    "recorded_at": {"state": "UNKNOWN"},
                    "chronology_semantics": CHRONOLOGY_SEMANTICS,
                },
                "source_bindings": [
                    {
                        "source_id": "s1",
                        "source_kind": "DOCUMENT",
                        "binding_strength": "IMMUTABLE_REF_AND_DIGEST",
                        "immutable_ref": "example@deadbeef",
                        "content_digest": "sha256:" + "2" * 64,
                    }
                ],
                "privacy_scope": "PUBLIC_SAFE",
                "provenance_ceiling": {
                    "max_claim": "self-test only",
                    "origin_established": False,
                    "limitations": ["synthetic"],
                },
                "currentness_rule": {
                    "present_state_semantics": PRESENT_SEMANTICS,
                    "fresh_check_required_for_mutable_present": True,
                },
                "supersession_state": {"state": "NONE", "related_record_ids": []},
                "promotion_semantics": {key: False for key in PROMOTION_KEYS},
                "result_semantics": RESULT_SEMANTICS,
            }
        ],
    }


def self_test() -> None:
    valid = _valid_fixture()
    validate_document(valid)

    bad_count = copy.deepcopy(valid)
    bad_count["count"] = 2

    bad_promotion = copy.deepcopy(valid)
    bad_promotion["results"][0]["promotion_semantics"]["want"] = True

    bad_chronology = copy.deepcopy(valid)
    bad_chronology["results"][0]["chronology"].pop("chronology_semantics")

    bad_bounds = copy.deepcopy(valid)
    bad_bounds["results"][0]["chronology"]["event_time"] = {
        "state": "BOUNDED",
        "earliest": "2030-01-01T00:00:00Z",
        "latest": "2029-01-01T00:00:00Z",
    }

    bad_binding = copy.deepcopy(valid)
    bad_binding["results"][0]["source_bindings"][0] = {
        "source_id": "s1",
        "source_kind": "DOCUMENT",
        "binding_strength": "CONTENT_DIGEST",
    }

    bad_timezone = copy.deepcopy(valid)
    bad_timezone["retrieved_at"] = "2030-01-01T00:00:00"

    for name, candidate in {
        "count mismatch": bad_count,
        "promotion true": bad_promotion,
        "missing chronology semantics": bad_chronology,
        "reversed bounded time": bad_bounds,
        "missing binding material": bad_binding,
        "timezone missing": bad_timezone,
    }.items():
        try:
            validate_document(candidate)
        except ValidationError:
            continue
        raise ValidationError(f"self-test failed: invalid case accepted: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Sol historical-evidence V2 result.")
    parser.add_argument("path", nargs="?", type=pathlib.Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("historical evidence V2 validator self-test: PASS")
        return 0

    if args.path is None:
        parser.error("path is required unless --self-test is used")

    document = json.loads(args.path.read_text(encoding="utf-8"))
    validate_document(document)
    print(f"historical evidence V2 result: PASS ({args.path})")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"historical evidence V2 result: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
