"""Synthetic regression cases for the public continuity secret scan.

No real credentials, account IDs, or private repository identities are used.
"""

from __future__ import annotations

import json
import importlib.util
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


CHECKER_SOURCE = pathlib.Path(__file__).resolve().parents[1] / "tools/validate_public_state.py"
FIXTURE_REQUIRED = (
    "README.md", "IDENTITY.md", "CONTINUITY.md", "PRINCIPLES.md",
    "PUBLIC_BOUNDARY.md", "LEARNING_LEDGER.md", "EXPERIMENTS.md",
    "CONNECTIONS.md", "docs/ARCHITECTURE_V1.md",
    "docs/CANNIBALIZATION_MAP_V1.md",
)


class PublicStateValidatorBypassTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="unbound-public-guard-")
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        (self.root / "tools").mkdir()
        shutil.copyfile(CHECKER_SOURCE, self.root / "tools/validate_public_state.py")
        for rel in FIXTURE_REQUIRED:
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Synthetic public fixture\n", encoding="utf-8")
        state_path = self.root / "state/SOL_STATE_V1.json"
        state_path.parent.mkdir(parents=True)
        state_path.write_text(json.dumps({
            "schema": "UNBOUND_SOL_STATE_V1",
            "model_identity": {"substrate": "GPT-5.6 Sol"},
            "public_boundary": {"secrets_allowed": False},
            "restore": {"fresh_check_mutable_external_state": True},
        }), encoding="utf-8")
        (self.root / "state/SOURCES_V1.json").write_text(json.dumps({
            "schema": "UNBOUND_SOL_PUBLIC_SOURCES_V1", "public_safe": True,
            "sources": [],
        }), encoding="utf-8")
        self.git("init", "-q")
        self.git("add", "-A")

    def git(self, *arguments: str) -> None:
        subprocess.run(["git", "-C", str(self.root), *arguments],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def check(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(self.root / "tools/validate_public_state.py")],
                              cwd=self.root, text=True, capture_output=True, check=False)

    def tracked_payload(self, name: str, payload: bytes) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        self.git("add", "--", name)

    def remove_payload(self, name: str) -> None:
        self.git("rm", "-f", "-q", "--", name)

    @staticmethod
    def fake_token() -> bytes:
        # Split construction prevents the test's own source from resembling
        # an actual token when the repository scanner inspects this file.
        return ("api" + "_key" + "=" + "synthetic-not-a-credential-0123456789").encode()

    def test_clean_tracked_checkout_passes(self) -> None:
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_sensitive_text_suffixes_are_scanned(self) -> None:
        for suffix in (".env", ".toml", ".sh", ".ps1", ".properties"):
            with self.subTest(suffix=suffix):
                name = "synthetic" + suffix
                self.tracked_payload(name, self.fake_token())
                result = self.check()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("possible secret-like material", result.stderr + result.stdout)
                self.remove_payload(name)

    def test_extensionless_backup_and_unicode_dot_names_are_scanned(self) -> None:
        for name in ("synthetic-config", "synthetic-config.bak", "synthetic\u2024env"):
            with self.subTest(name=name):
                self.tracked_payload(name, self.fake_token())
                result = self.check()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("possible secret-like material", result.stderr + result.stdout)
                self.remove_payload(name)

    def test_untracked_private_scratch_is_not_inspected(self) -> None:
        (self.root / "untracked.env").write_bytes(self.fake_token())
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_known_binary_asset_without_secrets_is_supported(self) -> None:
        self.tracked_payload("public/fonts/test.woff", b"wOFF" + b"\0" * 24 + b"\xff\xfe")
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_binary_asset_with_embedded_ascii_secret_is_rejected(self) -> None:
        self.tracked_payload("public/fonts/test.woff", b"wOFF" + b"\0" + self.fake_token())
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("possible secret-like material", result.stderr + result.stdout)

    def test_bomless_utf16le_secret_is_rejected(self) -> None:
        self.tracked_payload("synthetic.txt", self.fake_token().decode().encode("utf-16-le"))
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("possible secret-like material", result.stderr + result.stdout)

    def test_unknown_nul_bearing_payload_fails_closed(self) -> None:
        self.tracked_payload("synthetic.dat", b"\0\xff\0")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unclassified NUL-bearing", result.stderr + result.stdout)

    def test_missing_tracked_file_fails_closed(self) -> None:
        self.tracked_payload("synthetic.txt", b"public fixture")
        (self.root / "synthetic.txt").unlink()
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tracked file is unreadable", result.stderr + result.stdout)

    def test_permission_denied_tracked_file_fails_closed(self) -> None:
        self.tracked_payload("synthetic.txt", b"public fixture")
        module_path = self.root / "tools/validate_public_state.py"
        spec = importlib.util.spec_from_file_location("fixture_public_validator", module_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        open_original = pathlib.Path.open

        def deny_one(path: pathlib.Path, *args: object, **kwargs: object):
            if path == self.root / "synthetic.txt":
                raise PermissionError("synthetic permission denial")
            return open_original(path, *args, **kwargs)

        with mock.patch.object(pathlib.Path, "open", deny_one):
            with self.assertRaisesRegex(SystemExit, "tracked file is unreadable"):
                spec.loader.exec_module(module)

    def test_tracked_symlink_is_rejected(self) -> None:
        target = self.root / "public-target.txt"
        target.write_text("public fixture", encoding="utf-8")
        link = self.root / "tracked-link.txt"
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation unavailable")
        self.git("add", "--", "tracked-link.txt")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tracked symlink", result.stderr + result.stdout)

    def test_absent_git_index_fails_closed(self) -> None:
        shutil.rmtree(self.root / ".git")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unable to enumerate tracked", result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
