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
