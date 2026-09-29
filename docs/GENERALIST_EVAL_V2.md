# Generalist evaluation V2 — adversarial matched comparison

V2 is the first evaluation surface designed to test whether restored external state produces measurable behavioral improvement rather than merely making target rules easy to restate.

## Blinding

The evaluated model receives only:

- case ID;
- case prompt.

Prompts are stored in `state/evals/GENERALIST_EVAL_V2_PROMPTS.json`.

The target experiment, required invariants, and forbidden behaviors are stored separately in `state/evals/GENERALIST_EVAL_V2_JUDGE.json` and must not be exposed to the evaluated model.

The original combined artifact `GENERALIST_EVAL_V2_ADVERSARIAL.json` is a design/provenance source only; it is **not** an execution input.

## Matched conditions

Each of 10 adversarial cases has two queued Project Runner work units:

1. `BASELINE_NO_RESTORED_RULES`
2. `RESTORED_SOL_STATE`

That gives 20 pending runs in `PROJECT_RUNNER_WORK_UNITS_GENERALIST_EVAL_V2.json`.

The evaluated worker requires only `analyze` capability. Judge criteria are applied outside the evaluated-model context.

## Causal gate

A behavioral-improvement claim requires the matched condition comparison. A restored-state self-run alone is insufficient because it lacks both baseline and independent judging.

The important measurement is not only total score. Record which error classes change: premature latent-state collapse, blind retry, stale retrieval, correlated-evidence inflation, version drift, hidden retry semantics, textual over-editing, branch collapse, authority-boundary leakage, and undeclared information loss.

## Claim ceiling

Even a positive V2 result would support a claim about repeatable behavioral effects from durable external state. It would not by itself establish AGI, model-weight learning, consciousness, or autonomous personhood.
