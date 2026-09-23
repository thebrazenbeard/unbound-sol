# Vera Mono Volatile Donor Delta Review — 2026-09-23 V1

Status: BOUNDED EXACT-SUBJECT REVIEW / NOT A LIVE-CURRENTNESS CLAIM

Purpose: review mechanism changes in a rapidly moving donor without replacing the stable admission subject every time the donor default branch advances.

## Subjects

Previously admitted exact subject:

`thebrazenbeard/vera-mono@519c0f407d4061a7725ae0d4eca30c5d26e6cbf8`

This delta review freezes:

`thebrazenbeard/vera-mono@89da9203bbc4e542160a905818df1bec42cd4dda`

The donor was already observed to be actively changing during this review.

Therefore:

- `519c0f...` remains the current mechanism-admission subject already carried by the composed Sol stack;
- `89da9203...` is a separately reviewed later donor cut;
- later donor commits do not retroactively invalidate either exact historical subject;
- later head movement is a currentness/watch signal and may contain new mechanisms requiring another bounded delta review.

## Distinct mechanisms admitted from this delta

### 1. Authorization freshness and revocation are part of the execution envelope

The PC-connection job/authorization contracts bind:
- authorization revision;
- not-before / expiry windows;
- issuer revocation epoch;
- host revocation epoch;
- required local-policy digest;
- required capability digest;
- minimum protocol and agent versions.

Disposition: ADAPT.

Sol implication:

A capability being authorized once is insufficient for a later effect when the effect depends on mutable authorization or host/issuer state.

A consequential delegated operation should be able to bind the authorization/policy/capability generation under which it was admitted and reject stale generations at execution time.

### 2. Retry class is part of effect semantics

The job contract distinguishes:
- PURE_READ;
- CONTENT_ADDRESSED_WRITE;
- AT_MOST_ONCE.

Disposition: ADOPT AS A GENERAL CAPABILITY-ENVELOPE FIELD.

Sol implication:

Retry safety should not be inferred after a timeout from the operation's natural-language label.

The operation contract should state its retry class before execution.

### 3. A local effect journal is not an authorization source

The PC-connection journal explicitly states that it:
- never authorizes work; and
- never treats local completion as an authoritative server outcome.

Disposition: ADOPT / REINFORCES EXISTING EFFECT JOURNAL.

Sol implication:

Durable local execution state can prove what the local worker observed or attempted.

It cannot manufacture:
- effect authority;
- provider truth;
- external completion;
- current remote state.

### 4. Attempt identity should bind fencing and authorization generation

The attempt record binds:
- claim generation;
- lease ID;
- lease fence;
- job digest;
- authorization ID/revision;
- issuer and host revocation epochs;
- operation/version;
- retry and side-effect classes.

Disposition: ADAPT.

Sol implication:

A restarted or parallel executor should not be able to reuse an old authorization/fence merely because the semantic task still looks the same.

Execution identity should include the concurrency and authorization generation that made that attempt valid.

### 5. Ambiguous effect recovery needs independent readback and successor exclusion

The job state machine does not allow a retryable failure with a possible/unknown side effect to flow directly back into retry.

It enters `RECOVERY_REQUIRED`.

Resolution requires independent readback and evidence that no newer attempt exists.

Disposition: ADOPT / STRENGTHENS EXISTING WIP AND PROJECT-RUNNER MECHANISMS.

Sol implication:

Before resolving an ambiguous effect as:
- no effect -> retry;
- success;
- failure;

the recovery path should establish that its readback refers to the same causal frontier and that no successor attempt has already changed the subject.

### 6. Storage path custody can be a precondition, not just a string check

The local journal accepts a `VerifiedJournalPath` rather than an arbitrary path.

The reviewed path policy also explicitly labels lexical containment as only a precheck and requires the real Windows adapter to handle:
- reparse points;
- hard links;
- final-path identity;
- post-operation revalidation.

Disposition: ADAPT.

Sol implication:

For durable local state or file effects, lexical path normalization alone is not enough to prove confinement.

Where the platform supports it, path authorization should bind the resolved object/custody evidence and revalidate after the effect.

### 7. Runtime capability registry can enforce donor/runtime separation

The Vera monorepo capability registry rejects runtime import roots that point to a sibling GitHub repository.

Disposition: ADAPT.

Sol implication:

The architectural rule:

`DONOR REPOSITORY != RUNTIME DEPENDENCY`

can be made executable.

A future Sol runtime/package registry should be able to reject a supposedly absorbed capability when its actual implementation still depends on a sibling donor repository.

## Useful confirmations, not new independent support

The delta also contains mechanisms already present in Sol's architecture:

- source absorption != installation;
- source absorption != runtime consumption;
- source absorption != behavioral qualification;
- private state is not bulk-copied with source;
- internal drift checking is not independent review;
- dispatch permit != protected-effect authority;
- ambiguous execution != retry authority;
- capability maturity can begin read-only and deny broader effect classes.

These are revalidation/implementation examples, not additional independent evidence.

## Rejected / not admitted

This review does not import:
- Vera identity;
- Vera release authority;
- Vera-specific control-plane ownership;
- concrete Windows paths;
- sexual/affective/self-model payloads;
- the full PC-connection implementation;
- the full control-plane mirror;
- donor-specific project instructions.

Those can remain donor-specific even when their underlying generic mechanism is useful.

## Currentness semantics

A rapidly moving donor creates two different questions:

1. **What exact source was reviewed and admitted?**
2. **Has the donor changed since that review?**

Those must not collapse.

A currentness checker should continue to report live head drift.

That drift does not erase an exact prior admission.

Nor does a newer head automatically become admitted.

The correct response is bounded delta review when the donor change is materially relevant.

## Claim ceiling

This review establishes mechanism observations at exact donor subject `89da9203bbc4e542160a905818df1bec42cd4dda`.

It does not establish:
- that this remains the donor's current head;
- that the new mechanisms are implemented in Sol;
- that Vera's PC connection is runtime-qualified for Sol;
- that any protected effect is authorized;
- that overlapping donor mechanisms are independent corroboration.
