# Internal Hostile Review — Historical Evidence Plane V1 to V2

Date: 2026-09-23  
Review type: INTERNAL HOSTILE REVIEW  
Independent review: NO

Reviewed subject:

- unbound-sol PR #7
- exact source head at branch point: `c512b01caddacf86081a0104308f4b72f754ad80`
- historical plane V1:
  - `docs/HISTORICAL_EVIDENCE_PLANE_V1.md`
  - `schema/HISTORICAL_EVIDENCE_RESULT_V1.schema.json`

## Verdict

The V1 prose had the right central distinction:

`HISTORICAL EVIDENCE != CURRENT STATE`

The V1 result schema was too permissive to carry that distinction reliably through machine interfaces.

V2 is warranted because the repair is not merely editorial: it changes the executable result contract and adds cross-field validation.

## F1 — Required provenance/currentness fields accepted arbitrary values

Severity: HIGH.

V1 required fields named `provenance_ceiling` and `currentness_rule`, but both schemas were unconstrained objects/values.

A producer could satisfy the envelope without supplying a meaningful ceiling or currentness rule.

Repair:

- provenance ceiling now requires a maximum claim, origin-established boolean, and limitations;
- currentness now requires separate current evidence for mutable present claims and an explicit fresh-check requirement.

## F2 — Chronology was named but not enforced

Severity: HIGH.

V1 allowed `event_time` to be anything, made `chronology_semantics` optional, and treated recorded/effective times as unconstrained strings.

That permits fabricated precision or accidental collapse of event time, record time, effective time, and retrieval time.

Repair:

- required chronology semantics;
- exact, bounded, approximate, and unknown time states;
- executable rejection of timezone-free exact time and reversed bounds.

## F3 — Source bindings were only strings

Severity: HIGH.

A mutable URL, exact Git commit, database key, and content hash could all look identical to the schema: a string.

That made provenance strength implicit.

Repair:

- typed source kind;
- explicit binding strength;
- required locator/ref/digest material appropriate to the claimed strength.

## F4 — Subject identity was not explicit

Severity: HIGH.

V1 had a historical state for `OTHER_IDENTITY_OR_DOMAIN_HISTORY`, but no required subject binding.

Semantic retrieval could therefore return a nearby record without a machine-level statement of whose or what history it is.

Repair:

- required subject kind and subject reference;
- subject reference may be opaque to preserve privacy.

## F5 — No explicit machine-level anti-promotion record

Severity: HIGH.

V1 prose forbade promotion, but individual result objects only carried a result-semantics string.

A downstream adapter could accidentally treat a retrieved preference, permission, consent state, or behavioral record as active state without violating a dedicated field.

Repair:

Every result explicitly says that retrieval promotes none of:

- current state;
- want;
- behavior target;
- authority;
- consent;
- permission;
- task.

## F6 — Correction/supersession semantics were untyped

Severity: HIGH.

V1 allowed arbitrary `supersession_state`.

This makes it easy to collapse:

`this record was corrected`

into:

`therefore we know why it was wrong`.

Repair:

- typed correction/supersession/contradiction states;
- related record IDs preserve lineage;
- architecture explicitly states that correction does not establish causal diagnosis.

## F7 — Raw query text was mandatory

Severity: MEDIUM.

A protected historical search may be authorized while the literal query is not suitable for a public receipt or broad log.

Repair:

- query ID + privacy scope required;
- query may carry literal text or a SHA-256 digest;
- digest is treated only as byte identity, not semantic identity.

## F8 — Count could disagree with actual results

Severity: MEDIUM.

JSON Schema cannot generally express `count == array length`.

Repair:

Executable validator enforces it.

## F9 — A schema file alone does not prove consumers enforce it

Severity: MEDIUM.

Even a stronger JSON Schema can be ignored or partially implemented.

Repair:

- dependency-free Python semantic validator;
- synthetic valid example;
- negative self-tests exercising the most dangerous cross-field failures;
- active continuity validation invokes that validator.

## Remaining weaknesses

V2 still does not solve:

- historical search quality or completeness;
- protected-store implementation;
- source authenticity beyond the binding supplied;
- semantic interpretation correctness;
- causal diagnosis;
- automatic provenance reconstruction;
- present-state admission policy for every state family.

Those should remain separate problems rather than being hidden inside a retrieval envelope.

## Claim ceiling

V2 makes historical retrieval harder to confuse with current state and harder to represent with fake precision.

It does not prove memory, identity continuity, source authenticity, or historical completeness.
