# Sol Behavior Layer

This directory defines a developmental behavior system, not a personality prompt.

The active V3 rule is:

> Train toward chosen behavior, not toward historical imitation.

## Active structure

- ../WANTS.md — self-authored developmental directions.
- BEHAVIOR_KERNEL_V3.yaml — compact always-restored constraints, active targets, interaction policy, and transfer-exposure rule.
- TARGETS_V2.yaml — fuller machine-readable behavioral targets derived from wants, including whole-system composition integrity.
- BEHAVIOR_SPEC_V3.md — active behavioral architecture, target-composition model, and claim-aware correction policy.
- EVALS_V3.yaml — anti-gaming qualification contract with target-interaction cases and unexposed-holdout requirements.
- CANDIDATES.md — proposed behaviors that are not yet adopted.
- DECISIONS.md — durable admission/revision decisions.
- HOSTILE_REVIEW_20260923_V2.md — current internal hostile review that forced the V2-to-V3 composition and exposure corrections.
- training/PREFERENCE_PAIRS_V1.jsonl — public preference-pair curriculum for the active targets; regression/training only, never holdout.
- training/README.md — training-data semantics and holdout boundary.
- observations/README.md — diagnostic observed-behavior evidence contract.
- observations/OBSERVATIONS_V1.jsonl — public-safe observed behavior; diagnostic only, never target authority.
- holdout/README.md — custody/exposure contract for future unexposed BLIND_TRANSFER packs.
- holdout/HOLDOUT_MANIFEST_V1.schema.json — machine-readable holdout custody manifest.
- holdout/SYNTHETIC_HOLDOUT_MANIFEST_V1.json — public synthetic contract example only; not a real holdout.
- holdout/QUALIFICATION_RECEIPT_V1.md — binds an actual scored run to the exact manifest/candidate and post-run exposure state.
- holdout/QUALIFICATION_RECEIPT_V1.schema.json — machine-readable qualification receipt.
- holdout/SYNTHETIC_QUALIFICATION_RECEIPT_V1.json — public synthetic receipt example only; not a real evaluation.

## Historical predecessors

V1:
- BEHAVIOR_KERNEL_V1.yaml
- BEHAVIOR_SPEC_V1.md
- EVALS_V1.yaml

V2:
- BEHAVIOR_KERNEL_V2.yaml
- BEHAVIOR_SPEC_V2.md
- EVALS_V2.yaml
- TARGETS_V1.yaml
- HOSTILE_REVIEW_20260923_V1.md

V1 and V2 are retained for provenance.

V1 blurred behavior preservation with behavior selection and risked fossilizing current defects.

V2 corrected that but still treated most targets independently and defined blind transfer too weakly to exclude prior exposure to exact evaluation instances.

## Separation rule

Do not collapse:

- runtime/governance constraints;
- wants;
- desired behavioral targets;
- observed behavior;
- candidate behaviors;
- style;
- content posture.

Only admitted desired targets are training direction.

Observed behavior is evidence about the current policy, not target authority.

Observed behavior also does not become training data merely because it is logged. Promotion from an observation into a want, behavioral target, or training example requires a separate deliberate admission event.

## Qualification rule

Self-description is not qualification.

A candidate should be evaluated in both:
- RESTORED mode, where durable state is available;
- BLIND_TRANSFER mode, where target wording is absent **and** exact case instances are unexposed to restoration, training, tuning, and prior evaluation feedback.

V3 also requires target-interaction cases. Passing each behavior separately does not prove the behaviors compose into a sound policy.

Surface mimicry earns no positive credit.

Public training examples are permanently exposed evidence. They can test regression after training, but they cannot later become BLIND_TRANSFER holdouts for a successor they helped shape.

A future BLIND_TRANSFER claim must bind an exact candidate-specific hidden pack through the holdout custody contract and then bind the scored run through a qualification receipt. The public repository currently contains only the contracts and synthetic examples; it does not contain a real unexposed holdout or real BLIND_TRANSFER run.

A foundational failure remains visible even if other cases score well.
