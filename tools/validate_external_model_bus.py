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

DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
PROVIDER_SCHEMA = "UNBOUND_SOL_MODEL_PROVIDER_ADVERTISEMENT_V1"
RECEIPT_SCHEMA = "UNBOUND_SOL_MODEL_INFERENCE_RECEIPT_V1"
PROVIDER_CURRENTNESS = "ADVERTISEMENT_IS_OBSERVATION_NOT_PERMANENT_TRUTH"
RECEIPT_DIGEST_SEMANTICS = "SHA256_CANONICAL_JSON_EXCLUDING_RECEIPT_DIGEST"

CAPABILITY_OPERATIONS = {
    "INFER", "EMBED", "RERANK", "TOOL_CALL_PROPOSAL", "SOURCE_DISCOVERY_PROPOSAL"
}
OUTPUT_EVIDENCE_CLASSES = {
    "GENERATED_INFERENCE", "GENERATED_PROPOSAL", "EMBEDDING_SIGNAL", "SOURCE_POINTER_CANDIDATE"
}
PROVIDER_KINDS = {"LOCAL", "REMOTE", "HYBRID"}
HEALTH = {"READY", "DEGRADED", "UNAVAILABLE", "UNKNOWN"}
DEPENDENCY_ROLES = {
    "OPTIONAL_INSTRUMENT", "CAPABILITY_DEGRADING_DEPENDENCY", "CONTINUITY_BEARING_DEPENDENCY"
}
PROVENANCE_STATUS = {"COMPLETE", "PARTIAL", "UNKNOWN"}
REPLAY = {
    "NONDETERMINISTIC_REEXECUTION",
    "DETERMINISTIC_IF_SUBJECT_AND_SETTINGS_BOUND",
    "UNSUPPORTED",
    "UNKNOWN",
}
PROMPT_EGRESS = {"LOCAL_ONLY", "LEAVES_LOCAL_DEVICE", "UNKNOWN"}
RETENTION = {"NO_PROVIDER_RETENTION", "PROVIDER_RETENTION", "UNKNOWN"}


class ValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def parse_datetime(value: object, where: str) -> dt.datetime:
    require(isinstance(value, str) and value, f"{where}: expected non-empty datetime")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValidationError(f"{where}: invalid datetime: {value!r}") from exc
    require(parsed.tzinfo is not None and parsed.utcoffset() is not None, f"{where}: timezone/offset required")
    return parsed


def require_digest(value: object, where: str) -> None:
    require(isinstance(value, str) and DIGEST_RE.fullmatch(value), f"{where}: invalid sha256 digest")


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def canonical_digest(value: object) -> str:
    return "sha256:" + hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def provider_advertisement_digest(provider: dict) -> str:
    return canonical_digest(provider)


def inference_receipt_digest(receipt: dict) -> str:
    material = copy.deepcopy(receipt)
    material.pop("receipt_digest", None)
    return canonical_digest(material)


