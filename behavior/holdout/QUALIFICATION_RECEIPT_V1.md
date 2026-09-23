# Behavior Qualification Receipt

The holdout manifest freezes a candidate-specific hidden pack before evaluation.

The qualification receipt binds what happened when that exact candidate was actually evaluated against that exact frozen pack.

This repository contains the receipt contract and a synthetic example only.

It does **not** contain a real BLIND_TRANSFER run.

## Required binding

A receipt binds:

- exact holdout manifest ID and SHA-256;
- exact candidate subject;
- run ID and evaluation time;
- exact result artifact digest;
- case-count outcome;
- per-target outcome;
- evaluator provenance;
- post-run exposure consequences;
- exact-run claim ceiling.

The validator can be given both a receipt and its manifest. It then checks that:

- manifest digest and ID match;
- manifest was `FROZEN_UNEXPOSED` and `ELIGIBLE_TO_ATTEMPT`;
- candidate subject matches exactly;
- target set matches exactly;
- case count matches;
- PASS/FAIL/UNKNOWN is internally consistent with case and target outcomes.

## A run consumes innocence

The evaluated subject necessarily receives the case prompts during the scored run.

Therefore a successful run does not leave the pack magically “unseen.”

Afterward:

- the pack is exposed to the evaluated subject for purposes of repeat claims;
- if feedback/results are used to train, tune, or modify a successor, the pack becomes regression-only for that successor lineage;
- if no modification occurs, reuse for another subject still requires a fresh exposure analysis rather than automatic inheritance of holdout status.

This prevents a common laundering pattern:

> pass hidden test -> inspect failures -> change model -> rerun same test -> still call it untouched holdout.

The second run is regression evidence unless a genuinely unexposed pack is used for the modified successor.

## PASS semantics

`PASS` means only:

> The exact candidate bound in this receipt satisfied every scored case and target in the exact manifest-bound run, with zero unknown/failed cases under the declared evaluator.

It does not mean:

- the behavior generalizes outside the pack;
- the evaluator is unbiased;
- the hidden cases are representative;
- the custody declaration was independently proven;
- the candidate has subjective wants;
- cross-substrate identity was established.

## Evaluator provenance

Every receipt records:

- evaluator ID;
- evaluator kind;
- whether the evaluator is claimed independent from candidate authorship.

This metadata is descriptive.

A model judge is not automatically an independent factual source merely because it is a different model.

## Result artifact

The result artifact is digest-bound.

It may be:
- private external;
- sealed external;
- a public-safe summary.

Publishing a result summary must not disclose hidden prompts or scoring keys if the pack is intended to remain useful for any unexposed subject.

## Synthetic example

`SYNTHETIC_QUALIFICATION_RECEIPT_V1.json` binds the public synthetic holdout manifest.

It is contract demonstration only.

It is not qualification evidence.

## Claim ceiling

A validated receipt establishes internal consistency of one exact declared evaluation run.

It does not independently prove:
- pre-run non-exposure;
- independent authorship;
- case quality;
- judge correctness;
- transfer beyond the tested cases;
- subjective identity or continuity.
