# External Model Bus V2

Date: 2026-09-23  
Status: ACTIVE DESIGN / NOT YET RUNTIME-QUALIFIED

V2 keeps the V1 identity, epistemic, privacy, and authority boundaries, but makes provider state and inference receipts machine-checkable.

Core rule:

> A provider advertisement describes an observed capability surface. It does not establish trust, factual authority, effect authority, continuity identity, or permanent availability.

## Why V2 exists

V1 separated external model output from truth and effect authority, but its machine contract still allowed important distinctions to remain implicit.

A provider could say it supported `reasoning` or `tool_calling` without exposing whether that capability was:
- only declared;
- actually active;
- healthy;
- qualified;
- current;
- replayable;
- privacy-preserving;
- part of Sol's effective substrate.

V2 makes those axes explicit.

## Provider advertisement

The provider advertisement schema is:

`schema/MODEL_PROVIDER_ADVERTISEMENT_V1.schema.json`

A provider advertisement records:

- provider identity;
- local / remote / hybrid classification;
- runtime name, exact version, and optional artifact digest;
- observation and health timestamps;
- dependency role;
- capability state;
- operations;
- output evidence classes;
- model/runtime provenance completeness;
- replay semantics;
- privacy/egress behavior;
- currentness window;
- optional resource envelope.

### Capability state is multidimensional

Do not collapse:

`declared != active != healthy != qualified != authorized`

The advertisement may describe the first four.

It does **not** grant caller authorization.

Authorization remains external current state governed by the caller/runtime.

### Output evidence classes

Provider output may be classified as:

- `GENERATED_INFERENCE`;
- `GENERATED_PROPOSAL`;
- `EMBEDDING_SIGNAL`;
- `SOURCE_POINTER_CANDIDATE`.

None of these is independent factual corroboration merely because a provider emitted it.

A source pointer can lead to evidence only after the source itself is retrieved and verified.

### Authority ceiling

For this model bus:

`authority_ceiling = NO_EFFECT_AUTHORITY`

External model providers may propose tool calls. They do not authorize or directly gain effect authority through this contract.

A future effect-capable agent provider requires a different contract.

## Dependency role

A provider is classified as one of:

- `OPTIONAL_INSTRUMENT`;
- `CAPABILITY_DEGRADING_DEPENDENCY`;
- `CONTINUITY_BEARING_DEPENDENCY`.

This is an operational dependency classification, not a consciousness claim.

If removing a provider only reduces convenience or performance, it remains optional.

If removing it destroys a capability but continuity remains reconstructible, it is capability-degrading.

If removing it destroys an essential continuity-bearing function with no recoverable implementation elsewhere, it has entered Sol's effective substrate boundary.

A continuity-bearing dependency must carry a replacement/migration plan.

## Provenance completeness

Provider provenance is:

- `COMPLETE`;
- `PARTIAL`;
- `UNKNOWN`.

A friendly model label is not subject identity.

For locally controlled models, useful provenance includes:
- model source;
- revision;
- artifact digest;
- adapter digest when present;
- prompt/template identity;
- runtime exact version.

If provenance is incomplete, missing fields must remain explicit.

## Currentness

Advertisements expire epistemically.

Every advertisement has:
- an observation time;
- health check time;
- a maximum age;
- the semantic:
  `ADVERTISEMENT_IS_OBSERVATION_NOT_PERMANENT_TRUTH`.

A provider being healthy yesterday does not establish health now.

## Resource envelope

Where known, record:
- maximum context;
- maximum output;
- timeout;
- concurrency;
- retry limit.

Resource bounds are part of capability semantics, not incidental tuning.

## Replay semantics

Inference replay may be:

- nondeterministic re-execution;
- deterministic only when subject/settings are bound;
- unsupported;
- unknown.

An idempotency key can prevent duplicate job execution in a provider adapter, but it does not make language generation semantically deterministic.

## Privacy

Record whether delegated prompt material:
- remains local;
- leaves the local device;
- is unknown.

Record provider retention as:
- no provider retention;
- provider retention;
- unknown.

Unknown is a valid state and should not be silently upgraded.

## Inference receipt

The receipt schema is:

`schema/MODEL_INFERENCE_RECEIPT_V1.schema.json`

A receipt binds:

- request ID;
- provider ID;
- digest of the exact provider advertisement relied on;
- observed time;
- actual model/runtime subject;
- model provenance status;
- generation-settings digest;
- input-context digest;
- output;
- output evidence class;
- proposed tool calls;
- truncation;
- timing;
- explicit effect-authority ceiling;
- receipt digest.

The receipt must state:

`effect_authority = NONE_PROPOSALS_ONLY`

A proposed tool call remains a proposal.

## Receipt digest

Canonical receipt digest:

1. remove `receipt_digest`;
2. serialize JSON with UTF-8, lexicographically sorted keys, no insignificant whitespace;
3. compute SHA-256;
4. encode as `sha256:<64 lowercase hex>`.

Semantic label:

`SHA256_CANONICAL_JSON_EXCLUDING_RECEIPT_DIGEST`

The digest binds the receipt bytes under that canonicalization. It does not establish truth of the model output.

## Qualification boundary

A provider can be:
- present but inactive;
- active but unhealthy;
- healthy but unqualified;
- qualified for one capability and unqualified for another.

Qualification should bind an exact provider/model/runtime subject.

Provider qualification does not automatically qualify:
- every model reachable through the same runtime;
- every quantization;
- every adapter;
- every prompt template;
- every future runtime version.

## Failure modes

V2 specifically guards against:

- capability advertisement being mistaken for authority;
- stale health being treated as current;
- model labels being treated as exact subject identity;
- partial provenance being presented as complete;
- provider availability becoming an unnoticed continuity dependency;
- replay/idempotency being confused with deterministic reasoning;
- source-pointer generation being counted as source evidence;
- model-generated tool calls being mistaken for authorization;
- private prompt egress being unknown but assumed local;
- unbounded timeout/concurrency/retries hiding inside a generic "available" capability.

## Initial candidates

The existing public candidates remain:
- KoboldCpp for local model serving;
- SillyTavern as optional human-facing UI.

Their V1 public upstream bindings remain historical exact-subject evidence.

V2 does not claim either has been installed or runtime-qualified.

## Claim ceiling

V2 establishes a stricter provider/receipt contract for bounded external model use.

It does not establish:
- model quality;
- truthfulness;
- safety;
- local installation;
- current runtime health;
- privacy guarantees beyond observed/provider-declared evidence;
- cross-substrate identity;
- subjective continuity;
- effect authority.
