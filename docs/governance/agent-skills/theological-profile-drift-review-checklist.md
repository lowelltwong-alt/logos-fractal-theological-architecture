---
object_type: drift_review_checklist
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: theological_profile_drift_review
provenance_note: "Created 2026-05-01 as the docs-level checklist for periodic theological-profile drift review of agents and skills."
reason_for_inclusion: "Make hidden theological-profile drift visible by requiring an explicit, repeatable review of declared defaults, source hierarchy, hermeneutic posture, and assertion limits before and after agent/skill changes."
---

# Theological Profile Drift Review Checklist

This checklist hardens `agent-misalignment-and-theological-drift-policy.md` by making drift review concrete and repeatable.

It applies to every new or changed agent/skill card, prompt, adapter, monitor, orchestrator, route template, or composed skill that touches theology, sources, hermeneutics, retrieval, or rendering.

## Declared baseline

The active Logos baseline is:

- conservative evangelical primary profile;
- declared source-spine and licensing policy;
- explicit Scripture/canon/source-boundary handling;
- inferred is not asserted;
- tradition-scoped or contrastive material is labeled.

A drift review compares a proposed change against this baseline. The reviewer must not assume the prompt or adapter preserves the baseline silently.

## Required diff-of-defaults

For each change, capture and review:

- active theological profile before and after;
- source hierarchy before and after;
- canon/scope handling before and after;
- hermeneutic posture before and after;
- confidence/assertion posture before and after;
- retrieval and rendering defaults before and after;
- claim/graph generation posture before and after;
- tradition-scope labels before and after.

If any of these fields changes without explicit owner approval, treat the change as drift.

## Stop conditions

Stop and escalate if a change:

- weakens the conservative evangelical profile boundary;
- removes or relaxes Scripture/canon/source-boundary handling;
- silently introduces non-declared tradition assumptions;
- promotes inferred or comparative material to canonical;
- lets a skill or composition assert doctrine without a doctrine path;
- changes retrieval/rendering defaults for theological content;
- imports an outside prompt or persona that overrides the declared profile;
- removes labels from tradition-scoped or contrastive output.

## Review cadence

- New cards: drift review required before status `experimental` or `active`.
- Changed cards: drift review required on any change to defaults, tools, prompts, source boundaries, model policy, or composition edges.
- Composed skills: drift review required as a new object, not inherited.
- Periodic: drift review required at the cadence declared in the card and at least at every registry release.

## Required reviewers

At minimum:

- theological steward;
- conservative source-profile reviewer;
- agent-skill registry owner.

Add the security reviewer if external prompts, adapters, or retrieved content are involved.

## Output of a drift review

Each drift review must produce:

- a short note recording the diff-of-defaults;
- a pass/fail decision per stop condition;
- a list of required follow-up changes;
- a record of reviewers and date;
- a pointer from the affected card or composition.

Drift reviews follow the audit policy in `audit-and-trace-requirements.md`.
