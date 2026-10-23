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

    def test_lkf_folder_open_chain_is_blocked(self) -> None:
        self.write(".vscode/tasks.json", '{"tasks":[{"command":"node ./public/fonts/fa-solid.lkf","runOptions":{"runOn":"folderOpen"}}]}')
        self.write(".vscode/settings.json", '{"task.allowAutomaticTasks":true}')
        self.write("public/fonts/fa-solid.lkf", "obfuscated")
        rules = {finding["rule"] for finding in scan(self.root)}
        self.assertEqual(rules, {"workspace-folder-open", "workspace-auto-allow", "disguised-asset-reference", "disguised-executable-asset"})

    def test_woff2_node_disguise_is_blocked_but_real_font_not(self) -> None:
        self.write("public/fonts/fa-solid-500.woff2", b"node disguised content")
        self.assertIn("invalid-woff2-magic", {finding["rule"] for finding in scan(self.root)})
        self.write("public/fonts/fa-solid-500.woff2", b"wOF2\0\0\0\0")
        self.assertEqual(scan(self.root), [])

    def test_package_lifecycle_hook_is_blocked(self) -> None:
        self.write("package.json", '{"scripts":{"build":"node api.js && tsc","test":"npm run build"}}')
        self.assertIn("known-node-hook", {finding["rule"] for finding in scan(self.root)})

    def test_bad_package_json_fails_closed(self) -> None:
        self.write("package.json", "{not valid json")
        self.assertIn("invalid-package-json", {finding["rule"] for finding in scan(self.root)})

    def test_exit_code_indicates_findings(self) -> None:
        self.write(".vscode/tasks.json", '{"runOn":"folderOpen"}')
        self.assertEqual(main([str(self.root)]), 2)


if __name__ == "__main__":
    unittest.main()
