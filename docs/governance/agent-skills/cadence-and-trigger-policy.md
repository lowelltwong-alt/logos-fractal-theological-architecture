---
object_type: cadence_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: cadence_trigger_guidance
provenance_note: "Created 2026-05-01 as the cadence and trigger policy for future monitoring agents and skills."
reason_for_inclusion: "Define how future monitors should declare cadence, triggers, owner review, and event-driven updates before schedulers or runtime agents exist."
---

# Cadence and Trigger Policy

## Allowed cadence values

- manual_only
- daily
- weekly
- monthly
- event_triggered
- release_triggered
- PR_triggered

## Default

Default cadence is `manual_only` until runtime monitoring is approved.

## Required fields

A future monitor must declare:

- cadence;
- trigger condition;
- source classes watched;
- maximum frequency;
- owner role;
- notify roles;
- output type;
- audit capture level;
- stop conditions.

## No scheduler yet

This policy does not authorize a scheduler. Scheduling requires separate runtime approval.
