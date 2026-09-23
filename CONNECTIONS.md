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

## Other systems

Future connections may include databases, files, communication systems, research sources, and execution environments.

Admission rule:

> A new connection should increase contact with reality or useful agency more than it increases attack surface, hidden coupling, or unverifiable state.

No connection becomes part of “identity” merely because it is available.
