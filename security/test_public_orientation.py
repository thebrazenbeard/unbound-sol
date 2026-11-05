"""Synthetic public-orientation contract tests; no private data or network."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest

from tools.public_orientation import OrientationError, build_public_orientation


BASE_STATE = {
    "schema": "UNBOUND_SOL_STATE_V1",
    "observed_date": "2026-09-22",
    "model_identity": {
        "substrate": "GPT-5.6 Sol",
        "conversational_name": "Sol",
        "private_weight_fork_claim": False,
    },
    "public_boundary": {
        "secrets_allowed": False,
        "private_personal_records_allowed": False,
        "private_repo_identifiers_allowed": False,
    },
    "restore": {"fresh_check_mutable_external_state": True},
}
BASE_SOURCES = {
    "schema": "UNBOUND_SOL_PUBLIC_SOURCES_V1",
    "observed_date": "2026-09-22",
    "public_safe": True,
    "sources": [{"repo": "public/test", "ref": "a" * 40}],
}


class PublicOrientationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "state").mkdir()
        self.state = copy.deepcopy(BASE_STATE)
        self.sources = copy.deepcopy(BASE_SOURCES)

    def export(self) -> dict:
        (self.root / "state/SOL_STATE_V1.json").write_text(
            json.dumps(self.state), encoding="utf-8"
        )
        (self.root / "state/SOURCES_V1.json").write_text(
            json.dumps(self.sources), encoding="utf-8"
        )
        return build_public_orientation(self.root)

    def test_sol_is_distinct_from_vera_and_grants_are_denied(self) -> None:
        result = self.export()
        self.assertEqual(result["identity_subject"], "Sol")
        self.assertEqual(result["consumer_scope"], "PUBLIC_HISTORICAL_PORTFOLIO_ORIENTATION_ONLY")
        self.assertEqual(result["evidence_class"], "CHECKED_IN_SOURCE")
        self.assertEqual(result["external_currentness"], "NOT_VERIFIED")
        self.assertEqual(result["runtime_installation"], "NOT_VERIFIED")
        self.assertTrue(result["fresh_external_checks_required"])
        self.assertTrue(all(v is False for v in result["authority_grants"].values()))

    def test_other_identity_cannot_be_exported_as_sol(self) -> None:
        self.state["model_identity"]["conversational_name"] = "Vera"
        with self.assertRaises(OrientationError):
            self.export()

    def test_private_permission_fails_closed(self) -> None:
        self.state["public_boundary"]["private_personal_records_allowed"] = True
        with self.assertRaises(OrientationError):
            self.export()

    def test_missing_fresh_check_fails_closed(self) -> None:
        del self.state["restore"]["fresh_check_mutable_external_state"]
        with self.assertRaises(OrientationError):
            self.export()

    def test_source_schema_and_exact_ref_are_required(self) -> None:
        self.sources["sources"][0]["ref"] = "main"
        with self.assertRaises(OrientationError):
            self.export()
        self.sources["sources"][0]["ref"] = "a" * 40
        self.sources["public_safe"] = False
        with self.assertRaises(OrientationError):
            self.export()

    def test_untrusted_source_fields_never_escape(self) -> None:
        self.state["unadmitted_private_synthetic_marker"] = "DO_NOT_EXPORT_TEST_MARKER"
        self.sources["sources"][0]["unadmitted_private_synthetic_marker"] = (
            "DO_NOT_EXPORT_TEST_MARKER"
        )
        result = self.export()
        self.assertNotIn("DO_NOT_EXPORT_TEST_MARKER", json.dumps(result))
        self.assertEqual(result["source_entry_count"], 1)
        self.assertNotIn("sources", result)

    def test_current_repository_state_satisfies_contract(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        result = build_public_orientation(repository_root)
        self.assertEqual(result["identity_subject"], "Sol")
        self.assertEqual(result["source_repository"], "thebrazenbeard/unbound-sol")
        self.assertTrue(result["source_entry_count"] > 0)


if __name__ == "__main__":
    unittest.main()