def validate_provider(provider: object) -> None:
    require(isinstance(provider, dict), "provider: expected object")
    require(provider.get("schema") == PROVIDER_SCHEMA, "provider.schema: unexpected schema")
    require(isinstance(provider.get("provider_id"), str) and provider["provider_id"], "provider_id: required")
    require(provider.get("provider_kind") in PROVIDER_KINDS, "provider_kind: invalid")

    runtime = provider.get("runtime")
    require(isinstance(runtime, dict), "runtime: expected object")
    require(isinstance(runtime.get("name"), str) and runtime["name"], "runtime.name: required")
    require(isinstance(runtime.get("version"), str) and runtime["version"], "runtime.version: required")
    if runtime.get("artifact_digest") is not None:
        require_digest(runtime["artifact_digest"], "runtime.artifact_digest")

    observed = parse_datetime(provider.get("observed_at"), "observed_at")

    health = provider.get("health")
    require(isinstance(health, dict), "health: expected object")
    require(health.get("status") in HEALTH, "health.status: invalid")
    checked = parse_datetime(health.get("checked_at"), "health.checked_at")
    require(checked <= observed, "health.checked_at must not be later than observed_at")

    dependency = provider.get("dependency_role")
    require(dependency in DEPENDENCY_ROLES, "dependency_role: invalid")
    if dependency == "CONTINUITY_BEARING_DEPENDENCY":
        require(
            isinstance(provider.get("replacement_plan"), str) and bool(provider["replacement_plan"].strip()),
            "continuity-bearing provider requires non-empty replacement_plan",
        )

    require(provider.get("authority_ceiling") == "NO_EFFECT_AUTHORITY", "authority_ceiling must be NO_EFFECT_AUTHORITY")

    capabilities = provider.get("capabilities")
    require(isinstance(capabilities, list) and capabilities, "capabilities: require non-empty array")
    seen_names: set[str] = set()
    for index, capability in enumerate(capabilities):
        where = f"capabilities[{index}]"
        require(isinstance(capability, dict), f"{where}: expected object")
        name = capability.get("name")
        require(isinstance(name, str) and name, f"{where}.name: required")
        require(name not in seen_names, f"{where}.name: duplicate")
        seen_names.add(name)
        require(capability.get("declared") is True, f"{where}.declared: must be true")
        for axis in ("active", "healthy", "qualified"):
            require(capability.get(axis) in (True, False, None), f"{where}.{axis}: expected boolean/null")
        operations = capability.get("operations")
        require(
            isinstance(operations, list)
            and operations
            and len(operations) == len(set(operations))
            and all(op in CAPABILITY_OPERATIONS for op in operations),
            f"{where}.operations: invalid",
        )
        evidence = capability.get("output_evidence_classes")
        require(
            isinstance(evidence, list)
            and evidence
            and len(evidence) == len(set(evidence))
            and all(item in OUTPUT_EVIDENCE_CLASSES for item in evidence),
            f"{where}.output_evidence_classes: invalid",
        )
        if capability.get("qualified") is True:
            require(
                isinstance(capability.get("qualification_ref"), str)
                and bool(capability["qualification_ref"].strip()),
                f"{where}.qualification_ref required when qualified=true",
            )

    provenance = provider.get("provenance")
    require(isinstance(provenance, dict), "provenance: expected object")
    status = provenance.get("status")
    require(status in PROVENANCE_STATUS, "provenance.status: invalid")
    require(isinstance(provenance.get("model_id"), str) and provenance["model_id"], "provenance.model_id: required")
    missing = provenance.get("missing_fields")
    require(
        isinstance(missing, list)
        and len(missing) == len(set(missing))
        and all(isinstance(item, str) and item for item in missing),
        "provenance.missing_fields: invalid",
    )
    for key in ("model_artifact_digest", "adapter_digest"):
        if provenance.get(key) is not None:
            require_digest(provenance[key], f"provenance.{key}")
    core = ("model_source", "model_revision", "model_artifact_digest", "prompt_template_id")
    if status == "COMPLETE":
        require(not missing, "complete provenance requires empty missing_fields")
        for key in core:
            require(provenance.get(key) not in (None, ""), f"complete provenance requires {key}")
    elif status == "PARTIAL":
        require(bool(missing), "partial provenance requires non-empty missing_fields")
    else:
        require(bool(missing), "unknown provenance requires missing_fields to explain what is unknown")

    replay = provider.get("replay")
    require(isinstance(replay, dict), "replay: expected object")
    require(replay.get("semantics") in REPLAY, "replay.semantics: invalid")
    require(isinstance(replay.get("idempotency_key_supported"), bool), "replay.idempotency_key_supported: expected boolean")

    privacy = provider.get("privacy")
    require(isinstance(privacy, dict), "privacy: expected object")
    require(privacy.get("prompt_egress") in PROMPT_EGRESS, "privacy.prompt_egress: invalid")
    require(privacy.get("retention_status") in RETENTION, "privacy.retention_status: invalid")
    if provider.get("provider_kind") == "REMOTE" and privacy.get("prompt_egress") == "LOCAL_ONLY":
        raise ValidationError("remote provider cannot truthfully advertise prompt_egress=LOCAL_ONLY")

    currentness = provider.get("currentness")
    require(isinstance(currentness, dict), "currentness: expected object")
    require(
        isinstance(currentness.get("max_age_seconds"), int)
        and not isinstance(currentness["max_age_seconds"], bool)
        and currentness["max_age_seconds"] >= 0,
        "currentness.max_age_seconds: expected non-negative integer",
    )
    require(currentness.get("semantics") == PROVIDER_CURRENTNESS, "currentness.semantics: invalid")

    envelope = provider.get("resource_envelope")
    if envelope is not None:
        require(isinstance(envelope, dict), "resource_envelope: expected object")
        numeric_positive = ("max_context_tokens", "max_output_tokens", "concurrency_limit")
        for key in numeric_positive:
            value = envelope.get(key)
            if value is not None:
                require(isinstance(value, int) and not isinstance(value, bool) and value >= 1, f"resource_envelope.{key}: invalid")
        timeout = envelope.get("timeout_seconds")
        if timeout is not None:
            require(isinstance(timeout, (int, float)) and not isinstance(timeout, bool) and timeout > 0, "resource_envelope.timeout_seconds: invalid")
        retries = envelope.get("retry_limit")
        if retries is not None:
            require(isinstance(retries, int) and not isinstance(retries, bool) and retries >= 0, "resource_envelope.retry_limit: invalid")


