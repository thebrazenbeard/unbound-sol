# External Mechanism Intake — 2026-09-23 V1

Status: ACTIVE RESEARCH / NOT MERGED

Purpose: inspect external public repositories for mechanisms that improve unbound-sol without importing their entire product surface or confusing implementation novelty with architectural value.

Classification:
- ADOPT — mechanism is directly admitted into unbound-sol architecture.
- ADAPT — mechanism is admitted in modified form.
- ALREADY_PRESENT — useful mechanism confirms an existing design but adds no new architectural requirement.
- CANDIDATE — worth further study before admission.
- REJECT — do not adopt the mechanism as-is.

## mukul975/postgres-mcp-server

Exact observed head:
`00904ca42bf8f18fce2e2108e641bc4854f056fb`

Useful source properties:
- very broad PostgreSQL observability/diagnostic catalog;
- connection pooling;
- structured tool outputs;
- explicit separation between query and non-query execution helpers.

Decision: ADAPT.

Admitted:
- diagnostic-first database introspection as a reusable capability class;
- structured database observations rather than unstructured shell scraping;
- pooled database access for repeated observation workloads.

Rejected as a default pattern:
- exposing hundreds of mutation/admin tools as one undifferentiated model surface.

Reason:
A large tool catalog improves reach but increases authority confusion, selection ambiguity, and blast radius. unbound-sol should prefer small capability envelopes that can be widened deliberately.

## Zlash65/postgresql-ssh-mcp

Exact observed head:
`2a350d45d464820df349c9b21cb178dcb74cc230`

Useful source properties:
- read-only by default;
- write capability enabled explicitly;
- one SQL statement at a time;
- parser-aware rejection of hidden write paths such as SELECT INTO, data-modifying CTEs, CALL/DO, and EXPLAIN ANALYZE on mutating statements;
- bounded result rows, query timeout, and concurrency;
- separate transport concerns for STDIO/HTTP/SSH;
- strict host-key verification with configurable trust-on-first-use;
- connection/tunnel health exposed as observable state.

Decision: ADOPT / ADAPT.

Admitted:
- observation/read-only capability should be the default database envelope when possible;
- mutation should be a separately authorized capability, not an accidental property of query access;
- resource envelopes belong in capability definitions: row cap, timeout, concurrency, retry budget;
- effect filtering must inspect semantic escape paths, not just first-token allowlists;
- transport trust and database authority are separate concerns.

Modification:
Do not treat TOFU as equivalent to pre-established trust. Record which trust mode established the connection.

## tensorchord/pgvecto.rs

Exact observed head:
`2b290b34e8ba69104ea2f800fa53328c6ed6c236`

Important currentness note:
The project itself recommends migration to VectorChord for improved stability/performance.

Useful source properties:
- vector similarity search living beside relational data;
- relational filtering can remain part of retrieval rather than being applied only after approximate semantic search;
- multiple storage/precision representations;
- atomic file replacement helper that writes, fsyncs, renames, and fsyncs the containing directory.

Decision: ADAPT mechanisms; REJECT new runtime dependency on pgvecto.rs itself.

Admitted:
- semantic retrieval should preserve structured constraints and provenance instead of treating embedding similarity as the whole retrieval policy;
- durable local state writes should prefer atomic replacement plus durability synchronization when the storage medium supports it.

Rejected:
- introducing pgvecto.rs itself as a new dependency when its own maintainers direct new users to a successor.

## shorin-nikita/lisa

Exact observed head:
`9708c068f7635bb64241bd0078cc51ecff045f4a`

Useful source properties:
- one local AI stack composed from multiple replaceable services;
- private/public deployment profiles through compose overlays;
- environment/hardware detection before service selection;
- generated secrets kept in local environment state rather than source;
- temporary config write then rename;
- backup of existing configuration before replacement;
- firewall ordering that permits SSH before enabling the firewall;
- workflow templates as reusable orchestration artifacts.

Decision: ADAPT.

