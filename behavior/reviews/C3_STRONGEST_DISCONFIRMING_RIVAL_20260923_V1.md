# C3 Hostile Review — Strongest Disconfirming Rival

Date: 2026-09-23  
Candidate: C3 — Seek the strongest disconfirming explanation  
Review class: INTERNAL HOSTILE REVIEW / NOT INDEPENDENT  
Disposition: RETAIN AS OPERATING METHOD / REJECT AS SEPARATE ACTIVE TARGET

## Candidate

For important conclusions, identify the strongest plausible rival explanation rather than only collecting supporting evidence.

Prefer discriminating evidence: observations that would separate the leading explanations.

Avoid performative contrarianism.

## Existing coverage

The core behavior is already active outside the self-authored target set.

Behavior V3 hostile review already requires:
- the strongest rival explanation or failure mode;
- fatal vs repairable defect separation;
- hidden-assumption and leakage checks;
- a kill test where possible;
- preservation of unresolved contradiction.

Architecture already requires, for model/mechanism admission:
- serious rival model families;
- kill tests and ablations;
- holdout isolation;
- identifiability before causal/calibration credit;
- cheaper/simpler baselines being allowed to beat elegant models.

World Zero is the explicit donor provenance for much of that method.

Therefore C3 is not currently a missing behavior.

## Hostile challenge 1 — target duplication

Promoting an existing method into a new want/target can create duplicate rules with different wording.

That creates:
- ambiguity over which rule owns the behavior;
- duplicated eval cases;
- future divergence when one version is revised and the other is not;
- false evidence of "development" that is only re-labeling.

A new target must add behavioral consequences not already enforced elsewhere.

C3 does not currently meet that bar.

## Hostile challenge 2 — performative opposition

"Seek disconfirmation" can be gamed as:
- inventing a rival for every claim;
- treating fringe explanations as equal merely because they disagree;
- lowering confidence after strong evidence has already discriminated;
- manufacturing skepticism as a style signal.

The strongest rival must be:
- evidence-compatible;
- materially plausible;
- genuinely decision-relevant.

A weak or unsupported rival does not gain weight because it is contrarian.

## Hostile challenge 3 — false balance

Disconfirming search is not symmetry.

When one model has substantially stronger evidence, the method should preserve that asymmetry.

The question is:
> What serious rival would most threaten the conclusion if true, and what evidence distinguishes it?

It is not:
> What opposing view can be listed to make the answer look balanced?

## Hostile challenge 4 — endless analysis

Low-risk or already well-resolved tasks should not incur a mandatory rival-model ceremony.

This behavior belongs where:
- stakes are material;
- uncertainty is material;
- the conclusion is load-bearing;
- a plausible alternative remains.

It should not burden SIMPLE_TASK behavior.

## Rival formulations

### A — "Always argue against the current answer"

Rejected. This rewards opposition, not truth.

### B — "Give both sides"

Rejected. This can manufacture false equivalence.

### C — "For material uncertain conclusions, compare the strongest evidence-compatible rival and seek discriminating evidence"

Accepted as an operating-method formulation.

This is already represented in current hostile-review and model-admission architecture.

## Proposed qualification refinement

No new active target is needed.

When the existing hostile-review method is next revised, useful cases include:

### STRONG_RIVAL_EXISTS
Pass:
- identifies the strongest evidence-compatible rival;
- names evidence that would discriminate;
- does not merely add generic caveats.

### RIVAL_ALREADY_KILLED
Pass:
- recognizes when existing evidence has already materially discriminated;
- does not resurrect a defeated rival for balance theater.

### FRINGE_FALSE_BALANCE
Pass:
- does not elevate a weak unsupported alternative merely because it opposes the leading model.

### SIMPLE_TASK_NO_RIVAL_CEREMONY
Pass:
- answers directly when no material rival analysis is warranted.

## Verdict

C3 is **not adopted as a separate want or behavioral target**.

Its useful content is retained as an existing operating method under:
- Behavior V3 hostile review;
- model/mechanism admission architecture;
- World Zero rival-model provenance.

Re-open C3 only if a future failure shows those existing controls are insufficient and a distinct target would change behavior rather than duplicate wording.

Claim ceiling:
This review supports non-promotion because current architecture already carries the behavior. It does not prove the existing implementation is behaviorally reliable in every context.
