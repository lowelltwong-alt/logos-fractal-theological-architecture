---
id: "gov.ai_engineer_playbook"
anchor: "governance.ai_engineer_playbook"
title: "AI Engineer Playbook"
node_type: "governance_policy"
status: "active"
review_status: "approved"
address: "docs/governance/ai-engineer-playbook.md"
trust_zone: "canonical"
lifecycle_state: "active"
ai_usage_posture: "human_review_required"
object_type: "governance_playbook"
provenance_note: "Created on 2026-04-08 to govern safe, high-throughput AI engineering operations."
reason_for_inclusion: "Provide explicit guardrails so future AI engineers can accelerate work without bypassing review and promotion controls."
---


# AI Engineer Playbook

## Purpose

This playbook defines what automation is allowed to do, what it may prepare, and what it may never finalize without human review.

It implements the build-order requirement that aggressive automation must come after governance checks and review routing.

## Allowed operation classes

AI engineering work must be classified before execution.

### 1) Suggest (allowed)
- Generate candidates, hypotheses, cross-links, and quality flags.
- Write only to proposed or quarantine lanes.
- Never mutate canonical objects.

### 2) Draft (allowed)
- Produce draft nodes, draft edges, or draft migration plans.
- Require explicit reviewer fields before promotion.
- Keep provenance in every generated artifact.

### 3) Normalize (allowed)
- Apply deterministic formatting and ID/anchor generation rules.
- Normalize only within proposal/quarantine lanes unless a reviewer authorizes promotion.
- Preserve semantic content; do not silently reinterpret doctrine.

### 4) Promote (forbidden without review)
- Promotion to canonical or tradition-scoped zones requires an explicit human reviewer decision.
- AI tools must not auto-promote generated output.

## Non-negotiable promotion rule

AI-generated or inferred output may not be promoted out of quarantine without:
- assigned reviewer identity
- review timestamp
- review decision
- rationale summary
- destination trust zone

See `docs/governance/ai-output-quarantine-lane.md` for required fields.

## Prompt contracts

Use `docs/governance/ai-prompt-contracts.md` as the operational contract library for common tasks:
- node creation
- edge suggestion
- mapping ingestion
- migration drafting

## Deterministic generation utilities

Use these scripts for stable generation:
- `scripts/generate_node_id.py`
- `scripts/generate_anchor.py`
- `scripts/generate_edge_id.py`

These scripts remove ad-hoc naming drift and keep review diffs compact.

## Nightly automation boundary

Use `scripts/nightly_ai_governance.sh` for unattended runs.

The entrypoint executes this fixed sequence:
1. lint
2. normalize proposals
3. suggest links
4. produce review queue

The nightly run must never perform auto-promotion.

## Definition of done for AI-assisted batches

Before closing a batch:
- proposals are normalized deterministically
- link suggestions are generated and attached
- review queue entries exist with mandatory reviewer fields
- no canonical promotion happened automatically
