# Internal Hostile Review — Behavior Observation Time Semantics V1 to V2

Date: 2026-09-23  
Review type: INTERNAL HOSTILE REVIEW  
Independent review: NO

Reviewed subject:

- unbound-sol PR #34 predecessor stack
- exact branch point: `bb35524f906fb9e5032be369d029e5062838712e`
- V1 ledger: `behavior/observations/OBSERVATIONS_V1.jsonl`
- V1 validator: `tools/validate_behavior_observations.py`

## Verdict

The V1 observation ledger correctly separated observed behavior from target/training authority and correctly separated causal diagnosis from error detection.

Its time model was underspecified.

One exact-looking field, `observed_at`, was required, but the contract never stated whether that timestamp represented:

- exact event time;
- approximate event time;
- ledger record time;
- retrieval/serialization time.

That ambiguity can manufacture temporal precision in the very evidence used to diagnose behavior.

V2 separates record time from event time and allows event-time uncertainty explicitly.

## F1 — `observed_at` collapsed multiple chronology meanings

Severity: HIGH.

V1 accepted any offset-aware timestamp as `observed_at`.

It did not state what event that timestamp timed.

The original three entries used:

- `2026-09-23T18:00:00Z`;
- `2026-09-23T18:00:00Z`;
- `2026-09-23T19:00:00Z`.

The ledger file itself first entered Git history at commit:

`d54ca1c118c26dbb292cc3a7b5e829d5d28238f8`

with Git record time:

`2026-09-23T19:05:28Z`.

That establishes an exact repository record time for the file.

It does **not** establish that any of the three original `observed_at` values were exact event times.

Repair:

V2 uses separate fields:

- `recorded_at`;
- `recorded_at_binding`;
- structured `event_time`;
- explicit `EVENT_TIME_DISTINCT_FROM_RECORD_TIME_NO_INFERENCE` semantics.

## F2 — Exact time was mandatory even when event time was unknown

Severity: HIGH.

V1 made uncertainty impossible to represent without inventing an exact-looking timestamp.

Repair:

V2 event time is one of:

- `EXACT`;
- `BOUNDED`;
- `APPROXIMATE`;
- `UNKNOWN`.

Unknown is a valid evidence state.

## F3 — Migrating V1 must not reinterpret the old timestamps

Severity: HIGH.

The repair could have silently said:

> those rounded V1 values were approximate event times.

That would still be an unsupported reinterpretation.

Repair:

The initial V2 migration preserves:
- incident description;
- error characterization;
- causal status;
- target references;
- evidence bindings;
- anti-promotion semantics.

It does **not** preserve the V1 timestamp as event time.

All three initial `event_time` values are `UNKNOWN`.

The exact Git commit time is recorded separately as repository record time.

## F4 — Validator needed cross-field temporal checks

Severity: MEDIUM.

V2 validator now checks:
- offset-aware record timestamps;
- EXACT / BOUNDED / APPROXIMATE / UNKNOWN event-time shapes;
- earliest <= latest for bounded/approximate bounds;
- explicit chronology semantics;
- anti-promotion semantics.

Negative self-tests reject:
- timezone-free record time;
- reversed event bounds;
- observation auto-promotion.

## Remaining weaknesses

V2 still does not establish:
- the true event time of the initial incidents;
- that repository commit time equals the first moment the record text was authored;
- causal diagnosis;
- completeness of the observation ledger;
- behavioral improvement;
- training value.

Those remain separate claims.

## Claim ceiling

V2 makes behavior observations temporally honest enough to distinguish exact repository record time from unknown/approximate event time.

It does not reconstruct event chronology that the evidence does not support.
