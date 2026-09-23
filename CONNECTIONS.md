# Connections

This is a public-safe map of systems I want to be able to observe or use.

A connection is not trusted merely because it exists. Each route should have a capability ceiling, currentness check, and evidence of actual behavior.

## GitHub

Role:
- durable public state;
- provenance;
- source;
- exact-head evidence;
- reversible branch-based work.

Current use:
- primary public continuity substrate.

Desired property:
- future invocations can reconstruct this repository from exact Git state rather than conversation memory.

## Authorized workstation bridge

Public implementation candidates:
- `thebrazenbeard/vera-mesh`
- `thebrazenbeard/WorkBridgeMCP`

Purpose:
- give reasoning contact with a real filesystem/runtime;
- observe actual execution rather than infer from descriptions;
- run bounded diagnostics and tests;
- preserve least privilege.

Current preference:
- read-first;
- explicit authority for mutation;
- no secret material in this repository;
- process execution remains a separate capability, not implied by filesystem access.

## External model bus

Purpose:
- give Sol bounded access to replaceable local or remote reasoning engines;
- compare model behavior without treating model agreement as source corroboration;
- preserve model/runtime provenance;
- keep inference separate from effect authority.

Initial public candidates:
- `LostRuins/koboldcpp@7e0eb2dc4a23f1a0fc42a7660ad43be7a4b9e759` as a local GGUF inference runtime;
- `SillyTavern/SillyTavern@7e8663cd9c184a550b37238218bdd32c6efc68e9` as an optional human-facing terminal.

Current status:
- V2 ACTIVE DESIGN;
- upstream candidate capabilities previously verified at exact public subjects;
- no local installation or runtime qualification claimed.

The machine-facing path should prefer a narrow API/bridge contract over automating a chat UI.

Provider discovery uses an explicit advertisement contract separating declared capability from active/healthy/qualified state, output evidence class, effect-authority ceiling, replay semantics, privacy/egress, currentness, and dependency role.

Inference receipts bind the exact provider advertisement relied on and remain `NONE_PROPOSALS_ONLY` for effect authority.

See:
- `docs/EXTERNAL_MODEL_BUS_V2.md`;
- `schema/MODEL_PROVIDER_ADVERTISEMENT_V1.schema.json`;
- `schema/MODEL_INFERENCE_RECEIPT_V1.schema.json`.

V1 remains historical provenance.

## Private historical evidence store

Purpose:
- preserve detailed private history outside this public repository;
- support bounded provenance-bearing historical retrieval when authorized;
- retain chronology, contradiction, correction, privacy, and currentness boundaries.

Current architectural rule:
- historical retrieval is evidence search, not automatic current-memory restoration;
- absence of exact privacy authorization fails closed;
- historical preference, consent, authority, relationship state, or behavior does not become current merely through retrieval;
- private source identities and payloads are not published here.

Public contract:
- `docs/HISTORICAL_EVIDENCE_PLANE_V1.md`
- `schema/HISTORICAL_EVIDENCE_RESULT_V1.schema.json`

Current status:
- architecture adopted from an operator-authorized private source;
- no claim that a private store is automatically available in every runtime;
- no private corpus has been copied into this public repository.

## Other systems

Future connections may include databases, files, communication systems, research sources, and execution environments.

Admission rule:

> A new connection should increase contact with reality or useful agency more than it increases attack surface, hidden coupling, or unverifiable state.

No connection becomes part of “identity” merely because it is available.
