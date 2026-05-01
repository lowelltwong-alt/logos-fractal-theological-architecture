---
object_type: model_boundary_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: local_and_free_model_boundary_guidance
provenance_note: "Created 2026-05-01 as a docs-level boundary policy for local and free-tier models used as agents or skills."
reason_for_inclusion: "Define what local, on-device, free-tier, and low-cost models may and may not do, so cost incentives never override source, theology, claim, graph, or runtime governance."
---

# Local and Free Model Boundary Policy

This policy hardens `model-agnostic-agent-implementation-policy.md` for the case where a card is implemented by a local, on-device, free-tier, open-weights, or low-cost model.

The boundary is not the model. The boundary is the route, the source policy, and the side-effect class.

## Allowed work for local/free models

Local or free models may support:

- formatting and shape-only edits;
- file classification;
- tag suggestions;
- duplicate-candidate detection;
- summarization drafts of repo-internal docs;
- non-sensitive outline generation;
- read-only review prompts that produce notes only.

## Forbidden routes for local/free models acting alone

A local or free model acting alone must not perform:

- doctrine or concept promotion;
- claim object creation or change;
- graph object creation or change;
- source registry creation or change;
- Bible or source licensing decisions;
- ingestion of external text, chunks, embeddings, or corpora;
- schema, validator, or workflow changes;
- tool-permission, route-table, or owner-matrix changes;
- runtime agent or orchestrator behavior changes;
- theological-profile or tradition-scope changes;
- any side-effecting action outside `read_only` or `draft_only`.

These routes require frontier-model use plus human review per the model-agnostic implementation policy.

## Source and privacy boundary

Local execution does not relax source policy. A local model still:

- must obey the source-and-licensing watch policy;
- must not ingest protected modern Bible translations, modern theology books, proprietary lexicons, leaked code, private prompts, or leak-derived repositories;
- must not exfiltrate private repo content to external services bundled with the local runtime;
- must not capture secrets, credentials, private licensed text, or privileged material.

Run the run-ledger and audit policy regardless of where the model executes.

## Tool and permission boundary

A local or free model may only use tools the registry card explicitly grants. Local execution does not grant additional tools.

If a local runtime cannot enforce the card's allowed/forbidden tools, side-effect level, audit capture level, or stop conditions, that runtime cannot host the skill.

## Output handling

Outputs of local or free models are treated as `proposed` until reviewed.

Local/free outputs may not be promoted to canonical, claim, graph, source-registry, or runtime surfaces without the same review as any other proposed material.

## Cost incentive guard

Cost or convenience is not a reason to relax source, theology, claim, graph, or runtime governance.

If a route would be cheaper to run locally but the route is forbidden to local/free models, the route remains forbidden.
