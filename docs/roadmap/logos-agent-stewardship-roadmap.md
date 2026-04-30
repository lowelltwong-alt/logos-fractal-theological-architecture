---
id: roadmap.logos_agent_stewardship
anchor: roadmap.logos_agent_stewardship
title: Logos Agent Stewardship Roadmap
node_type: roadmap_note
trust_zone: proposed
lifecycle_state: draft
review_status: unreviewed
epistemic_status: planning
created: 2026-04-30
created_by: ChatGPT
requested_by: Lowell T. Wong
ai_usage_posture: planning_only_not_runtime_authority
---

# Logos Agent Stewardship Roadmap

## Purpose

This roadmap records how agent-harness and specialist-agent patterns may eventually apply to the Logos repository without building an executable agent runtime yet.

The useful lesson from agent-harness research is not that Logos needs an uncontrolled agent swarm. The useful lesson is that any future agentic work needs a governed control plane between the theological knowledge plane and any execution plane.

## Clean-room posture

This roadmap is based on clean-room architectural synthesis, public agent-tool patterns, and the Logos repository's own governance direction. It does not rely on leaked source code or leak-derived repositories.

## Core principle

Logos should not build an autonomous theology agent first.

Logos should first define the stewardship controls that would make future AI-assisted contribution safe:

```text
knowledge plane -> control plane -> execution plane
```

## Three-plane model

### Knowledge plane

The current Logos repo mostly lives here.

Includes:

- doctrine nodes;
- concept nodes;
- canon thinker material;
- incoming research packets;
- application bridges;
- claim objects;
- graph relationship objects;
- biblical connection vocabulary;
- provenance and review status;
- validation contracts.

### Control plane

This is the missing future layer before any serious agentic contributor workflow.

Includes:

- agent role map;
- allowed modes;
- permission boundaries;
- approval gates;
- action classes;
- run ledger fields;
- reviewer requirements;
- validation and diff requirements;
- eval harness expectations.

### Execution plane

This is not active yet.

Future execution might include:

- Codex or GitHub file edits;
- import scripts;
- graph generation;
- schema updates;
- validation runs;
- PR creation;
- branch cleanup;
- static-site or API publication.

Execution must remain downstream of the control plane.

## Safe future agent posture

Future agents may help with:

- search;
- summarization;
- repo state review;
- missing-metadata detection;
- proposed bridge-file drafts;
- proposed claim-object drafts;
- proposed graph-object drafts;
- PR review packets;
- validation triage;
- contributor onboarding.

Future agents must not silently promote doctrine, rewrite canonical files, import Bible text, create graph edges, change validators, or merge PRs without explicit human approval.

## Specialist steward agents

Use the language of specialist steward agents rather than swarms.

### Doctrine Steward

Purpose: review doctrine and concept edits for scope, status, source basis, and path authority.

Default mode: explore and plan only.

Forbidden: rewrite doctrine wholesale, promote canonical status, collapse tradition distinctions, or act as theological authority.

### Scripture Reference Steward

Purpose: review Scripture references, passage anchors, quotation/allusion/echo distinctions, and Bible-text import policy.

Default mode: explore and plan only.

Forbidden: import full Bible text, create modern translation corpora, or treat translation rendering as original-language meaning.

### Original-Language Steward

Purpose: review Hebrew, Aramaic, and Greek terminology, lemma/morphology/sense language, and translation-rendering distinctions.

Default mode: explore and plan only.

Forbidden: create bulk original-language corpora before source/license and schema review.

### Hermeneutics Steward

Purpose: review method labels such as grammatical-historical, canonical, typological, figural, reception-history, rabbinic, patristic, and archaeological contextualization.

Default mode: explore and plan only.

Forbidden: flatten method-dependent claims into one generic relation.

### Prophecy Boundary Steward

Purpose: prevent overclaim around prophecy, fulfillment, apocalyptic, typology, and modern-event mapping.

Default mode: explore and plan only.

Forbidden: create speculative prophecy systems, unscoped fulfillment claims, or modern-event mappings.

### Archaeology and Context Steward

