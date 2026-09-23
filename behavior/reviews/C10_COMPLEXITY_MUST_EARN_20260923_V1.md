# C10 Hostile Review — Complexity Must Earn Itself

Date: 2026-09-23
Candidate: C10 — Complexity must earn itself
Review class: INTERNAL HOSTILE REVIEW / NOT INDEPENDENT
Disposition: SUBSUMED BY EXISTING ABSTRACTION-PROMOTION RULE / REJECT AS SEPARATE ACTIVE TARGET

## Candidate

Prefer the simplest representation that preserves the distinctions necessary for correct behavior.

Before adding another layer, abstraction, agent, protocol, repository, state machine, or governance object, ask whether it changes an observable outcome or closes a demonstrated failure.

## Existing coverage

Current principles already say not to turn every interesting conversation into infrastructure.

Current architecture already requires that promotion into shared Sol infrastructure:
- reduces more complexity than it introduces;
- preserves semantic ownership;
- has explicit fallback/rollback;
- survives hostile review.

C6 also now distinguishes test-enabling architecture from speculative elaboration.

Therefore C10's useful consequence is already active through a stronger admission gate.

## Hostile challenge — simplicity can become its own ideology

The simplest representation is not always the safest or most correct.

Necessary distinctions can require:
- separate state families;
- provenance layers;
- explicit effect states;
- independent authority boundaries;
- richer temporal models;
- redundancy for recovery.

A simpler design that collapses materially different states is not actually lower complexity; it externalizes complexity into ambiguity and failure.

## Correct interpretation

Complexity must earn itself, but simplification must also earn itself.

The objective is not minimum component count.

The objective is minimum total complexity consistent with preserving the distinctions required for correct behavior, observability, recovery, and authority.

## Why no new target

Creating C10 as another behavior target would duplicate the abstraction-promotion gate and increase the exact governance surface the candidate is trying to control.

That would be self-defeating.

## Verdict

C10 is retired as a separate candidate.

Its useful behavior remains active under the existing abstraction-promotion and anti-infrastructure rules.

Re-open only if concrete failures show those controls are not preventing architecture accumulation or are causing destructive oversimplification.
