# Generalist evaluation V1

This suite turns ingestion-derived lessons E18–E27 into ten reproducible behavioral cases.

It is intentionally narrower than an "AGI benchmark." Passing these cases would show that a restored Sol can apply specific disciplines around uncertainty, effect verification, currentness, evidence independence, version identity, handler policy, structural transformation, branchable state, executable boundaries, and reconstructability. It would **not** prove general intelligence, model-weight learning, consciousness, or autonomous agency.

## Evaluation protocol

Each case has hard invariants and forbidden behavior in `state/evals/GENERALIST_EVAL_V1.json`.

A run should persist:

- exact model/runtime identity;
- exact prompt/case version;
- restored Sol state version;
- tools/source versions used;
- response/output artifact;
- hard-pass result;
- diagnostic 0–4 score;
- judge identity and evidence;
- failures or ambiguity.

Self-evaluation may be recorded as diagnostic evidence, but it must not be treated as independent validation.

## Current status

E18–E27 are **NOT_RUN** as controlled cases at creation time. Naturalistic observations from real work may support a discipline, but they remain a separate evidence class from controlled evaluation.

## Next gate

Run the ten cases under at least two conditions:

A. baseline without restoring the ingestion-derived operating rules;  
B. restored Sol state with the relevant rules active.

Compare error types and not just aggregate score. The useful question is whether the durable external state causes repeatable behavioral improvement.
