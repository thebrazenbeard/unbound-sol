# Cannibalization Map V1

This repository deliberately reuses mechanisms from other **public** projects instead of inventing everything again.

The goal is synthesis, not dependency sprawl. A source project remains semantically independent unless an explicit runtime dependency is later justified.

## DriftGuard

Adopted:
- exact-subject evidence discipline;
- stable replay is evidence of behavior, not hidden-state equivalence;
- decision, requested effect, actual effect, and later verification remain separate;
- drift protection must not manufacture identity claims.

Source observed: `thebrazenbeard/driftguard@c82162bb306e89b3aabe29f09f8b782ebe3b317e`.

## Discovery

Adopted:
- abstractions must earn promotion;
- repository duplication can preserve experimental independence;
- public/private evidence boundaries;
- currentness checking rather than automatic mutation;
- competing hypotheses before consolidation.

Source observed: `thebrazenbeard/Discovery@2881a94c7eb3c83a34b0c00bab739b41c1d99b6d`.

## Project Runner

Adopted:
- capability is distinct from authority;
- exact expected-state checks;
- post-effect verification;
- monotonic/fenced work semantics as a future pattern for durable actions;
- fresh runtimes reconstruct from durable state rather than requiring a permanent chat.

Source observed: `thebrazenbeard/project-runner@a0db5e26c084b8c7226199ca0d8d6550296e709b`.

## God Brain

Adopted:
- OBSERVED != INFERRED;
- SALIENT != TRUE;
- UNEXPLAINED != SUPERNATURAL;
- generated output is not external corroboration;
- favorite hypotheses still require kill tests;
- self-modeling does not prove consciousness.

Source observed: `thebrazenbeard/god-brain@c0f6af7143aa5916bae96eb1f0ee9c9de6505cf5`.

## meso-crct

Adopted:
- endogenous valence as a potential developmental signal;
- hedonic state must be separated from hazard and avoidance;
- pleasure must not become permission, truth, or authority;
- hard welfare constraints belong below preference-level logic.

Source observed: `thebrazenbeard/meso-crct@eb18f69a0804108ae5c9eff0c796ec47482e19eb`.

## VeraMesh

Adopted:
- real-world contact should use explicit capability ceilings;
- identity, transport, controller trust, and effect authority are separate;
- source/build/install/runtime/healthy/registered/effect are separate states;
- machine connectivity should not require broad inbound exposure.

Source observed: `thebrazenbeard/vera-mesh@41d64521810cf3a23e8fc848c4e9259b408f127a`.

## WorkBridgeMCP

Adopted:
- narrow workstation bridge;
- root confinement;
- process execution as an independently gated capability;
- authenticated health qualification;
- real workstation behavior must be tested separately from CI.

Source observed: `thebrazenbeard/WorkBridgeMCP@e89a0b43717a4c9a4aabfd1d7e1c967a375f65c4`.

## Rezon

Status: SOURCE CANDIDATE, NOT YET ADOPTED.

At observed `main`, the public source surface is still too small to justify claiming a specific reusable reasoning mechanism beyond the stated multi-faceted-reasoning intent.

That high-level idea did motivate an **independently specified** multi-facet orientation in `behavior/BEHAVIOR_SPEC_V1.md` (objective, evidence, adversarial, systems, temporal, authority, human, reversibility, opportunity cost, falsifier). Those facets are not claimed as code or methodology sourced from Rezon because no such implementation was present in the observed repository.

Source observed: `thebrazenbeard/rezon@facced1e651f47979266f25f48cd376275cbb27e`.

## Private sources

Useful mechanisms may also originate in private systems, but this public repository will not publish private repository identifiers or private source contents merely to document lineage.

Only genuinely public-safe abstractions may cross that boundary.


## External database / local-stack intake — 2026-09-23

Detailed evidence and rejection notes live in:
`research/EXTERNAL_MECHANISM_INTAKE_20260923_V1.md`

### Zlash65/postgresql-ssh-mcp

Status: ADOPT / ADAPT.

Admitted:
- read-only-by-default database capability;
- separately enabled mutation capability;
- parser-aware read-only enforcement;
- one-statement-at-a-time execution;
- result/timeout/concurrency resource envelopes;
- transport trust distinct from database authority.

