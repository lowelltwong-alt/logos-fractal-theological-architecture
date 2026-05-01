---
object_type: controlled_taxonomy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: signal_classification_guidance
provenance_note: "Created 2026-05-01 as the controlled taxonomy for Frontier Signal Intelligence."
reason_for_inclusion: "Define signal classes so future monitoring outputs can be routed consistently."
---

# Signal Taxonomy

## Signal classes

| Signal class | Description | Typical route |
|---|---|---|
| `frontier_math` | Major math result, solved conjecture, new proof technique, new benchmark result. | research_addition / validation_infra follow-up |
| `formal_verification` | Lean, Coq, Isabelle, theorem proving, proof automation, verification breakthrough. | governance_bridge / validation_infra |
| `ai_capability` | Model/tool capability change affecting Codex, Claude, local models, retrieval, or agent planning. | frontier_signal_intelligence / ai_workflow update |
| `algorithmic_progress` | New retrieval, graph, ranking, clustering, compression, verification, or optimization method. | research_addition / roadmap |
| `ontology_kg_standards` | RDF, SHACL, SKOS, PROV, JSON-LD, LinkML, named-graph, or identifier standards changes. | governance_bridge / validation_infra |
| `graph_rag_retrieval` | New GraphRAG, NOS, retrieval, summarization, or evidence rendering method. | roadmap / source registry / rendering contract |
| `source_licensing` | Bible, theology, lexicon, corpus, or commentary source-rights change. | source_registry |
| `open_corpora` | New public-domain or open-license corpus relevant to Logos. | source_registry / ingestion_pilot |
| `security_prompt_injection` | Prompt injection, data poisoning, agent poisoning, RAG poisoning, or supply-chain issue. | validation_infra / agent_skill_catalog |
| `theological_scholarship` | Serious source or scholarship that may affect concept/doctrine/source profiles. | research_addition / concept_promotion |
| `agent_skill_discovery` | New agent/skill pattern or candidate capability. | agent_skill_catalog |
| `contributor_workflow` | New contributor, review, PR, Codex, Claude, local model, or audit workflow. | ai_workflow / governance_bridge |
| `governance_regulatory` | Legal, copyright, privacy, data, or AI governance change. | governance_bridge / source_registry |

## Mandatory classification fields

- signal_class
- source
- source_status
- date_observed
- claim_summary
- affected_repo_surfaces
- recommended_route
- confidence
- review_required
- follow_up_trigger
