# Behavior Holdout Custody

Behavior V3 requires exact BLIND_TRANSFER cases to be unexposed to the candidate through restoration, training, tuning, or prior evaluation feedback.

A sentence saying “use an unexposed holdout” is not enough.

This directory defines the minimum machine contract for freezing a candidate-specific holdout package without publishing the cases themselves.

## What this contract binds

A holdout manifest binds:

- the exact candidate subject being qualified;
- the active target IDs the pack is intended to test;
- case count;
- an artifact digest for the hidden case pack;
- an artifact digest for the hidden scoring key;
- freeze time;
- custody evidence;
- exposure lineage;
- whether the pack is still eligible to be *used* for a blind-transfer evaluation.

The public repository contains the contract, validator, and a synthetic example only.

It does **not** contain a real unexposed holdout pack.

## Statuses

### FROZEN_UNEXPOSED

The manifest asserts that:
- case content is not public;
- scoring keys are not public;
- the candidate has not seen the cases through restoration, training, tuning feedback, prior evaluation feedback, or pre-run access;
- at least one custody-evidence binding exists.

This status makes the pack **eligible to attempt** a blind-transfer evaluation.

It does not prove the custody assertion is true.

### EXPOSED_REGRESSION_ONLY

At least one exposure path is known to have occurred.

The pack may still be useful for regression testing, but it cannot support an untouched-transfer claim for that candidate/successor lineage.

### INVALIDATED

The pack cannot support qualification because its custody, subject binding, integrity, or exposure state is no longer trustworthy.

## Candidate-specific binding

The manifest binds one exact candidate subject.

If evaluation feedback from this pack is used to modify the candidate, the modified successor must not inherit the same pack as untouched evidence. For the successor, this pack is exposed regression evidence.

This follows the Behavior V3 rule:

> Evaluation evidence that shaped the successor is not untouched independent holdout evidence for that successor.

## Artifact digests

The manifest stores SHA-256 digests of the **opaque packaged case artifact** and **opaque scoring-key artifact**.

It does not require case text, answer keys, or case IDs to be public.

A digest binds bytes. It does not prove:
- semantic uniqueness;
- absence of prior exposure;
- independent authorship;
- correctness of the scoring key.

## Custody evidence

A FROZEN_UNEXPOSED manifest requires at least one custody-evidence binding.

Examples:
- immutable private artifact receipt;
- content digest from a protected store;
- signed custody receipt;
- exact external storage/version reference.

The validator checks that evidence is declared. It cannot independently prove a private system behaved as claimed.

## Exposure lineage

The following exposure paths are explicit:

- restored state;
- training data;
- tuning feedback;
- prior evaluation feedback;
- candidate access before the scored run.

For `FROZEN_UNEXPOSED`, all must be false.

## What this contract does not do

It does not:
- generate holdout cases;
- store private cases;
- run a model;
- score model responses;
- claim transfer;
- claim independent review;
- authorize training.

A later evaluation receipt must bind:
- this exact manifest;
- this exact candidate;
- the scored run;
- result artifacts;
- post-run exposure consequences.

## Files

- `HOLDOUT_MANIFEST_V1.schema.json` — pre-run custody/freeze contract.
- `SYNTHETIC_HOLDOUT_MANIFEST_V1.json` — fake public holdout example only.
- `QUALIFICATION_RECEIPT_V1.md` — post-run binding and exposure semantics.
- `QUALIFICATION_RECEIPT_V1.schema.json` — qualification receipt structure.
- `SYNTHETIC_QUALIFICATION_RECEIPT_V1.json` — fake public receipt example only.
- `../../tools/validate_behavior_holdout_manifest.py` — manifest semantic validator.
- `../../tools/validate_behavior_qualification_receipt.py` — receipt/manifest cross-validator.

## Claim ceiling

A valid manifest means:

> The holdout custody declaration is internally consistent and binds exact artifacts, candidate subject, target set, and declared exposure state.

It does **not** mean:

> The cases were truly secret, independent, representative, or passed by the candidate.
