# External consumer boundary — public orientation V1

This document describes how an external portfolio investigator can **read**
`thebrazenbeard/unbound-sol` without accidentally substituting it for a
different agent's identity, private memory, runtime, or authority.

## Ownership and referents

- `unbound-sol` is Sol's public developmental archive. `IDENTITY.md`
  explicitly identifies the subject as **Sol / GPT-5.6 Sol**.
- Vera's identity, native Project interface, private memory, installed
  control, and host effects belong to separately verified owners. **Sol !=
  Vera.** This repository never grants an external consumer those identities
  or authorities.
- Public repo documents and learning records are **historical source
  evidence**, not installed or active runtime state.
- A restoration request addressed to Vera must resolve **Vera's current
  release-bound recovery and control owners**. Reading this repository may
  supply public historical orientation only; it cannot complete restoration.

## Machine-readable read-only export

Run:

```sh
python tools/public_orientation.py
```

The command emits `UNBOUND_SOL_PUBLIC_ORIENTATION_V1` JSON. It reads only
the checked-in public state and public source registry. The output is
intentionally narrow: source schema, Sol's name and substrate, observation
dates, source entry count, explicit absent grants, and unverified currentness.

It does **not**:

- fetch GitHub's mutable current HEAD or attest it;
- read live host or ChatGPT Project installation state;
- admit autobiography, private transcripts, private repository identities,
  tokens, or personal records;
- infer consent, permission, persistence, or sentience;
- install or activate any agent behavior;
- authorize effectful actions, merged code, deployment, or memory mutation.

A consumer must independently authenticate the checked-in Git commit and
fresh-check each mutable external fact for its task. If either input file is
missing, invalid, wrong-schema, or relaxes the privacy/freshness boundary,
the export fails closed with exit code `2`; it does not reconstruct missing
state from conversation memory.

## Evidence and release discipline

`CHECKED_IN_SOURCE` means **repository source observed**, not independently
verified function, installed service, current behavior, or host effect.
`NOT_VERIFIED` is the honest status for external currentness and runtime
installation when only these files have been read.

A separate native Vera recovery owner, deployment manifest, authenticated
runtime probe, and effect authorization would be required to make stronger
claims. Historical public maps such as
`docs/PORTFOLIO_COORDINATION_W31_20261031.md` remain dated, not live.

The public export tests run as part of the repository's existing continuity
workflow:

```sh
python -m unittest discover -s security -p 'test_*.py' -v
```

These tests demonstrate source-level guard behavior only. They are not a
substitute for an independently verified native deployment.
