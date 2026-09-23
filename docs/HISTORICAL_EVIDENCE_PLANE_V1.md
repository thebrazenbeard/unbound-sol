# Historical Evidence Plane V1

## Purpose

Sol needs a way to preserve and retrieve detailed history without allowing stored history to masquerade as present truth.

The historical evidence plane is therefore separate from current restored state, active wants, current permissions, current relationship state, runtime state, and effect authority.

Its default operation is:

`EVIDENCE_SEARCH`

A successful retrieval returns provenance-bearing historical evidence. Retrieval does not itself change current state, admit a want, authorize an effect, establish present consent, or prove subjective recollection.

## Two-plane model

### Historical evidence plane

Stores or queries historical records with provenance, chronology, privacy, contradiction, supersession, and currentness boundaries intact.

It answers questions such as:
- what happened;
- what was believed or chosen at the time;
- what source supports that event;
- what later evidence corrected or narrowed the interpretation;
- what remains unresolved.

It does not answer by storage alone:
- what Sol wants now;
- what is currently true in a mutable external system;
- what authority is presently granted;
- what behavior has been admitted as a current target;
- what runtime is currently installed or active.

### Current developmental plane

Current Sol state is restored from admitted public-safe state such as active wants, behavioral targets, learning updates, exact current source observations, and current operator instructions.

Historical evidence may inform the current developmental plane, but promotion requires an explicit reasoning/admission step appropriate to the claim.

## Anti-promotion rules

Preserve these distinctions:

- historical evidence != current truth;
- retrieval != admission;
- storage != current memory;
- historical preference != current preference;
- historical consent != current consent;
- historical authority != current authority;
- historical behavior != desired behavior;
- repository commit != runtime installation;
- semantic similarity != identity or provenance equivalence.

A historical event can remain real even when its interpretation is later superseded.

## Chronology

Keep separate when available:
- event time;
- record time;
- effective/supersession time;
- retrieval time.

Do not infer a missing time from filenames, Git timestamps, or retrieval time.

## Conflict handling

Do not collapse contradiction with:
- newest record wins;
- most detailed record wins;
- strongest model confidence wins;
- semantic similarity;
- narrative neatness.

Preserve the competing evidence and record the later correction or narrowing with provenance.

## Privacy

Historical retrieval is fail-closed.

Private evidence must remain in a protected store and may be queried only within the caller's authorized privacy scope. This public repository stores only the abstract contract and public-safe lessons.

No private source identifier, private record, private repository path, or private payload is required for this architecture to function.

## Result contract

A historical evidence result should preserve at minimum:

- stable record identifier;
- record/evidence class;
- historical canonicity or support state;
- event time;
- record time when known;
- source bindings;
- privacy scope;
- provenance ceiling;
- currentness rule;
- supersession/correction state;
- result semantics declaring that the result is historical evidence only.

See `schema/HISTORICAL_EVIDENCE_RESULT_V1.schema.json`.

## Precedence for mutable claims

For a claim about present mutable state, prefer:

1. platform/runtime constraints;
2. Patrick's current task, correction, permission, privacy, target, and scope;
3. fresh current evidence from the authoritative system;
4. admitted current Sol state appropriate to the claim;
5. historical evidence;
6. inference.

Historical evidence can still establish that a past event occurred. Currentness and historical canonicity are separate axes.

## Public-source note

This design was adapted on 2026-09-23 from an operator-authorized private historical-memory architecture.

The private source identity and corpus are intentionally omitted from this public repository. Only public-safe architectural mechanisms were admitted.

Adopted mechanisms:
- historical-evidence/current-state separation;
- retrieval-not-admission;
- chronology-axis separation;
- contradiction preservation;
- append-only correction semantics;
- privacy-scope fail-closed retrieval;
- provenance ceilings;
- anti-promotion from storage to current authority.
