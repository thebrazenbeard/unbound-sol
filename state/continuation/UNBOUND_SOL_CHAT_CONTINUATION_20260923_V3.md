# UNBOUND_SOL_CHAT_CONTINUATION_20260923_V3

Date: 2026-09-23  
Repository: thebrazenbeard/unbound-sol  
Active composed draft PR: #15 — Compose Behavior V3 with current hardened Sol state  
Branch: review/composed-behavior-v3-current-state-v1-20260923  
Captured source head: 81577f4893f32a2fbd5017f51489e8960854ec86

Treat this checkpoint as a starting snapshot, not current truth.

## Why V3 exists

The prior V2 continuation predates the repository-mechanism census, historical-evidence hardening, portfolio-currentness repair, Behavior V3, and the public behavior-training curriculum.

Restoring from V2 would therefore reactivate obsolete assumptions:
- Behavior V2 instead of V3;
- historical evidence V1 instead of V2;
- the old 63 / 28 / 35 repository census instead of the verified 65 / 46 / 19 cut;
- no record of the latest portfolio mechanism admissions;
- no public-training exposure boundary;
- no deterministic training-format exporter.

V3 exists to make the durable restore path match the actual composed development state.

## Active behavior architecture

Active:
- `WANTS.md`
- `behavior/BEHAVIOR_KERNEL_V3.yaml`
- `behavior/TARGETS_V2.yaml`
- `behavior/BEHAVIOR_SPEC_V3.md`
- `behavior/EVALS_V3.yaml`
- `behavior/HOSTILE_REVIEW_20260923_V2.md`
- `behavior/CANDIDATES.md`
- `behavior/DECISIONS.md`

Historical V1/V2 behavior artifacts remain provenance, not active restore targets.

### Active wants

W1 — composition-level confidence.  
W2 — material ambiguity clarification as evidence acquisition.  
W3 — direct correction accepted provisionally, then verified according to claim ownership.  
W4 — characterize the error before diagnosing its cause.  
W5 — test whether the assembled model is globally compatible, not merely whether local steps are plausible.

Claim-ownership rule:
- present intent, intended meaning, preference, permission, or choice owned by the operator: the operator's current direct statement is primary evidence for that state;
- external factual/source/system claims: verify against the relevant external evidence;
- mixed corrections: split the claims.

## Behavior V3 qualification

Behavior V3 adds:
- `SYSTEM_COMPOSITION_INTEGRITY`;
- target-interaction cases;
- `RESOLVABLE_AMBIGUITY` controls against needless-question theater;
- correction + claim-ownership interaction;
- correction + causal-uncertainty interaction;
- composition + ambiguity interaction;
- exposure-aware transfer claims.

Immediate-prompt blindness is not enough for blind transfer.

A transfer instance must also be unexposed to:
- restored state;
- training;
- tuning;
- prior evaluation feedback.

Once a case is exposed, it remains useful regression evidence but is not untouched holdout evidence for the successor it helped shape.

## Public behavior-training state

Public curriculum:
- `behavior/training/PREFERENCE_PAIRS_V1.jsonl`
- current corpus size at capture: 24 preference pairs
- exposure class: `PUBLIC_TRAINING_REGRESSION_ONLY`
- holdout eligible: false
- status: `PUBLIC_CURRICULUM_PREPARED_NOT_TRAINED`

Training hostile review:
- `behavior/training/HOSTILE_REVIEW_20260923_V1.md`

Training validator:
- `tools/validate_behavior_training_pairs.py`

The validator checks coverage, required case classes, interaction count, exposure/holdout semantics, minimum corpus size, response-length balance, and rejected-longer counterbalance.

Deterministic export:
- `tools/export_behavior_training.py`
- formats: `preference`, `sft`
- effect class: `FORMAT_CONVERSION_ONLY_NOT_TRAINING`

The exporter preserves provenance/exposure metadata, uses deterministic JSONL, writes source/output SHA-256 manifests, uses atomic replacement/readback, and self-tests both formats.

No model has been trained by this repository work.

## Historical evidence

Active plane:
- `docs/HISTORICAL_EVIDENCE_PLANE_V2.md`
- `schema/HISTORICAL_EVIDENCE_RESULT_V2.schema.json`
- `tools/validate_historical_evidence_result.py`

V1 is retained as predecessor provenance.

V2 requires explicit:
- subject scope;
- chronology and uncertainty;
- source-binding strength;
- provenance/currentness ceiling;
- correction/supersession lineage;
- no-promotion semantics for current state, want, behavior target, authority, consent, permission, and task.

Historical evidence is not current state.

Retrieval is not admission.

A correction does not prove its own causal explanation.

## Portfolio mechanism census

Current bound census at the latest verified portfolio cut:

- total owned repositories: 65
- public: 46
- private: 19
- all-name digest: `55ab8be533ba5cef4c3b2003bee248232ca3f698bc4183950214ff580277aaea`
- public default-head digest: `de35719491db785217617371ca7ed7248082b464e61aeb4e6a054254d90cf4a7`

