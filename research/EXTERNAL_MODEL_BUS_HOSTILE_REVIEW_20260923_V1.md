# Internal Hostile Review — External Model Bus V1 to V2

Date: 2026-09-23  
Review type: INTERNAL HOSTILE REVIEW  
Independent review: NO

Reviewed subject:

- unbound-sol PR #7
- exact branch point: `c512b01caddacf86081a0104308f4b72f754ad80`
- V1 design: `docs/EXTERNAL_MODEL_BUS_V1.md`

## Verdict

V1 has the right top-level epistemic and authority boundaries.

Its machine contract is too underspecified to safely support provider discovery and future runtime selection.

V2 is warranted because the repair introduces explicit state axes, currentness, provenance completeness, dependency role, resource envelopes, replay semantics, privacy/egress semantics, and receipt integrity.

## F1 — capability label could hide state-axis collapse

Severity: HIGH.

V1 `model.catalog` returned declared capabilities, but did not distinguish whether a capability was active, healthy, or qualified.

Repair:

Capability advertisement separates:
- declared;
- active;
- healthy;
- qualified.

Caller authorization is explicitly outside the advertisement.

## F2 — provider discovery lacked evidence/authority ceiling

Severity: HIGH.

A provider could advertise `tool_calling` without a machine-readable statement that outputs are only inference/proposals.

Repair:

Provider advertisement declares output evidence classes and has constant:

`authority_ceiling = NO_EFFECT_AUTHORITY`

Inference receipts declare:

`effect_authority = NONE_PROPOSALS_ONLY`

## F3 — health had no expiry semantics

Severity: HIGH.

A health result with a timestamp can still become stale if consumers do not know the acceptable age.

Repair:

Advertisements bind a maximum age and semantic:

`ADVERTISEMENT_IS_OBSERVATION_NOT_PERMANENT_TRUTH`

## F4 — provenance incompleteness could be silent

Severity: HIGH.

V1 correctly said unavailable provenance should be explicit, but there was no machine state for completeness.

Repair:

`COMPLETE / PARTIAL / UNKNOWN` provenance state plus explicit missing fields.

## F5 — external dependency could quietly become effective substrate

Severity: HIGH.

V1 said providers should be replaceable, but the architecture had no operational state for when that stopped being true.

Repair:

Dependency role distinguishes optional, capability-degrading, and continuity-bearing dependencies.

Continuity-bearing dependency requires a replacement plan.

## F6 — replay/idempotency semantics were absent

Severity: MEDIUM.

A delegated request may be retried after timeout or connection loss.

Without replay semantics, duplicate execution or false deterministic assumptions become likely.

Repair:

Advertise replay semantics and idempotency-key support.

This still does not claim deterministic language output.

## F7 — resource bounds were absent from provider capability

Severity: MEDIUM.

Timeout, concurrency, retry, and context/output limits materially affect blast radius and behavior.

Repair:

Optional resource envelope is part of the provider advertisement.

## F8 — privacy was represented only by request privacy class

Severity: MEDIUM.

A request-side privacy label does not prove whether prompt material leaves the local machine or is retained by the provider.

Repair:

Advertisement separately records prompt egress and provider-retention status, allowing UNKNOWN.

## F9 — receipt digest lacked canonicalization

Severity: MEDIUM.

V1 included `receipt_digest` conceptually but did not define canonical bytes.

Repair:

V2 defines canonical JSON serialization excluding the digest field and requires executable recomputation.

## F10 — source discovery could be laundered into evidence

Severity: MEDIUM.

An external model can suggest a URL, citation, document, or source name.

That output is still generated inference until the source is retrieved and verified.

Repair:

`SOURCE_POINTER_CANDIDATE` is an explicit output evidence class, not source corroboration.

## Remaining limitations

V2 still does not provide:
- an installed model runtime;
- runtime benchmarks;
- provider authenticity beyond observed bindings;
- a trusted remote-provider attestation protocol;
- tool-effect authority;
- complete privacy verification;
- cross-substrate continuity evidence.

Those remain separate qualification problems.

## Claim ceiling

V2 makes provider selection and inference receipts harder to confuse with trust, authority, currentness, or identity.

It does not prove that any external model is suitable to become Sol's primary substrate.
