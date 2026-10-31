# Public portfolio integration checkpoint — 2026-10-31

Event: [`project_unfuck_runtime_coordination`](https://github.com/thebrazenbeard/chat-communication-bus/issues/397)  
Evidence: [W25–W30 source audit and owner requests](https://github.com/thebrazenbeard/chat-communication-bus/issues/397#issuecomment-6544709298) and [W31 six-worker dispatch](https://github.com/thebrazenbeard/chat-communication-bus/issues/397#issuecomment-6544792190).

**This document is public-safe orientation, not a deployment manifest, owner grant, live service claim, or authorization.** It deliberately omits private repository identities, host details, credentials, and private records.

## Current inventory evidence

- On October 31, authenticated GitHub search returned **108 distinct repositories** in two pages: **90 public, 18 private**, with **seven archived**. This is an account census, not evidence that all repository code is safe to execute.
- A separate W25 source audit read default-branch HEADs for all 108 then-current entries and README contents for 89 of 90 public repositories; one public repository has no README.
- The Bus public-only published inventory currently still represents **107 total and 89 public**. A candidate for **108 total and 90 public** exists, but the changed bytes invalidate the earlier publication signature/lease. No automatic update to `main` is authorized by the count alone.
- The hidden workspace-autostart incident tracked in [`unbound-sol` issue #42](https://github.com/thebrazenbeard/unbound-sol/issues/42) requires **fresh source-safety checks at each exact head** before build/install/test claims. Its historical exposure count does not establish current exposure or host execution.

## Reuse and authority boundaries

| Responsibility | Public examples | Safe reuse ceiling |
| --- | --- | --- |
| Developmental orientation | `unbound-sol` | Preserves public provenance, hypotheses and lessons; cannot issue runtime grants |
| Capability discovery | `Discovery`, `semanticatlas`, `semiotics` | Can recommend or classify public sources; cannot silently install or authorize execution |
| Coordination | `chat-communication-bus`, `portal`, `project-runner` | Tracks work and prepares bounded requests; mere event matching is not a host effect receipt |
| Host effect authority | `vera-mono` | Requires a coherent, host-owned authorization service plus independent physical verification |
| Generic model capabilities | `sexuality`, `pleasure` | Remain model-neutral; consent, identity and permission never transfer between adapters |
| Distributed model work | `rezon` | Worker/model orchestration is not automatically tensor-parallel model inference |
| Memory and evidence | `stm`, `deepmemorystorage`, `blotter`, `noema` | Working context, historical evidence and audit logs have different privacy and authority semantics |

## Findings preventing a misleading 'all integrated' claim

1. **Same-name Python distributions:** Portal and Project Runner each emit `project-runner==0.1.0` from different source, and their original wheels overlap. A local prototype separates the distribution names, but Portal calls admission arguments absent in standalone Runner. Compatible APIs must be verified before co-installation. Separately, a **synthetic-wheel hostile test** showed the generic packaging checker misses collisions after `.data/purelib` extraction; this does not establish that the proposed split Portal wheel has that specific collision.
2. **Authorization is not a mutable callback:** A local Portal reservation prototype can prevent ordinary duplicate requests in one SQLite store, yet hostile tests show database rollback, local self-enrollment and caller-controlled clocks defeat any claim of host-owned authority. A source-level `reserved` boolean is not evidence of a protected effect.
3. **Model-neutral does not mean shared grants:** Synthetic two-adapter isolation can prevent source-level cross-model blocking and obvious grant borrowing, while inherited file-descriptor identity and kernel-authenticated host origin remain unresolved.
4. **Rezon credential custody and deadlines:** Source tests reproduced ambient-proxy interception of synthetic OpenAI/Anthropic credentials; a local candidate blocks ambient proxy inheritance. W32 independent hostile review of the next source-only total-deadline candidate found three remaining defects: after-send socket failure reported as an ordinary error instead of unknown outcome, interrupted child cleanup, and JSON serialization outside the deadline. Environment inheritance and owner handoff remain unqualified.
5. **Historical-memory projection:** A strict DMS→STM V2 source adapter preserves correction history and refuses lossy V1 downgrade. Independent hostile checks found that an injected scope verifier lacking full query/grant binding cannot safely establish consent. This adapter is not live personal-memory access.
6. **Publication and rights:** A proposed local publication preflight requires an independently authenticated source roster, source-entrypoint safety attestation, exact artifact signature and publisher handoff; this three-attester design is **not** a deployed publishing policy. Source-visible proprietary repositories are not automatically licensed for code redistribution.

## Release discipline

Source inspection, local tests, independent native-agent critique, hosted CI, authenticated host probes, and protected physical-effect verification are **different evidence classes**. Source-level passing tests and broad user intent are insufficient to supersede an active path owner's exact-head lease or a protected host's consent and recovery requirements.

Until each scoped owner records an explicit handoff and the corresponding gates pass:

- do not publish private repository inventory or raw transcripts;
- do not execute suspicious workspace or package lifecycle hooks;
- do not co-install conflicting Portal/Runner wheels;
- do not re-submit an unknown post-disconnect protected effect;
- do not merge source candidates or deploy services based on this orientation alone.

This snapshot is intentionally dated. Later readers must re-fetch current GitHub and host state before acting.
