---
object_type: routing_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: frontier_signal_routing_guidance
provenance_note: "Created 2026-05-01 as the routing policy for frontier signals."
reason_for_inclusion: "Define how high-signal external discoveries enter existing AI workflow routes without bypassing review or trust-zone boundaries."
---

# Signal Routing Policy

## Routing principle

Signals route to existing repo workflows. Signals do not create their own mutation path.

## Route mapping

| Signal result | Route |
|---|---|
| Staged observation | `research_addition` |
| Process or vocabulary proposal | `governance_bridge` |
| Concept/doctrine implication | `concept_promotion` after staging |
| Source-rights implication | `source_registry` |
| Future text/corpus intake | `ingestion_pilot` after source review |
| Claim candidate | `claim_object` after concept/source basis exists |
| Graph relation candidate | `graph_object` after vocabulary and claim/source basis exist |
| AI tool process change | AI workflow route table / template update |
| New skill/agent idea | `agent_skill_catalog` |
| Validator/schema implication | `validation_infra` |

## Review escalation

Require reviewer escalation when a signal affects:

- doctrine;
- anthropology;
- Scripture/canon/source hierarchy;
- conservative evangelical source spine;
- Bible/source licensing;
- claim objects;
- graph relationship objects;
- validators/schemas;
- runtime agents or skills;
- AI tool permissions;
- theological profile or tradition scope.

## No direct mutation

No signal may directly mutate canonical doctrine, concept truth, source registries, claims, graphs, schemas, validators, or runtime agents.
