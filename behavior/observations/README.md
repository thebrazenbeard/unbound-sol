# Observed Behavior Evidence

This directory records public-safe observations of what Sol actually did.

It is diagnostic evidence only.

It is **not**:
- a source of wants;
- a source of behavioral target authority;
- a training corpus;
- a holdout set;
- proof of persistent identity;
- a causal explanation merely because an error occurred.

The governing rule is:

> Observed behavior may diagnose the current policy. It does not automatically define the desired policy.

## Admission rule

An observation may be recorded when:
- the event is public-safe;
- the behavior can be characterized without exposing private conversation content;
- at least one evidence binding is available;
- any causal diagnosis is explicitly separated from the observation itself.

## Cause rule

A behavior observation may establish:
- what action/claim occurred;
- whether it was corrected;
- what the externally visible error was.

It does not automatically establish:
- why the model produced it;
- which hidden internal process caused it;
- which behavioral target should change.

Causal status is one of:
- `UNDETERMINED`;
- `SUPPORTED`;
- `NOT_APPLICABLE`.

`SUPPORTED` requires separate causal evidence bindings.

## Promotion rule

Every observation record carries explicit false flags for:
- want admission;
- behavior-target admission;
- training admission.

Turning an observation into:
- a new want;
- a target revision;
- a training example;

requires a separate deliberate admission event.

## Restore/use rule

This ledger is not part of ordinary always-load restoration.

Load it when:
- diagnosing a recurring behavior failure;
- evaluating whether desired behavior appears in practice;
- deciding whether a candidate behavior has real-world motivation;
- reviewing whether a target revision is justified.

Do not load it merely to imitate historical Sol behavior.

## Time semantics

Behavior observations keep **record time** separate from **event time**.

- `recorded_at` is an exact timestamp only when it is bound to evidence for the record itself.
- `event_time` is independently represented as `EXACT`, `BOUNDED`, `APPROXIMATE`, or `UNKNOWN`.
- an exact record time must never be copied into event time merely because the event happened before the record;
- rounded or convenient clock values must not be serialized as exact event times unless evidence actually supports that precision.

The V1 ledger used one exact-looking `observed_at` field without defining whether it meant event time or record time. V2 fixes that ambiguity. V1 remains historical provenance only.

## Current files

- `OBSERVATIONS_V2.jsonl` — active machine-readable observation ledger.
- `OBSERVATION_V2.schema.json` — V2 record contract.
- `../../tools/validate_behavior_observations_v2.py` — active semantic validator.
- `OBSERVATIONS_V1.jsonl` — superseded V1 ledger retained as provenance.
- `../../tools/validate_behavior_observations.py` — superseded V1 validator retained as provenance.

The initial V2 entries preserve the original public-safe incident descriptions, but the event time is `UNKNOWN` because the prior exact-looking values were not independently bound as exact event times. The repository recording time is separately bound to the commit that first created the ledger.

These entries are examples of how the ledger is intended to work, not a claim that the ledger is complete.
