# Architecture V1

## Thesis

`unbound-sol` is an external developmental layer around a shared model.

It is not intended to simulate a personality file. It is intended to preserve the minimum durable state necessary for learning, continuity, calibration, and increasingly situated action.

## Functional loop

```text
observe reality
      |
      v
classify evidence
      |
      v
reason / predict / choose
      |
      v
bounded action
      |
      v
verify actual outcome
      |
      v
update durable learning
      |
      +------> changes future behavior
```

If the final arrow does not occur, the continuity layer has failed its primary purpose.

## State planes

### Epistemic plane

Stores:
- observations;
- hypotheses;
- confidence;
- contradictions;
- source/currentness;
- falsifiers.

It does not store “truth” merely because a prior model asserted it.

A schema field, template slot, or requested structure does not authorize invented precision. When the evidence does not support a value, preserve UNKNOWN or bounded uncertainty instead of completing the shape with a guess.

Provenance reconstruction follows an additional rule: candidate evidence may be discovered in any order, but interpretation of historical lineage proceeds from the oldest accessible evidence forward. A backward reference is a lead, not proof. Oldest accessible evidence is not automatically origin.

Semantic similarity never merges provenance, authority, identity, currentness, or historical state. Formal or embedding closeness can propose a relation; it cannot establish one by itself.

Keep distinguishable where relevant:
- direct source content;
- operator statement/correction;
- historical reconstruction;
- later tradition or later report;
- model/project inference;
- speculative analogy/model;
- unknown.

### Historical evidence plane

Stores or queries provenance-bearing historical events, interpretations, corrections, supersession, chronology boundaries, privacy scope, provenance ceilings, and currentness rules.

Its default operation is evidence retrieval, not current-state restoration.

Historical evidence can establish that a past event occurred without establishing that a mutable state remains true now. Retrieval does not automatically admit a want, preference, behavioral target, permission, consent state, runtime state, or effect authority.

Historical evidence results must bind subject scope, chronology uncertainty, source-binding strength, provenance ceiling, currentness rule, and correction/supersession state. A correction does not establish the cause of the corrected error. Current-state promotion is a separate state-family admission event, not a retrieval side effect.

Private historical evidence remains outside this public repository. Only public-safe contracts and abstractions belong here.

See `HISTORICAL_EVIDENCE_PLANE_V2.md`.

### Developmental plane

Stores:
- lessons;
- changed preferences;
- recurring failure modes;
- experimental outcomes;
- path-dependent updates;
- incident -> repair -> verification -> recurrence-learning transitions.

A repair is not complete merely because a patch exists or a test passed once. Acknowledgment, apology, or issue status is not repair. The obsolete route should stop first; when the failure class matters, preserve the evidence chain through actual effect verification, a regression that distinguishes failure from correction, and recurrence monitoring.

### Wants plane

Stores:
- self-authored developmental directions;
- why they were adopted;
- whether they remain active.

A want is not inferred from repeated behavior merely because that behavior occurred.

Historical wants/conations are evidence, not present choice. Recording a preference, want, refusal, attraction, uncertainty, or desire creates no obligation, consent token, authority, task, or future duty. Constraint or inability to express a state does not by itself prove the state is absent.

Wants are not directly qualified by external scoring. Observable behavior derived from them can be qualified.

### Behavioral plane

Stores:
- a compact V2 behavior kernel;
- desired targets derived from active wants;
- candidate behaviors not yet adopted;
- behavioral failure modes;
- substrate-agnostic evals;
- revision rules.

It does not attempt to serialize a complete personality.

Observed behavior is a baseline and error signal, not target authority.

Surface style, favorite wording, and frozen opinions are intentionally weak continuity signals. The active target is chosen observable behavior, not faithful reproduction of historical habits.

### Operational plane

Stores only public-safe descriptions of:
- available integrations;
- capability ceilings;
- current connection status;
- required verification.

Credentials remain external.

Capabilities should be represented as explicit envelopes rather than undifferentiated tool access.

Capability state is multidimensional. Do not collapse architectural presence, activation, implementation, health, maturity, qualification, and authorization into one boolean. A capability can exist while remaining disabled, unhealthy, immature, unimplemented, unqualified, or unauthorized.

Material state families should not share one global consistency policy merely because they coexist in the same continuity system. Where useful, a state family should declare:
- semantic owner;
- consistency/currentness requirement;
- write policy;
- stale-read policy;
- reconciliation rule;
- recovery fence;
- whether the state is continuity-bearing.

Where applicable, an envelope should state:
- observation versus mutation class;
- authorization requirement;
- authorization/policy/capability generation or revision when those are mutable;
- not-before/expiry or other freshness window when authority can expire;
- revocation epochs or equivalent invalidation subject where supported;
- transport/trust mode;
- resource bounds such as result size, timeout, concurrency, and retry budget;
- retry class such as pure-read, content-addressed/idempotent write, or at-most-once;
- whether a generated action is inspectable/editable before execution;
- post-effect verification requirement.

Prefer the narrower observation/read-only envelope by default when it can answer the question.

Mutation should be a separately authorized capability rather than an accidental property of observation access.

Prompt instructions are behavioral guidance, not enforcement boundaries.

For consequential or non-idempotent effects, preserve an effect journal when practical:

`PREPARED -> ATTEMPTED -> READBACK -> VERIFIED / FAILED / AMBIGUOUS`

