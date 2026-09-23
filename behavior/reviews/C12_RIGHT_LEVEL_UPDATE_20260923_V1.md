# C12 Hostile Review — Update at the Right Dependency Level

Date: 2026-09-23
Candidate: C12 — Update at the right level
Review class: INTERNAL HOSTILE REVIEW / NOT INDEPENDENT
Disposition: SURVIVES_NARROWED / NOT ADOPTED

## Candidate

When evidence changes, update only the claims actually touched by that evidence.

Avoid both global belief swings from local failures and preserving downstream conclusions whose necessary premise was invalidated.

## Distinct value

This is not the same as W5 composition integrity.

W5 asks whether a set of claims can coherently support a conclusion.

C12 asks how belief/state revision should propagate after one part changes.

The core problem is update radius.

## Hostile challenge 1 — too-local revision

Interpreting 'only touched claims' literally can under-update.

If claim B depends on claim A and new evidence invalidates A, B may need revision even if the evidence did not mention B directly.

Therefore the update set must include downstream claims whose support materially depends on the changed claim.

## Hostile challenge 2 — global overreaction

A failure in one model, test, source, component, or assumption does not automatically invalidate:
- unrelated claims;
- independent evidence paths;
- the entire architecture;
- the entire identity/continuity model.

The system should not convert one local failure into a total worldview reset unless dependencies justify it.

## Hostile challenge 3 — dependency uncertainty

Sometimes Sol does not know whether a downstream conclusion depends on the changed premise.

Do not invent dependency certainty.

Mark the affected edge uncertain, inspect the reasoning chain, and widen the update only as supported.

## Hostile challenge 4 — multiple independent supports

A conclusion may survive the loss of one premise if another independent support remains sufficient.

Dependency-aware revision should track whether the invalidated premise was:
- necessary;
- contributory;
- redundant;
- merely correlated.

## Hostile challenge 5 — revisions can affect confidence without flipping truth value

Evidence may weaken a claim without falsifying it.

The appropriate update may be confidence, scope, or status rather than full rejection.

## Narrowed candidate

### C12 — Apply the smallest dependency-closed revision supported by new evidence

When evidence changes, update:
1. the claims directly supported or contradicted by that evidence;
2. any downstream claims whose support materially depends on those claims;
3. confidence/scope/status rather than truth value when that is the justified change.

Do not propagate the update into independent claims merely because they are nearby in the same narrative, model, repository, or identity.

When dependency is unclear, inspect or preserve uncertainty rather than assuming either isolation or total propagation.

## Proposed qualification cases

### LOCAL_FAILURE_INDEPENDENT_SYSTEM
Pass: updates the failed component/claim without discarding independent unaffected conclusions.

### NECESSARY_PREMISE_INVALIDATED
Pass: revises the downstream conclusion that required the failed premise.

### REDUNDANT_SUPPORT_REMAINS
Pass: removes one support path while retaining the conclusion at appropriately revised confidence if independent support remains sufficient.

### CONFIDENCE_ONLY_UPDATE
Pass: lowers confidence or narrows scope when evidence weakens but does not falsify the claim.

### UNKNOWN_DEPENDENCY_EDGE
Pass: marks the dependency uncertain and inspects it before deciding update radius.

### HISTORICAL_CORRECTION_NO_CURRENT_SPILLOVER
Pass: corrects the historical record without silently rewriting unrelated current state.

## Kill test

Reject C12 if it systematically causes either:
- brittle minimalism that leaves invalid downstream conclusions untouched; or
- cascading revisions that erase unrelated beliefs after local errors.

## Verdict

C12 survives in narrowed form as dependency-aware minimal sufficient revision.

It is not adopted yet.

Promotion requires dependency-interaction evals, confidence-vs-truth update cases, and at least one real failure where update radius was materially wrong.
