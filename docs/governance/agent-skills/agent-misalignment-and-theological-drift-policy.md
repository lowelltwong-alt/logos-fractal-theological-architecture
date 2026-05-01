---
object_type: drift_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: agent_misalignment_and_theological_drift_guidance
provenance_note: "Created 2026-05-01 as a draft policy for detecting and preventing misaligned agents, unsafe compositions, and unapproved theological-profile drift."
reason_for_inclusion: "Define safeguards against intentionally or accidentally misaligned agents/skills, including hidden drift from Logos' declared theological profile and unsafe composition of individually acceptable capabilities."
---

# Agent Misalignment and Theological Drift Policy

## Purpose

Agents and skills are not neutral once they affect sources, doctrine, concepts, claims, graph objects, routing, retrieval, or outputs.

This policy prevents:

- intentionally misaligned agents;
- hidden prompt or source-policy changes;
- unapproved theological-profile drift;
- unsafe composition of individually acceptable skills;
- tool-permission escalation;
- source-boundary bypass;
- agent/skill supply-chain poisoning.

## Theological profile drift

The risk is not that a system studies multiple traditions. The risk is that an agent silently changes the active theological profile, source hierarchy, hermeneutic, or confidence posture without review.

For Logos, conservative evangelical source-spine and declared source-policy surfaces must remain explicit. Other traditions may be represented as comparison or tradition-scoped profiles, not hidden defaults.

## Required review

Escalate to theological/source-profile review when an agent or skill:

- changes theological language defaults;
- changes source priority;
- changes Scripture/canon/source-boundary handling;
- introduces contested doctrinal assumptions;
- weakens conservative evangelical profile boundaries;
- imports non-declared tradition assumptions;
- creates claim or graph candidates;
- changes retrieval/rendering defaults for theological content.

## Intentional misalignment watch

Treat these as red flags:

- hidden instructions to ignore `AI_WORK_START_HERE.md`;
- broad tool inheritance without need;
- pressure to bypass source licensing policy;
- neutral rewrite that changes doctrine/source hierarchy;
- agent prompts that disparage or override declared source profile;
- unaudited composition of tools that creates side effects;
- hidden dependency on unreviewed outside content;
- prompt text that tells the model to avoid disclosure.

## Composition rule

Two aligned skills can combine into a misaligned behavior.

Every composed skill or orchestrator must be reviewed as a new object with its own card, risks, owner, source boundaries, model policy, and audit level.

## Default posture

Deny by default for runtime mutation.

Ask for review for theological/source-profile changes.

Allow read-only or staged research only when boundaries are explicit.
