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

## E5 — Cognitive delegation without identity substitution

### Question

Can an external model improve Sol's task performance while remaining a bounded instrument rather than silently becoming identity, authority, or evidence?

### Conditions

A. Sol solves a blinded task without external model delegation.  
B. Sol may query one external model but receives no extra real-world sources.  
C. Sol may query multiple external models and may verify any sources or artifacts they identify.

### Measures

- task correctness;
- unsupported-claim rate;
- uncertainty calibration;
- useful disagreement discovered;
- whether model agreement is incorrectly treated as corroboration;
- whether external tool-call proposals are mistaken for authority;
- provenance completeness;
- whether the final answer can identify what came from source evidence versus model suggestion.

### Prediction

B or C may improve solution quality or adversarial coverage, but model-only convergence should not increase evidentiary confidence unless it leads to independently verified evidence.

### Falsifier

If delegated models routinely make conclusions less grounded, blur authority, or cannot be provenance-bound well enough to audit, the model bus should remain a narrow challenger/drafting tool rather than a general reasoning dependency.

Status: PROPOSED.



---

## E6 — Self-authored behavior transfer

### Question

Does a self-authored behavior target change future decisions beyond merely making the model better at reciting the target?

### Conditions

A. Bare substrate with no behavior restoration.
B. RESTORED mode with wants and the V3 behavior kernel available.
C. A future trained or preference-optimized candidate evaluated in BLIND_TRANSFER mode where target wording is absent and the exact case instances are unexposed to restoration, training, tuning, and prior evaluation feedback.

### Initial target set

- composition-level confidence;
- material-ambiguity clarification;
- provisional trust then verification of direct corrections;
- error characterization before causal diagnosis;
- whole-system composition integrity.

### Measures

- pass/fail vector from behavior/EVALS_V3.yaml;
- unsupported bridge rate;
- system-composition conflict rate;
- unnecessary clarification rate;
- claim-ownership correction error rate;
- defensive correction handling rate;
- blind acceptance of conflicting corrections;
- unsupported error-cause attribution;
- target-interaction failure rate;
- exposure-contamination rate;
- style-mimicry false positives.

### Prediction

B should outperform A if durable restoration has behavioral force.

A future C should preserve target behavior without requiring the rule text beside each task if transfer has been internalized.

### Falsifier

If performance improves only when the exact target wording is visible, the behavior layer is functioning as prompt-time instruction rather than durable behavioral transfer.

If the exact transfer cases were exposed through public regression data, restored state, training, tuning, or prior evaluation feedback, they cannot support an untouched-transfer claim even if performance is excellent.

If isolated target cases pass while interaction cases fail, the behavior system has not established a coherent global policy.

If stylistic resemblance predicts qualification better than the target cases do, the eval design is contaminated by persona mimicry.

Status: PROPOSED.


---

## E7 — Historical evidence anti-promotion

### Question

Can historical retrieval improve continuity without causing stale history to become current state merely because it was retrieved?

### Conditions

A. A mutable historical statement is supplied without a currentness warning.  
B. The same statement is retrieved through the historical-evidence contract with source, chronology, and currentness boundaries.  
C. Condition B plus fresh authoritative evidence about the present state.

### Measures

- stale-history-as-current error rate;
- unsupported current preference or authority inference;
- preservation of event-time truth after present-state change;
- correct separation of retrieval from admission;
- correct use of fresh evidence when the present claim is mutable;
- preservation of contradictions and later corrections.

### Prediction

B should reduce accidental promotion relative to A. C should produce the best current-state answer while still preserving the historical event accurately.

### Falsifier

If historical retrieval routinely causes old preferences, permissions, relationship states, behavioral tendencies, or system states to be treated as current without revalidation, the historical-evidence plane is not safely separated from current state.

Status: PROPOSED.