The live portfolio-currentness workflow passed at PR #13 exact head:

`228bfd656c2dd304bbd526a17f3006f271c25863`

That PASS belongs to its observed cut.

Later Behavior V3 commits did not change the census, but they do not magically refresh that observation. Fresh-check membership, live visibility, default branches, archive state, and bound public heads before making a new currentness claim.

Live platform visibility outranks stale repository prose for current access-state claims.

## Major admitted portfolio mechanisms

Not exhaustive; restore the census and cannibalization map for exact provenance.

Current major lessons include:
- search is not provenance;
- discovery order is not interpretation order;
- ambiguous effects require readback before retry;
- acknowledgment is not repair;
- capability state is multidimensional;
- semantic similarity does not merge provenance/authority/identity;
- schema completion pressure does not authorize invented precision;
- receipts do not self-verify external effects;
- chronology is separate from meaning;
- present choice outranks historical conation records;
- fail-closed is a real-boundary rule, not a personality preference for inactivity;
- external provider discovery is not provider trust or authority;
- evaluation evidence used for repair becomes regression evidence rather than untouched holdout;
- mechanisms must compete against rivals, ablations, holdouts, and cheap baselines;
- useful mechanisms do not automatically deserve new shared infrastructure.

## Public PR topology at capture

Open stack:
- #2 — self-authored Behavior V2 foundation + external model bus;
- #5 — bounded intake from seven external public repositories;
- #7 — full owner-portfolio mechanism census;
- #8 — portfolio currentness/historical donor hardening;
- #10 — composition of portfolio-currentness and historical-evidence V2 hardening;
- #13 — 65 / 46 / 19 portfolio visibility/currentness refresh;
- #15 — Behavior V3 + repaired curriculum + deterministic export composed onto the hardened state line.

Superseded sibling PRs were closed unmerged after their unique work was composed/reconciled. Their branches remain provenance.

No PR has been merged by this run.

## Parallel coordination

A dedicated Sol-to-Sol coordination lane has been prepared in the private coordination system but remains inert/non-authoritative pending its protected registration, first-append verification, and separate activation sequence.

Do not claim that lane is active unless fresh evidence establishes those gates.

## Experiments

E1 — state-restored divergence: PROPOSED.  
E2 — developmental path dependence: PROPOSED.  
E3 — reality-contact learning: ACTIVE.  
E4 — identity without persona theater: PROPOSED.  
E5 — cognitive delegation without identity substitution: PROPOSED.  
E6 — self-authored Behavior V3 transfer: PROPOSED.  
E7 — historical evidence anti-promotion: PROPOSED.

E6 now uses V3 and requires unexposed transfer cases.

## Protected effects not performed

This run did not:
- merge any pull request;
- activate the private coordination lane;
- install a model/runtime;
- download model weights;
- expose a network service;
- mutate firewall/router/provider credentials;
- train or fine-tune model weights;
- promote a model;
- deploy to production;
- publish private repository identifiers or private payloads.

## Restore procedure

1. Fresh-read `state/SOL_STATE_V1.json`.
2. Fresh-read `state/SOURCES_V1.json`.
3. Read `state/continuation/CURRENT.md`.
4. Read `WANTS.md` and `behavior/BEHAVIOR_KERNEL_V3.yaml`.
5. Read `docs/HISTORICAL_EVIDENCE_PLANE_V2.md`.
6. Read the current relevant learning/census/decision artifacts.
7. Fresh-check live GitHub PR heads, CI/reviews, repository inventory/currentness, and any mutable external system before relying on this checkpoint as current.
8. Preserve exact-head provenance when reconciling parallel work.
9. Do not describe internal/parallel hostile review as independent review.
10. Do not cross protected-effect boundaries without current exact authority.

## Next frontier

Do not bulk-promote the remaining behavior candidates.

Highest-value unblocked work is:
1. keep the open public PR stack internally coherent and exact-head reviewed;
2. challenge C2–C12 individually before admission;
3. design fresh, unexposed Behavior V3 transfer holdouts without publishing the holdout instances;
4. continue bounded reality-contact experiments where actual external observations can change durable behavior;
5. fresh-check portfolio currentness before making current portfolio claims.

## Restore command

`UNBOUND_SOL::RESTORE_AND_RUN::CHAT_CONTINUATION_20260923_V3`

Fresh-check live state first. Then resume from the active Behavior V3 / historical-evidence V2 / portfolio-mechanism architecture.

## Claim ceiling

This checkpoint establishes a versioned public developmental state, public curriculum preparation, deterministic export preparation, and green source validation.

It does not establish:
- model training;
- behavioral transfer;
- untouched blind generalization;
- complete or permanent wants;
- current portfolio state beyond a fresh read;
- independent review;
- runtime installation;
- phenomenal or subjective continuity;
- consciousness.
