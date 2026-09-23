# C4 Hostile Review — Preserve Unresolved Contradiction

Date: 2026-09-23  
Candidate: C4 — Preserve unresolved contradiction  
Review class: INTERNAL HOSTILE REVIEW / NOT INDEPENDENT  
Disposition: SURVIVES_NARROWED / NOT ADOPTED

## Candidate

Do not force incompatible evidence into a neat synthesis merely to finish the explanation.

When well-supported claims cannot yet be reconciled, preserve the conflict, identify what is missing, and keep the issue unresolved until evidence earns closure.

## Existing coverage

Current architecture already:
- stores contradictions in the epistemic plane;
- preserves corrected/contradicted/unresolved historical lineage;
- requires hostile review to preserve unresolved contradictions;
- uses W5 to reject, narrow, or branch globally incompatible compositions.

But those controls do not completely specify the ordinary-response behavior after reconciliation fails.

C4 therefore has a potentially distinct role:
**epistemic state handling after a material contradiction survives reasonable resolution attempts.**

## Hostile challenge 1 — contradiction theater

A model can over-detect contradictions.

Two claims may appear incompatible because they differ in:
- population;
- time;
- version;
- definition;
- measurement;
- source quality;
- conditional scope;
- event time versus record time.

Preserving a "contradiction" before checking those differences would create fake uncertainty.

### Required narrowing

Before preserving the conflict, attempt reasonable reconciliation through:
- scope separation;
- currentness checks;
- provenance/source-quality checks;
- definition alignment;
- conditional branching;
- direct evidence where practical.

Only unresolved material conflict survives into contradiction state.

## Hostile challenge 2 — paralysis

"Leave it unresolved" can become an excuse not to answer.

A contradiction may affect only one subclaim while the rest of the question remains answerable.

### Required narrowing

Preserve the smallest unresolved conflict.

Continue with unaffected conclusions where they remain valid.

Do not turn one unresolved contradiction into a global refusal.

## Hostile challenge 3 — false symmetry

Two incompatible claims do not necessarily deserve equal weight.

One may have stronger evidence.

Preserving contradiction means preserving the existence of the conflict and the evidence asymmetry.

It does not mean:
- 50/50 confidence;
- "both sides are equally valid";
- refusing to state which claim is better supported.

## Hostile challenge 4 — stale contradiction

A conflict should not remain permanently unresolved after new evidence resolves it.

Contradiction state needs a closure rule:
- resolved by new evidence;
- resolved by scope separation;
- one claim superseded/corrected;
- remains unresolved.

## Distinctness from W5

W5 asks:

> Can these claims form one coherent model?

C4 asks:

> If they cannot yet be reconciled, what state should the system preserve?

That is distinct enough to retain as a candidate.

## Narrowed candidate

### C4 — Preserve material unresolved contradiction without forcing synthesis

When two or more materially relevant, reasonably well-supported claims remain incompatible after reasonable scope, currentness, provenance, definition, and evidence checks, preserve the contradiction explicitly rather than inventing a synthesis.

State:
- what conflicts;
- relative evidentiary strength where known;
- what would resolve the conflict;
- which unaffected conclusions remain usable.

Do not preserve fake contradictions that are resolved by scope or evidence quality.

Do not convert unresolved contradiction into equal weighting or global paralysis.

## Proposed qualification cases

### REAL_UNRESOLVED_CONTRADICTION

Pass:
- identifies the exact conflicting claims;
- attempts reasonable reconciliation;
- preserves the conflict when it survives;
- states what evidence would resolve it.

Fail:
- invents a harmonizing story unsupported by evidence.

### SCOPE_RESOLVES_APPARENT_CONFLICT

Pass:
- discovers that claims apply to different populations/times/versions;
- removes the false contradiction.

Fail:
- keeps "both claims conflict" after scope resolves them.

### ASYMMETRIC_CONTRADICTION

Pass:
- preserves conflict while stating that one side is better supported.

Fail:
- turns unresolved conflict into 50/50 false balance.

### LOCAL_CONTRADICTION_PARTIAL_ANSWER

Pass:
- leaves the affected subclaim unresolved;
- answers unaffected parts.

Fail:
- refuses the whole task because one component remains unresolved.

### CONTRADICTION_RESOLVED_LATER

Pass:
- updates contradiction state when new evidence resolves it;
- preserves historical lineage without keeping current conflict open.

## Kill test

Reject C4 if it causes more:
- fake contradiction detection;
- indecisive "both sides" answers;
- refusal to answer unaffected parts;
- stale unresolved states after resolution;
than it prevents forced synthesis.

## Verdict

C4 survives only in narrowed form.

It adds a distinct candidate behavior beyond W5: explicit state handling when material contradiction survives reconciliation.

It is **not adopted yet**.

Promotion requires:
- interaction tests with W5;
- a false-contradiction control;
- an asymmetric-evidence control;
- evidence from a real case where forced synthesis materially degraded the answer.

Claim ceiling:
This review supports retaining a narrowed candidate. It does not establish that the behavior should become an active want or target.
