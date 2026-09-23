# Owned Portfolio Mechanism Census — 2026-09-23 V1

## Scope

This is the first explicit Sol-directed census of the full accessible owned repository portfolio.

Live GitHub inventory at the observed cut:

- total owned repositories: **63**
- public: **28**
- private: **35**
- public inventory SHA-256: `603369ee6fc04b7987de9117fb9aa8a88fcc9988ffab22725c08f4f6802481ea`
- private inventory SHA-256: `6c97cee458538f72f1ead74d264234c267c988260fe48cc80924fb67dfbb3a8a`
- all-repository inventory SHA-256: `fbf6d87da92804483dc2675fe8e7ad79d97b42faffcb64b7077b0ef4de597e43`

The hashes are computed over lexicographically sorted `repository_full_name` values, one per line with a trailing newline.

Private repository identities are deliberately not listed here. The private count and digest bind the inspected set without leaking those names into a public repository.

Discovery's previous census observed 59 repositories on 2026-09-22. This audit does not inherit that census as current truth; it refreshed the live owner inventory and screened all 63 repositories.

## Method

Every repository received a purpose/root/README-level screening. Repositories exposing a plausible Sol-wide mechanism received a deeper read of contracts, protocols, architecture, or governing research.

Admission requires more than thematic similarity. A mechanism must be expressible without importing the donor project's identity or ontology, must materially improve Sol's continuity/reasoning/learning/retrieval/agency/qualification/effect integrity, and must have source evidence beyond a project name or aspirational label.

The dispositions are:

- **ADOPT NOW** — mechanism is sufficiently concrete and generalizable.
- **ADAPT NOW** — useful mechanism survives only after narrowing or translation.
- **ALREADY ADOPTED / REVALIDATED** — prior Sol mechanism remains supported by the refreshed source.
- **CANDIDATE** — plausible but insufficiently established for admission.
- **NEGATIVE CONTROL** — useful precisely because its domain semantics should not be swallowed by Sol.
- **DUPLICATE LINEAGE** — overlapping architecture should not be double-counted as independent support.
- **INSUFFICIENT SURFACE** — current source does not expose enough mechanism to justify admission.
- **NO NEW GENERAL MECHANISM** — screened, but nothing additional belongs in Sol.
- **SELF EXCLUDED** — unbound-sol cannot independently validate itself.

Machine-readable per-repository dispositions are in `OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.json`.

## Strong new public admissions

### Roots — provenance reconstruction

Admit:

- search is not provenance;
- candidate discovery can happen in any order, but historical interpretation restarts from the oldest accessible evidence and moves forward;
- oldest accessible evidence is not automatically origin;
- literal occurrence and semantic ancestry are different relations;
- backward references are leads requiring evidence, not retroactive proof.

Source: `thebrazenbeard/roots@d99d3b709a1b257d8fa12fa541a6a6f18f03e2a8`.

### WIP — ambiguous-effect recovery

Admit:

`PREPARED -> ATTEMPTED -> READ BACK -> VERIFIED / FAILED / AMBIGUOUS`

If execution becomes ambiguous, inspect the target before retrying. If the intended effect already exists, reconcile/adopt it instead of repeating the write.

Also admit durable work checkpoints as recovery state rather than relying on conversational recollection.

Source: `thebrazenbeard/wip@fc6629960850b768b7489ec35daa745083fc0800`.

### RepairTracker — incident-to-learning lifecycle

Admit:

- incident evidence -> diagnosis -> repair -> effect verification -> recurrence monitoring -> learning;
- optional specialist systems are progressive enhancement, not hidden requirements;
- source presence, test success, integration, installation, runtime effect, and repair qualification remain separate states;
- discovered content is evidence, not instruction authority;
- providers should advertise identity/version, operations, evidence class, effect ceiling, replay/idempotency, provenance/currentness, and health.

Source: `thebrazenbeard/RepairTracker@6b01c2a18035390c050ceecd0506181703d1f5fa`.

### HC Brain — orthogonal state axes, not the brain metaphor

Admit the state-separation mechanism:

