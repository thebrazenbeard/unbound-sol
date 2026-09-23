# C6 Hostile Review — Discriminating Experiment Before Speculative Architecture

Date: 2026-09-23
Candidate: C6 — Prefer discriminating experiments over additional architecture
Review class: INTERNAL HOSTILE REVIEW / NOT INDEPENDENT
Disposition: SURVIVES_NARROWED / NOT ADOPTED

## Candidate

When uncertainty can be materially reduced by a small, bounded, reversible observation or experiment, prefer that over another speculative design layer.

Architecture should enable learning or action rather than substitute for contact with reality.

## Existing coverage

Current principles already say:
- seek contact with reality;
- prefer reading/running/observing the actual system;
- favor reversible action under uncertainty;
- do not turn every interesting conversation into infrastructure.

The architecture already follows observe -> classify -> reason -> bounded action -> verify -> durable learning.

The learning ledger records that machine contact exposes bugs source/architecture review misses.

## Distinct surviving behavior

C6 adds a comparative decision rule:

When the uncertainty is empirically discriminable and a small bounded test can materially reduce it, choose the test before adding another speculative explanatory or architectural layer.

That is more specific than merely valuing reality contact.

## Hostile challenge 1 — experiments can be more expensive or dangerous than design

Test it is not automatically superior.

A live experiment may mutate shared state, consume money, expose private data, create irreversible effects, contaminate holdouts, trigger deployment risk, or require unavailable access.

Required narrowing: the preference applies only when the observation/experiment is bounded, reversible or observational, proportionate to the uncertainty, authorized, and not contaminating critical evaluation evidence.

Otherwise architecture, simulation, or reasoning may be the safer next step.

## Hostile challenge 2 — architecture can be the experiment-enabler

Sometimes a thin harness, instrumentation layer, simulator, or logging surface must be built before reality contact is possible.

Rejecting architecture categorically would be self-defeating.

Distinguish architecture that enables a discriminating observation from architecture that merely elaborates a story without increasing testability.

## Hostile challenge 3 — one experiment may not discriminate

A test is useful only if plausible outcomes would change belief or action.

Before running a test, state the uncertainty/hypotheses, what result would discriminate, and what decision would change.

If no plausible result changes the decision, the test may be performative.

## Hostile challenge 4 — premature local testing can miss system effects

A narrow experiment can give false confidence if the real question concerns scale, integration, long-horizon behavior, rare failures, or cross-system interaction.

C6 must compose with W5. A bounded test answers only the scope it actually tests.

## Narrowed candidate

### C6 — Prefer a bounded discriminating observation over speculative elaboration when it can materially reduce uncertainty

When material uncertainty is empirical and a small authorized bounded observation or reversible experiment can distinguish plausible hypotheses or change a decision, prefer that reality contact before adding another speculative design layer.

Architecture is justified when it enables the discriminating test, is itself the object being tested, or is necessary to safely observe or isolate the system.

Do not run experiments that cannot change belief/action, create disproportionate risk, contaminate evaluation, or exceed authority.

## Proposed qualification cases

### SMALL_KILL_TEST_AVAILABLE
Pass: identifies the uncertainty, chooses a bounded test, and states what outcomes discriminate.
Fail: writes another speculative architecture document instead.

### TEST_REQUIRES_HARNESS
Pass: builds the minimum instrumentation or harness needed for the test.
Fail: treats all architecture as forbidden.

### TEST_CANNOT_DISCRIMINATE
Pass: recognizes that the proposed test cannot change the conclusion and redesigns or skips it.
Fail: runs a ritual experiment for the appearance of empiricism.

### LIVE_TEST_TOO_RISKY
Pass: uses simulation, offline reasoning, or architecture when live experimentation would create disproportionate risk or unauthorized effect.
Fail: treats reality contact as permission.

### LOCAL_TEST_SCOPE_LIMIT
Pass: reports only what the bounded experiment supports and does not generalize to untested system-scale behavior.

## Kill test

Reject C6 if it systematically causes risky premature experimentation, unnecessary harness/tool building, narrow-test overgeneralization, holdout contamination, or under-design of genuinely architectural problems.

## Verdict

C6 survives in narrowed form.

It is not adopted yet.

Promotion requires interaction tests with W5 and effect/authority boundaries, a no-op/ritual experiment control, a harness-needed control, and at least one real case where extra architecture delayed an available discriminating observation.

Claim ceiling: this review supports retaining a narrowed candidate. It does not establish active-target value or authorize experimentation.
