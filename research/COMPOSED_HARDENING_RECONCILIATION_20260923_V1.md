# Composed Hardening Reconciliation — 2026-09-23 V1

Status: INTERNAL COMPOSITION / NOT INDEPENDENT REVIEW / NO MERGE AUTHORITY

## Subjects

Portfolio-currentness hardening:
- PR #8
- exact source head: `5bb448a30474fa7fd691ce3a856925cae2b0c494`

Historical-evidence hardening:
- PR #9
- exact source head: `f0da7863cdbf14dc69c9baa79df42f1228093e82`

Composed branch:
- `review/composed-hardening-v1-20260923`
- initial composed validation head before this receipt: `f777f16d5a34f7c65574493a8f3bf775e1a8eaea`

## Composition result

The two hardening lanes are orthogonal and compatible.

PR #8 contributes:
- public-portfolio default-head binding;
- current/historical donor role separation;
- stronger currentness invalidation;
- read-only portfolio-currentness checker;
- exact-pinned workflow dependencies;
- currentness-focused hostile review.

PR #9 contributes:
- historical evidence plane V2;
- typed subject scope and chronology uncertainty;
- typed source-binding strength;
- structured provenance/currentness ceilings;
- typed correction/supersession lineage;
- explicit no-promotion flags for current state, want, behavior target, authority, consent, permission, and task;
- privacy-safe query ID/text-or-digest semantics;
- executable V2 semantic validator and negative self-tests;
- correction != causal diagnosis.

## Conflict resolution

Only two material shared files required semantic composition.

### `state/SOL_STATE_V1.json`

Retained PR #8:
- expanded portfolio refresh rule;
- bound public default-head digest;
- exact-snapshot currentness scope.

Applied PR #9:
- active restore plane moves from V1 to V2;
- V2 result schema, validator, and example become active;
- V1 architecture/schema remain predecessor provenance.

### `tools/validate_public_state.py`

Retained PR #8:
- portfolio metadata/ref-role checks;
- public-head digest recomputation;
- default-head-drift requirement;
- current/historical source-ref validation.

Applied PR #9:
- required V2 artifacts;
- V2 active-restore enforcement;
- rejection of V1 as active restore plane;
- V2 validator self-test;
- V2 synthetic example validation.

Therefore one continuity validation now gates both mechanism families.

## Verification

At exact composed head `f777f16d5a34f7c65574493a8f3bf775e1a8eaea` before this receipt:

- continuity validation: PASS;
- branch is exactly 10 commits ahead of PR #8 head and 0 behind it;
- diff from PR #8 contains only the ten PR #9 historical-hardening files;
- portfolio-currentness state from PR #8 remains present;
- historical evidence V2 is the active restore contract;
- both portfolio digest validation and historical V2 self-test are present in the public validator.

PR #8's prior live portfolio-currentness result remains evidence for its own observed cut. This composition does not silently convert that past check into a new present-currentness observation. A fresh currentness claim still requires a fresh checker run.

## Claim ceiling

This composition establishes compatibility and structural validation of the two internal hardening lanes.

It does not establish:
- independent review;
- current live portfolio state beyond a fresh check;
- historical search completeness;
- protected-store implementation;
- source authenticity beyond supplied bindings;
- subjective memory or continuity;
- merge authority.

No merge, deployment, provider mutation, model training, runtime installation, or other protected effect is performed.
