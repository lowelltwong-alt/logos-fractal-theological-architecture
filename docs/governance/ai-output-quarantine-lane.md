---
id: "gov.ai_output_quarantine_lane"
anchor: "governance.ai_output_quarantine_lane"
title: "AI Output Quarantine Lane"
node_type: "governance_policy"
status: "active"
review_status: "approved"
address: "docs/governance/ai-output-quarantine-lane.md"
trust_zone: "canonical"
lifecycle_state: "active"
ai_usage_posture: "human_review_required"
object_type: "quarantine_lane_policy"
provenance_note: "Created on 2026-04-08 to isolate AI output until reviewer adjudication."
reason_for_inclusion: "Prevent AI-generated drafts from entering canonical lanes without explicit reviewer accountability."
---


# AI Output Quarantine Lane

## Lane purpose

The quarantine lane stores AI-generated outputs that are not yet approved for promotion.

## Location

- `data/ai-output/quarantine/proposals/`
- `data/ai-output/quarantine/normalized/`
- `data/ai-output/quarantine/suggestions/`
- `reports/ai-review-queue/`

## Mandatory reviewer fields before promotion

Every proposed artifact must include:
- `reviewer_id`
- `reviewed_at_utc`
- `review_decision` (`approved` | `rejected` | `needs_changes`)
- `review_rationale`
- `promotion_target_trust_zone`

If any field is missing, promotion is blocked.

## Promotion gate

No tool or script may promote quarantine output automatically.

Promotion must be a separate explicit human action after reviewer fields are complete.

## Audit expectation

Review queue artifacts must preserve:
- source proposal path
- deterministic IDs used
- reviewer decision status
- timestamp
