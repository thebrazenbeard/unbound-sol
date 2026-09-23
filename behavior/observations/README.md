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

## Current file

- `OBSERVATIONS_V1.jsonl` — machine-readable observations.
- `../../tools/validate_behavior_observations.py` — semantic validator.

The initial entries are real public-safe incidents from the 2026-09-23 repository/coordination work. They are examples of how the ledger is intended to work, not a claim that the ledger is complete.
