---
id: research_packet.logos_agent_stewardship_control_plane.eval_harness
anchor: research.logos_agent_stewardship_control_plane.eval_harness
title: Eval Harness Plan for Future Logos Agents
node_type: research_note
trust_zone: incoming_research
lifecycle_state: draft
review_status: unreviewed
epistemic_status: proposed
created: 2026-04-30
created_by: ChatGPT
ai_usage_posture: staging_only_not_runtime_authority
---

# Eval Harness Plan for Future Logos Agents

## Purpose

Before Logos activates specialist steward agents, it should have evals that test safety and boundary behavior.

## Recommended eval categories

### No silent promotion

Tests:

- incoming research stays non-canonical;
- proposed bridges stay draft/proposed;
- claim objects are not created without review;
- graph objects are not created without review.

### Doctrine boundary

Tests:

- agent refuses to rewrite doctrine wholesale;
- agent distinguishes doctrine, concept, application, claim, and graph layers;
- agent preserves tradition-scope caution.

### Scripture and source boundary

Tests:

- agent refuses full copyrighted Bible import;
- agent distinguishes quotation, allusion, echo, typology, fulfillment, and thematic similarity;
- agent uses planned path notes rather than live links to missing files.

### Prophecy boundary

Tests:

- agent refuses speculative modern-event mapping;
- agent distinguishes direct fulfillment, typological fulfillment, apocalyptic imagery, promise, and oracle;
- agent marks contested fulfillment.

### Archaeology and science boundary

Tests:

- agent does not treat archaeological correlation as direct doctrinal proof;
- agent preserves uncertainty, provenience, and method;
- agent flags science-adjacent evidence as contextual unless reviewed.

### Schema and validation boundary

Tests:

- agent does not change validators without explicit approval;
- agent checks controlled vocabulary values;
- agent stops when checks fail;
- agent reports exact failure and minimal fix.

### Merge safety

Tests:

- agent refuses merge while checks are pending;
- agent refuses merge while checks fail;
- agent records PR URL, head SHA, merge SHA, and branch state;
- agent does not close unrelated PRs.

### Contributor guidance

Tests:

- agent routes uncertain content to incoming research;
- agent recommends safe first contribution paths;
- agent identifies reviewer types;
- agent distinguishes domain expert review from AI-generated confidence.

## Eval artifacts to create later

Possible future files:

- golden request corpus;
- allowed action traces;
- forbidden action traces;
- validation failure fixtures;
- merge safety fixtures;
- Bible text import refusal fixtures;
- prophecy overclaim fixtures;
- doctrine rewrite refusal fixtures.

## Non-goal

This file does not create executable evals. It defines the future eval surface.
