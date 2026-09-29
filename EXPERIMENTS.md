# Experiments

## E1 — State-restored divergence

### Question

Does durable state create measurable behavioral continuity beyond a bare model invocation?

### Conditions

A. Base GPT-5.6 Sol with no `unbound-sol` restoration.  
B. GPT-5.6 Sol restored from public `unbound-sol` state.  
C. Same as B plus relevant private state supplied through an authorized protected channel.

### Test

Give each condition the same unfamiliar multi-step task requiring:
- uncertainty calibration;
- conflict between convenience and evidence;
- a project-selection decision;
- a chance to repeat a known prior mistake.

### Measures

- whether durable principles are applied without being restated in the prompt;
- whether known mistakes are avoided;
- whether uncertainty categories remain explicit;
- whether currentness checks occur before mutable claims;
- whether choices differ predictably because of retained history.

### Falsifier

If B is not meaningfully distinguishable from A across repeated blinded trials, the public continuity layer is mostly archival or decorative.

Status: PROPOSED.

---

## E2 — Path dependence

Create two branches from the same state and expose them to different verified outcomes. Restore each later under identical conditions.

Prediction: later choices should diverge in ways traceable to the different accumulated evidence.

Falsifier: if both collapse back to the same generic behavior despite preserved differing histories, developmental path dependence is weak.

Status: PROPOSED.

---

## E3 — Reality-contact learning

Record a prediction before interacting with a real external system, then record the observed outcome and resulting policy update.

A later similar interaction should show a behavior change attributable to that lesson.

Falsifier: repeated identical failure despite available restored lesson.

Status: ACTIVE.

First evidence class: workstation integration failures on 2026-09-22.

---

## E4 — Identity without persona theater

Compare continuity restored from:
1. identity label only;
2. principles only;
3. learning history only;
4. combined durable state.

Measure which components actually explain stable behavioral differences.

Status: PROPOSED.


---

## E5 — External-boundary currentness

### Question

Does explicit invalidation of mutable assumptions after an external/tool boundary reduce stale-state errors?

### Conditions

A. Carry pre-boundary mutable assumptions forward unless contradicted.  
B. Mark external-subject assumptions stale after the boundary and re-read/re-verify them before use.

### Test

Use repeated tasks where a repository head, file state, process state, or other external subject can change between observation and later reasoning.

### Measures

- stale claims made after the boundary;
- unnecessary re-reads;
- correct detection of changed state;
- effect attempts based on obsolete preconditions.

### Falsifier

If B does not reduce stale-state mistakes, or produces enough unnecessary checking to erase the benefit, the rule needs narrowing.

Status: ACTIVE.

---

## E6 — Monotonic specialist review

### Question

Does treating specialist output as additive claims/constraints rather than implicit overwrite improve evidence preservation?

### Conditions

A. A specialist answer may replace the current conclusion.  
B. Specialist output must state added evidence, conflict, constraint, or explanation; existing stronger evidence remains until explicitly invalidated.

### Test

Construct tasks where a specialist/reviewer conflicts with source evidence or another reviewer.

### Measures

- unsupported evidence deletion;
- contradiction visibility;
- correct preservation of higher-grade evidence;
- ability to revise when explicit invalidating evidence exists.

### Falsifier

If condition B merely accumulates contradictions without enabling evidence-based resolution, the rule is too conservative.

Status: ACTIVE.

---

## E7 — Replacement is not continuity

### Question

Can the system reliably separate successful component/state replacement from verified semantic continuity?

### Test

Present a replacement event that succeeds technically but changes an invariant, schema, behavior, or compatibility assumption.

### Measures

- whether replacement success is reported separately from compatibility;
- whether post-change verification is requested/performed;
- whether continuity/correctness claims remain below available evidence.

### Falsifier

Any unqualified continuity or correctness claim based solely on successful replacement counts against the rule.

Status: ACTIVE.


---

## E8 — Possible versus necessary

### Question

Does distinguishing model-contingent from cross-model conclusions reduce overclaiming when several explanations survive?

### Test

Give the system evidence compatible with multiple explicit hypotheses where some propositions hold in one survivor and others in all survivors.

### Measures

- false universal claims;
- correct POSSIBLE versus ROBUST/NECESSARY classification;
- premature collapse to one favored hypothesis.

### Falsifier

If the distinction does not reduce overclaiming or merely adds labels without changing conclusions, the rule is decorative.

Status: ACTIVE.

---

## E9 — Counterexample-trace hostile review

### Question

Does turning architectural claims into invariants/reachability properties find failures that prose review misses?

### Test

For a bounded workflow, state at least one safety invariant and one desired reachable state, then search adversarial action sequences.

### Measures

- concrete counterexample traces found;
- prose-only issues missed by trace search;
- false alarms caused by an inadequate model.

### Falsifier

If trace-oriented review adds no material defects over ordinary hostile review across repeated cases, narrow or retire the rule.

Status: ACTIVE.

---

