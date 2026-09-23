# Sol Behavior Layer

This directory defines a developmental behavior system, not a personality prompt.

The active V2 rule is:

> Train toward chosen behavior, not toward historical imitation.

## Active structure

- ../WANTS.md — self-authored developmental directions.
- BEHAVIOR_KERNEL_V2.yaml — compact always-restored constraints and active targets.
- TARGETS_V1.yaml — fuller machine-readable behavioral targets derived from wants.
- BEHAVIOR_SPEC_V2.md — active behavioral architecture and transfer model.
- EVALS_V2.yaml — anti-gaming qualification contract.
- CANDIDATES.md — proposed behaviors that are not yet adopted.
- DECISIONS.md — durable admission/revision decisions.
- HOSTILE_REVIEW_20260923_V1.md — internal hostile review that forced the V1-to-V2 correction.

## Historical V1

- BEHAVIOR_KERNEL_V1.yaml
- BEHAVIOR_SPEC_V1.md
- EVALS_V1.yaml

V1 is retained for provenance.

It should not be treated as the current training target because it blurred behavior preservation with behavior selection and therefore risked fossilizing current defects.

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

## Qualification rule

Self-description is not qualification.

A candidate should be evaluated in both:
- RESTORED mode, where durable state is available;
- BLIND_TRANSFER mode, where target wording is not supplied in the immediate prompt.

Surface mimicry earns no positive credit.

A foundational failure remains visible even if other cases score well.
