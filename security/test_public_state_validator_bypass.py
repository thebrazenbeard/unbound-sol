"""Synthetic regression cases for the public continuity secret scan.

No real credentials, account IDs, or private repository identities are used.
"""

from __future__ import annotations

import json
import importlib.util
import os
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

    def check(self, timeout: float = 5.0) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(self.root / "tools/validate_public_state.py")],
                              cwd=self.root, text=True, capture_output=True,
                              check=False, timeout=timeout)

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

    def test_index_staged_secret_overwritten_by_harmless_worktree_is_rejected(self) -> None:
        name = "synthetic-index.env"
        self.tracked_payload(name, self.fake_token())
        (self.root / name).write_text("harmless unstaged replacement\n", encoding="utf-8")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("possible secret-like material", result.stderr + result.stdout)

    def test_benign_index_with_unstaged_worktree_secret_is_rejected(self) -> None:
        name = "synthetic-worktree.env"
        self.tracked_payload(name, b"harmless public fixture")
        (self.root / name).write_bytes(self.fake_token())
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("possible secret-like material", result.stderr + result.stdout)

    def test_normalized_git_blob_and_crlf_worktree_are_both_inspected(self) -> None:
        (self.root / ".gitattributes").write_text("*.txt text eol=lf\n", encoding="utf-8")
        self.git("add", ".gitattributes")
        self.tracked_payload("normalized.txt", b"harmless public fixture\r\n")
        staged = subprocess.check_output(["git", "-C", str(self.root), "show", ":normalized.txt"])
        self.assertNotEqual(staged, (self.root / "normalized.txt").read_bytes())
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
        self.tracked_payload("synthetic.dat", b"\0public\0")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unclassified NUL-bearing", result.stderr + result.stdout)

    def test_invalid_utf8_without_nul_fails_closed(self) -> None:
        self.tracked_payload("synthetic.txt", b"public\xffsource")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid UTF-8", result.stderr + result.stdout)

    def test_missing_tracked_file_fails_closed(self) -> None:
        self.tracked_payload("synthetic.txt", b"public fixture")
        (self.root / "synthetic.txt").unlink()
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tracked file is unreadable", result.stderr + result.stdout)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "POSIX FIFO unavailable")
    def test_tracked_regular_file_replaced_with_fifo_fails_without_blocking(self) -> None:
        self.tracked_payload("synthetic-fifo", b"public fixture")
        path = self.root / "synthetic-fifo"
        path.unlink()
        os.mkfifo(path)
        result = self.check(timeout=1.5)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("non-regular", result.stderr + result.stdout)

    def test_permission_denied_tracked_file_fails_closed(self) -> None:
        self.tracked_payload("synthetic.txt", b"public fixture")
        module_path = self.root / "tools/validate_public_state.py"
        spec = importlib.util.spec_from_file_location("fixture_public_validator", module_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        open_original = os.open

        def deny_one(path: object, *args: object, **kwargs: object):
            if pathlib.Path(path) == self.root / "synthetic.txt":
                raise PermissionError("synthetic permission denial")
            return open_original(path, *args, **kwargs)

        with mock.patch.object(os, "open", deny_one):
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

    def test_parent_redirected_between_lstat_and_open_is_rejected(self) -> None:
        # No real secrets or external paths: the target lives in temporary
        # test-only storage, and the redirect is triggered at the open boundary.
        self.tracked_payload("nested/payload.txt", b"safe indexed fixture")
        with tempfile.TemporaryDirectory(prefix="synthetic-public-redirect-") as outer:
            outside = pathlib.Path(outer)
            (outside / "payload.txt").write_bytes(b"harmless external synthetic")
            target = self.root / "nested/payload.txt"
            original_open = os.open
            swapped = []

            def swap_parent(path: object, *args: object, **kwargs: object):
                if pathlib.Path(path) == target and not swapped:
                    target.parent.rename(self.root / "nested.original")
                    try:
                        target.parent.symlink_to(outside, target_is_directory=True)
                    except (OSError, NotImplementedError):
                        if os.name != "nt":
                            self.skipTest("symlink creation unavailable")
                        junction = subprocess.run(
                            ["cmd", "/d", "/c", "mklink", "/J", str(target.parent), str(outside)],
                            capture_output=True, check=False,
                        )
                        if junction.returncode:
                            self.skipTest("Windows junction creation unavailable")
                    swapped.append(True)
                return original_open(path, *args, **kwargs)

            spec = importlib.util.spec_from_file_location(
                "fixture_public_validator_parent_swap", self.root / "tools/validate_public_state.py"
            )
            self.assertIsNotNone(spec)
            self.assertIsNotNone(spec.loader)
            module = importlib.util.module_from_spec(spec)
            with mock.patch.object(os, "open", swap_parent):
                with self.assertRaisesRegex(SystemExit, "tracked symlink or redirected path"):
                    spec.loader.exec_module(module)
            self.assertTrue(swapped)

    def test_absent_git_index_fails_closed(self) -> None:
        # Git packs/loose objects can be read-only on Windows; an atomic move
        # gives the same missing-checkout condition without removing blobs.
        (self.root / ".git").rename(self.root / ".git-disabled")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unable to enumerate tracked", result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