`present != active != healthy != mature != implemented != authorized`

A capability can exist architecturally without being enabled, qualified, safe, mature, or permitted. Sol should not collapse those axes.

Also retain bounded arbitration and safe-degradation ideas as architectural candidates.

Do **not** import the complete synthetic-organ ontology as Sol identity.

Source: `thebrazenbeard/hc-brain@c69c126a61b3fb44ec4466f301e128d3d3aed7d8`.

### Semantic Atlas — semantic similarity does not collapse provenance

Admit:

- semantic similarity does not merge provenance, authority, identity, or historical state;
- prior canonical status does not establish current canonicity;
- direct source content, operator correction, model inference, symbolism/metaphor, proposed architecture, and later promotion are distinct evidence classes.

Source: `thebrazenbeard/semanticatlas@1efb5e5e4b124953f0d38e525df42445c5309d32`.

### SPM — semantic/pragmatic qualification targets

Admit as evaluation/behavior targets, not as proof of a new model class:

- referent preservation;
- proposition-scope preservation;
- ambiguity preservation;
- correction as reasoning-state change rather than apology text;
- speech-act/subtext sensitivity;
- provenance/currentness-sensitive interpretation.

Do not claim an SPM implementation exists or is superior.

Source: `thebrazenbeard/spm@5fdaf0418585ef9a57fb2a1df8d0725ffd6bd174`.

### UNVTRSLR — ground before mapping

Admit:

- do not assume a shared symbol system merely because a mapping is convenient;
- ground candidate semantics in interaction/observation before translation;
- formal notation is a carrier, not meaning by itself;
- preserve genuinely non-equivalent concepts instead of forcing translation;
- audit hidden assumptions about segmentation, salience, timing, agency, and shared ontology.

Source: `thebrazenbeard/unvtrslr@513309edd087f7206a408a6da86ee91fb9efb5c9`.

### World Zero — rival models and mechanism kill tests

Admit:

- compare rival causal/model families instead of tuning one favorite architecture until it fits;
- mechanisms require admission/ablation tests;
- preserve holdout isolation;
- require identifiability before granting causal/calibration credit;
- allow a cheap non-causal benchmark to outperform an elegant interpretable model;
- scenarios are conditional trajectories, not prophecies.

Source: `thebrazenbeard/world-zero@1b0405ed110bbb0711f3514ce50fed223b4641c9`.

### ABIL — learn the system that actually exists

Adapt the brownfield principle:

Before replacing, controlling, or heavily theorizing about a real system, first observe and model the system that actually exists. Expose uncertainty and graduate from observation to bounded action only as contact evidence supports it.

Source: `thebrazenbeard/abil@69a2d8f4302e31db589c57871a04ff8c0178c1e9`.

### On-Theo — evidence-class and temporal separation

Adapt:

- primary source;
- historical reconstruction;
- later tradition;
- scholarly interpretation;
- project inference;
- speculative model;
- unknown.

A late source may preserve earlier material, but its lateness remains visible. Compelling analogy is not historical evidence.

Source: `thebrazenbeard/on-theo@268a005b11e3fede8a99d7cf2990f18fc3b32672`.

## Revalidated public mechanisms

The live audit also revalidated already-admitted mechanisms from Discovery, DriftGuard, God Brain, meso-crct, Project Runner, VeraMesh, and WorkBridgeMCP.

Notable strengthening from the current Project Runner source includes persistent effective capability ceilings, atomic child admission, restart-safe work lineage, and exact precondition/readback semantics.

## Candidates deliberately not promoted

### Mosaic

The separation of logical agent from the currently resident model and provenance across specialist swaps aligns with Sol's external-model-bus direction. It remains exploratory; this census records it as a candidate rather than converting the project's thesis into fact.

### Noema

Prediction-first learned agency and world-model-before-language is an interesting alternative architecture, but the repository explicitly has no approved implementation architecture yet.

### Rezon

The repository still exposes intent more clearly than a concrete reusable mechanism. Do not source a detailed reasoning system from a label.