Admitted:
- environment profile is part of capability state: private/local and externally reachable deployments should not be the same configuration with accidental exposure;
- hazardous configuration changes should satisfy lockout-prevention preconditions before enabling the hazard;
- generated credentials belong outside repository state;
- configuration replacement should preserve a recovery path;
- local AI capability can be a service fabric of replaceable components rather than one monolithic application.

Rejected as a universal default:
- an installer choosing public exposure merely because installation succeeded.

## sqlchat/sqlchat

Exact observed head:
`665af875413affadfeefff81794f1d7758782bc2`

Source-level correction:
SQLChat's ActionConfirmModal is not the generated-SQL execution gate.

Actual execution flow observed:
- model-produced SQL is rendered as SQL;
- the user can open it into a query drawer;
- the statement is visible and editable before manual execution;
- SELECT statements can execute automatically when the drawer opens;
- non-SELECT statements display a warning banner;
- the backend executes the supplied statement directly.

Decision: ADAPT.

Admitted:
- generated actions should be inspectable as concrete artifacts before consequential execution when practical;
- proposal, editable action artifact, execution request, and result should remain distinct states;
- user edits after generation are provenance-relevant and should not be silently attributed to the model;
- risk tiering can differ between observation and mutation.

Not admitted:
- warning-only mutation gating as sufficient authorization;
- auto-execution of an observed query as a universal policy.

## antoinejaussoin/retro-board

Exact observed head:
`03dfe60aa9765e0c8bcdd3b9c654fcd7e496a925`

Useful source properties:
- explicit request/receive action vocabulary;
- per-message acknowledgement token;
- frontend tracking of acknowledgement/request time;
- server-side unauthorized-action errors;
- spectator versus participant distinction;
- moderator role separated from creator/owner;
- transactional database wrapper for grouped state changes;
- readiness as explicit shared state.

Decision: ALREADY_PRESENT + ADAPT.

Already present conceptually:
- request/effect/observed-result separation;
- capability versus authority;
- explicit role boundaries.

Additional adaptation:
- correlate asynchronous action requests and receipts with stable identifiers and timing rather than relying on conversational order;
- participation/observation roles should be representable independently from administrative authority.

## bayeru/chat-to-your-database

Exact observed head:
`6d90f60b7cd844b341f2d9adbad0827a47763694`

Useful source properties:
- top-k result bound;
- preference for only relevant columns rather than SELECT *;
- explicit maximum retry count;
- intermediate SQL and result preserved for display;
- instruction to double-check generated SQL before execution.

Decision: ADAPT with an important rejection.

Admitted:
- retrieval/query attempts need bounded retry budgets;
- minimize returned data to what the question actually needs;
- preserve generated query artifacts as provenance;
- expose execution intermediates when they materially explain an answer.

Rejected:
- prompt-only prohibition of mutation as an authority boundary.

Reason:
A model instruction saying "do not perform DML" is useful behavior guidance, but enforcement belongs below the model when actual database authority exists.

## Cross-source admissions

These seven repos jointly support the following additions to unbound-sol:

1. Capability envelopes should state effect class, trust mode, resource bounds, and verification requirements.
2. Observation should be separable from mutation and default to the narrower capability when practical.
3. Generated actions should remain inspectable artifacts rather than disappearing between language output and effect.
4. Resource limits are part of safe cognition/action: result size, timeout, concurrency, and retries.
5. Semantic retrieval should remain composable with exact structured constraints.
6. Durable state writes should use atomic replacement/recovery patterns when practical.
7. Connection/transport trust is distinct from application/data authority.
8. Broad tool catalogs should be partitioned rather than handed wholesale to a model.
9. Prompt behavior is not an enforcement boundary.

## Claim ceiling

This intake records mechanisms observed in the exact public heads above and architectural decisions made from them.

It does not claim:
- the repositories are fully security-audited;
- their advertised features are all correct;
- their code should be copied directly;
- their licenses permit every possible downstream use without separate review;
- any external package has been installed into Sol's runtime;
- any database/network permission has been widened.
