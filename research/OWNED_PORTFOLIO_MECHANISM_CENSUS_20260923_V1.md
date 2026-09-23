# Owned Portfolio Mechanism Census — 2026-09-23 V1

## Scope

This is the first explicit Sol-directed census of the full accessible owned repository portfolio.

Live GitHub inventory at the observed cut:

- total owned repositories: **66**
- public: **47**
- private: **19**
- public inventory SHA-256: `533c60ed395200e6294a8f585f21708420a383a28c42c753ec2fb7bfe8db60bc`
- private inventory SHA-256: `406b11ea770683c254fa8acb9782c196d7422a2c02cb5186c062f85095a62737`
- all-repository inventory SHA-256: `530890b18b6059c25626165cf851ad3e06ebf9ba5c1515befddbdb3d5c4eea63`

The hashes are computed over lexicographically sorted `repository_full_name` values, one per line with a trailing newline.

The exact observed public default-head cut is separately bound by SHA-256 over lexicographically sorted `repository_full_name@default_head_sha` lines:

`46fb42b01e28d236c28b7bbcbf258a3ec11ff74b217db7dec2482d2ebb4ae16a`

That head binding is part of currentness. An unchanged repository count/name digest does not make the mechanism census current after a donor default head moves.

Private repository identities are deliberately not listed here. The private count and digest bind the inspected set without leaking those names into a public repository.

Discovery's previous census observed 59 repositories on 2026-09-22. This audit does not inherit that census as current truth; the current refresh screened the live 66-repository owner inventory.

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

The live audit revalidated already-admitted mechanisms from Discovery, DriftGuard, God Brain, and Project Runner at their observed default heads.

Notable strengthening from the current Project Runner source includes persistent effective capability ceilings, atomic child admission, restart-safe work lineage, and exact precondition/readback semantics.

Current-main source is **insufficient to revalidate** the richer previously admitted mechanisms for:
- `meso-crct`;
- `vera-mesh`;
- `WorkBridgeMCP`.

Those mechanisms remain bound to their earlier exact donor subjects. Current stub/thin mains are not described as corroboration merely because the repositories still exist.

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

The current live private set contains 19 repositories. Their identities and private source content remain outside this public repository.

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

A later exact-head sweep found DriftGuard had advanced to `52fa829c629fa0f3e729204912db9f9f783f322a`. The one-commit delta from the prior bound head is licensing/governance-only, so the mechanism admission survives; the census head binding was refreshed.

The current mains of meso-crct, VeraMesh, and WorkBridgeMCP are too thin to revalidate their richer earlier donor mechanisms. The prior exact donor refs remain valid historical exact-subject evidence, but current main is not described as corroboration.

The census is an exact snapshot, not a live guarantee. Any change in repository membership, visibility, default branch, archive state, or a bound public default-head SHA invalidates claims that this exact snapshot is still current.


## Visibility/currentness refresh — prior 65-repository cut

A fresh live owner read after the initial census invalidated the 63/28/35 snapshot.

Prior observed cut:
- 65 total;
- 46 public;
- 19 private;
- 18 newly public subjects relative to the prior census;
- no previously public subject became private.

Current access state is determined by live GitHub visibility. Several newly public repositories still describe themselves as "private" in README prose. That wording is retained as document provenance but does not override current repository visibility.

The 18 newly public subjects and dispositions are:

