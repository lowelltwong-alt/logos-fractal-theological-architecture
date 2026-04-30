---
object_type: routing_algorithm
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: mandatory_routing_logic
provenance_note: "Created 2026-04-30 as the route-selection algorithm for AI-assisted repository work."
---

# AI Routing Algorithm

This algorithm determines how AI-assisted work is classified, scoped, and executed.

## Algorithm

1. Read `AGENTS.md` and `AI_WORK_START_HERE.md`.
2. Inspect local state and fetch live remote state.
3. Decide whether the task is new work or continuation work.
4. If local state is unsafe, stop and report.
5. Classify the task into one primary route.
6. Select the work mode: Explore, Plan, Edit, or Execute.
7. Select tool settings using the settings matrix.
8. Load the mandatory route template.
9. Perform only the scoped work.
10. Validate.
11. Open a PR.
12. Answer whether the router itself is affected.

## Route selection questions

Ask these questions in order.

### Is this only investigation?

If the task is only to inspect, summarize, compare, audit, or advise, use Explore or Plan mode and do not edit files unless explicitly asked.

### Is this staged research?

If the task adds research from chat, uploaded files, public sources, or source synthesis, route to `research_addition`.

Default location: `incoming/research/`.

### Is this a roadmap or source map?

If the task maps existing packets, docs, research families, or repository workstreams, route to `source_document_integration_map` or `roadmap_update`.

### Is this a governed reference or vocabulary bridge?

If the task promotes staged research into `docs/governance/` without creating claim or graph objects, route to `governance_bridge`.

### Is this doctrine or concept promotion?

If the task promotes staged theology into `docs/concepts/` or `docs/doctrine/`, route to `concept_promotion` or `doctrine_promotion`.

If it creates or changes canonical doctrine meaning, use the highest available reasoning setting and stop if source basis is unclear.

### Is this a source profile or tradition profile?

If the task creates thinker, tradition, theologian, or source profile cards, route to `source_profile_card`.

Do not ingest copyrighted source text.

### Is this source registry or licensing infrastructure?

If the task creates source registry entries, source templates, Bible source metadata, or ingestion gates, route to `source_registry`.

### Is this a claim object?

If the task creates machine-readable claim objects or changes existing claim objects, route to `claim_object`.

Claims must not outrun doctrine, concept, source, or evidence basis.

### Is this a graph object or relationship object?

If the task creates typed graph edges, relationship objects, graph objects, or relation data, route to `graph_object`.

Graph work requires approved vocabulary, source basis, and provenance.

### Is this ingestion?

If the task adds text, chunks, embeddings, corpora, source files, or ingestion sidecars, route to `ingestion_pilot`.

Ingestion must be plan-first and source-policy-first.

### Is this validation, schema, CI, or infra?

If the task changes schemas, validators, scripts, workflows, PR templates, or checks, route to `validation_infra`.

### Is this runtime agent or execution planning?

If the task adds `.claude/agents`, runtime tools, tool registries, action gateways, approval flows, hooks, or external execution, route to `runtime_agent_planning` unless explicitly authorized for runtime code.

Default is planning only.

## Highest-risk route wins

If a task matches more than one route, select the highest-risk route.

Risk order from low to high:

1. roadmap/source map
2. staged research
3. governance bridge
4. concept/source profile
5. source registry
6. claim object
7. graph object
8. validation/schema/CI
9. ingestion
10. runtime execution

## Stop instead of guessing

Stop and report if:

- the route is unclear;
- the task requires a missing template;
- source rights are unclear;
- concept or claim basis is missing;
- existing repo conventions conflict;
- validations fail in unrelated areas;
- local git state is unsafe;
- execution would require a side effect not authorized by the prompt.
