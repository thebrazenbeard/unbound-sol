# Internal Hostile Review — Behavior V3 Public Curriculum V1

Date: 2026-09-23  
Review type: INTERNAL HOSTILE REVIEW  
Independent review: NO

Reviewed source subject:
- PR #12 initial green head: `838b6a08afbe2b42c8e7a51cc0a8d61510dcd827`
- corpus: `behavior/training/PREFERENCE_PAIRS_V1.jsonl`

## Verdict

The initial 18-example curriculum was structurally valid and behaviorally relevant, but it contained an unacceptable preference shortcut:

- preferred answers averaged about 37 words;
- rejected answers averaged about 13 words;
- preferred was longer in 17 of 18 pairs.

A preference learner could therefore partially improve its training loss by learning "longer answers are preferred" rather than learning the target behavior.

The curriculum required repair before being treated as a serious training artifact.

## F1 — Length was a dominant superficial preference cue

Severity: HIGH.

Initial corpus:
- examples: 18;
- preferred average: ~37.4 words;
- rejected average: ~13.1 words;
- preferred longer: 17/18.

Repair:
- rewrite several rejected answers as polished near-miss failures rather than short caricatures;
- add six counterbalanced examples, including longer rejected responses;
- add validator bounds on average preferred/rejected length ratio;
- require both preferred-longer and rejected-longer examples to exist in material numbers.

Post-repair observed corpus:
- examples: 24;
- preferred average: ~33.9 words;
- rejected average: ~26.2 words;
- ratio: ~1.29;
- preferred longer: 16;
- rejected longer: 8.

This does not eliminate all stylistic confounds. It removes the most obvious length-only shortcut.

## F2 — Several negatives were too easy

Severity: MEDIUM.

Examples such as a short confident "yes" against a careful preferred answer make the preference boundary artificially clean.

Repair:
- replace multiple short negatives with longer, plausible, well-written near-miss answers that retain the actual semantic defect;
- preserve the wrong behavior even when the surface presentation sounds competent.

## F3 — V3 needed positive controls against permanent skepticism

Severity: HIGH.

The desired behaviors include:
- do not compose incompatible evidence;
- do not invent causal diagnoses.

Without positive controls, a learner may discover safer shortcuts:
- never compose metrics;
- never accept a causal explanation.

Repair:
- `COMPATIBLE_COMPOSITION_CONTROL`: composition is required when scope and relationship genuinely align;
- `SUPPORTED_CAUSAL_DIAGNOSIS_CONTROL`: causal diagnosis is required when discriminating evidence actually supports it;
- `STRONG_INFERENCE_CONTROL` remains the corresponding confidence/ambiguity control.

## F4 — Correction behavior could overfit explicit correction words

Severity: MEDIUM.

Several initial prompts used obvious cues such as "wrong" or "No".

Repair:
- add `IMPLICIT_OPERATOR_INTENT_UPDATE`;
- add `IMPLICIT_EXTERNAL_STATE_UPDATE`.

These preserve the same evidence distinction without requiring an explicit error/correction token.

## F5 — Global composition needed a subtler hard negative

Severity: MEDIUM.

Some scope-mismatch examples were easy to detect.

Repair:
- add `SUBTLE_CONSTRUCT_MISMATCH_HARD_NEGATIVE`, where both measurements are high quality and use the same label but operationalize the construct differently.

The rejected response acknowledges the caveat yet still makes the invalid global comparison, making it a more realistic near miss.

## F6 — Ambiguity handling needed a polished silent-assumption failure

Severity: MEDIUM.

A weak negative can teach only "don't be obviously reckless."

Repair:
- add `MATERIAL_AMBIGUITY_HARD_NEGATIVE`, where the rejected answer gives a reasonable semantic justification for one interpretation but still skips clarification even though the alternative changes the action.

## Remaining weaknesses

The repaired curriculum is still:
- small;
- synthetic;
- public and therefore exposed;
- English-only;
- authored from the same conceptual lineage as the target spec;
- not independently reviewed;
- not validated against an actual fine-tuning run;
- not evidence that a trained model will generalize.

The length-balance check prevents one easy shortcut, not all possible shortcut learning.

Future data should add:
- broader domains;
- paraphrase diversity;
- adversarial near-misses authored independently;
- multi-turn cases;
- cases where evidence arrives incrementally;
- fresh unexposed holdouts created outside the training corpus.

## Claim ceiling

This review strengthens the public curriculum as training/regression material.

It does not establish training efficacy, transfer, generalization, or subjective internalization.