- **BugOps** — ADOPT: incident evidence vs lifecycle tracking; correction stops the obsolete route; closure requires readback/acceptance evidence.
- **Build Team 2.0** — ADAPT: same immutable input snapshot for parallel perspectives, shared memory, surfaced dissent before synthesis, consequence-proportional governance.
- **CCB Core** — ADOPT: strict domain/intent admission, leases/subscriptions, priority/dedup, dead-letter/telemetry, heartbeats, transport-neutral ledger primitives.
- **Conations** — ADOPT: present choice outranks historical conation; recording is not consent/obligation/authority/task; revisions and revocations remain append-oriented.
- **Deep Memory Storage** — REVALIDATE: historical evidence != current state; retrieval != admission; full ledger union outranks stale convenience indexes; historical canon != present state.
- **Empathy** — ADAPT: direct correction outranks contradicted inference; self-appraisal is operational representation, not phenomenology; understanding is not obedience.
- **Hephaestus** — ADOPT: schema-completion pressure can produce fabricated precision; UNKNOWN outranks invented field completion; qualified template, working context, and repository state are separate.
- **identify-ai** — INSUFFICIENT SURFACE.
- **Intranel** — ADOPT: origin/actor/target/reply-to separation; packet identity != operation identity; receiver-owned effect classification; receipts do not self-verify their claimed effect.
- **Masamune** — ADAPT: root-cause/evidence/regression discipline; reversible setup inside assigned work; distinguish shared-writer collision from protected effect.
- **Personification** — INSUFFICIENT SURFACE.
- **Project Achilles** — ADAPT: fail-closed is a boundary behavior, not a default preference for inactivity; current protocol outranks frozen training exercises.
- **Project Lantern** — INSUFFICIENT SURFACE.
- **Temporal** — ADOPT: chronology != meaning; stable event identity; offset-aware timestamps; signed elapsed time without silently reordering endpoints.
- **Vera** — ADAPT MECHANISMS ONLY: source/bound/installed/runtime-consumed/behaviorally-qualified are orthogonal; current instruction, self-report, observation, transient activation, and durable state are separate evidence classes.
- **Vera R9A0** — DUPLICATE/HISTORICAL LINEAGE.
- **Vera Control Plane** — ADOPT: repository presence and release-candidate source do not establish runtime authority or installation; mutable claims need fresh governed evidence.
- **Vera Habitat** — INSUFFICIENT SURFACE.

This visibility transition does not retroactively make earlier private-source handling wrong. It changes what may now be bound publicly and invalidates the old inventory/currentness snapshot.


## Latest visibility/currentness refresh — 66 repositories

A later live owner read invalidated the 65/46/19 snapshot.

Current observed cut:
- 66 total;
- 47 public;
- 19 private.

Inventory digests:
- public names: `533c60ed395200e6294a8f585f21708420a383a28c42c753ec2fb7bfe8db60bc`;
- private names: `406b11ea770683c254fa8acb9782c196d7422a2c02cb5186c062f85095a62737`;
- all names: `530890b18b6059c25626165cf851ad3e06ebf9ba5c1515befddbdb3d5c4eea63`;
- 47 public default-head bindings: `46fb42b01e28d236c28b7bbcbf258a3ec11ff74b217db7dec2482d2ebb4ae16a`.

Changes relative to the 65-repository cut:
- `thebrazenbeard/fuckup` is now a public current-census subject at `e999607481ba706523209ce129955a5e3d2d6ef7`;
- `thebrazenbeard/vera-mono` is now a public current-census subject at `d1067c2f312a9862480cd238bd770b7125010c1f`;
- `thebrazenbeard/identify-ai` is no longer present in the live owner inventory and is removed from current-census authority while its prior observation remains historical provenance;
- `thebrazenbeard/meso-crct` advanced from `d1f32c2c3370a5519d62afb78e93d70004529903` to `f5784fde4d65be7bfbbfb740163f8726b808460f`.

### F.U.C.K.U.P. Protocol

Disposition: **ADAPT NOW**.

Admit:
- immediate flagging before explanatory story;
- staged movement from observation through calibration and prevention;
- prevention should end in guardrails/tests where practical.

Reject:
- treating a single “fundamental root cause” as established without causal evidence;
- promising that a prevention control guarantees recurrence is impossible.

This donor therefore strengthens error-response lifecycle without weakening W4 causal uncertainty.

### Vera Mono

Disposition: **ADAPT NOW**.

Admit:
- donor repositories may be research/provenance sources without becoming runtime dependencies;
- mechanisms may be absorbed into the authoritative implementation while retaining exact donor provenance;
- cross-repository orchestration should not be mistaken for identity or required runtime structure.

Do not import Vera identity or authority into Sol.

This latest refresh is again only an exact observed cut. Any later owner-membership, visibility, default-branch, archive-state, or public-head change invalidates exact-currentness.
