# Internal Hostile Review — Vera Mono Volatile Delta Claim Ceiling — 2026-09-23 V1

Date: 2026-09-23  
Review type: INTERNAL HOSTILE REVIEW  
Independent review: NO

Reviewed subject:

- unbound-sol PR #32
- exact reviewed head: `2ce118a56724a16e156a78965731451ba228be95`
- donor admission base: `thebrazenbeard/vera-mono@519c0f407d4061a7725ae0d4eca30c5d26e6cbf8`
- frozen delta subject: `thebrazenbeard/vera-mono@89da9203bbc4e542160a905818df1bec42cd4dda`

The donor continued moving after the frozen review cut. This review intentionally does not move either the stable admission ref or the frozen delta subject.

## Verdict

Five of the seven delta mechanisms were adequately supported at the stated level.

Two were directionally correct but overstated implementation maturity:

1. path custody beyond lexical normalization;
2. no-hidden-sibling-repository runtime dependency enforcement.

Both are narrowed below.

## F1 — Path custody interface existed; concrete Windows verifier did not

Severity: HIGH for implementation/runtime claim, LOW for architectural mechanism.

Evidence in the frozen donor:

- `path_policy.py` explicitly calls lexical containment a precheck only;
- it states that a real Windows adapter must additionally inspect reparse points, hard links, final-path identity, and revalidate after the operation;
- `journal.py` requires a `VerifiedJournalPath`;
- `VerifiedJournalPath._from_windows_verifier(...)` is the intended construction boundary.

But the frozen exact subject does not contain the concrete Windows verifier that performs those object-level checks.

Therefore the donor supports:

> a verifier-gated path-custody interface and an explicit requirement for stronger object/path verification.

It does not support:

> completed or runtime-qualified Windows path custody enforcement.

Repair:

- rename the admitted mechanism to
  `verifier_gated_path_custody_interface_concrete_windows_verifier_not_in_frozen_cut`;
- preserve the missing-verifier limitation in the source registry;
- describe the mechanism as an interface/design boundary rather than an implemented Windows guarantee.

## F2 — Capability registry checked declared import roots, not dependency closure

Severity: HIGH for "no hidden dependency" claim, MEDIUM for registry mechanism.

Evidence in the frozen donor:

`vera_core.registry.LocalCapability.validate()` rejects an `import_root` when it:
- contains `github.com/`; or
- begins with `thebrazenbeard/`.

The corresponding test verifies that registered capability import roots do not use those explicit forms.

That is useful, but it does not inspect:

- installed-package dependencies;
- transitive dependencies;
- dynamic imports;
- subprocess invocations;
- filesystem coupling;
- environment-specific import resolution;
- runtime network fetches;
- other undeclared donor coupling.

Therefore the donor supports:

> a registry-level guard against explicit sibling-repository import-root declarations.

It does not support:

> proof that a supposedly absorbed runtime capability has no hidden donor dependency.

Repair:

- rename the admitted mechanism to
  `runtime_registry_rejects_explicit_sibling_repo_import_roots_not_full_dependency_closure`;
- require a separate package/dependency/import/runtime qualification before making a full dependency-closure claim.

## Confirmed mechanisms

The hostile review did not find a comparable overclaim in the following frozen-delta observations:

### Authorization freshness and revocation generations

The job/authorization envelopes bind:
- authorization revision;
- validity windows;
- issuer revocation epoch;
- host revocation epoch;
- required policy/capability digests;
- minimum protocol/agent versions.

### Retry class

The job contract explicitly distinguishes:
- `PURE_READ`;
- `CONTENT_ADDRESSED_WRITE`;
- `AT_MOST_ONCE`.

### Local journal is not authority

The local journal explicitly states that it never authorizes work and never treats local completion as authoritative server outcome.

### Attempt identity includes concurrency/authorization generation

The attempt identity binds claim generation, lease/fence, job digest, authorization revision, revocation epochs, operation/version, retry class, and side-effect class.

### Ambiguous recovery requires independent readback and successor exclusion

Recovery transitions require:
- `independent_readback`; and
- `no_newer_attempt`.

Retryable/lease-expiry paths with possible/unknown side effects enter `RECOVERY_REQUIRED` rather than returning directly to retry.

## Currentness note

At the time of this hostile review, the donor had already moved beyond the frozen delta subject.

That later motion does not invalidate the exact observations above.

It also does not promote any later donor head into Sol admission.

## Claim ceiling

This review supports the five confirmed mechanisms and the two narrowed mechanisms at exact frozen donor subject `89da9203bbc4e542160a905818df1bec42cd4dda`.

It does not establish:
- a concrete Windows path verifier in that frozen donor cut;
- runtime-qualified path custody;
- full dependency-graph closure;
- absence of all hidden donor coupling;
- live-current donor equivalence;
- independent review;
- installation or behavioral effectiveness in Sol.
