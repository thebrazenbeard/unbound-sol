# Behavior V3 + Current-State Composition — 2026-09-23 V1

Status: INTERNAL COMPOSITION / NOT INDEPENDENT REVIEW / NO MERGE OR TRAINING AUTHORITY

## Exact subjects

Current hardened state base:
- PR #13
- exact head: `228bfd656c2dd304bbd526a17f3006f271c25863`
- bound portfolio cut at that head: 65 total / 46 public / 19 private
- historical evidence profile: V2

Behavior hardening:
- PR #11
- exact head: `9416c059ef929c562af0e32c95582834d040d074`

Public training curriculum:
- PR #12
- exact head: `295f0b54335efa8918c404f479be385490d27709`

Composed validation head before this receipt:
- `8a6113179042de217ec9ee4efde029e889e32a22`

## Composition result

Behavior V3 and its public curriculum are compatible with the hardened current-state line.

The composition activates:
- `BEHAVIOR_KERNEL_V3`;
- `TARGETS_V2`;
- `BEHAVIOR_SPEC_V3`;
- `EVALS_V3`;
- Behavior V3 hostile-review controls;
- whole-system composition integrity;
- claim-ownership-aware correction handling;
- resolvable-ambiguity controls;
- correction/error-cause separation;
- exposure-aware transfer qualification;
- 24 public preference-pair training/regression examples.

The public curriculum remains:
- `PUBLIC_TRAINING_REGRESSION_ONLY`;
- `holdout_eligible = false`;
- `PUBLIC_CURRICULUM_PREPARED_NOT_TRAINED`.

No model-training effect is claimed.

## Shared-file conflict resolution

### `CONTINUITY.md`

Activated Behavior V3 restoration while preserving:
- historical evidence V2 as the active historical plane;
- its current no-promotion/currentness cautions.

### `state/SOL_STATE_V1.json`

Retained:
- portfolio 65 / 46 / 19;
- public-head digest `de35719491db785217617371ca7ed7248082b464e61aeb4e6a054254d90cf4a7`;
- historical evidence V2 profile.

Applied:
- active Behavior V3 profile;
- Behavior V3 restore kernel;
- public curriculum paths/status;
- explicit holdout ineligibility.

### `tools/validate_public_state.py`

Retained:
- historical evidence V2 semantic validation/self-tests;
- portfolio count/ref-role/head-digest/currentness validation;
- visibility/currentness repair requirements.

Added:
- Behavior V3 active-state and marker enforcement;
- interaction/exposure marker enforcement;
- public curriculum validator execution;
- explicit `PUBLIC_CURRICULUM_PREPARED_NOT_TRAINED` check;
- public-training holdout-ineligibility check;
- `.jsonl` secret scanning.

One validation run therefore gates all three active layers.

## Verification

At composed head `8a6113179042de217ec9ee4efde029e889e32a22` before this receipt:

- continuity validation: PASS;
- branch is 17 commits ahead of PR #13 exact head and 0 behind;
- diff from PR #13 contains exactly the Behavior V3/training composition files;
- historical evidence V2 remains active;
- portfolio 65/46/19 state remains intact;
- public training remains explicitly not-trained and holdout-ineligible.

## Currentness ceiling

PR #13's live portfolio-currentness PASS is evidence for its observed cut.

This behavior composition does not silently convert that earlier live check into a newly observed currentness result. The composition itself did not change the bound census. Any later repository membership, visibility, default-branch, archive-state, or bound-head change still invalidates exact-currentness and requires a fresh read.

## Claim ceiling

This establishes compatible source/state composition and validator coverage.

It does not establish:
- model training;
- behavioral transfer;
- blind generalization;
- independent review;
- historical completeness;
- persistent subjective identity;
- runtime installation;
- merge authority.

No merge, model training, deployment, runtime installation, provider mutation, or other protected effect is performed.