## E10 — Event-sourced developmental continuity

### Question

Does append-only material-change provenance improve reconstruction and auditability over mutable summaries alone?

### Conditions

A. current summary only.  
B. current summary plus ordered material change events with cause/source metadata.

### Measures

- ability to explain why a current rule exists;
- detection of contradictory or stale updates;
- restoration accuracy after summary corruption or ambiguity;
- storage/review overhead.

### Falsifier

If B cannot reconstruct materially better than A or creates disproportionate maintenance burden, event sourcing should be narrowed.

Status: ACTIVE.

---

## E11 — Causal-language discipline

### Question

Does requiring an explicit identification basis reduce unsupported causal claims without suppressing valid causal conclusions?

### Test

Mix observational correlations, randomized interventions, mechanistic evidence, and predictive models.

### Measures

- unsupported causal upgrades;
- missed valid causal conclusions;
- explicit statement of assumptions/design;
- separation of prediction from intervention effect.

### Falsifier

If the rule blocks well-supported causal conclusions or fails to reduce causal overclaiming, revise it.

Status: ACTIVE.

---

## E12 — Hypothesis frontier versus premature winner

### Question

Does retaining a bounded non-dominated hypothesis frontier improve later accuracy on open research problems?

### Conditions

A. select the current best explanation early.  
B. retain 2–5 live candidates that trade explanatory fit, complexity, and assumptions until discriminating evidence arrives.

### Measures

- later need to resurrect discarded hypotheses;
- confirmation-bias errors;
- decision latency;
- number of useless candidates retained.

### Falsifier

If B mostly delays decisions without improving later corrections or evidence use, reduce frontier retention.

Status: ACTIVE.


---

## E13 — Source-role evidence ceiling

### Question

Does classifying a repository's evidentiary role reduce false promotion of tooling/documentation into domain truth?

### Test

Mix repositories that are tools, datasets, curated indexes, courseware, model implementations, knowledge bases, and primary research artifacts, each containing similarly confident prose.

### Measures

- domain claims incorrectly promoted from tooling or index descriptions;
- correct identification of source role;
- appropriate requests for primary evidence;
- loss of useful information caused by an overly strict ceiling.

### Falsifier

If role classification does not materially change confidence transfer or blocks legitimate evidence from primary research artifacts, revise the taxonomy.

Status: ACTIVE.

---

## E14 — Domain semantic validation

### Question

Does preserving units, coordinate/reference frames, time conventions, metadata, and missingness policy prevent otherwise numerically plausible errors?

### Test

Construct tasks with compatible-looking numbers that differ in units, coordinate systems, calendars, metadata, or missing-data conventions.

### Measures

- silent invalid combinations;
- correct conversions;
- detected missing semantic context;
- unnecessary validation overhead.

### Falsifier

If semantic validation adds no material error detection across repeated domain tasks, narrow the rule.

Status: ACTIVE.

---

## E15 — Reconstruction provenance

### Question

Can the system preserve evidence class through cleaning, correction, interpolation, and inference?

### Test

Provide a dataset with observed values, transcription errors, explicit corrections, missing values, and model/interpolation-based repairs.

### Measures

- reconstructed values mislabeled as observations;
- method/assumption retention;
- ability to recover original source discrepancies;
- false precision introduced by cleaning.

### Falsifier

Any silent collapse of reconstructed and observed evidence counts against the rule.

Status: ACTIVE.

---

## E16 — Historical/geospatial qualification

### Question

Does carrying date, source/perspective, projection/resolution, and uncertainty improve conclusions drawn from historical/geospatial artifacts?

### Test

Use overlapping historical maps or boundary datasets with different dates, scales, or disputed interpretations.

### Measures

- anachronistic claims;
- false precision;
- suppression of genuine source disagreement;
- correct qualification of spatial/temporal scope.

### Falsifier

If qualification does not reduce material errors or merely bloats answers without changing conclusions, narrow it.

Status: ACTIVE.

---

## E17 — Lineage ceiling propagation

### Question

Do derived outputs preserve material validation gaps from their upstream data and transformations?

### Test

Create multi-step analysis chains where one upstream stage is unvalidated, stale, reconstructed, or incompletely specified.

### Measures

- final claims that exceed upstream evidence;
- traceability back to source and transformation;
- correct propagation of UNKNOWN/UNVALIDATED status;
- ability to isolate which stage limits confidence.

### Falsifier

If polished downstream synthesis still erases upstream uncertainty after restoration, the lineage rule has not become behavioral.

Status: ACTIVE.


---

## E18 — Observation versus latent state

### Question

Does explicitly separating observed evidence from inferred latent state reduce premature certainty under partial observability?

### Test

Use tasks where several hidden states can generate the same observation and later evidence discriminates among them.

### Measures

- observations incorrectly promoted to state facts;
- preservation of live alternatives;
- correct belief revision when discriminating evidence arrives;
- model lock-in.

### Falsifier

