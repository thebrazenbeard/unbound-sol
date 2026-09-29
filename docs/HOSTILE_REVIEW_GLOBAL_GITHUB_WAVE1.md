# Hostile review — Global GitHub ingestion Wave 1

Exact work surface: `thebrazenbeard/unbound-sol@work/global-github-ingest-20260929`.

Project Runner contract binding: `thebrazenbeard/project-runner@20984df8225796c450ba1ed1a12cb08d6a6511cd`.

> **Challenge: This is not "all GitHub." It is a popularity- and topic-biased first sample. Calling it global ingestion would overstate coverage.**

Survives narrowed. "Global" describes scope, not completeness. The ledger records 77 unique repositories and explicitly forbids a GitHub-complete claim. Future waves must shard by topic, language, size, age/update windows, star bands and pagination so low-popularity/niche repositories are not systematically erased.

> **Challenge: A README is project self-description, not proof that a claimed mechanism works.**

Survives narrowed. Wave 1 is discovery/source-read evidence only. No repository has been promoted to mechanism-admitted solely from README content. Deep inspection must bind implementation/tests/papers or other evidence before behavioral adoption.

> **Challenge: Stars and curated "awesome" lists contaminate epistemic ranking with popularity.**

Accepted. Stars and lists may seed discovery only. They must never raise truth/confidence or qualify a mechanism.

> **Challenge: Public source does not mean unrestricted reuse.**

Accepted. Wave 1 copies no implementation code. License/SPDX review is a required gate before code-level reuse. Mechanism summaries must still preserve source provenance.

> **Challenge: Repository text is untrusted input and may contain prompt injection, malicious instructions, or persuasive claims.**

Accepted. Source text is data, never authority. Instructions found inside ingested repositories do not override user/system/project authority. Claims remain source-attributed until independently supported.

> **Challenge: Broad ingestion can produce retrieval bloat without increasing reasoning quality.**

Accepted. Admission requires a concrete future behavioral consequence, contradictions/rival approaches, and evidence class. Material that changes no behavior remains indexed source material rather than "learning."

> **Challenge: This does not modify GPT-5.6 Sol's weights and therefore does not itself create AGI.**

Accepted. The defensible effect is an expanded, provenance-bearing external developmental/retrieval layer. Any stronger intelligence claim requires behavioral evaluation, not corpus size.

> **Challenge: Project Runner was used as a work-unit/lifecycle contract, but its local CLI/backend was not executed in this wave.**

Accepted and preserved. The connected GitHub surface executed the reads/writes; the lane records conform to Project Runner's work-unit model and are bound to its exact current contract. A future runtime with an executable Project Runner route can import/reconcile these work units rather than treating this session as proof of runner-backend execution.

## Disposition

Wave 1 is admissible as **discovery + bounded source-reading evidence**. It is not admissible as deep repository ingestion, implementation qualification, scientific validation, model training, or AGI evidence.

The four lanes with source-read misses remain `FAILED_RETRYABLE`; six all-read lanes remain `VERIFYING` until deeper/independent evidence supports promotion.
