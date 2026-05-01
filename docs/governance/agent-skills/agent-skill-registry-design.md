---
object_type: registry_design
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: agent_skill_registry_design
provenance_note: "Created 2026-05-01 as the design note for a future agent/skill capability registry."
reason_for_inclusion: "Define how agents, skills, subagents, monitors, and orchestrators should be cataloged before runtime implementation."
---

# Agent / Skill Registry Design

## Purpose

The Agent/Skill Registry is the canonical catalog of planned or implemented AI capabilities.

It should govern:

- identity;
- ownership;
- purpose;
- capabilities;
- routes supported;
- input and output types;
- allowed tools;
- forbidden tools;
- model policy;
- source boundaries;
- doctrinal profile boundaries;
- side-effect class;
- audit requirements;
- review cadence;
- graph relationships.

## Canonical vs derived surfaces

Canonical:

- agent/skill cards;
- edge vocabulary;
- tag taxonomy;
- owner routing matrix;
- orchestrator subscription policy;
- review policies.

Derived:

- embeddings;
- duplicate candidates;
- overlap candidates;
- community summaries;
- GraphRAG reports;
- orchestrator impact reports.

Derived surfaces are discovery aids, not truth.

## Future implementation phases

1. Docs-only governance.
2. YAML/JSON card templates.
3. Schema and validation.
4. Derived index generation.
5. Tool-specific adapters.
6. Runtime agents and orchestrators.
7. Scheduled monitors and notifications.
