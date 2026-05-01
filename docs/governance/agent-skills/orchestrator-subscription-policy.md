---
object_type: orchestrator_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: orchestrator_subscription_guidance
provenance_note: "Created 2026-05-01 as a draft policy for orchestrator subscriptions to skill and signal changes."
reason_for_inclusion: "Define how orchestrators should be notified of relevant skill, signal, route, or drift changes without allowing automatic orchestrator mutation."
---

# Orchestrator Subscription Policy

## Principle

A skill or signal change may notify an orchestrator. It may not automatically rewrite the orchestrator.

## Subscription triggers

- new skill candidate;
- skill status change;
- tool permission change;
- model policy change;
- side-effect level change;
- new composition edge;
- duplicate/merge candidate;
- theological drift risk edge;
- unsafe composition edge;
- new signal category affecting route;
- source boundary change.

## Required output

An orchestrator impact assessment should include:

- affected orchestrator;
- reason;
- skill/signal involved;
- route affected;
- risk;
- recommended change;
- owner role;
- approval needed.

## Human approval

Orchestrator updates require explicit review when they affect permissions, routing, theological profile, source boundaries, runtime behavior, or audit requirements.