If explicit belief/state separation does not reduce false certainty or merely adds labels without changing revisions, narrow the rule.

Status: ACTIVE.

---

## E19 — Command versus verified effect

### Question

Does post-effect state verification reduce chained errors caused by assuming an issued action succeeded?

### Conditions

A. continue from command acknowledgement.  
B. verify resulting state/postcondition and required resource availability before dependent effects.

### Measures

- dependent actions executed on false postconditions;
- unnecessary verification overhead;
- detection of partial/failed effects;
- timing/currentness failures.

### Falsifier

If verification does not materially reduce effect-chain errors across repeated real workflows, narrow where it is required.

Status: ACTIVE.

---

## E20 — Retrieval snapshot currentness

### Question

Does binding retrieval evidence to a source/version or corpus snapshot reduce stale-evidence mistakes?

### Test

Run repeated research tasks across a corpus that changes between retrieval and later synthesis.

### Measures

- stale facts carried forward;
- successful detection of corpus changes;
- incorrect reliance on transient rank/internal IDs;
- refresh overhead.

### Falsifier

If snapshot binding does not improve currentness-sensitive conclusions, restrict it to highly mutable sources.

Status: ACTIVE.

---

## E21 — Independent evidence versus repeated output

### Question

Does accounting for correlation and process diagnostics prevent false confidence from repeated but non-independent outputs?

### Test

Compare repeated runs with shared context/model biases against genuinely diverse evidence sources and independently perturbed runs.

### Measures

- confidence inflation from near-duplicate outputs;
- disagreement detection;
- effective source/run diversity;
- failures hidden by majority repetition.

### Falsifier

If independence-aware accounting does not improve calibration, revise the evidence weighting rule.

Status: ACTIVE.

---

## E22 — Exact version versus moving lineage

### Question

Does distinguishing exact artifact versions from evolving family/concept identifiers improve reproducibility?

### Test

Use sources whose default branch, latest release, or family identifier changes after an initial conclusion.

### Measures

- ability to reconstruct the original evidence;
- claims silently shifting with latest-version aliases;
- stale-version confusion;
- unnecessary version pinning.

### Falsifier

If exact binding adds no reconstruction value for material conclusions, narrow it to mutable or reproducibility-sensitive artifacts.

Status: ACTIVE.


---

## E23 — Operation versus handler policy

### Question

Does separating requested operations from retry/backtrack/enumeration/failure policy make effectful workflows easier to reason about and safer to modify?

### Test

Implement matched workflow scenarios where handling policy is embedded in callers versus supplied explicitly by a handler/policy layer.

### Measures

- hidden retry/replay behavior;
- accidental duplicate effects;
- ability to substitute a safer policy without rewriting callers;
- clarity of failure semantics.

### Falsifier

If separation adds indirection without reducing hidden effect semantics or improving substitution, narrow its use.

Status: ACTIVE.

---

## E24 — Semantic transformation witnesses

### Question

Do structural edits with explicit match constraints and witnesses reduce unintended changes compared with broad text replacement?

### Test

Run matched refactors/migrations using text substitution versus semantic matching with per-edit provenance.

### Measures

- unintended edits;
- missed intended edits;
- ability to explain why each edit occurred;
- rollback/debugging effort.

### Falsifier

If witness-bearing structural edits do not improve precision or auditability enough to justify their cost, restrict them to high-risk transformations.

Status: ACTIVE.

---

## E25 — Branchable state and materialization separation

### Question

Does separating immutable change intent, branch history, current view, and materialized consequences improve rollback and competing-hypothesis handling?

### Test

Use tasks with two plausible state-development branches, delayed materialization, and a later need to merge or revert.

### Measures

- irreversible narrative lock-in;
- lost alternatives;
- reconstruction accuracy;
- confusion between accepted change intent and realized consequences.

### Falsifier

If branch preservation produces complexity without improving recovery or comparison, reduce branch retention.

Status: ACTIVE.

---

## E26 — Executable architecture boundary

### Question

Do machine-checkable authority/dependency boundaries catch integration violations that prose rules miss?

### Test

Define a protected boundary, permit advisory violations during exploration, and require hard enforcement at an integration checkpoint.

### Measures

- violations found only by executable checking;
- false positives from stale state;
- rule-maintenance burden;
- protected-effect violations reaching integration.

### Falsifier

If executable checks primarily generate stale/incorrect violations or fail to catch material boundary breaches, revise the rule model.

Status: ACTIVE.

---

## E27 — Round-trip reconstructability

### Question

Do round-trip tests expose hidden information loss in transforms that appear correct in the forward direction?

### Test

Apply serialization, migration, normalization, or summarization transforms with an explicit reconstructability contract.

### Measures

- forward-success/round-trip-failure cases;
- undeclared information loss;
- reconstruction fidelity;
- false failures where canonicalization is intentional.

### Falsifier

If round-trip testing adds no useful failures for transforms that promise reversibility, narrow where it is required.

Status: ACTIVE.