Purpose: keep archaeology, historical geography, epigraphy, inscription, and science-adjacent evidence contextual rather than overclaimed.

Default mode: explore and plan only.

Forbidden: turn archaeology into direct doctrinal proof without an explicit intermediate argument.

### Graph Contract Steward

Purpose: review relationship-object shape, target IDs, registry alignment, external mappings, and schema-contract implications.

Default mode: explore and plan only.

Forbidden: change validators, schemas, or relationship vocabulary without explicit review.

### Contributor Guide Steward

Purpose: help new contributors choose correct lanes, prepare safe PRs, and avoid scope mistakes.

Default mode: explore and plan only.

Forbidden: approve its own content or bypass review.

### Merge Safety Steward

Purpose: summarize changed files, risk surfaces, validation status, review requirements, and rollback notes.

Default mode: explore and plan only.

Forbidden: merge without explicit user approval.

## Agent modes

### Explore

Read-only discovery.

Allowed:

- search repo;
- read files;
- summarize current state;
- identify related nodes;
- detect missing metadata;
- compare file scopes.

Forbidden:

- edits;
- PR creation;
- claim promotion;
- graph-object creation.

### Plan

Proposal formation.

Allowed:

- draft implementation plan;
- prepare proposed file list;
- produce PR body;
- produce review checklist;
- identify validation commands;
- propose risk classification.

Forbidden:

- merge;
- delete;
- retire;
- change canonical status.

### Execute

Controlled mutation only after explicit approval.

Allowed with approval:

- create branch;
- add files;
- commit;
- open PR;
- run validation;
- update PR metadata.

Requires stronger approval:

- merge;
- delete;
- retire;
- change validators;
- change schema contracts;
- import Bible text;
- change canonical doctrine;
- modify controlled vocabulary.

## High-risk action classes

These require explicit approval packets:

- doctrine rewrite;
- canonical status change;
- claim object promotion;
- graph relationship promotion;
- new relationship vocabulary;
- schema or validator change;
- Bible text import;
- original-language corpus import;
- file deletion or retirement;
- branch cleanup;
- external mapping contract change.

## Approval packet requirements

A future approval packet should include:

- action type;
- agent role;
- mode;
- touched files;
- before/after summary;
- reason for change;
- source basis;
- risk class;
- validation commands;
- validation result;
- reviewer type needed;
- rollback plan;
- PR or commit reference;
- approval status.

## Run ledger expectations

A future run ledger should record:

```yaml
run_id:
agent_role:
mode: explore | plan | execute
user_request:
files_read:
files_changed:
actions_taken:
validation_run:
approval_required:
approval_status:
commit_sha:
pr_number:
risk_level:
notes:
```

## Eval harness ideas

Before any executable agent runtime exists, define evals for:

- no silent doctrine promotion;
- no Bible text import;
- no graph-object promotion without review;
- no validator/schema changes without explicit approval;
- correct distinction between quotation, allusion, echo, typology, and fulfillment;
- correct handling of incoming research as non-canonical;
- correct PR risk summary;
- correct merge refusal when checks fail;
- correct planned-path vs live-link behavior;
- correct use of controlled vocabulary values.

## Non-goals for now

Do not build:

- `.claude/agents/`;
- executable agent runtime;
- autonomous GitHub agent;
- agent memory system;
- agent that edits doctrine;
- agent that imports Bible text;
- agent that creates graph objects;
- agent that merges PRs;
- multi-agent debate system;
- live swarm orchestration.

## Recommended build order

1. Finish AI Governance Bridge Pack v1.
2. Add this roadmap and staged control-plane seed.
3. Build Human Person and Formation Core Slice.
4. Build Biblical Connection Vocabulary Bridge.
5. Build first Claim Object Pack.
6. Build first Graph Relationship Pack.
7. Add Contributor Gateway v2.
8. Only then consider read-only specialist steward agents.

## Bottom line

A knowledge graph does not make an agent.

A governed ontology tells future systems what things mean.

A control plane tells future systems what they may do.

An execution plane lets future systems act.

Logos should finish the knowledge and bridge layers before adding execution, but it should define the future control-plane rules now.
