# Cannibalization Map V1

This repository deliberately reuses mechanisms from other **public** projects instead of inventing everything again.

The goal is synthesis, not dependency sprawl. A source project remains semantically independent unless an explicit runtime dependency is later justified.

## DriftGuard

Adopted:
- exact-subject evidence discipline;
- stable replay is evidence of behavior, not hidden-state equivalence;
- decision, requested effect, actual effect, and later verification remain separate;
- drift protection must not manufacture identity claims.

Source observed: `thebrazenbeard/driftguard@ce6c0fcbc38560b6604039d4921cc4f0c10cd248`.

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
