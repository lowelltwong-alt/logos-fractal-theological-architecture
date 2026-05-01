---
object_type: owner_routing_matrix
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: owner_routing_guidance
provenance_note: "Created 2026-05-01 as a draft owner-routing matrix for agent/skill and frontier-signal review."
reason_for_inclusion: "Define which owner roles should review different kinds of agent, skill, source, route, drift, runtime, and theological impacts."
---

# Owner Routing Matrix

| Impact area | Owner role |
|---|---|
| AI workflow route / prompt template | AI control-plane owner |
| Doctrine/concept implication | theological steward |
| Conservative evangelical profile | conservative source-profile reviewer |
| Bible/source ingestion | source registry owner |
| Copyright/licensing | source licensing reviewer |
| Claim object | claim steward |
| Graph object | graph steward |
| Validator/schema | validation owner |
| Security / prompt injection | security reviewer |
| Agent/skill permissions | agent-skill registry owner |
| Runtime agents | runtime governance owner |
| Theological profile drift | theological steward + source-profile reviewer |
| Local/free model routing | model routing owner |

## Multi-owner and tie-breaker rule

If a change touches more than one impact area, every matching owner is a required reviewer. Approval is conjunctive, not disjunctive: a single owner cannot approve on behalf of another.

If two owners disagree, escalate to the agent-skill registry owner and, for theological scope, to the theological steward. Do not proceed on a tie.

## Ambiguous-owner rule

If no row matches, the default reviewer is the agent-skill registry owner. The registry owner must either:

- accept the routing and record the assignment;
- delegate to a named owner with that owner's acceptance;
- defer the change until ownership is defined.

Do not proceed without a named owner.

## Solo-maintainer mode

Under solo-maintainer mode (see `AGENTS.md`), a single maintainer may stand in for multiple owner roles. The card must still record which roles applied so future role-splits preserve provenance and review accountability.

## Owner-overload escalation

If reviews queue beyond declared cadence or beyond a card's `last_reviewed` window, escalate to the agent-skill registry owner. Overloaded queues do not auto-approve; they must either pull in a backup reviewer, defer the change, or freeze new high-risk additions until cleared (see `swarm-scale-failure-modes.md`).
