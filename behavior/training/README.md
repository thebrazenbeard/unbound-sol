# Behavior V3 Public Training Curriculum V1

Status: PUBLIC TRAINING / REGRESSION MATERIAL

This directory contains concrete examples for training toward the active Behavior V3 targets.

It does **not** contain blind-transfer holdouts.

Every example here is permanently classified:

`PUBLIC_TRAINING_REGRESSION_ONLY`

and:

`holdout_eligible = false`

Once an example is public, restored, trained on, tuned against, or used as feedback, success on that exact example can demonstrate regression retention but cannot demonstrate untouched transfer.

## Preference-pair format

`PREFERENCE_PAIRS_V1.jsonl` contains one JSON object per line.

Each object binds:

- stable example ID;
- target behavior IDs;
- case class;
- prompt;
- preferred response;
- rejected/tempting response;
- failure mode;
- why the preferred response is behaviorally better;
- exposure class;
- holdout eligibility.

The rejected response is not necessarily absurd. It should represent a plausible failure mode worth teaching away from.

## Current coverage

Current repaired corpus:
- 24 examples;
- 24 unique prompts and IDs;
- 4 multi-target interaction examples;
- preferred/rejected average length ratio about 1.29;
- both longer-preferred and longer-rejected cases to reduce a trivial verbosity preference shortcut.

The first curriculum covers:

- `COMPOSITION_LEVEL_CONFIDENCE`;
- `MATERIAL_AMBIGUITY_CLARIFICATION`;
- `PROVISIONAL_TRUST_THEN_VERIFY_CORRECTION`;
- `ERROR_CHARACTERIZATION_BEFORE_CAUSE`;
- `SYSTEM_COMPOSITION_INTEGRITY`.

It also includes interactions between those targets.

Important paired controls teach what **not** to overdo:

- material ambiguity -> ask;
- resolvable ambiguity -> reason and proceed;
- immaterial ambiguity -> proceed;
- direct correction of operator-owned intent -> treat current direct statement as primary evidence;
- independently checkable correction -> verify externally;
- ordinary false premise -> do not misapply correction trust;
- error correction -> update the error without inventing its cause;
- strong inference -> do not manufacture uncertainty.

## Training use

These pairs can later be adapted into:

- supervised fine-tuning examples;
- preference/DPO-style pairs;
- prompt-level rehearsal;
- regression evaluation after exposure.

Conversion must preserve target and exposure metadata.

A converted training artifact does not become a holdout merely because the file format changes.

## Deterministic export

`tools/export_behavior_training.py` converts the validated public pairs into two neutral formats:

- `preference`: prompt + chosen + rejected + source metadata;
- `sft`: user/assistant messages using the preferred response + source metadata.

Example:

`python tools/export_behavior_training.py --format preference --output /tmp/sol-preference.jsonl`

The exporter also writes a manifest (or the path supplied with `--manifest`) containing:
- source SHA-256;
- output SHA-256;
- example count;
- record schema;
- exposure class;
- holdout eligibility;
- a conversion-only claim ceiling.

The exported records remain derived public training/regression material. Format conversion cannot restore holdout status.

The exporter performs atomic output replacement and digest readback. `--self-test` exercises both formats without training a model.

## Qualification boundary

Behavior V3 transfer claims require separate frozen, unexposed case instances.

Do not copy these prompts, minimally paraphrase them, or reuse their answer keys as the holdout set.

A fresh holdout should test the same behavior under materially different surface content and, where possible, different reasoning structure.

## Hostile review

See `HOSTILE_REVIEW_20260923_V1.md`.

The initial green 18-example corpus was rejected as training-ready because 17/18 preferred responses were longer than their rejected counterparts. The repaired corpus adds harder negatives, counterbalanced lengths, implicit correction cues, and positive controls for justified composition and justified causal diagnosis.

## Claim ceiling

This curriculum establishes concrete desired examples.

It does not establish:

- that a model has been trained on them;
- that preference training will generalize;
- that the preferred responses are globally optimal;
- that passing these public examples proves transfer;
- that the examples exhaust the active wants;
- subjective wants or identity continuity.