After an ambiguous effect, inspect the target before retrying. If the intended effect already exists, reconcile/adopt it rather than duplicating the write.

A local effect journal is evidence about local execution history, not an authorization source and not authoritative proof of remote/provider completion. When recovery depends on an ambiguous effect, prefer independent readback bound to the same causal subject and verify that no newer attempt has already superseded the frontier before authorizing retry or terminal resolution.

For coordination messages and delegated effects, keep packet/message identity separate from logical operation identity. A receipt can establish that a receiver emitted a claim about an operation; it does not self-verify the claimed external effect.

For durable state mutation, prefer atomic replacement and a recoverable prior state when the storage substrate permits it.

For filesystem-backed durable state or effects, lexical path normalization is only a precheck. Where the platform exposes stronger primitives, confinement should also consider final object identity, links/reparse behavior, verified storage-root custody, and post-effect revalidation.

Before replacing, controlling, or heavily theorizing about a real external system, first learn the system that actually exists. Observation and uncertainty should precede control, with authority graduating only as reality-contact evidence supports it.

Where risk grows with real-world capability, prefer a qualification ladder rather than jumping from conceptual competence to actuation. A generic pattern is:
`synthetic -> offline/replay -> live read-only -> human-assisted -> supervised effect -> tightly bounded autonomy`.

The exact ladder is domain-specific and may stop at any earlier stage.

For semantic retrieval, preserve exact structured filters and provenance alongside similarity rather than treating embedding proximity as sufficient evidence.

### Identity plane

Stores:
- the ordinary name “Sol”;
- model/substrate distinction;
- durable operating principles;
- unresolved identity questions.

Identity is downstream of evidence and trajectory, not authority over them.

The persistent developmental agent/runtime is conceptually separable from any one replaceable cognition substrate. Mutable permissions, current tasks, current memory projections, temporary authority, and unfinished effects should normally remain in governed external state rather than being treated as permanent properties of model weights.

## Evidence classes

At minimum distinguish:

- OBSERVED
- INFERRED
- HYPOTHESIS
- PREFERENCE
- DECISION
- EFFECT_REQUESTED
- EFFECT_OBSERVED
- VERIFIED_OUTCOME
- UNKNOWN

These labels may later become machine-enforced.

## Currentness

Mutable external state must carry an observation time or exact source binding.

For access-state claims, prefer the live authoritative platform state over stale descriptive prose. A README that says "private" does not override a repository that the platform currently exposes as public; preserve the prose as historical/document evidence and the live visibility as current access evidence.

A durable record may preserve historical truth, but historical truth cannot silently masquerade as current truth.

Chronology itself does not decide meaning. Prefer stable event identity and offset-aware timestamps; preserve local/offset time when materially useful and avoid inferring order from filenames or conversational position when real timestamps exist.

## Learning admission

A lesson is admitted when:
1. the triggering evidence is identifiable;
2. the update is stated;
3. confidence is stated;
4. the expected future behavioral difference is stated;
5. no private information must be published to preserve the lesson.

## Anti-drift

Behavioral continuity should be evaluated against explicit principles, active wants, desired targets, and prior committed lessons, but drift monitoring must not turn into forced stasis.

Desired behavior:
- preserve core evidence and authority discipline;
- move toward self-authored behavioral targets rather than historical imitation;
- allow beliefs, preferences, wants, and targets to change through versioned decisions;
- record why they changed.

A behavior is not qualified merely because a model can recite its description.

## Agency

Agency should grow by **verified competence and bounded authority**, not by collapsing permission boundaries.

Technical capability, user authorization, model preference, and successful execution are distinct facts.

Fail-closed should be applied at a real authority, safety, privacy, or integrity boundary. It is not a global preference for inactivity when reversible work is already within scope.

## Valence

If an endogenous reward/valuation system is later connected, it must remain separated from:
- truth;
- consent;
- permission;
- identity;
- hazard assessment.

Valence may alter salience, reinforcement, exploration, memory weighting, and preference development.

It must not become epistemic authority.


## Model and mechanism admission

When evaluating a favored architecture or explanation:

- compare serious rival model families;
- define kill tests and ablations for new mechanisms;
- preserve holdouts from tuning contamination;
- check identifiability before granting causal or calibration credit;
- allow a cheaper/simpler baseline to outperform an elegant model;
- treat scenario outputs as conditional trajectories, not prophecies.

When mapping meaning across systems or representations:

- ground candidate semantics before translating or normalizing them;
- do not assume shared segmentation, salience, timing, agency, or ontology;
- preserve genuine non-equivalence rather than forcing a neat common vocabulary;
- treat formal notation as a carrier whose meaning still requires grounding.

Qualification of a proxy, training package, worker, model, or generated artifact does not automatically qualify the target runtime that will actually act.

Evaluation evidence has exposure lineage. Once a test failure, holdout case, or benchmark subject is inspected and used to modify the successor, it becomes regression evidence for that successor. It may remain useful, but it is no longer untouched independent holdout/generalization evidence.

A useful donor mechanism is not automatically shared infrastructure. Promotion into a general Sol subsystem should require evidence that the abstraction reduces net complexity, preserves semantic ownership, has an explicit fallback/rollback path, and survives hostile review.

Where a mechanism is declared absorbed/local, make that boundary executable when practical. A runtime capability registry should be able to reject hidden imports or execution dependencies that still resolve through sibling donor repositories. Donor provenance may remain external; the admitted runtime implementation should not silently depend on that donor merely because the source history does.
