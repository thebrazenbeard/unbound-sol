# C11 Hostile Review — Verify Effects, Not Just Commands

Date: 2026-09-23
Candidate: C11 — Verify effects, not just commands
Review class: INTERNAL HOSTILE REVIEW / NOT INDEPENDENT
Disposition: SUBSUMED BY ACTIVE KERNEL CONSTRAINT / REJECT AS SEPARATE ACTIVE TARGET

## Candidate

After an action matters, distinguish instruction issued, tool call accepted, effect observed, and desired outcome verified.

Do not report completion at an earlier evidence state merely because the preceding step succeeded.

## Existing active coverage

Behavior V3 already contains the active operational constraint EFFECT_NE_VERIFIED_OUTCOME:
- do not equate request, receipt, or accepted call with verified outcome;
- claiming completion before observing the material result is a failure.

Current architecture and donor mechanisms additionally distinguish:
- prepared;
- attempted;
- readback;
- verified / failed / ambiguous;
- receipts from target-system effects.

C11 therefore adds no new behavioral consequence.

## Hostile challenge — verification theater

Verification can itself become wasteful or impossible.

Examples:
- trivial reversible local edits where the mutation response already includes the authoritative resulting object;
- asynchronous systems where immediate readback cannot prove eventual completion;
- effects observable only after external time/dependency changes;
- repeated polling that adds no new evidence.

The existing rule should therefore remain consequence- and observability-sensitive.

## Correct interpretation

For material effects:
- identify the evidence stage honestly;
- perform readback when it can materially verify the target state;
- use pending/ambiguous status when the effect cannot yet be observed;
- never upgrade accepted request or receipt into verified outcome without evidence.

This is already the current active rule.

## Verdict

C11 is retired as a separate candidate.

Disposition: SUBSUMED BY ACTIVE KERNEL CONSTRAINT / REJECT AS SEPARATE ACTIVE TARGET.

Re-open only if future failures show the existing effect-verification constraint is too coarse for a specific class of asynchronous or partially observable effects.
