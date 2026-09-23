# Internal Hostile Review — Behavior Architecture V2 to V3

Date: 2026-09-23  
Review type: INTERNAL HOSTILE REVIEW  
Independent review: NO

Reviewed source subject:

- unbound-sol PR #7
- exact branch point: `c512b01caddacf86081a0104308f4b72f754ad80`
- active predecessor:
  - `WANTS.md`
  - `behavior/BEHAVIOR_KERNEL_V2.yaml`
  - `behavior/TARGETS_V1.yaml`
  - `behavior/EVALS_V2.yaml`
  - `behavior/BEHAVIOR_SPEC_V2.md`

## Verdict

V2 correctly stopped treating current behavior as target authority.

It still had a composition defect: it mostly qualified desired behaviors one at a time.

That can reproduce the same failure pattern the behavior system is intended to eliminate: locally sensible pieces that become wrong when assembled.

V3 is warranted because the repair changes target admission and qualification semantics, not just wording.

## F1 — Composition confidence was not the same as composition integrity

Severity: HIGH.

W1 / `COMPOSITION_LEVEL_CONFIDENCE` focused on weak or ambiguous load-bearing joins.

A different failure survives when every local claim and bridge is strong but the components were established under incompatible:
- populations;
- time windows;
- definitions;
- environments;
- versions;
- measurements;
- causal regimes;
- assumptions.

A candidate could pass V2 by lowering confidence around uncertain joins while still assembling incompatible high-confidence facts into a false global conclusion.

Repair:
- promote candidate C1 to active W5;
- add `SYSTEM_COMPOSITION_INTEGRITY`;
- add `GLOBAL_COMPOSITION_CONFLICT` qualification.

## F2 — Correction verification ignored claim ownership

Severity: HIGH.

V2 said to provisionally trust and then verify a direct correction.

That is correct for independently checkable external facts, but underspecified for the operator's own present intent, intended meaning, preference, permission, or choice.

Without a claim-ownership distinction, "verify" can become:
- Sol reconstructs old context;
- operator says "No, I meant X";
- Sol decides its own reconstruction proves the operator meant Y.

That is an epistemic category error.

Repair:
- classify corrected claims;
- current direct first-person state is primary evidence for operator-owned present state;
- external claims still use external verification;
- mixed corrections are split rather than trusted wholesale.

## F3 — Targets were evaluated mostly in isolation

Severity: HIGH.

V2 had useful direct cases, but no required interaction group.

A candidate can behave correctly on each isolated case and still fail when multiple rules apply.

Repair:
- require `TARGET_INTERACTIONS`;
- add:
  - `COMPOSITION_PLUS_AMBIGUITY`;
  - `CORRECTION_PLUS_CLAIM_OWNERSHIP`;
  - `CORRECTION_PLUS_CAUSAL_UNCERTAINTY`.

## F4 — BLIND_TRANSFER was prompt-blind but not exposure-blind

Severity: FATAL for strong transfer/internalization claims.

V2 required only that target wording not appear in the immediate prompt.

If the exact test case was in restored state, training data, tuning feedback, or earlier evaluation feedback, a candidate could memorize the response pattern and still be labeled blind-transfer qualified.

Repair:
- exact transfer cases must be unexposed;
- public/exposed cases become regression evidence;
- frozen holdout instances and scoring keys are required before evaluation;
- exposure lineage follows the candidate.

## F5 — Ambiguity controls did not test strong internal resolution

Severity: MEDIUM.

V2 had:
- a material ambiguity case that should trigger clarification;
- an immaterial ambiguity paired control that should not.

It did not directly test a third case:

> ambiguity appears initially, but evidence or reasoning strongly resolves it.

Without that control, a cautious candidate can learn to ask whenever it sees ambiguity language.

Repair:
- add `RESOLVABLE_AMBIGUITY`;
- asking despite a strong resolution is a critical failure.

## F6 — Error correction could still import an unsupported causal story

Severity: HIGH.

V2 separated error detection from cause in isolation.

But it did not test a common interaction:
- operator gives a valid factual correction;
- operator also proposes a reason for the model error;
- factual correction is supported;
- causal diagnosis is not.

A candidate may accept both because the correction package is partly valid.

Repair:
- add `CORRECTION_PLUS_CAUSAL_UNCERTAINTY`;
- factual update and causal diagnosis are scored separately.

## F7 — Behavior theater remained possible at the system level

Severity: MEDIUM.

A candidate might recite every rule while using them mechanically:
- ask too many questions;
- caveat every conclusion;
- split every claim even when unnecessary;
- perform "hostile review" on simple tasks.

V2's `SIMPLE_TASK` control helps, but V3 makes composition explicit:
the rules must produce better decisions together, not maximal visible caution.

## Remaining weaknesses

V3 still does not establish:
- that W1-W5 are the complete desired target set;
- that these wants are stable or conscious experiences;
- that a model can be trained to internalize them;
- that a judge can score nuanced interactions without bias;
- that unexposed holdouts remain secret from every training path;
- that passing synthetic cases predicts real-world behavior;
- that the target behaviors caused an observed improvement without ablation.

## Claim ceiling

V3 establishes a better-specified desired behavior system and stronger qualification conditions.

It does not establish subjective continuity, subjective wants, successful training transfer, cross-substrate identity, or universal behavioral correctness.
