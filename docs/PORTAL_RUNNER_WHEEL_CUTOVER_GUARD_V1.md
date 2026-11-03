# Portal / Project Runner side-by-side Windows qualification

This is a **source/package test**, not permission to change a live runtime.
Portal and standalone Project Runner formerly shared an installed `runner`
namespace. An editable `project-runner` distribution may actually resolve from
a Portal source checkout. CLI `--help` alone does not detect that collision.

The executable guard is `tools/portal_runner_wheel_qualification.py`. It does
not uninstall packages, alter PATH, replace launchers, restart services,
authenticate Executor, or grant a capability.

1. Establish exact released wheel provenance and SHA-256 digests for Portal and
   Project Runner. Do not infer that GitHub PR test success grants release.
2. Before any proposed switch, run `snapshot --python <existing-python>
   --output <unused-private-report.json>` using an absolute private report path.
   This records only `name==version` entries—not potentially secret-bearing
   editable VCS URLs. Store the previous launcher path separately in the
   host-owned release record. The snapshot is **not** a complete reinstall
   lockfile.
3. Build/download the exact approved wheels into an operator-owned directory,
   verify their SHA-256, and prepare an offline dependency wheelhouse.
4. Run `stage --candidate-dir <unused-absolute-directory>
   --portal-wheel <exact-portal.whl> --runner-wheel <exact-runner.whl>
   --portal-sha256 <64-hex> --runner-sha256 <64-hex>
   --wheelhouse <local-offline-wheelhouse>`. Staging creates a **new virtual
   environment only**. The command never touches the existing Python install.
5. Run `verify --python <candidate-venv-python>` from a neutral directory.
   The guard requires both modules to resolve under that environment, the
   exact package versions, installed Runner schema resources, and both CLI
   help endpoints. It always returns `NO_HOST_OR_EXECUTION_AUTHORIZATION`.
6. An authorized host owner must separately approve a launcher/service switch
   after preserving the old launcher target and recovery path. **No command in
   this repository performs that switch.** Verify the chosen interpreter and
   actual installed-host behavior again after the switch.
7. On a failed post-switch check, stop new effect admission and have the host
   owner restore the recorded previous launcher target; do not delete either
   environment automatically. Re-run qualification before resuming effects.

An offline candidate PASS cannot qualify live Executor delivery, host identity,
worker authorization, model training, or a production service deployment.
The Project Runner Executor-discovery producer also has an independent source
ownership/release gate. Do not use a hand-written test mapping as its receipt.
