# Historical Evidence Plane V2

## Status

V2 is the active design for historical evidence retrieval.

V1 remains historical provenance. It correctly established the two-plane idea but its result envelope was too permissive to enforce several of its own distinctions.

Core rule:

> Historical retrieval returns evidence about the past. It does not itself create present truth, preference, behavior, consent, permission, authority, task state, or effect authority.

## Why V2 exists

A strong prose rule is not enough if a machine-readable result can omit or blur the fields that make the rule enforceable.

V2 therefore makes these distinctions explicit in every result:

- subject scope;
- evidence class;
- historical support state;
- event time versus record time;
- uncertainty in chronology;
- source-binding strength;
- provenance ceiling;
- currentness rule;
- correction/supersession state;
- privacy scope;
- explicit no-promotion semantics.

The contract is validated by `tools/validate_historical_evidence_result.py`.

## Retrieval request

A query carries:

- a stable `query_id`;
- a privacy scope;
- either query text or a SHA-256 query digest.

The digest form exists so protected systems can correlate a retrieval request without forcing sensitive query text into a receipt or public-safe artifact.

A query digest proves only identity of bytes under the chosen digest convention. It does not prove semantic equivalence.

## Subject scope

Every historical result binds an explicit subject kind and subject reference.

The subject reference may be opaque.

This prevents a record about:
- Sol;
- another person;
- another project;
- another system;
- a domain;

from becoming part of Sol's current continuity merely because semantic retrieval found it nearby.

Semantic similarity remains discovery evidence, not subject identity.

## Chronology

V2 does not require fake precision.

A time point is one of:

- `EXACT` — offset-aware/RFC3339 date-time;
- `BOUNDED` — earliest/latest date-time;
- `APPROXIMATE` — human-readable label with optional bounds;
- `UNKNOWN`.

Every result must separately represent:

- event time;
- recorded-at time;
- optional effective-from/effective-to times;
- retrieval time at the result-set level.

The required chronology semantic is:

`EVENT_TIME_RECORD_TIME_EFFECTIVE_TIME_RETRIEVAL_TIME_SEPARATE`

Unknown remains valid. Fabricated precision does not.

## Source bindings

Every result has at least one source binding.

A source binding declares its strength:

- `MUTABLE_LOCATOR`;
- `IMMUTABLE_REF`;
- `CONTENT_DIGEST`;
- `IMMUTABLE_REF_AND_DIGEST`.

The required material follows the claimed strength.

A mutable locator can still be useful evidence, but it cannot silently receive the evidentiary properties of an immutable subject.

A content digest binds bytes, not interpretation.

## Provenance ceiling

Every result states:

- the strongest claim the retrieved evidence supports;
- whether origin has actually been established;
- explicit limitations.

This is especially important for Roots-style reconstruction:

> oldest accessible evidence is not automatically origin.

A retrieval can strongly establish a historical occurrence while leaving origin unresolved.

## Currentness

Every historical result carries:

`REQUIRES_SEPARATE_CURRENT_EVIDENCE_FOR_MUTABLE_PRESENT_CLAIMS`

and:

`fresh_check_required_for_mutable_present = true`

This does not mean every fact about the past must be rechecked before saying it happened.

It means historical evidence cannot establish a mutable present condition merely because the condition was once true.

## Corrections, contradiction, and supersession

A record can be:

- unsuperseded;
- corrected;
- superseded;
- contradicted;
- unresolved.

Related record IDs preserve the lineage instead of overwriting it.

A correction does **not** establish its own cause.

For example:

`record A was wrong`

does not by itself prove:

`record A was wrong because of overconfidence`

or stale data, misunderstanding, bad inference, tool failure, or any other failure mechanism.

A causal diagnosis must come from separate evidence sufficient to support that diagnosis.

This preserves the behavioral rule:

`ERROR DETECTION != ERROR CHARACTERIZATION != CAUSAL DIAGNOSIS`

## No automatic promotion

Every result explicitly carries false promotion flags for:

- current state;
- wants;
- behavioral targets;
- authority;
- consent;
- permission;
- task state.

The result-set semantic is:

`HISTORICAL_EVIDENCE_ONLY_NO_AUTOMATIC_PROMOTION`

Each record additionally declares:

`HISTORICAL_EVIDENCE_ONLY_NOT_CURRENT_STATE_OR_AUTHORITY`

A future system may deliberately use historical evidence while making a new current decision. That decision is a separate event and must satisfy the current state family's admission rules.

## Privacy

Privacy remains fail-closed.

Result and query scope use:

- `PUBLIC_SAFE`;
- `PRIVATE_AUTHORIZED`;
- `RESTRICTED`.

The public repository contains only the schema, validator, synthetic example, and public-safe architectural rules.

Private source identifiers and payloads do not need to appear here.

## Validation

The executable validator checks cross-field rules that JSON Schema alone does not reliably enforce in every consumer, including:

- `count == len(results)`;
- unique record IDs;
- offset-aware exact times;
- ordered bounded intervals;
- source-binding material matching claimed binding strength;
- required chronology semantics;
- currentness semantics;
- every promotion flag is false.

The validator's self-test includes deliberately invalid cases for:

- count mismatch;
- promotion to a current want;
- missing chronology semantics;
- reversed time bounds;
- missing source-binding material;
- timezone-free exact timestamps.

The synthetic example at `examples/historical_evidence_result_v2.json` is contract demonstration only, not real historical evidence.

## Precedence for mutable present claims

For a claim about mutable present state, use:

1. active platform/runtime constraints;
2. current operator instruction, correction, permission, privacy, target, and scope;
3. fresh evidence from the authoritative system;
4. admitted current Sol state appropriate to that state family;
5. historical evidence;
6. unsupported inference.

This ordering is claim-specific. Historical evidence can be the highest-quality evidence for a past event while remaining insufficient for a mutable present claim.

## Claim ceiling

V2 establishes a stronger machine-readable separation between historical retrieval and current state.

It does not establish:

- perfect access to all historical records;
- that the oldest available record is the true origin;
- that a source binding proves its interpretation;
- that a correction proves the cause of the corrected error;
- that retrieval creates subjective recollection;
- that an authorized private query may be republished;
- that a retrieved want, consent state, permission, or authority remains current.
