"""Offline, no-host-effect tests for side-by-side Portal/Runner qualification."""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile
from contextlib import redirect_stdout


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "portal_runner_wheel_qualification",
    ROOT / "tools" / "portal_runner_wheel_qualification.py",
)
assert spec and spec.loader
qual = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qual)


def wheel(path: Path, name: str, payload: bytes = b"test") -> str:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(name, payload)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def installable_wheel(path: Path, dist_name: str, version: str, module: str,
                      code: str = "# synthetic package\n",
                      requires_dist: str | None = None) -> str:
    dist = f"{dist_name.replace('-', '_')}-{version}"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(f"{module}/__init__.py", code)
        archive.writestr(f"{dist}.dist-info/METADATA",
                         f"Metadata-Version: 2.1\nName: {dist_name}\nVersion: {version}\n"
                         + (f"Requires-Dist: {requires_dist}\n" if requires_dist else ""))
        archive.writestr(f"{dist}.dist-info/WHEEL",
                         "Wheel-Version: 1.0\nRoot-Is-Purelib: true\nTag: py3-none-any\n")
        archive.writestr(f"{dist}.dist-info/RECORD", "")
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PortalRunnerQualificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_exact_pinned_wheels_have_no_application_file_collision(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        portal_hash = wheel(portal, "portal/__init__.py")
        runner_hash = wheel(runner, "runner/__init__.py")
        receipt = qual.validate_wheels(portal, runner, portal_hash, runner_hash)
        self.assertEqual(receipt["portal_sha256"], portal_hash)

    def test_wheel_collision_and_sha_substitution_fail_closed(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        portal_hash = wheel(portal, "runner/schema.py")
        runner_hash = wheel(runner, "runner/schema.py")
        with self.assertRaisesRegex(ValueError, "overwrite"):
            qual.validate_wheels(portal, runner, portal_hash, runner_hash)
        with self.assertRaisesRegex(ValueError, "mismatch"):
            qual.validate_wheels(portal, runner, "0" * 64, runner_hash)

    def test_cross_platform_casefold_alias_is_a_collision(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        portal_hash = wheel(portal, "Runner/Schema.py")
        runner_hash = wheel(runner, "runner/schema.py")
        with self.assertRaisesRegex(ValueError, "overwrite"):
            qual.validate_wheels(portal, runner, portal_hash, runner_hash)

    def test_wheel_rejects_traversal_and_windows_path_aliases(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        runner_hash = wheel(runner, "runner/schema.py")
        for unsafe in ("../escape.py", "runner/../escape.py", "runner\\schema.py",
                       "/absolute.py", "C:relative.py", "runner/name. "):
            with self.subTest(member=unsafe):
                portal_hash = wheel(portal, unsafe)
                with self.assertRaisesRegex(ValueError, "unsafe"):
                    qual.validate_wheels(portal, runner, portal_hash, runner_hash)

    def test_wheel_rejects_relocated_data_member_instead_of_missing_collision(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        # A wheel's .data/purelib is installed into site-packages/; a raw ZIP
        # member comparison would miss the collision with runner/schema.py.
        portal_hash = wheel(portal, "portal_coordinator-0.2.0.data/purelib/runner/schema.py")
        runner_hash = wheel(runner, "runner/schema.py")
        with self.assertRaisesRegex(ValueError, "relocated"):
            qual.validate_wheels(portal, runner, portal_hash, runner_hash)

    def test_wheel_rejects_windows_reserved_device_basename(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        runner_hash = wheel(runner, "runner/schema.py")
        for name in ("portal/CON.py", "portal/lpt1.txt", "NUL", "runner/COM9.bin"):
            with self.subTest(name=name):
                portal_hash = wheel(portal, name)
                with self.assertRaisesRegex(ValueError, "reserved"):
                    qual.validate_wheels(portal, runner, portal_hash, runner_hash)

    def test_duplicate_member_in_wheel_is_rejected(self) -> None:
        portal = self.root / "portal.whl"
        runner = self.root / "runner.whl"
        with zipfile.ZipFile(portal, "w") as archive:
            archive.writestr("portal/__init__.py", b"first")
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                archive.writestr("portal/__init__.py", b"second")
        runner_hash = wheel(runner, "runner/__init__.py")
        with self.assertRaisesRegex(ValueError, "repeats"):
            qual.validate_wheels(portal, runner,
                                 hashlib.sha256(portal.read_bytes()).hexdigest(), runner_hash)

    def test_candidate_must_be_new_absolute_and_not_system_root(self) -> None:
        with self.assertRaisesRegex(ValueError, "absolute"):
            qual.require_unused_candidate(Path("relative-venv"))
        with self.assertRaisesRegex(ValueError, "unused"):
            qual.require_unused_candidate(self.root)
        with self.assertRaisesRegex(ValueError, "root"):
            qual.require_unused_candidate(Path(self.root.anchor))
        self.assertEqual(qual.require_unused_candidate(self.root / "new"),
                         (self.root / "new").resolve())

    def test_probe_rejects_global_editable_binding_and_false_authority(self) -> None:
        python = self.root / "python.exe"
        python.touch()
        fake = {
            "virtual_environment": False,
            "all_modules_under_prefix": False,
            "portal_version": "0.2.0",
            "runner_version": "0.1.0",
            "worker_schema_valid_shape": True,
        }
        with patch.object(qual, "_run", return_value=json.dumps(fake)):
            with self.assertRaisesRegex(ValueError, "HOLD"):
                qual.probe_python(python)
        fake["virtual_environment"] = True
        with patch.object(qual, "_run", return_value=json.dumps(fake)):
            with self.assertRaisesRegex(ValueError, "HOLD"):
                qual.probe_python(python)

    def test_probe_checks_both_cli_entrypoints_and_never_grants_authority(self) -> None:
        # Use the running platform's executable naming to avoid assuming Windows.
        bin_dir = self.root / "bin"
        bin_dir.mkdir()
        python = bin_dir / "python"
        python.touch()
        suffix = ".exe" if qual.sys.platform == "win32" else ""
        for name in ("portal", "project-runner"):
            (bin_dir / (name + suffix)).touch()
        good = {
            "virtual_environment": True,
            "all_modules_under_prefix": True,
            "portal_version": "0.2.0",
            "runner_version": "0.1.0",
            "worker_schema_valid_shape": True,
        }
        with patch.object(qual, "_run", return_value=json.dumps(good)) as run:
            result = qual.probe_python(python)
        self.assertEqual(result["authority"], "NO_HOST_OR_EXECUTION_AUTHORIZATION")
        self.assertEqual(run.call_count, 3)
        self.assertEqual(run.call_args_list[1].args[0][-1], "--help")
        self.assertEqual(run.call_args_list[2].args[0][-1], "--help")

    def test_snapshot_omits_raw_freeze_and_rejects_tokenized_version(self) -> None:
        python = self.root / "python.exe"
        python.touch()
        output = self.root / "private-snapshot.json"
        safe = {
            "schema": "PORTAL_RUNNER_REDACTED_INSTALLED_SNAPSHOT_V1",
            "freeze_equivalent": ["portal-coordinator==0.2.0", "project-runner==0.1.0"],
            "note": "Version-only snapshot; interpreter, paths, VCS URLs and credentials omitted.",
        }
        with patch.object(qual, "_run", return_value=json.dumps(safe)):
            qual.sanitized_snapshot(python, output)
        self.assertEqual(json.loads(output.read_text())["freeze_equivalent"],
                         safe["freeze_equivalent"])
        self.assertNotIn("interpreter", json.loads(output.read_text()))
        self.assertNotIn("prefix", json.loads(output.read_text()))
        with self.assertRaisesRegex(ValueError, "unused"):
            qual.sanitized_snapshot(python, output)
        bad = dict(safe)
        bad["freeze_equivalent"] = ["project-runner @ https://example.invalid/repo"]
        fresh = self.root / "fresh.json"
        with patch.object(qual, "_run", return_value=json.dumps(bad)):
            with self.assertRaisesRegex(ValueError, "unsafe"):
                qual.sanitized_snapshot(python, fresh)
        self.assertFalse(fresh.exists())

    def test_snapshot_rejects_spoofed_schema_or_note_content(self) -> None:
        python = self.root / "python.exe"
        python.touch()
        valid = {
            "schema": "PORTAL_RUNNER_REDACTED_INSTALLED_SNAPSHOT_V1",
            "freeze_equivalent": ["project-runner==0.1.0"],
            "note": "Version-only snapshot; interpreter, paths, VCS URLs and credentials omitted.",
        }
        for field, content in (("schema", "source=/private/location"),
                               ("note", "interpreter=/private/location")):
            with self.subTest(field=field):
                data = dict(valid, **{field: content})
                output = self.root / f"spoof-{field}.json"
                with patch.object(qual, "_run", return_value=json.dumps(data)):
                    with self.assertRaisesRegex(ValueError, "unsafe"):
                        qual.sanitized_snapshot(python, output)
                self.assertFalse(output.exists())

    def test_stage_never_reuses_existing_target_or_wheelhouse(self) -> None:
        with patch.object(qual, "venv") as virtualenv:
            result = qual.main([
                "stage", "--disposable-test-only", "--candidate-dir", str(self.root),
                "--portal-wheel", str(self.root / "missing1.whl"),
                "--runner-wheel", str(self.root / "missing2.whl"),
                "--portal-sha256", "0" * 64,
                "--runner-sha256", "0" * 64,
                "--wheelhouse", str(self.root),
            ])
        self.assertEqual(result, 2)
        virtualenv.EnvBuilder.assert_not_called()

    def test_real_offline_stage_ignores_inherited_pip_target_and_prefix(self) -> None:
        wheels = self.root / "wheelhouse"
        wheels.mkdir()
        portal = wheels / "portal_coordinator-0.2.0-py3-none-any.whl"
        runner = wheels / "project_runner-0.1.0-py3-none-any.whl"
        portal_sha = installable_wheel(portal, "portal-coordinator", "0.2.0", "portal")
        runner_sha = installable_wheel(runner, "project-runner", "0.1.0", "runner")
        # Before the fix, pip inherited PIP_TARGET and wrote both packages
        # outside the new candidate before returning HOLD on the CLI probe.
        for inherited_key in ("PIP_TARGET", "PIP_PREFIX"):
            with self.subTest(inherited_key=inherited_key):
                candidate = self.root / f"candidate-{inherited_key.lower()}"
                outside = self.root / f"outside-{inherited_key.lower()}"
                options = [
                    "stage", "--disposable-test-only", "--candidate-dir", str(candidate),
                    "--portal-wheel", str(portal), "--runner-wheel", str(runner),
                    "--portal-sha256", portal_sha, "--runner-sha256", runner_sha,
                    "--wheelhouse", str(wheels),
                ]
                with patch.dict(os.environ, {inherited_key: str(outside)}, clear=False):
                    with redirect_stdout(io.StringIO()):
                        status = qual.main(options)
                # Fake test wheels have no CLI entrypoints or schema, so verify
                # HOLD follows the successful isolated candidate installation.
                self.assertEqual(status, 2)
                self.assertFalse(outside.exists(), "pip escaped the isolated candidate")
                self.assertTrue(candidate.exists())
                self.assertTrue(any(p.parent.name == "portal" for p in candidate.rglob("__init__.py")),
                                "synthetic portal package did not reach candidate")

    def test_stage_installs_pinned_copy_if_original_wheel_swaps_before_pip(self) -> None:
        wheels = self.root / "wheelhouse"
        wheels.mkdir()
        portal = wheels / "portal_coordinator-0.2.0-py3-none-any.whl"
        runner = wheels / "project_runner-0.1.0-py3-none-any.whl"
        portal_sha = installable_wheel(portal, "portal-coordinator", "0.2.0", "portal",
                                       code="# PINNED_BENIGN_CODE\n")
        runner_sha = installable_wheel(runner, "project-runner", "0.1.0", "runner")
        candidate = self.root / "candidate"
        real_create = qual.venv.EnvBuilder.create

        def swap_after_private_copy(builder: object, destination: Path) -> None:
            installable_wheel(portal, "portal-coordinator", "0.2.0", "portal",
                              code="# UNPINNED_REPLACEMENT_CODE\n")
            real_create(builder, destination)

        with patch.object(qual.venv.EnvBuilder, "create", new=swap_after_private_copy):
            with redirect_stdout(io.StringIO()):
                status = qual.main([
                    "stage", "--disposable-test-only", "--candidate-dir", str(candidate),
                    "--portal-wheel", str(portal), "--runner-wheel", str(runner),
                    "--portal-sha256", portal_sha, "--runner-sha256", runner_sha,
                    "--wheelhouse", str(wheels),
                ])
        self.assertEqual(status, 2)  # Missing synthetic CLI/schema; no cutover.
        installed = [p for p in candidate.rglob("__init__.py") if p.parent.name == "portal"]
        self.assertEqual(len(installed), 1)
        self.assertIn("PINNED_BENIGN_CODE", installed[0].read_text())
        self.assertNotIn("UNPINNED_REPLACEMENT_CODE", installed[0].read_text())

    def test_direct_reference_dependencies_cannot_escape_offline_wheelhouse(self) -> None:
        wheels = self.root / "wheelhouse"
        wheels.mkdir()
        portal = wheels / "portal_coordinator-0.2.0-py3-none-any.whl"
        runner = wheels / "project_runner-0.1.0-py3-none-any.whl"
        runner_sha = installable_wheel(runner, "project-runner", "0.1.0", "runner")
        for kind, target in (("file", (self.root / "outside.whl").as_uri()),
                             ("https", "https://example.invalid/outside.whl")):
            with self.subTest(kind=kind):
                portal_sha = installable_wheel(
                    portal, "portal-coordinator", "0.2.0", "portal",
                    requires_dist=f"outside-dependency @ {target}",
                )
                candidate = self.root / f"candidate-{kind}"
                with redirect_stdout(io.StringIO()):
                    status = qual.main([
                        "stage", "--disposable-test-only", "--candidate-dir", str(candidate),
                        "--portal-wheel", str(portal), "--runner-wheel", str(runner),
                        "--portal-sha256", portal_sha, "--runner-sha256", runner_sha,
                        "--wheelhouse", str(wheels),
                    ])
                self.assertEqual(status, 2)
                self.assertFalse((candidate / "bin").exists())
                self.assertFalse((candidate / "Scripts").exists())

    @unittest.skipIf(os.name == "nt", "POSIX owner/mode and symlink semantics")
    def test_stage_rejects_nonprivate_candidate_parent_before_any_write(self) -> None:
        parent = self.root / "shared"
        parent.mkdir(mode=0o755)
        parent.chmod(0o755)
        candidate = parent / "candidate"
        wheels = self.root / "wheelhouse"
        wheels.mkdir()
        portal = wheels / "portal_coordinator-0.2.0-py3-none-any.whl"
        runner = wheels / "project_runner-0.1.0-py3-none-any.whl"
        ph = installable_wheel(portal, "portal-coordinator", "0.2.0", "portal")
        rh = installable_wheel(runner, "project-runner", "0.1.0", "runner")
        with redirect_stdout(io.StringIO()):
            status = qual.main([
                "stage", "--disposable-test-only", "--candidate-dir", str(candidate),
                "--portal-wheel", str(portal), "--runner-wheel", str(runner),
                "--portal-sha256", ph, "--runner-sha256", rh,
                "--wheelhouse", str(wheels),
            ])
        self.assertEqual(status, 2)
        self.assertFalse(candidate.exists())

    @unittest.skipIf(os.name == "nt", "POSIX owner/mode and symlink semantics")
    def test_stage_detects_parent_symlink_swap_after_preflight(self) -> None:
        private_parent = self.root / "private-parent"
        private_parent.mkdir(mode=0o700)
        moved_parent = self.root / "moved-parent"
        outside = self.root / "outside"
        outside.mkdir(mode=0o700)
        candidate = private_parent / "candidate"
        wheels = self.root / "wheelhouse"
        wheels.mkdir()
        portal = wheels / "portal_coordinator-0.2.0-py3-none-any.whl"
        runner = wheels / "project_runner-0.1.0-py3-none-any.whl"
        ph = installable_wheel(portal, "portal-coordinator", "0.2.0", "portal")
        rh = installable_wheel(runner, "project-runner", "0.1.0", "runner")
        original = qual.validate_wheels
        calls = 0

        def swap_parent(*args: object) -> dict[str, str]:
            nonlocal calls
            calls += 1
            receipt = original(*args)
            if calls == 1:
                private_parent.rename(moved_parent)
                private_parent.symlink_to(outside, target_is_directory=True)
            return receipt

        with patch.object(qual, "validate_wheels", side_effect=swap_parent):
            with redirect_stdout(io.StringIO()):
                status = qual.main([
                    "stage", "--disposable-test-only", "--candidate-dir", str(candidate),
                    "--portal-wheel", str(portal), "--runner-wheel", str(runner),
                    "--portal-sha256", ph, "--runner-sha256", rh,
                    "--wheelhouse", str(wheels),
                ])
        self.assertEqual(status, 2)
        self.assertFalse((outside / "candidate").exists())
        self.assertFalse((moved_parent / "candidate").exists())

    def test_default_stage_holds_before_any_path_based_writes(self) -> None:
        wheels = self.root / "wheelhouse"
        wheels.mkdir()
        portal = wheels / "portal_coordinator-0.2.0-py3-none-any.whl"
        runner = wheels / "project_runner-0.1.0-py3-none-any.whl"
        ph = installable_wheel(portal, "portal-coordinator", "0.2.0", "portal")
        rh = installable_wheel(runner, "project-runner", "0.1.0", "runner")
        candidate = self.root / "candidate"
        with patch.object(qual.venv.EnvBuilder, "create") as create:
            with redirect_stdout(io.StringIO()) as output:
                result = qual.main([
                    "stage", "--candidate-dir", str(candidate),
                    "--portal-wheel", str(portal), "--runner-wheel", str(runner),
                    "--portal-sha256", ph, "--runner-sha256", rh,
                    "--wheelhouse", str(wheels),
                ])
        self.assertEqual(result, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "HOST_CUSTODY_HOLD")
        create.assert_not_called()
        self.assertFalse(candidate.exists())

    @unittest.skipIf(os.name == "nt", "POSIX symlink adversary reproduction")
    def test_default_stage_blocks_actual_parent_swap_before_create(self) -> None:
        parent = self.root / "private-parent"
        parent.mkdir(mode=0o700)
        outside = self.root / "outside"
        outside.mkdir(mode=0o700)
        candidate = parent / "candidate"
        wheels = self.root / "wheelhouse"
        wheels.mkdir()
        portal = wheels / "portal_coordinator-0.2.0-py3-none-any.whl"
        runner = wheels / "project_runner-0.1.0-py3-none-any.whl"
        ph = installable_wheel(portal, "portal-coordinator", "0.2.0", "portal")
        rh = installable_wheel(runner, "project-runner", "0.1.0", "runner")
        actual_create = qual.venv.EnvBuilder.create

        def attack_at_create(builder: object, destination: Path) -> None:
            parent.rename(self.root / "moved-parent")
            parent.symlink_to(outside, target_is_directory=True)
            actual_create(builder, destination)

        with patch.object(qual.venv.EnvBuilder, "create", new=attack_at_create):
            with redirect_stdout(io.StringIO()) as output:
                status = qual.main([
                    "stage", "--candidate-dir", str(candidate),
                    "--portal-wheel", str(portal), "--runner-wheel", str(runner),
                    "--portal-sha256", ph, "--runner-sha256", rh,
                    "--wheelhouse", str(wheels),
                ])
        self.assertEqual(status, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "HOST_CUSTODY_HOLD")
        self.assertFalse((outside / "candidate").exists())


if __name__ == "__main__":
    unittest.main()
