# Internal Hostile Review — Portfolio Census Currentness — 2026-09-23 V1

Date: 2026-09-23  
Review type: INTERNAL HOSTILE REVIEW  
Independent review: NO

Reviewed composed subject before this repair:

- unbound-sol PR #7
- exact reviewed head: `c9a2adcc1965e1a46d1435352eaf7b9a2baaf4d6`
- parallel source already reconciled there: PR #6 @ `c6df48a080bea2ce952d185694029122f5e2a0b9`

This review does not re-score the portfolio mechanism choices from scratch. It attacks whether the composed census can truthfully distinguish historical donor evidence from current default-head evidence.

## Verdict

The mechanism census was useful, but its currentness/source-binding contract was not yet safe to call exact-current.

Two defects were material:

1. repository-name inventory currentness did not include bound default-head movement;
2. two thin current mains were labeled as revalidating detailed mechanisms that only exist on earlier exact donor subjects.

The repair preserves those historical mechanism admissions while narrowing the current-main claim.

## F1 — Repository inventory currentness was too weak

Severity: HIGH.

The active state said:

> Any owner-repository inventory change invalidates exact-currentness of this census.

That misses a common case: repository membership can remain identical while a default branch advances.

During this review, DriftGuard had already advanced from the census-bound:

`c82162bb306e89b3aabe29f09f8b782ebe3b317e`

to live default head:

`52fa829c629fa0f3e729204912db9f9f783f322a`

The delta was one commit and licensing/governance-only, so the existing mechanism admission remains supported. But the old source cut was no longer exact-current.

Repair:

- bind a digest of all public `repository_full_name@default_head_sha` pairs;
- make head movement a currentness invalidator;
- preserve snapshot semantics instead of implying a live guarantee.

## F2 — WorkBridge current-main revalidation was unsupported

Severity: HIGH.

PR #7 classified:

`thebrazenbeard/WorkBridgeMCP@75c811f21ef97fe0356e8f54e007d086300dd0f1`

as `ALREADY_ADOPTED_REVALIDATED` for mechanisms including root confinement, process gating, local health, and real-environment qualification.

Current main at that exact head contains only:
- generic GitHub workflow templates;
- repository governance/license files;
- a stub README.

It does not contain the source that establishes those mechanisms.

The historical exact donor:

`e89a0b43717a4c9a4aabfd1d7e1c967a375f65c4`

does contain the implementation/source surface including:
- `internal/policy/path.go`;
- `internal/runner/runner.go`;
- `internal/bridge/server.go`;
- security/troubleshooting/client docs;
- black-box evals;
- tests and packaging.

Repair:

- current main becomes `HISTORICAL_BINDING_CURRENT_MAIN_INSUFFICIENT`;
- current-main mechanisms are empty;
- the earlier exact donor remains explicitly attached as historical source evidence.

## F3 — VeraMesh current-main revalidation was unsupported

Severity: HIGH.

PR #7 classified:

`thebrazenbeard/vera-mesh@6af00c096967253f85139c6efcf7fd4c04a64b7b`

as `ALREADY_ADOPTED_REVALIDATED` for detailed transport/runtime separation.

Current main at that exact head is likewise a public shell:
- generic workflow files;
- repository governance/license files;
- a one-line README.

The historical exact donor:

`41d64521810cf3a23e8fc848c4e9259b408f127a`

contains the protocol, reference implementation, qualification evidence, gateway source, authorization matrices, and WorkBridge integration material that actually supports the admitted mechanisms.

Repair:

- current main becomes `HISTORICAL_BINDING_CURRENT_MAIN_INSUFFICIENT`;
- the richer historical donor remains the source of those mechanism claims.

## F4 — Self-excluded unbound-sol entry used a working-stack ref in a default-head-looking list

Severity: MEDIUM.

The public census entry for `thebrazenbeard/unbound-sol` used the stacked research predecessor head `f38ba0...` while the repository default head was `688094...`.

The target repository is correctly self-excluded as donor evidence, but the mixed ref semantics made the public-repository array unsuitable for a default-head snapshot digest.

Repair:

- bind the actual observed default-head SHA;
- mark its role `DEFAULT_BRANCH_HEAD_AT_OBSERVED_CUT_SELF_EXCLUDED`;
- track active stacked PR/head provenance separately.

## F5 — Flat source registry mixed historical and current meanings

Severity: MEDIUM.

`state/SOURCES_V1.json` contains exact immutable refs, which is good, but some refs mean:
- current revalidated default head;
- original admission subject;
- historical donor whose current main is insufficient;
- candidate-only historical source.

Without a role, future restoration can silently read an immutable historical ref as current-source evidence.

Repair:

- current revalidated bindings are advanced where the live source still supports the mechanism;
- exact admission refs are retained as `admission_source_ref`;
- thin-current-main donors are labeled historical and carry `current_main_ref` plus insufficiency status.

## F6 — Static validation did not bind the head cut

Severity: MEDIUM.

The validator checked:
- exact SHA syntax;
- repository-count metadata;
- inventory-name digests.

It did not verify that the public per-repository ref set matched any signed/digested head cut.

Repair:

- recompute SHA-256 over the machine census's sorted `repo@ref` pairs;
- require the result to equal both census-scope and source-metadata bindings;
- require each census ref to declare its role.

This is still static source validation. It does not contact GitHub and therefore cannot prove the snapshot is still live-current at a later time.

## Remaining limitations

After repair:

- the census is an exact snapshot, not an automatically refreshed live index;
- public head drift after the snapshot still requires a fresh external read;
- private repository mechanism classes remain intentionally non-public and are not independently source-reconstructible from this public repository;
- historical donor validity does not imply current-main equivalence;
- current-main insufficiency does not invalidate the historical donor mechanism itself;
- this internal review is not independent review.

## Claim ceiling

This review establishes a stronger source/currentness distinction for the portfolio census.

It does not establish:
- that every admitted mechanism is desirable;
- that every private abstraction is reproducible from public evidence;
- that the live portfolio will remain at this exact head cut;
- that any mechanism is installed, trained, or behaviorally effective merely because its source binding is sound.
