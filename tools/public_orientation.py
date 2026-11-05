#!/usr/bin/env python3
"""Read-only, public-safe orientation for external portfolio consumers.

This export is historical source evidence about Sol, not Vera identity,
native Project control, an installed runtime, or permission for any effect.
It deliberately emits a fixed allowlist rather than copying source records.
"""
from __future__ import annotations

from datetime import date
import json
from pathlib import Path
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


class OrientationError(ValueError):
    """Checked-in orientation source is missing or fails its contract."""


def _load_object(root: Path, relative: str) -> dict[str, Any]:
    try:
        value = json.loads((root / relative).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise OrientationError(f"unreadable public orientation source: {relative}") from exc
    if not isinstance(value, dict):
        raise OrientationError(f"expected JSON object: {relative}")
    return value


def _date(value: object, source: str) -> str:
    if not isinstance(value, str):
        raise OrientationError(f"missing observed date: {source}")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise OrientationError(f"invalid observed date: {source}") from exc
    if parsed.isoformat() != value:
        raise OrientationError(f"noncanonical observed date: {source}")
    return value


def build_public_orientation(root: Path = ROOT) -> dict[str, Any]:
    """Export only fixed, non-authoritative claims from admitted public files.

    The root argument supports isolated synthetic tests. CLI callers use the
    checked-in root exclusively. No network, host, memory, or provider probes
    are performed, so currentness remains explicitly unverified.
    """
    state = _load_object(root, "state/SOL_STATE_V1.json")
    sources = _load_object(root, "state/SOURCES_V1.json")

    if state.get("schema") != "UNBOUND_SOL_STATE_V1":
        raise OrientationError("unexpected state schema")
    identity = state.get("model_identity")
    if not isinstance(identity, dict) or (
        identity.get("substrate") != "GPT-5.6 Sol"
        or identity.get("conversational_name") != "Sol"
    ):
        raise OrientationError("this source does not identify Sol")
    if identity.get("private_weight_fork_claim") is not False:
        raise OrientationError("unsupported private-model claim")

    boundary = state.get("public_boundary")
    if not isinstance(boundary, dict) or any(
        boundary.get(name) is not False
        for name in (
            "secrets_allowed",
            "private_personal_records_allowed",
            "private_repo_identifiers_allowed",
        )
    ):
        raise OrientationError("public privacy boundary is not fail-closed")
    restore = state.get("restore")
    if not isinstance(restore, dict) or (
        restore.get("fresh_check_mutable_external_state") is not True
    ):
        raise OrientationError("fresh external verification is not required")

    if sources.get("schema") != "UNBOUND_SOL_PUBLIC_SOURCES_V1":
        raise OrientationError("unexpected source registry schema")
    if sources.get("public_safe") is not True:
        raise OrientationError("source registry is not public-safe")
    items = sources.get("sources")
    if not isinstance(items, list):
        raise OrientationError("source registry must contain a list")
    for item in items:
        if not isinstance(item, dict) or not re.fullmatch(
            r"[0-9a-f]{40}", str(item.get("ref", ""))
        ):
            raise OrientationError("source registry lacks an exact public ref")

    return {
        "schema": "UNBOUND_SOL_PUBLIC_ORIENTATION_V1",
        "source_repository": "thebrazenbeard/unbound-sol",
        "identity_subject": "Sol",
        "identity_substrate": "GPT-5.6 Sol",
        "consumer_scope": "PUBLIC_HISTORICAL_PORTFOLIO_ORIENTATION_ONLY",
        "evidence_class": "CHECKED_IN_SOURCE",
        "external_currentness": "NOT_VERIFIED",
        "runtime_installation": "NOT_VERIFIED",
        "state_observed_date": _date(state.get("observed_date"), "state"),
        "sources_observed_date": _date(sources.get("observed_date"), "sources"),
        "source_entry_count": len(items),
        "authority_grants": {
            "vera_identity_or_control": False,
            "sol_identity_transfer": False,
            "private_memory_admission": False,
            "effect_authorization": False,
            "merge_or_deployment": False,
        },
        "fresh_external_checks_required": True,
    }


def main() -> int:
    try:
        result = build_public_orientation()
    except OrientationError as exc:
        print(f"public orientation unavailable: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