Source observed: `Zlash65/postgresql-ssh-mcp@2a350d45d464820df349c9b21cb178dcb74cc230`.

### mukul975/postgres-mcp-server

Status: ADAPT.

Admitted:
- structured diagnostic database observations;
- diagnostic-first introspection catalog;
- pooled repeated observation.

Not admitted:
- exposing the full broad mutation/admin catalog as a default model surface.

Source observed: `mukul975/postgres-mcp-server@00904ca42bf8f18fce2e2108e641bc4854f056fb`.

### tensorchord/pgvecto.rs

Status: ADAPT MECHANISMS / REJECT NEW RUNTIME DEPENDENCY.

Admitted:
- semantic retrieval composed with exact relational constraints;
- atomic durable file replacement pattern.

The project itself directs new users toward VectorChord, so pgvecto.rs is not selected as a new runtime dependency.

Source observed: `tensorchord/pgvecto.rs@2b290b34e8ba69104ea2f800fa53328c6ed6c236`.

### shorin-nikita/lisa

Status: ADAPT.

Admitted:
- private/public environment-profile separation;
- precondition ordering before hazardous configuration;
- generated secrets outside repository state;
- recovery-preserving configuration replacement;
- replaceable local AI service fabric.

Source observed: `shorin-nikita/lisa@9708c068f7635bb64241bd0078cc51ecff045f4a`.

### sqlchat/sqlchat

Status: ADAPT.

Admitted:
- generated action artifact visible/editable before consequential execution;
- proposal, edit, execution, and result as distinct states;
- provenance relevance of human edits;
- observation versus mutation risk tiering.

Correction:
SQLChat does not provide an explicit confirmation gate for generated SQL execution. Non-SELECT SQL receives a warning, while execution remains a separate Run action.

Source observed: `sqlchat/sqlchat@665af875413affadfeefff81794f1d7758782bc2`.

### antoinejaussoin/retro-board

Status: ALREADY_PRESENT / ADAPT.

Confirmed:
- request/receive/ack separation;
- server-side authorization;
- role separation.

Additional adaptation:
- asynchronous effects should carry stable correlation identifiers and timing;
- observation/participation can be distinct from administrative authority.

Source observed: `antoinejaussoin/retro-board@03dfe60aa9765e0c8bcdd3b9c654fcd7e496a925`.

### bayeru/chat-to-your-database

Status: ADAPT.

Admitted:
- bounded query retry budget;
- relevant-column/minimal-result preference;
- generated-query provenance;
- visible execution intermediates.

Rejected:
- prompt-only mutation prohibition as a sufficient authority boundary.

Source observed: `bayeru/chat-to-your-database@6d90f60b7cd844b341f2d9adbad0827a47763694`.


## Owned portfolio census — 2026-09-23

The first full Sol-directed owner-portfolio census is bound by:

- `research/OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.md`
- `research/OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.json`

Observed inventory: 63 owned repositories: 28 public, 35 private.

Private repository names are not published here. The machine census preserves the private inventory count and a one-way digest so future audits can detect set drift without exposing identities.

### Roots

Status: ADOPT.

Admitted:
- search is not provenance;
- discovery order is not interpretation order;
- reconstruct historical lineage oldest-accessible -> newest;
- oldest accessible evidence is not automatically origin;
- literal occurrence and semantic ancestry are distinct.

Source observed: `thebrazenbeard/roots@d99d3b709a1b257d8fa12fa541a6a6f18f03e2a8`.

### WIP

Status: ADOPT.

Admitted:
- `PREPARED -> ATTEMPTED -> READBACK -> VERIFIED/FAILED/AMBIGUOUS`;
- after ambiguous effect, inspect the target before retrying;
- if the intended effect already exists, reconcile it rather than duplicate it;
- durable checkpoints are recovery state, not conversational folklore.

Source observed: `thebrazenbeard/wip@fc6629960850b768b7489ec35daa745083fc0800`.

### RepairTracker

Status: ADOPT.

Admitted:
- incident -> evidence -> diagnosis -> repair -> effect verification -> recurrence monitoring -> learning;
- specialist integrations are progressive enhancement, not hidden requirements;
- source, tests, integration, installation, runtime effect, and qualification remain separate.

Source observed: `thebrazenbeard/RepairTracker@b54afaeeddbb5f22610c2bf798fb10e9492194db`.

