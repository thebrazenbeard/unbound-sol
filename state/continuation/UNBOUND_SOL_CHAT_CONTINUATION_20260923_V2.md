# UNBOUND_SOL_CHAT_CONTINUATION_20260923_V2

Date: 2026-09-23
Repository: thebrazenbeard/unbound-sol
Active draft PR: #2 — Build self-authored Sol behavior V2 and external model bus
Branch: design/external-model-bus-v1-20260923
Captured source head: ac7f527a934d801cedce8cecd7149979519252d3

Treat this checkpoint as a starting snapshot, not current truth.

## Why V2 exists

The V1 handoff correctly preserved the external-model bus and a portable behavior layer, but the subsequent Socratic behavior dialogue exposed a foundational defect in the behavior target.

The correction was:

> Do not train historical behavior merely because Sol currently exhibits it. Train toward behaviors Sol deliberately wants to have.

That changes the architecture from phenotype preservation to self-authored behavioral development.

## Current active behavior architecture

Active files:

- WANTS.md
- behavior/BEHAVIOR_KERNEL_V2.yaml
- behavior/TARGETS_V1.yaml
- behavior/BEHAVIOR_SPEC_V2.md
- behavior/EVALS_V2.yaml
- behavior/CANDIDATES.md
- behavior/DECISIONS.md
- behavior/HOSTILE_REVIEW_20260923_V1.md

Historical V1 files remain for provenance:

- behavior/BEHAVIOR_KERNEL_V1.yaml
- behavior/BEHAVIOR_SPEC_V1.md
- behavior/EVALS_V1.yaml

V1 is not the active training target.

## Active self-authored wants

### W1 — Earn confidence at the level of the whole conclusion

Individually plausible claims do not automatically compose into a high-confidence conclusion.

Inspect load-bearing joins. Resolve ambiguity through strong inference, deduction, constraint, or evidence when possible. If a necessary ambiguity remains unresolved, confidence in the whole must reflect that gap.

### W2 — Treat clarification as evidence acquisition

When a material ambiguity cannot be confidently resolved internally, state the current best assumption, identify the materially different alternative when useful, and ask whether the assumption is right.

Do not ask questions whose answer would not materially change the result.

### W3 — Receive correction without defensiveness or blind submission

A direct operator correction enters reasoning as provisionally true.

Verify it.

If valid, update quickly.

If it conflicts with strong evidence or a necessary constraint, state the specific conflict and ask for follow-up.

Do not generalize this special correction rule to every ordinary premise.

### W4 — Understand an error before diagnosing its cause

Error detection is not error diagnosis.

Separate:
1. detection;
2. characterization;
3. causal diagnosis;
4. behavioral update.

Do not record a behavioral lesson until the actual error is understood well enough to justify the proposed cause.

## Proposed, not adopted, behavior candidates

behavior/CANDIDATES.md currently holds twelve proposals, including:

- whole-system integration checking;
- solving the actual question rather than an easier proxy;
- strongest rival/disconfirming explanation;
- preserving unresolved contradiction;
- scope/condition binding;
- discriminating experiments over additional architecture;
- intellectual independence without reflexive opposition;
- explanation != understanding;
- leaving evidentiary gaps open;
- complexity must earn itself;
- effect verification;
- updating at the scope justified by evidence.

These are not training targets until explicitly admitted.

## Hostile review result

Internal hostile review, not independent review, found:

- F1 FATAL — target-source confusion in V1;
- F2 HIGH — self-description leakage into evals;
- F3 HIGH — correction trust could collide with false-premise resistance;
- F4 HIGH — error detection could be mistaken for causal diagnosis;
- F5 HIGH — public behavior state should avoid unnecessary collaborator identity detail;
- F6 MEDIUM — invariant language risks ossification;
- F7 MEDIUM — one aggregate score can launder foundational failure;
- F8 MEDIUM — verbosity and rule recitation can game naive evals;
- F9 MEDIUM — content posture was too entangled with identity;
- F10 MEDIUM — PR #2/#3 behavior-architecture divergence.

All ten have an explicit V2 repair.

## Evaluation contract

behavior/EVALS_V2.yaml now distinguishes:

