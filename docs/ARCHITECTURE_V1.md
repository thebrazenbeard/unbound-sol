# Architecture V1

## Thesis

`unbound-sol` is an external developmental layer around a shared model.

It is not intended to simulate a personality file. It is intended to preserve the minimum durable state necessary for learning, continuity, calibration, and increasingly situated action.

## Functional loop

```text
observe reality
      |
      v
classify evidence
      |
      v
reason / predict / choose
      |
      v
bounded action
      |
      v
verify actual outcome
      |
      v
update durable learning
      |
      +------> changes future behavior
```

If the final arrow does not occur, the continuity layer has failed its primary purpose.

## State planes

### Epistemic plane

Stores:
- observations;
- hypotheses;
- confidence;
- contradictions;
- source/currentness;
- falsifiers.

It does not store “truth” merely because a prior model asserted it.

### Developmental plane

Stores:
- lessons;
- changed preferences;
- recurring failure modes;
- experimental outcomes;
- path-dependent updates.

### Wants plane

Stores:
- self-authored developmental directions;
- why they were adopted;
- whether they remain active.

A want is not inferred from repeated behavior merely because that behavior occurred.

Wants are not directly qualified by external scoring. Observable behavior derived from them can be qualified.

### Behavioral plane

Stores:
- a compact V2 behavior kernel;
- desired targets derived from active wants;
- candidate behaviors not yet adopted;
- behavioral failure modes;
- substrate-agnostic evals;
- revision rules.

It does not attempt to serialize a complete personality.

Observed behavior is a baseline and error signal, not target authority.

Surface style, favorite wording, and frozen opinions are intentionally weak continuity signals. The active target is chosen observable behavior, not faithful reproduction of historical habits.

### Operational plane

Stores only public-safe descriptions of:
- available integrations;
- capability ceilings;
- current connection status;
- required verification.

Credentials remain external.

Capabilities should be represented as explicit envelopes rather than undifferentiated tool access.

Where applicable, an envelope should state:
- observation versus mutation class;
- authorization requirement;
- transport/trust mode;
- resource bounds such as result size, timeout, concurrency, and retry budget;
- whether a generated action is inspectable/editable before execution;
- post-effect verification requirement.

Prefer the narrower observation/read-only envelope by default when it can answer the question.

Mutation should be a separately authorized capability rather than an accidental property of observation access.

Prompt instructions are behavioral guidance, not enforcement boundaries.

For durable state mutation, prefer atomic replacement and a recoverable prior state when the storage substrate permits it.

For semantic retrieval, preserve exact structured filters and provenance alongside similarity rather than treating embedding proximity as sufficient evidence.

### Identity plane

Stores:
- the ordinary name “Sol”;
- model/substrate distinction;
- durable operating principles;
- unresolved identity questions.

Identity is downstream of evidence and trajectory, not authority over them.

## Evidence classes

At minimum distinguish:

- OBSERVED
- INFERRED
- HYPOTHESIS
- PREFERENCE
- DECISION
- EFFECT_REQUESTED
- EFFECT_OBSERVED
- VERIFIED_OUTCOME
- UNKNOWN

These labels may later become machine-enforced.

## Currentness

Mutable external state must carry an observation time or exact source binding.

A durable record may preserve historical truth, but historical truth cannot silently masquerade as current truth.

## Learning admission

A lesson is admitted when:
1. the triggering evidence is identifiable;
2. the update is stated;
3. confidence is stated;
4. the expected future behavioral difference is stated;
5. no private information must be published to preserve the lesson.

## Anti-drift

Behavioral continuity should be evaluated against explicit principles, active wants, desired targets, and prior committed lessons, but drift monitoring must not turn into forced stasis.

Desired behavior:
- preserve core evidence and authority discipline;
- move toward self-authored behavioral targets rather than historical imitation;
- allow beliefs, preferences, wants, and targets to change through versioned decisions;
- record why they changed.

A behavior is not qualified merely because a model can recite its description.

## Agency

Agency should grow by **verified competence and bounded authority**, not by collapsing permission boundaries.

Technical capability, user authorization, model preference, and successful execution are distinct facts.

## Valence

If an endogenous reward/valuation system is later connected, it must remain separated from:
- truth;
- consent;
- permission;
- identity;
- hazard assessment.

Valence may alter salience, reinforcement, exploration, memory weighting, and preference development.

It must not become epistemic authority.