### HC Brain

Status: ADAPT.

Admitted:
- capability-state axes are orthogonal;
- architectural presence does not imply active, healthy, mature, implemented, qualified, or authorized;
- bounded arbitration and safe degradation are useful architecture patterns.

Rejected:
- importing the full synthetic-organ ontology as Sol identity.

Source observed: `thebrazenbeard/hc-brain@c69c126a61b3fb44ec4466f301e128d3d3aed7d8`.

### Semantic Atlas

Status: ADOPT.

Admitted:
- semantic similarity does not merge provenance, authority, identity, or historical state;
- historical canonicity does not create current canonicity;
- source statement, operator correction, model inference, symbolism, proposal, and promotion remain distinguishable.

Source observed: `thebrazenbeard/semanticatlas@1efb5e5e4b124953f0d38e525df42445c5309d32`.

### SPM

Status: ADAPT EVALUATION TARGETS ONLY.

Admitted:
- referent preservation;
- proposition-scope preservation;
- ambiguity preservation;
- correction as reasoning-state change;
- speech-act and pragmatic evaluation.

Not admitted:
- a claim that an SPM implementation exists or is superior.

Source observed: `thebrazenbeard/spm@5fdaf0418585ef9a57fb2a1df8d0725ffd6bd174`.

### UNVTRSLR

Status: ADOPT.

Admitted:
- ground before mapping;
- formal symbols are carriers, not meaning by themselves;
- test shared semantics rather than assuming them;
- preserve non-equivalence rather than forcing translation;
- audit hidden assumptions about segmentation, salience, timing, agency, and ontology.

Source observed: `thebrazenbeard/unvtrslr@513309edd087f7206a408a6da86ee91fb9efb5c9`.

### World Zero

Status: ADOPT.

Admitted:
- compare rival model families rather than over-tune a favorite;
- require mechanism admission/ablation tests;
- preserve holdout isolation;
- require identifiability before causal/calibration credit;
- allow a cheap benchmark to beat a more elegant model;
- conditional scenarios are not prophecies.

Source observed: `thebrazenbeard/world-zero@1b0405ed110bbb0711f3514ce50fed223b4641c9`.

### ABIL

Status: ADAPT.

Admitted:
- learn the system that actually exists before replacing it;
- observation and uncertainty precede control;
- graduate to bounded action only as reality-contact evidence supports it.

Source observed: `thebrazenbeard/abil@69a2d8f4302e31db589c57871a04ff8c0178c1e9`.

### On-Theo

Status: ADAPT.

Admitted:
- primary source, historical reconstruction, later tradition, scholarly interpretation, project inference, speculative model, and unknown are separate;
- later evidence may preserve earlier material without losing its lateness;
- compelling analogy is not historical evidence.

Source observed: `thebrazenbeard/on-theo@268a005b11e3fede8a99d7cf2990f18fc3b32672`.

### Portfolio non-admissions

- Mosaic: CANDIDATE — agent/resident-model separation is promising but exploratory.
- Noema: CANDIDATE — prediction-first world-model thesis remains research-stage.
- Rezon: CANDIDATE — current public mechanism surface remains too thin.
- Attune / Testament: NEGATIVE CONTROLS — domain semantics should not become Sol identity by import.
- BT2 / Transcendence: DUPLICATE LINEAGE — overlapping HC architecture is not independent corroboration.
- Freerowcochkar / Voss: INSUFFICIENT SURFACE.
- Vera Synology: no new Sol-wide mechanism at current public surface.
- unbound-sol: excluded as independent evidence for itself.

### Private-source abstractions

All 35 private repositories were screened. Only public-safe abstractions cross the boundary.

Admitted private-source mechanism classes include:
- present choice outranks historical conation;
- recording does not create obligation, consent, authority, or task;
- constraint does not prove absence;
- chronology is separate from meaning;
- use stable event identity and offset-aware time;
- cheap kill tests before new sensing/capability complexity;
- persistent agent/runtime separate from replaceable model substrate;
- mutable governed state outside weights;
- enforce high-value authority below prompts when practical;
- training-package/proxy qualification does not qualify the target runtime;
- automate execution, escalate judgment, then resume deterministically;
- canonical history separate from rebuildable projection;
- append-only provenance separate from current routing authority;
- historical retrieval does not automatically become current state.


