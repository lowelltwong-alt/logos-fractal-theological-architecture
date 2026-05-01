---
object_type: swarm_scale_failure_modes
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: swarm_scale_failure_guidance
provenance_note: "Created 2026-05-01 as a docs-level catalog of failure modes specific to a large agent/skill ecosystem."
reason_for_inclusion: "Anticipate failure modes that only appear at thousands of agents/skills so registry design, owner routing, audit, and orchestrator policy can prevent them before runtime exists."
---

# Swarm-Scale Failure Modes

This file lists failure modes that are unlikely with a few skills but become likely as the registry grows.

It is docs-only. It does not enable runtime, schedulers, or orchestrators. It defines preventive guardrails the registry, cards, and adapters must satisfy before runtime can be approved.

## Catalogued failure modes

### Drift accumulation

Many small, individually approved changes can shift theological profile, source policy, or assertion posture over time.

Guardrail: keep `theological-profile-drift-review-checklist.md` cadence active per card and per registry release; pin a baseline; require diff-of-defaults review; never approve a release that fails drift review.

### Subscription fan-out

A single change can wake every orchestrator subscribed to a tag, route, or owner.

Guardrail: cap orchestrator subscriptions per change; require subscription cards to declare maximum frequency; default to digest-style notification rather than per-event; prohibit cascading subscriptions where one orchestrator subscribes to another orchestrator without explicit approval.

### Orchestrator cycles

Two or more orchestrators can subscribe to each other's outputs and form a loop.

Guardrail: require subscription cards to declare upstream and downstream cards; prohibit cycles by registry rule; require manual review when a cycle is proposed; require a termination condition on every chain.

### Composition explosion

Pairwise composition produces O(n^2) potential edges; chained composition produces more.

Guardrail: composition is allowed only via reviewed `composes_with` edges per `unsafe-composition-review-checklist.md`; do not auto-generate composition edges; treat any auto-generated candidates as `proposed` and unaudited.

### Duplicate and near-duplicate sprawl

Many cards converge on similar capabilities, owners cannot keep up, and duplicates leak permissions across owners.

Guardrail: enforce `duplicate-merge-and-derivative-policy.md`; require a periodic dedupe pass; require a service-level for duplicate-candidate review; do not approve a new card if an existing card already covers the capability without a derivative justification.

### Owner overload and ambiguous ownership

A small set of owners becomes the bottleneck, or a card has no clearly mapped owner.

Guardrail: see `owner-routing-matrix.md` escalation and tie-breaker rules; require explicit owner per card; require backup owner for high-risk classes; queue overflow must escalate to the agent-skill registry owner rather than auto-approve.

### Permission creep

Adapters, parents, or orchestrators silently grant tools beyond what the card declares.

Guardrail: see `safety-controls-floor.md`; no wildcard grants; no tool inheritance without per-tool review; runtime adapters that cannot enforce per-tool grants cannot host high-risk cards.

### Audit silencing

At scale, audit events are dropped, sampled, or rolled up so high-risk events disappear in noise.

Guardrail: see `audit-and-trace-requirements.md` minimum capture floor by capability class; high-risk capability classes cannot be downsampled; aggregated dashboards do not replace per-event capture for high-risk routes.

### Cost and resource exhaustion

A bug, cycle, or runaway monitor consumes model tokens, network, or storage.

Guardrail: every monitor card declares maximum frequency, maximum cost, and stop conditions; runtime adapters must support a manual pause and an auto-pause on quota breach; no scheduler is approved without quota and pause controls.

### Source-policy bypass at scale

Many small staged ingests evade per-PR review by appearing routine.

Guardrail: route every ingest through `source_registry` and `ingestion_pilot` per the route table; do not allow batch ingestion shortcuts; periodic source-policy audit by the source registry owner.

### Prompt-injection contamination spread

A poisoned external doc taints retrieved context across many skills.

Guardrail: treat retrieved third-party content as untrusted; quarantine on suspicion; isolate runs that touched suspected content; require security reviewer escalation; do not promote tainted content forward through the registry.

### Generated-index drift

Embeddings, duplicate detectors, GraphRAG summaries, and orchestrator impact reports become trusted by habit.

Guardrail: derived surfaces are discovery aids, not canonical truth (see `generated-index-and-graphrag-roadmap.md`); decisions must cite canonical cards, not derived reports; rebuild and re-review derived surfaces on a declared cadence.

### Coordinated rollback

A bad release affects many cards at once and rollback must be unambiguous.

Guardrail: every registry release declares a rollback target, an affected-cards list, and a recovery owner; no release is approved without a rollback plan; runtime adapters must support a coordinated pause across all cards in a release.

## Pre-runtime gate

No scheduler, runtime monitor, runtime orchestrator, or runtime subagent is approved unless its card and adapter document how it prevents the relevant failure modes above.

If a failure mode is not addressed, the default answer is no.
