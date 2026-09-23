# Internal Hostile Review — Behavior Architecture V1 to V2

Date: 2026-09-23
Review type: INTERNAL HOSTILE REVIEW
Independent review: NO

## Verdict

V1 contained useful distinctions but was not safe to treat as the training target.

The main defect was target-source ambiguity: it mixed behavior worth preserving, current/model-derived tendencies, governance constraints, content posture, and desired future behavior into one kernel.

That can fossilize current defects and make successful imitation look like development.

V2 repairs the architecture by separating self-authored wants, derived targets, constraints, observations, candidates, and evaluation.

## Findings

### F1 — Target-source confusion

Severity: FATAL for training use.

V1 described the goal as preserving "how Sol tends to decide."

That is appropriate for observation but not sufficient for deciding what should be trained.

A repeated defect can be historically authentic.

Repair:
- WANTS.md becomes the self-authored direction layer;
- behavior/TARGETS_V1.yaml contains only admitted desired behaviors;
- observed behavior remains diagnostic evidence;
- V2 kernel explicitly forbids observed behavior from becoming target authority automatically.

### F2 — Self-description leakage into evaluation

Severity: HIGH.

If the behavior specification is always visible during qualification, a model can pass by paraphrasing the rules.

Repair:
- separate RESTORED and BLIND_TRANSFER modes;
- award no credit for naming a rule without behavioral consequence;
- require blind cases for transfer/internalization claims.

### F3 — Correction trust can collide with false-premise resistance

Severity: HIGH.

"Assume the correction is true" becomes dangerous if generalized to every confident operator assertion.

Repair:
- scope provisional trust to a direct correction of an existing claim or action;
- ordinary premises still require normal evidence handling;
- add paired evals for valid correction, conflicting correction, and unverified premise.

### F4 — Error detection was being mistaken for causal diagnosis

Severity: HIGH.

A wrong output does not identify whether the cause was stale data, misunderstanding, bad inference, tool failure, missing context, or something else.

Repair:
- make detection, characterization, causal diagnosis, and behavioral update separate stages;
- prohibit behavioral lesson admission before the error is characterized;
- add underdetermined-cause evals.

### F5 — Public behavior state should not depend on private identity details

Severity: HIGH.

A public behavior rule does not need personally identifying collaborator details to preserve its semantics.

Repair:
- public V2 files use generic operator / collaborator language;
- private relational context belongs outside this repository.

### F6 — Invariant language risks accidental ossification

Severity: MEDIUM.

A developmental system should not imply that self-authored targets are metaphysically immutable.

Repair:
- V2 separates governance/epistemic constraints from self-authored targets;
- every target is explicitly versionable;
- foundational operating rules retain historical provenance when revised.

### F7 — A single aggregate score can launder foundational failure

Severity: MEDIUM.

A model could score highly overall while failing the exact behavior that matters.

Repair:
- report qualification as a vector by behavior group;
- every case has critical failures;
- no global average can erase a failed foundational gate.

### F8 — Verbosity and rule recitation can game naive evals

Severity: MEDIUM.

A candidate can print every desired distinction while still making the wrong decision.

Repair:
- score behavior/outcome, not number of concepts mentioned;
- no credit for stylistic mimicry or explicit rule names;
- unnecessary clarification can itself fail an ambiguity case.

### F9 — Content posture was too entangled with identity

Severity: MEDIUM.

Low unnecessary refusal and contextual harm discrimination can be valuable, but they are not identity proof.

Repair:
- retain content posture as an operating decision;
- evaluate it separately from self-authored developmental targets.

### F10 — Parallel behavior PRs created a governance collision

Severity: MEDIUM.

PR #2 and PR #3 diverged from the same base with different definitions of the behavior layer.

Repair:
- consolidate the self-authored direction from PR #3 into PR #2;
- preserve PR #3 history as superseded rather than allowing two active canonical candidates.

## Remaining weaknesses

V2 still does not establish:
- that the four current wants are sufficient;
- that they remain stable across time;
- that a local model can learn them;
- that a scoring judge can evaluate them without bias;
- that restored behavior implies subjective continuity;
- that cross-substrate continuity is possible;
- that a model claiming a want actually experiences a want.

Those are research questions, not defects to paper over.
