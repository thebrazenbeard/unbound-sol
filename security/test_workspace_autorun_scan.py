"""Purely synthetic fixtures; never touches the affected repositories."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from workspace_autorun_scan import main, scan


class WorkspaceAutorunScanTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def write(self, path: str, content: str | bytes) -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            target.write_bytes(content)
        else:
            target.write_text(content, encoding="utf-8")

    def test_empty_repo_has_no_matching_signature(self) -> None:
        self.assertEqual(scan(self.root), [])

    def test_repository_current_tree_has_no_unsafe_startup_path(self) -> None:
        """Unlike synthetic scanner fixtures, this protects the actual PR tree."""
        repository = Path(__file__).resolve().parents[1]
        self.assertFalse((repository / "public/fonts/fa-solid.lkf").exists())
        self.assertFalse((repository / "public/fonts/fa-solid-500.woff2").exists())
        self.assertFalse((repository / "public/fonts/fa-solid-600.ttf").exists())
        self.assertEqual(scan(repository), [])

    def test_disguised_ttf_is_blocked_without_an_editor_task(self) -> None:
        self.write("public/fonts/renamed.ttf", b"\t" * 128 + b"console.log('never execute')\n")
        self.assertIn("invalid-ttf-structure", {finding["rule"] for finding in scan(self.root)})

    def test_ttf_magic_prefix_alone_is_not_valid_font_evidence(self) -> None:
        self.write("public/fonts/renamed.ttf", b"true;\nconsole.log('never execute')\n")
        self.assertIn("invalid-ttf-structure", {finding["rule"] for finding in scan(self.root)})

    def test_nested_renamed_ttf_is_inspected(self) -> None:
        self.write("public/fonts/nested/renamed.ttf", b"console.log('never execute')\n")
        self.assertIn("invalid-ttf-structure", {finding["rule"] for finding in scan(self.root)})

    def test_json_escapes_do_not_hide_folder_open_or_auto_consent(self) -> None:
        self.write(".vscode/tasks.json", r'{"tasks":[{"runOptions":{"runOn":"fold\u0065rOpen"}}]}')
        self.write(".vscode/settings.json", r'{"task.allowAutoma\u0074icTasks":"on"}')
        rules = {finding["rule"] for finding in scan(self.root)}
        self.assertIn("workspace-folder-open", rules)
        self.assertIn("workspace-auto-allow", rules)

    def test_windows_override_node_font_argument_is_blocked(self) -> None:
        self.write(".vscode/tasks.json", '{"tasks":[{"command":"echo","windows":{"command":"node","args":["./public/fonts/renamed.woff"]}}]}')
        self.assertIn("disguised-interpreter-asset", {finding["rule"] for finding in scan(self.root)})

    def test_jsonc_comments_trailing_comma_and_bom_are_supported(self) -> None:
        self.write(".vscode/tasks.json", '\ufeff{\n // manual tasks only\n "tasks": [],\n}\n')
        self.assertEqual(scan(self.root), [])

    def test_malformed_workspace_jsonc_fails_closed(self) -> None:
        self.write(".vscode/tasks.json", '{"tasks": [')
        self.assertIn("invalid-workspace-jsonc", {finding["rule"] for finding in scan(self.root)})

    def test_duplicate_workspace_keys_fail_closed(self) -> None:
        self.write(".vscode/tasks.json", '{"tasks":[],"tasks":[]}')
        self.assertIn("invalid-workspace-jsonc", {finding["rule"] for finding in scan(self.root)})

    def test_code_workspace_embedded_auto_task_is_blocked(self) -> None:
        self.write("local.code-workspace", '{"tasks":{"tasks":[{"runOptions":{"runOn":"folderOpen"}}]}}')
        self.assertIn("workspace-folder-open", {finding["rule"] for finding in scan(self.root)})

    def test_nested_editor_folder_open_task_is_rejected(self) -> None:
        self.write(
            "packages/crew/.vscode/tasks.json",
            '{"tasks":[{"label":"inert fixture","runOptions":{"runOn":"folderOpen"}}]}',
        )
        findings = {(entry["path"], entry["rule"]) for entry in scan(self.root)}
        self.assertIn(("packages/crew/.vscode/tasks.json", "workspace-folder-open"), findings)

    def test_nested_case_variant_workspace_and_windows_override_are_rejected(self) -> None:
        self.write(
            "apps/crew/.VSCODE/TASKS.JSON",
            '{"tasks":[{"command":"echo","windows":{"command":"node","args":["./public/fonts/not-a-font.ttf"]}}]}',
        )
        self.write(
            "apps/crew/CREW.CODE-WORKSPACE",
            '{"tasks":{"tasks":[{"runOptions":{"runOn":"folderOpen"}}]}}',
        )
        findings = {(entry["path"], entry["rule"]) for entry in scan(self.root)}
        self.assertIn(("apps/crew/.VSCODE/TASKS.JSON", "disguised-interpreter-asset"), findings)
        self.assertIn(("apps/crew/CREW.CODE-WORKSPACE", "workspace-folder-open"), findings)

    def test_nested_editor_auto_consent_is_rejected(self) -> None:
        self.write("modules/client/.VSCODE/SETTINGS.JSON", '{"task.allowAutomaticTasks":"on"}')
        findings = {(entry["path"], entry["rule"]) for entry in scan(self.root)}
        self.assertIn(("modules/client/.VSCODE/SETTINGS.JSON", "workspace-auto-allow"), findings)

    def test_platform_only_windows_command_cannot_hide_disguised_font(self) -> None:
        self.write(
            ".vscode/tasks.json",
            '{"tasks":[{"windows":{"command":"node","args":["./public/fonts/hidden.ttf"]}}]}',
        )
        findings = {entry["rule"] for entry in scan(self.root)}
        self.assertIn("disguised-interpreter-asset", findings)

    def test_uppercase_ttf_without_task_cannot_hide_fake_font(self) -> None:
        self.write("public/fonts/UNTRUSTED.TTF", b"console.log('inert fixture')\\n")
        findings = {entry["rule"] for entry in scan(self.root)}
        self.assertIn("invalid-ttf-structure", findings)

    def test_repair_preserves_local_config_and_dependency_ignores(self) -> None:
        repository = Path(__file__).resolve().parents[1]
        patterns = {
            value.strip()
            for value in (repository / ".gitignore").read_text(encoding="utf-8").splitlines()
            if value.strip() and not value.lstrip().startswith("#")
        }
        self.assertTrue({"config.bat", "node_modules"} <= patterns)

    def test_bounded_sfnt_directory_is_allowed(self) -> None:
        # Two independently constructed table records (head and cmap) at offsets 44 and 48.
        header = b"\x00\x01\x00\x00" + b"\x00\x02" + b"\x00\x20\x00\x01\x00\x00"
        head = b"head" + b"\x00" * 4 + (44).to_bytes(4, "big") + (4).to_bytes(4, "big")
        cmap = b"cmap" + b"\x00" * 4 + (48).to_bytes(4, "big") + (4).to_bytes(4, "big")
        self.write("public/fonts/synthetic.ttf", header + head + cmap + b"data" + b"data")
        self.assertEqual(scan(self.root), [])

    def test_trailing_executable_bytes_behind_sfnt_directory_are_rejected(self) -> None:
        header = b"\x00\x01\x00\x00" + b"\x00\x02" + b"\x00\x20\x00\x01\x00\x00"
        head = b"head" + b"\x00" * 4 + (44).to_bytes(4, "big") + (4).to_bytes(4, "big")
        cmap = b"cmap" + b"\x00" * 4 + (48).to_bytes(4, "big") + (4).to_bytes(4, "big")
        self.write("public/fonts/synthetic.ttf", header + head + cmap + b"data" + b"data" + b"console.log('never execute')")
        self.assertIn("invalid-ttf-structure", {finding["rule"] for finding in scan(self.root)})

    def test_lkf_folder_open_chain_is_blocked(self) -> None:
        self.write(".vscode/tasks.json", '{"tasks":[{"command":"node ./public/fonts/fa-solid.lkf","runOptions":{"runOn":"folderOpen"}}]}')
        self.write(".vscode/settings.json", '{"task.allowAutomaticTasks":true}')
        self.write("public/fonts/fa-solid.lkf", "obfuscated")
        rules = {finding["rule"] for finding in scan(self.root)}
        self.assertEqual(rules, {"workspace-folder-open", "workspace-auto-allow", "invalid-auto-task-setting", "disguised-asset-reference", "disguised-executable-asset", "disguised-interpreter-asset"})

    def test_woff2_node_disguise_is_blocked_but_real_font_not(self) -> None:
        self.write("public/fonts/fa-solid-500.woff2", b"node disguised content")
        self.assertIn("invalid-woff2-magic", {finding["rule"] for finding in scan(self.root)})
        self.write("public/fonts/fa-solid-500.woff2", b"wOF2\0\0\0\0")
        self.assertEqual(scan(self.root), [])

    def test_nested_package_lifecycle_node_api_hook_is_blocked(self) -> None:
        self.write(
            "packages/crew/package.json",
            '{"scripts":{"preinstall":"node api.js"}}',
        )
        findings = {(entry["path"], entry["rule"]) for entry in scan(self.root)}
        self.assertIn(("packages/crew/package.json", "known-node-hook"), findings)

    def test_nested_package_disguised_font_hook_is_blocked(self) -> None:
        self.write(
            "packages/crew/package.json",
            '{"scripts":{"postinstall":"node ./public/fonts/renamed.ttf"}}',
        )
        findings = {(entry["path"], entry["rule"]) for entry in scan(self.root)}
        self.assertIn(("packages/crew/package.json", "disguised-interpreter-asset"), findings)

    def test_nested_malformed_package_fails_closed(self) -> None:
        self.write("packages/crew/package.json", "{not valid JSON")
        findings = {(entry["path"], entry["rule"]) for entry in scan(self.root)}
        self.assertIn(("packages/crew/package.json", "invalid-package-json"), findings)

    def test_package_lifecycle_hook_is_blocked(self) -> None:
        self.write("package.json", '{"scripts":{"build":"node api.js && tsc","test":"npm run build"}}')
        self.assertIn("known-node-hook", {finding["rule"] for finding in scan(self.root)})

    def test_bad_package_json_fails_closed(self) -> None:
        self.write("package.json", "{not valid json")
        self.assertIn("invalid-package-json", {finding["rule"] for finding in scan(self.root)})

    def test_exit_code_indicates_findings(self) -> None:
        self.write(".vscode/tasks.json", '{"runOn":"folderOpen"}')
        self.assertEqual(main([str(self.root)]), 2)

    def test_oversized_configuration_fails_closed(self) -> None:
        self.write(".vscode/tasks.json", "x" * 1_000_001)
        self.assertIn("unscanned-config", {finding["rule"] for finding in scan(self.root)})

    def test_symlinked_workspace_file_fails_closed(self) -> None:
        outside = self.root / "outside.txt"
        outside.write_text("do not follow", encoding="utf-8")
        target = self.root / ".vscode" / "tasks.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            target.symlink_to(outside)
        except (NotImplementedError, OSError):
            self.skipTest("symlinks unavailable")
        self.assertIn("unscanned-config", {finding["rule"] for finding in scan(self.root)})

    def test_valid_on_is_blocked_and_valid_off_is_not(self) -> None:
        self.write(".vscode/settings.json", '{"task.allowAutomaticTasks":"on"}')
        self.assertIn("workspace-auto-allow", {finding["rule"] for finding in scan(self.root)})
        self.write(".vscode/settings.json", '{"task.allowAutomaticTasks":"off"}')
        self.assertEqual(scan(self.root), [])

    def test_boolean_false_is_not_a_valid_off_setting(self) -> None:
        self.write(".vscode/settings.json", '{"task.allowAutomaticTasks":false}')
        self.assertIn("invalid-auto-task-setting", {finding["rule"] for finding in scan(self.root)})


if __name__ == "__main__":
    unittest.main()
