"""Regression contract: PR-controlled files must never supply the security runner."""

from pathlib import Path
import unittest


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/windows-editor-startup-safety.yml"


class WindowsWorkflowTrustBoundaryTest(unittest.TestCase):
    def setUp(self):
        self.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_pr_candidate_is_data_and_base_owns_executable_scanner(self):
        self.assertIn("pull_request_target:", self.workflow)
        self.assertIn("ref: ${{ github.event.pull_request.base.sha || github.sha }}", self.workflow)
        self.assertIn("path: trusted-tools", self.workflow)
        self.assertIn("ref: ${{ github.event.pull_request.head.sha || github.sha }}", self.workflow)
        self.assertIn("path: candidate", self.workflow)
        self.assertIn("python -B trusted-tools/security/workspace_autorun_scan.py candidate", self.workflow)
        self.assertIn("python -B -m unittest discover -s trusted-tools/security", self.workflow)
        self.assertNotIn("python -B security/workspace_autorun_scan.py .", self.workflow)

    def test_workflow_restricts_token_and_fails_on_source_mismatch(self):
        self.assertIn("contents: read", self.workflow)
        self.assertEqual(self.workflow.count("persist-credentials: false"), 2)
        self.assertIn("EXPECTED_TRUSTED_SHA:", self.workflow)
        self.assertIn("EXPECTED_CANDIDATE_SHA:", self.workflow)
        self.assertIn("throw \"Trusted source commit mismatch\"", self.workflow)
        self.assertIn("throw \"Candidate source commit mismatch\"", self.workflow)