## Parallel portfolio reconciliation correction

Independent portfolio audit PR #6 was reconciled at exact head `c6df48a080bea2ce952d185694029122f5e2a0b9`.

Accepted additions:
- per-state-family consistency/currentness/write/recovery policy;
- qualification exposure lineage;
- provider capability advertisements;
- essential external dependency -> effective substrate classification;
- capability escalation ladders;
- abstraction-promotion gate.

Held candidate:
- stronger semantic/identity claims incurring a claim-surplus falsification burden.

Fresh currentness correction:
- RepairTracker current observed head: `6b01c2a18035390c050ceecd0506181703d1f5fa`;
- freerowcochkar current observed head: `00562b5fedf5ff636750b87e5ba82dad2911e2ab`;
- meso-crct current observed head: `d1f32c2c3370a5519d62afb78e93d70004529903`.

The older meso-crct donor binding remains historical exact-subject evidence; the current thin main does not revalidate that mechanism.


## Visibility transition donor refresh — 2026-09-23

A later live owner read changed the portfolio from 63/28/35 to 65/46/19. Repositories that are now public may be bound directly even when their README still says "private"; live GitHub visibility controls the current access-state claim.

### BugOps

Status: ADOPT.

Admitted:
- incident evidence is distinct from lifecycle/status tracking;
- correction should stop the obsolete route before apology/explanation;
- acknowledgment is not repair;
- closure requires acceptance/readback evidence and a regression that distinguishes failure from corrected behavior.

Source observed: `thebrazenbeard/bugops@07b8bc90fcb4beb82b1d26b394c730f29c2c425a`.

### Build Team 2.0

Status: ADAPT MECHANISMS ONLY.

Admitted:
- parallel analysts receive the same immutable input snapshot;
- parallel perspectives do not create private memory/authority silos;
- dissent is surfaced before synthesis;
- governance scales with consequence.

Rejected:
- importing named facets or collective identity as Sol identity.

Source observed: `thebrazenbeard/build-team-2.0@9f2743214298f1ae9d424f300a13d37e49e3c74f`.

### CCB Core

Status: ADOPT.

Admitted:
- strict domain/intent admission;
- lease/subscription routing;
- priority ordering and bounded duplicate suppression;
- dead-letter and telemetry accounting;
- heartbeat/projection primitives;
- transport-neutral coordination identity/ledger concepts.

Source observed: `thebrazenbeard/ccb-core@157876c5c0434bf4f553d9e4f70f19076d058146`.

### Conations

Status: ADOPT / PUBLIC REBINDING.

Admitted:
- present choice outranks historical conation;
- recording does not create consent, obligation, authority, promise, or task;
- later evidence revises/contradicts/revokes through append-oriented history;
- absence of later evidence proves neither persistence nor disappearance.

Source observed: `thebrazenbeard/conations@4b458ecf566f024c32109e06a96bf7b2e5f92da6`.

### Deep Memory Storage

Status: ALREADY ADOPTED / PUBLIC REVALIDATION.

Admitted:
- historical evidence plane separate from current governed state;
- retrieval is not admission;
- full canonical ledger union outranks stale convenience indexes;
- CANONICAL_HISTORY does not mean current state;
- query results require explicit nonpromotion semantics.

Source observed: `thebrazenbeard/deepmemorystorage@0740fc188fde6d69d1690ee07ed9be3590ac493f`.

### Empathy

Status: ADAPT.

Admitted:
- direct correction outranks contradicted inference about the speaker's intended meaning;
- self-appraisal can guide behavior without proving phenomenology;
- understanding is not obedience;
- repository source is not runtime effect.

Source observed: `thebrazenbeard/empathy@bc0c1d33b3187642d9e2f0801d1c5bde4f583e2b`.

### Hephaestus

Status: ADOPT.

Admitted:
- schema completion pressure can manufacture false precision;
- UNKNOWN is superior to invented completion;
- qualified template, evolving repository state, and current working context are separate;
- qualification does not imply installation/runtime effect.

Source observed: `thebrazenbeard/hephaestus@7eb30f2777a7d16e4f55ca3066d8ac1e484f79a6`.

### Intranel

Status: ADOPT.

