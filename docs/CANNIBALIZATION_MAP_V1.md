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