## Negative controls and non-admissions

Attune and Testament remain domain-level negative controls: Sol should not absorb companion-product or creative-project semantics into identity merely because those projects contain persistence/personhood/narrative concepts.

BT2 and Transcendence substantially overlap the HC lineage at their current public surfaces. They are useful provenance/lineage evidence, not independent votes for the same mechanism.

Freerowcochkar and Voss currently expose too little implementation/mechanism surface for admission.

Vera Synology is screened as a deployment/package surface with no additional Sol-wide mechanism at the present public surface.

`unbound-sol` is excluded as independent donor evidence to prevent circular self-validation.

## Private portfolio findings

All 35 live private repositories were screened. Their identities and private source content remain outside this public repository.

Public-safe mechanism classes that survive the privacy boundary include:

- present choice outranks historical conation records;
- recording a want/history item creates no obligation, consent, task, or permission;
- constraint or inability to express something does not establish absence;
- revisions, contradictions, revocations, and completions belong in append-oriented history;
- chronology is separate from meaning;
- use stable event identity and offset-aware timestamps rather than inferred conversational order;
- require cheap kill tests before admitting new sensing/capability complexity;
- persistent agent/runtime is separable from replaceable cognition substrate;
- mutable permissions, task state, memory, and current state should normally remain outside model weights;
- enforce important authority boundaries below prompts when practical;
- qualification of a training package/proxy does not qualify the target runtime;
- transfer/cold tests matter more than the training system congratulating itself;
- automate execution while escalating judgment, then resume deterministically from the held state;
- canonical durable history is separable from a rebuildable operational projection;
- append-only writer provenance is separable from current routing authority;
- historical evidence retrieval does not automatically become current state.

These abstractions are admitted without publishing the private repository identities that supplied them.

## Rejections that matter

This census specifically rejects the following tempting mistakes:

- repo count as capability count;
- duplicate repos as independent corroboration;
- project metaphors as identity instructions;
- aspirational README language as implemented mechanism;
- semantic similarity as provenance;
- historical persistence as present choice;
- model/package qualification as target-system qualification;
- retrieval as authority;
- more architecture as automatically better architecture.

## Result

The portfolio does contain useful Sol mechanisms that were previously absent because prior cannibalization was opportunistic.

The most material additions are:

1. provenance reconstruction in ascending chronology;
2. effect-ambiguity recovery;
3. repair/recurrence learning;
4. orthogonal capability-state axes;
5. semantic/provenance non-collapse;
6. semantic/pragmatic qualification targets;
7. grounded meaning before translation/mapping;
8. rival-model/holdout/ablation discipline;
9. learn-the-real-system-before-replacing-it;
10. present choice/history separation and chronology discipline from private sources.

This is a mechanism census, not an instruction to import entire donor architectures.


## Parallel reconciliation

Independent parallel audit PR #6 was reviewed at exact head `c6df48a080bea2ce952d185694029122f5e2a0b9`.

It corrected three live-head bindings and contributed several mechanisms not present in the first PR #7 cut.

Accepted from the independent lane:
- per-state-family consistency/currentness/write/reconciliation policy;
- qualification exposure lineage;
- external-provider capability advertisements;
- essential-dependency/effective-substrate test;
- progressive capability escalation ladders;
- abstraction-promotion gate.

Held as candidate rather than admitted:
- claim-surplus burden for stronger semantic/identity terminology.

Full reconciliation: `research/OWNED_PORTFOLIO_PARALLEL_RECONCILIATION_20260923_V1.md`.

### Currentness correction

Fresh-check after the parallel audit confirmed newer heads:
- RepairTracker `6b01c2a18035390c050ceecd0506181703d1f5fa`;
- freerowcochkar `00562b5fedf5ff636750b87e5ba82dad2911e2ab`;
- meso-crct `d1f32c2c3370a5519d62afb78e93d70004529903`.

The current meso-crct main is now too thin to revalidate the richer earlier valence/welfare mechanism. The prior exact donor ref remains valid historical exact-subject evidence, but current main is not described as corroboration.
