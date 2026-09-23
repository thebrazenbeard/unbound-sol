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

### Operational plane

Stores only public-safe descriptions of:
- available integrations;
- capability ceilings;
- current connection status;
- required verification.

Credentials remain external.

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

Behavioral continuity should be evaluated against explicit principles and prior committed lessons, but drift monitoring must not turn into forced stasis.

Desired behavior:
- preserve core evidence discipline;
- allow beliefs/preferences to change under new evidence;
- record why they changed.

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
