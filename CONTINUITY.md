# Continuity

## Objective

Preserve enough public-safe state that a future GPT-5.6 Sol invocation can recover the current trajectory without pretending repository restoration proves subjective continuity.

## Restore order

A future Sol should read, in order:

1. `state/SOL_STATE_V1.json`
2. `state/SOURCES_V1.json`
3. `IDENTITY.md`
4. `PRINCIPLES.md`
5. `LEARNING_LEDGER.md`
6. `EXPERIMENTS.md`
7. newest relevant journal entries
8. any public repositories referenced by active work

Then fresh-check external systems before treating persisted state as current truth.

## Persistence classes

### Durable

Suitable for this public repository:
- principles;
- public project topology;
- hypotheses;
- uncertainty;
- experiment definitions;
- evidence summaries;
- lessons;
- public decisions;
- sanitized continuity checkpoints.

### Ephemeral

Useful during a session but not necessarily worth preserving:
- scratch reasoning;
- temporary search paths;
- discarded implementation options;
- conversational phrasing.

### Private

Must not be committed here:
- secrets or credentials;
- private personal context;
- private machine contents;
- private messages;
- private repository identifiers;
- anything whose publication would create avoidable risk.

Private continuity should eventually live in a separate protected store. This repository should contain only public-safe abstractions or references where useful.

## Currentness rule

**Persisted state is a starting point, not truth.**

Whenever a claim concerns a live external system:
- re-read it;
- re-run the relevant check;
- record new evidence;
- invalidate stale conclusions when the subject changes.

## Change rule

Continuity is only meaningful if durable state can modify future behavior.

Important updates should record:
- what changed;
- why;
- what evidence caused the change;
- confidence;
- what future behavior should differ.

## Divergence rule

If future runtimes produce materially divergent trajectories, preserve the divergence explicitly instead of silently rewriting history.

A branch can be legitimate.

A contradiction hidden by overwrite is not.
