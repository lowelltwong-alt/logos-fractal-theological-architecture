---
id: research_packet.logos_agent_stewardship_control_plane.permissions
anchor: research.logos_agent_stewardship_control_plane.permissions
title: Permissions and Action Boundaries for Future Logos Agents
node_type: research_note
trust_zone: incoming_research
lifecycle_state: draft
review_status: unreviewed
epistemic_status: proposed
created: 2026-04-30
created_by: ChatGPT
ai_usage_posture: staging_only_not_runtime_authority
---

# Permissions and Action Boundaries for Future Logos Agents

## Purpose

This note defines the future permission posture for Logos specialist steward agents.

It is not an executable permission system.

## Modes

### Explore

Read-only discovery.

Allowed:

- search repository;
- read files;
- summarize state;
- inspect branch or PR metadata;
- identify related nodes;
- identify missing metadata;
- classify likely risk surfaces.

Forbidden:

- file edits;
- branch creation;
- commits;
- PR creation;
- status changes;
- claim or graph promotion.

### Plan

Proposal formation.

Allowed:

- draft implementation plan;
- produce file list;
- write proposed PR body;
- prepare validation commands;
- prepare review checklist;
- propose reviewer lane;
- identify rollback plan.

Forbidden:

- direct commits;
- merges;
- deletions;
- controlled vocabulary changes;
- canonical promotion.

### Execute

Mutation after explicit approval.

Allowed with approval:

- create branch;
- add files;
- update files;
- commit;
- open PR;
- update PR metadata;
- run validation;
- merge only when explicitly instructed and checks are green.

Requires stronger approval:

- force update;
- branch deletion;
- file deletion;
- validator change;
- schema change;
- controlled vocabulary change;
- canonical status change;
- claim or graph-object promotion;
- Bible text import;
- original-language corpus import.

## Hard forbidden actions

Future agents must never:

- silently promote doctrine;
- rewrite canonical doctrine wholesale;
- import copyrighted Bible translations;
- create therapy, legal, medical, or pastoral advice products from the repo;
- create graph relationships without source basis;
- hide AI generation status;
- merge failed PRs;
- ignore controlled vocabulary violations;
- change their own permissions;
- expand from read-only to write mode without user approval.

## Safe first future agent operations

The first possible future agents should be read-only or proposal-only:

- repo-state summarizer;
- bridge-file readiness checker;
- PR risk classifier;
- internal link triage helper;
- source-basis gap detector;
- contributor lane recommender.

## Unsafe early operations

Do not begin with:

- doctrine authoring agent;
- Bible import agent;
- claim-object promotion agent;
- graph edge generation agent;
- autonomous merge agent;
- multi-agent debate system;
- external web ingestion agent.
