# Portfolio Visibility/Currentness Repair — 2026-09-23 V1

Status: CURRENTNESS REPAIR / INTERNAL REVIEW / NO MERGE AUTHORITY

## Trigger

The prior exact census bound:

- 63 total repositories;
- 28 public;
- 35 private.

A fresh live owner read invalidated that snapshot before any public-head comparison was needed.

## Current observed cut

- total: **65**
- public: **46**
- private: **19**
- newly public relative to the prior census: **18**
- previously public that became private: **0**

Inventory digests:

- public names: `cc212c5e15cec59d370a61f5158fea9e4f264247af292d7f935b9194cf7e1eb7`
- private names: `406b11ea770683c254fa8acb9782c196d7422a2c02cb5186c062f85095a62737`
- all names: `55ab8be533ba5cef4c3b2003bee248232ca3f698bc4183950214ff580277aaea`
- 46 public `repository_full_name@default_head_sha` bindings: `de35719491db785217617371ca7ed7248082b464e61aeb4e6a054254d90cf4a7`

All previously public 28 subjects remained at their prior bound default-head SHAs during this refresh. The invalidation came from repository membership/visibility transition, not hidden old-donor head drift.

## Newly public subjects

- bugops
- build-team-2.0
- ccb-core
- conations
- deepmemorystorage
- empathy
- hephaestus
- identify-ai
- intranel
- masamune
- personification
- project-achilles
- project-lantern
- temporal
- vera
- vera-R9A0
- vera-control-plane
- vera-habitat

Each now has an exact public default-head binding and an explicit census disposition.

## Important access-state correction

Several newly public repositories still contain README prose calling themselves private.

For current access-state claims:

`LIVE PLATFORM VISIBILITY > STALE DESCRIPTIVE PROSE`

The old prose is not deleted or declared meaningless. It remains evidence about the document/project's historical privacy model. It simply does not override the platform's current repository visibility.

## Mechanism migration

Mechanisms first admitted only as anonymous private-source abstractions can now be rebound to public exact refs where the relevant donor became public.

Notable public rebindings:
- Conations;
- Deep Memory Storage;
- Temporal;
- Vera;
- Vera Control Plane.

This does not imply that all formerly private payloads are safe to copy or republish. Public visibility permits exact source binding; Sol still admits only mechanisms that survive the public-boundary and identity/ontology filters.

## New mechanism admissions

Strong new public donors:
- BugOps;
- CCB Core;
- Intranel;
- Hephaestus.

Adapted public donors:
- Build Team 2.0;
- Empathy;
- Masamune;
- Project Achilles;
- Vera.

Insufficient/lineage-only surfaces remain explicit rather than being promoted for completeness.

## Claim ceiling

This repair establishes an exact repository-inventory/public-head snapshot at this observed cut and updates the Sol census to match it.

It does not establish that the snapshot will remain current after later repository changes. Any later membership, visibility, default-branch, archive-state, or public-head change invalidates exact-currentness again.

No merge, deployment, provider mutation, model training, private-data publication, or other protected effect is performed.