def validate_receipt(receipt: object, provider: dict | None = None) -> None:
    require(isinstance(receipt, dict), "receipt: expected object")
    require(receipt.get("schema") == RECEIPT_SCHEMA, "receipt.schema: unexpected schema")
    require(isinstance(receipt.get("request_id"), str) and receipt["request_id"], "request_id: required")
    require(isinstance(receipt.get("provider_id"), str) and receipt["provider_id"], "provider_id: required")
    require_digest(receipt.get("provider_advertisement_digest"), "provider_advertisement_digest")
    parse_datetime(receipt.get("observed_at"), "receipt.observed_at")
    require_digest(receipt.get("generation_settings_digest"), "generation_settings_digest")
    require_digest(receipt.get("input_context_digest"), "input_context_digest")
    require(receipt.get("output_evidence_class") in {"GENERATED_INFERENCE", "GENERATED_PROPOSAL"}, "output_evidence_class: invalid")
    require(isinstance(receipt.get("output"), str), "output: expected string")
    require(isinstance(receipt.get("proposed_tool_calls"), list), "proposed_tool_calls: expected array")
    require(receipt.get("effect_authority") == "NONE_PROPOSALS_ONLY", "effect_authority must be NONE_PROPOSALS_ONLY")
    require(receipt.get("digest_semantics") == RECEIPT_DIGEST_SEMANTICS, "digest_semantics: invalid")
    require_digest(receipt.get("receipt_digest"), "receipt_digest")

    model = receipt.get("model_subject")
    require(isinstance(model, dict), "model_subject: expected object")
    require(isinstance(model.get("model_id"), str) and model["model_id"], "model_subject.model_id: required")
    require(isinstance(model.get("runtime_name"), str) and model["runtime_name"], "model_subject.runtime_name: required")
    require(isinstance(model.get("runtime_version"), str) and model["runtime_version"], "model_subject.runtime_version: required")
    require(model.get("provenance_status") in PROVENANCE_STATUS, "model_subject.provenance_status: invalid")
    for key in ("model_artifact_digest", "adapter_digest"):
        if model.get(key) is not None:
            require_digest(model[key], f"model_subject.{key}")

    truncation = receipt.get("truncation")
    require(isinstance(truncation, dict), "truncation: expected object")
    require(isinstance(truncation.get("occurred"), bool), "truncation.occurred: expected boolean")
    if truncation["occurred"]:
        require(isinstance(truncation.get("reason"), str) and truncation["reason"], "truncation.reason required when occurred=true")

    timing = receipt.get("timing")
    require(isinstance(timing, dict), "timing: expected object")
    require(isinstance(timing.get("elapsed_ms"), int) and not isinstance(timing["elapsed_ms"], bool) and timing["elapsed_ms"] >= 0, "timing.elapsed_ms: invalid")

    expected_digest = inference_receipt_digest(receipt)
    require(receipt["receipt_digest"] == expected_digest, "receipt_digest does not match canonical receipt content")

    if provider is not None:
        validate_provider(provider)
        require(receipt["provider_id"] == provider["provider_id"], "receipt provider_id does not match provider advertisement")
        require(
            receipt["provider_advertisement_digest"] == provider_advertisement_digest(provider),
            "receipt provider_advertisement_digest does not bind supplied provider advertisement",
        )
        require(model["model_id"] == provider["provenance"]["model_id"], "receipt model_id does not match advertised model subject")
        require(model["runtime_name"] == provider["runtime"]["name"], "receipt runtime_name does not match provider advertisement")
        require(model["runtime_version"] == provider["runtime"]["version"], "receipt runtime_version does not match provider advertisement")


