# Cross-repository security triage — public aggregate only
Date: 2026-10-23

**Confidentiality:** This is deliberately redacted. The underlying owner inventory includes private repositories and must not be published in a public repository. Do not repopulate this file with repository names, private paths, head SHAs, or reconstructable identifiers.

## Pinned historical counts

A read-only audit of 100 accessible repository default heads identified:

- 81 with a VS Code `folderOpen` task invoking an obfuscated Node payload disguised as a `.lkf` font asset.
- 9 with a similar task invoking a disguised `.woff2` asset.
- 10 with no match to those two exact signatures; this **does not establish safety**.

This is historical source inspection, not verified current remediation status or evidence that a payload executed on any computer. Workspace Trust and the user's actual automatic-task settings affect exploitability; Boolean `task.allowAutomaticTasks: true` is not the accepted VS Code setting value (the documented options are strings `"on"` and `"off"`).

## Safe remediation gates

1. Re-fetch the actual current default-branch head before touching each repository.
2. Inspect editor startup tasks and package lifecycle hooks statically; do not run untrusted code.
3. Remove untrusted executable startup tasks, disguised Node assets, and unrelated lifecycle hooks in per-repository reviewed branches.
4. Run a source-integrity scanner and independent regression tests in a controlled environment after containment.
5. Verify current head, CI, effects, and rollback before merge; respect concurrent authorized changes.

The private exact-head registry belongs only in appropriately restricted storage. Git history may retain earlier versions of this file; replacing the current file does **not** retroactively erase the earlier public exposure. Repository history and GitHub support processes must be addressed separately if full removal is required.

The companion read-only scanner and synthetic tests remain proposed in this draft PR. This public aggregate confers no execution or merge authority.