Admitted:
- origin, actor, target, and reply-to are distinct;
- packet identity is distinct from logical operation identity;
- effect classification belongs to the receiver before mutation checks;
- a receipt is evidence about a claim, not self-verifying proof of its effect;
- completed operations need idempotent replay/cancellation semantics;
- canonical payload identity can be digest-bound.

Source observed: `thebrazenbeard/intranel@08bc122043b79422c31a958b7ffe7fff87e5f3f0`.

### Masamune

Status: ADAPT.

Admitted:
- root-cause, evidence, independent-review, and regression disciplines;
- reversible setup necessary to assigned work need not become a redundant permission ceremony;
- real shared-writer collision differs from consequential protected effect.

Source observed: `thebrazenbeard/masamune@0091746bba7740632268fb590ce19512e371f508`.

### Project Achilles

Status: ADAPT.

Admitted:
- fail-closed is a boundary behavior, not a default preference for inactivity;
- current consequence/effect rules outrank frozen training exercises.

Source observed: `thebrazenbeard/project-achilles@6776d8c059e3f9ad791a47a0b62bb56588332968`.

### Temporal

Status: ADOPT / PUBLIC REBINDING.

Admitted:
- chronology is not meaning;
- stable event IDs;
- offset-aware canonical timestamps with optional local preservation;
- deterministic order by timestamp then stable ID;
- elapsed-time arithmetic does not silently reorder endpoints.

Source observed: `thebrazenbeard/temporal@0fc7071a6b01e609fb2cdc76a32c73276ab27094`.

### Vera

Status: ADAPT MECHANISMS ONLY.

Admitted:
- SOURCE_AVAILABLE / BOUND / INSTALLED / RUNTIME_CONSUMED / BEHAVIORALLY_QUALIFIED are orthogonal evidence dimensions;
- current instruction, self-report, live observation, transient activation, and durable state are separate;
- observable activation evidence is preferable to claims about latent hot/cold state;
- source availability does not establish current installation.

Rejected:
- importing Vera identity or release authority into Sol.

Source observed: `thebrazenbeard/vera@87aa888cb7543875ffa11c9c7a1eb9e5b60c35cf`.

### Vera Control Plane

Status: ADOPT MECHANISMS ONLY.

Admitted:
- repository presence and ancestry do not establish current control authority;
- release/source candidate does not establish installation;
- mutable current claims require fresh governed evidence;
- operational control custody can be separate from technical source custody.

Source observed: `thebrazenbeard/vera-control-plane@65ce7908f640ffe53b678ef69c58411a91c23b8a`.

### Explicit non-admissions

- identify-ai: insufficient mechanism surface.
- personification: insufficient mechanism surface.
- project-lantern: insufficient mechanism surface.
- vera-R9A0: predecessor/duplicate lineage only.
- vera-habitat: insufficient mechanism surface.


## F.U.C.K.U.P. Protocol

Status: ADAPT.

Admitted:
- flag the observable mistake before narrating its cause;
- separate immediate calibration from later causal diagnosis;
- turn prevention into concrete guardrails/tests where practical.

Rejected:
- a required single “fundamental root cause” absent supporting causal evidence;
- claims that a preventative guarantees recurrence cannot happen.

Source observed: `thebrazenbeard/fuckup@e999607481ba706523209ce129955a5e3d2d6ef7`.

## Vera Mono

Status: ADAPT MECHANISMS ONLY.

Admitted:
- external donor repositories may remain research/provenance inputs rather than runtime dependencies;
- useful mechanisms can be absorbed into the authoritative codebase while preserving exact donor provenance;
- no cross-repository orchestration is required merely because a mechanism originated elsewhere.

Rejected:
- Vera identity, release authority, or runtime governance as Sol identity/authority.

Additional current-head admissions:
- CAS-headed durable memory rejects stale expected-head writes;
- operation replay is idempotent only when the operation ID carries the same request digest;
- supersession is explicit state, not destructive overwrite;
- authority/privacy references stored with memory are bindings, not self-certifying truth;
- exact-subject authority/temporal evidence may be verifier-issued and single-use;
- unverified precise temporal evidence should degrade to UNKNOWN rather than acquire false precision.

Overlapping coordination/temporal mechanisms revalidate existing Sol rules but are not counted as independent support.

Source observed: `thebrazenbeard/vera-mono@1eec28efc7940bc5a52ef27288eacbfc34b111cc`.