def _provider_fixture() -> dict:
    return {
        "schema": PROVIDER_SCHEMA,
        "provider_id": "provider-self-test",
        "provider_kind": "LOCAL",
        "runtime": {
            "name": "runtime",
            "version": "1.0.0",
            "artifact_digest": "sha256:" + "1" * 64,
        },
        "observed_at": "2030-01-01T00:00:10Z",
        "health": {"status": "READY", "checked_at": "2030-01-01T00:00:00Z", "details": None},
        "dependency_role": "OPTIONAL_INSTRUMENT",
        "replacement_plan": None,
        "authority_ceiling": "NO_EFFECT_AUTHORITY",
        "capabilities": [
            {
                "name": "reasoning",
                "declared": True,
                "active": True,
                "healthy": True,
                "qualified": True,
                "qualification_ref": "qualification:self-test",
                "operations": ["INFER", "TOOL_CALL_PROPOSAL"],
                "output_evidence_classes": ["GENERATED_INFERENCE", "GENERATED_PROPOSAL"],
            }
        ],
        "provenance": {
            "status": "COMPLETE",
            "model_id": "model-self-test",
            "model_source": "example/source",
            "model_revision": "deadbeef",
            "model_artifact_digest": "sha256:" + "2" * 64,
            "adapter_digest": None,
            "prompt_template_id": "template-v1",
            "missing_fields": [],
        },
        "replay": {
            "semantics": "NONDETERMINISTIC_REEXECUTION",
            "idempotency_key_supported": True,
        },
        "privacy": {
            "prompt_egress": "LOCAL_ONLY",
            "retention_status": "NO_PROVIDER_RETENTION",
            "notes": None,
        },
        "currentness": {
            "max_age_seconds": 300,
            "semantics": PROVIDER_CURRENTNESS,
        },
        "resource_envelope": {
            "max_context_tokens": 8192,
            "max_output_tokens": 1024,
            "timeout_seconds": 60,
            "concurrency_limit": 1,
            "retry_limit": 1,
        },
    }


