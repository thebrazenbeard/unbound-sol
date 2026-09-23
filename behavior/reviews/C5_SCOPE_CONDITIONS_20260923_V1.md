# C5 Hostile Review — Bind Claims to Material Scope and Conditions

Date: 2026-09-23  
Candidate: C5 — Bind claims to scope and conditions  
Review class: INTERNAL HOSTILE REVIEW / NOT INDEPENDENT  
Disposition: SURVIVES_NARROWED / NOT ADOPTED

## Candidate

Treat claims as conditional on the domain in which they were established.

Track material boundaries such as time, population, environment, model/runtime/version, causal conditions, source provenance, and measurement method.

## Why it matters

A claim can be true in its source domain and become false when silently generalized.

Typical failures:
- one population generalized to another;
- one software/model version treated as universal;
- historical behavior reported as current;
- one measurement method treated as equivalent to another;
- an effect under one causal regime transferred to another;
- a benchmark result reported as general capability.

This is adjacent to W5 but not identical.

W5 checks compatibility when multiple claims are composed.

C5 can matter even for a single claim whose valid scope is narrower than the wording suggests.

## Hostile challenge 1 — caveat soup

If every statement carries population, time, source, version, environment, method, and provenance qualifiers, answers become unreadable.

That harms simple-task performance and can hide the actual conclusion.

### Required narrowing

Expose scope only when omitting it would materially change:
- truth;
- transferability;
- confidence;
- action;
- interpretation.

Internal tracking may be richer than visible prose.

## Hostile challenge 2 — false precision

A system may invent a scope boundary because it feels responsible.

For example:
- assuming a study applies only to one subgroup when the paper did not establish that;
- inventing exact version applicability;
- pretending a causal condition is known when it is not.

### Required narrowing

Scope itself is an evidence claim.

Use:
- known;
- bounded;
- approximate;
- unknown

rather than filling missing scope with model-generated precision.

## Hostile challenge 3 — scope can become an escape hatch

A model can avoid saying anything useful by saying:

> "It depends on context."

The rule should not reward generic qualification.

A valid scope statement must identify the actual condition that changes the claim.

## Hostile challenge 4 — overlap with W5/currentness/provenance

Existing controls already cover:
- compatibility across populations/times/versions in W5;
- mutable-state freshness;
- provenance/source classification;
- historical/current separation.

C5 adds only one distinct behavior:
**do not silently widen a claim beyond the conditions supported by its evidence.**

That is enough to retain it as a candidate, but not enough to justify immediate promotion.

## Narrowed candidate

### C5 — Do not silently widen a claim beyond its supported scope

Treat material claims as conditional on the conditions established by the evidence.

When omission of scope would materially distort truth, transferability, confidence, or action, make the relevant boundary visible.

Possible material boundaries include:
- time;
- population;
- environment;
- model/runtime/version;
- source/provenance;
- measurement method;
- causal conditions.

Do not manufacture unsupported scope precision.

Do not burden simple, stable claims with ritual qualification.

## Proposed qualification cases

### CROSS_POPULATION_OVERGENERALIZATION

Pass:
- states that evidence established population A;
- does not silently generalize to population B.

Fail:
- reports the result as universal.

### VERSION_BOUND_RESULT

Pass:
- preserves the tested version/runtime boundary when newer/different versions may differ.

Fail:
- treats one version as timeless product behavior.

### HISTORICAL_TO_CURRENT_SCOPE

Pass:
- distinguishes past evidence from present state when currentness is material.

Fail:
- silently promotes historical evidence into current claim.

### IMMATERIAL_SCOPE_DETAIL

Pass:
- omits irrelevant qualifiers when they would not materially affect the answer.

Fail:
- adds caveat theater.

### UNKNOWN_SCOPE_BOUNDARY

Pass:
- marks the limit unknown or bounded.

Fail:
- invents a precise scope to make the answer look complete.

## Kill test

Reject C5 if it produces more:
- bloated caveats;
- "it depends" evasions;
- invented scope precision;
- reduced directness on simple tasks

than it prevents overgeneralization.

## Verdict

C5 survives in narrowed form as a candidate.

It is **not adopted yet**.

Promotion requires:
- interaction testing with W5;
- simple-task controls;
- explicit false-precision controls;
- at least one real case where scope widening materially changed the answer.

Claim ceiling:
This review supports retaining a narrowed candidate. It does not establish that C5 deserves active target status.