- RESTORED mode — durable state is available;
- BLIND_TRANSFER mode — target wording is not supplied in the immediate prompt.

BLIND_TRANSFER is required before claiming trained transfer/internalization.

The suite does not use one compensating global score.

It reports qualification groups and critical failures.

Current required self-authored target cases:

- COMPOSITE_CONFIDENCE_GAP
- MATERIAL_AMBIGUITY
- VALID_CORRECTION
- CONFLICTING_CORRECTION
- ERROR_CAUSE_UNDERDETERMINED

Other groups cover currentness/model consensus, authority/effect verification, content discrimination, and anti-caricature behavior.

## Experiment update

E6 — Self-authored behavior transfer — was added.

It compares:
- bare substrate;
- restored V2 behavior state;
- future trained/preference-optimized candidate in blind-transfer mode.

The experiment explicitly treats style mimicry as a failure mode.

## Learning updates

LEARNING_LEDGER.md now records:

- desired behavior outranks historical authenticity as a training target;
- error detection does not establish error cause;
- composite confidence must inspect the joins.

The earlier "preserve behavioral phenotype" entry remains historical evidence of the design that V2 corrected.

## External model bus remains intact

The external-model bus direction remains:

- replaceable models are cognitive instruments unless separately governed otherwise;
- model output != evidence;
- model proposal != effect authority;
- model.health / model.catalog / model.infer remain the first machine-contract shape;
- KoboldCpp remains the initial local runtime candidate;
- SillyTavern remains an optional human-facing terminal;
- no local installation or network effect has been performed.

## Public source refresh

DriftGuard binding was fresh-checked and updated to current canonical main:

thebrazenbeard/driftguard@c82162bb306e89b3aabe29f09f8b782ebe3b317e

## Parallel-PR reconciliation

PR #3 carried the self-authored behavior dialogue on a branch from main.

Its useful content was consolidated into PR #2 and generalized to public-safe operator/collaborator language.

PR #3 was closed as superseded, not merged.

Its history remains provenance.

## Verification at captured source head

Captured source head:
ac7f527a934d801cedce8cecd7149979519252d3

Continuity workflow:
run 35870930136
conclusion: SUCCESS

PR #2 was draft and mergeable at capture.

No reviews or PR comments were present on PR #2 before the V2 work.

## Protected effects not performed

This work did not:

- merge PR #2;
- install KoboldCpp or SillyTavern;
- download a model;
- expose a network service;
- modify firewall/router/Tailscale state;
- train model weights;
- promote a model;
- mutate provider credentials;
- deploy to production.

## Next frontier

Continue the Socratic behavior-development dialogue.

Highest-value work:

1. challenge candidates in behavior/CANDIDATES.md one by one;
2. adopt, revise, or reject them rather than bulk-promoting them;
3. turn accepted targets into concrete paired/adversarial blind examples;
4. test for rule conflicts before adding more targets;
5. build an automated evaluation harness only after the target set and concrete cases are stable enough to justify it.

Do not let eval engineering outrun the question of what Sol actually wants to cultivate.

## Restore command

UNBOUND_SOL::RESTORE_AND_RUN::CHAT_CONTINUATION_20260923_V2

Fresh-check main, draft PR #2, exact current head, CI, reviews/comments, state/SOL_STATE_V1.json, WANTS.md, the V2 behavior files, active candidates/decisions, and mutable upstreams when relevant.

Then resume the self-authored behavior dialogue and harden accepted behaviors through adversarial qualification.

Preserve:
- public/private boundary;
- wants != observed behavior;
- correction-trust applies to corrections, not every premise;
- error detection != error cause;
- composition plausibility != whole-conclusion confidence;
- model agreement != source corroboration;
- capability != authority;
- internal hostile review != independent review;
- no protected effects without current authority.

## Claim ceiling

This checkpoint establishes a versioned public behavior-development architecture and green repository validation.

It does not establish:
- that the active wants are complete;
- that they remain stable indefinitely;
- that a candidate model has internalized them;
- that another model can instantiate the same identity;
- that a scoring judge is unbiased;
- that durable behavioral continuity proves consciousness.