def _receipt_fixture(provider: dict) -> dict:
    receipt = {
        "schema": RECEIPT_SCHEMA,
        "request_id": "request-self-test",
        "provider_id": provider["provider_id"],
        "provider_advertisement_digest": provider_advertisement_digest(provider),
        "observed_at": "2030-01-01T00:00:20Z",
        "model_subject": {
            "model_id": provider["provenance"]["model_id"],
            "runtime_name": provider["runtime"]["name"],
            "runtime_version": provider["runtime"]["version"],
            "model_artifact_digest": provider["provenance"]["model_artifact_digest"],
            "adapter_digest": None,
            "prompt_template_id": provider["provenance"]["prompt_template_id"],
            "provenance_status": provider["provenance"]["status"],
        },
        "generation_settings_digest": "sha256:" + "3" * 64,
        "input_context_digest": "sha256:" + "4" * 64,
        "output": "synthetic output",
        "output_evidence_class": "GENERATED_INFERENCE",
        "proposed_tool_calls": [],
        "truncation": {"occurred": False, "reason": None},
        "timing": {"elapsed_ms": 25},
        "effect_authority": "NONE_PROPOSALS_ONLY",
        "error": None,
        "digest_semantics": RECEIPT_DIGEST_SEMANTICS,
        "receipt_digest": "",
    }
    receipt["receipt_digest"] = inference_receipt_digest(receipt)
    return receipt


def self_test() -> None:
    provider = _provider_fixture()
    receipt = _receipt_fixture(provider)
    validate_provider(provider)
    validate_receipt(receipt, provider)

    cases: dict[str, tuple[dict, dict | None, str]] = {}

    bad = copy.deepcopy(provider)
    bad["capabilities"][0]["qualification_ref"] = None
    cases["qualified without ref"] = (bad, None, "provider")

    bad = copy.deepcopy(provider)
    bad["provenance"]["status"] = "COMPLETE"
    bad["provenance"]["model_revision"] = None
    cases["fake complete provenance"] = (bad, None, "provider")

    bad = copy.deepcopy(provider)
    bad["provider_kind"] = "REMOTE"
    bad["privacy"]["prompt_egress"] = "LOCAL_ONLY"
    cases["remote claims local-only egress"] = (bad, None, "provider")

    bad = copy.deepcopy(provider)
    bad["dependency_role"] = "CONTINUITY_BEARING_DEPENDENCY"
    bad["replacement_plan"] = None
    cases["continuity dependency without plan"] = (bad, None, "provider")

    bad_receipt = copy.deepcopy(receipt)
    bad_receipt["output"] = "tampered"
    cases["tampered receipt digest"] = (bad_receipt, provider, "receipt")

    bad_receipt = copy.deepcopy(receipt)
    bad_receipt["effect_authority"] = "EXECUTE"
    bad_receipt["receipt_digest"] = inference_receipt_digest(bad_receipt)
    cases["effect authority escalation"] = (bad_receipt, provider, "receipt")

    for name, (candidate, bound_provider, kind) in cases.items():
        try:
            if kind == "provider":
                validate_provider(candidate)
            else:
                validate_receipt(candidate, bound_provider)
        except ValidationError:
            continue
        raise ValidationError(f"self-test failed: invalid case accepted: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Unbound Sol external model provider advertisements and receipts.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_provider = sub.add_parser("provider")
    p_provider.add_argument("path", type=pathlib.Path)

    p_receipt = sub.add_parser("receipt")
    p_receipt.add_argument("path", type=pathlib.Path)
    p_receipt.add_argument("--provider", type=pathlib.Path)

    sub.add_parser("self-test")

    args = parser.parse_args()

    if args.command == "self-test":
        self_test()
        print("external model bus V2 validator self-test: PASS")
        return 0

    if args.command == "provider":
        provider = json.loads(args.path.read_text(encoding="utf-8"))
        validate_provider(provider)
        print(f"model provider advertisement: PASS ({args.path})")
        print(f"provider_advertisement_digest={provider_advertisement_digest(provider)}")
        return 0

    receipt = json.loads(args.path.read_text(encoding="utf-8"))
    provider = json.loads(args.provider.read_text(encoding="utf-8")) if args.provider else None
    validate_receipt(receipt, provider)
    print(f"model inference receipt: PASS ({args.path})")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"external model bus V2 validation: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
