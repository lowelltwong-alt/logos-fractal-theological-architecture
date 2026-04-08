---
id: "gov.pr_architecture_invariants_checklist"
anchor: "governance.pr_architecture_invariants_checklist"
title: "PR Architecture Invariants Checklist"
node_type: "governance_checklist"
status: "active"
review_status: "approved"
address: "docs/governance/pr-architecture-invariants-checklist.md"
trust_zone: "canonical"
lifecycle_state: "active"
ai_usage_posture: "human_review_required"
object_type: "pull_request_checklist"
lifecycle_status: active
provenance_note: "Authored on 2026-04-08 to operationalize non-negotiable architectural governance in reviewable form."
reason_for_inclusion: "Provide enforceable invariants and a lightweight PR gate for ongoing repository integrity."
---

# PR Architecture Invariants Checklist

Use this checklist in every pull request touching governed content.

## Required checks

- [ ] **A1 Trust direction:** No higher-trust artifact depends on lower-trust artifacts.
  - Evidence noted (validator output or reviewer note).
- [ ] **A2 Doctrine role separation:** Topic/view/assessment roles remain separate and relationship-correct.
  - Evidence noted (changed files reviewed for role purity).
- [ ] **A3 Identity-label separation:** IDs/anchors remain stable unless an explicit migration is included.
  - Evidence noted (ID diff + migration note if needed).
- [ ] **A4 Deprecate-not-delete:** No governed artifact was removed without deprecation/migration handling.
  - Evidence noted (`git diff --name-status` reviewed for deletions).

## Minimal command set

Run (or capture equivalent CI output):

1. `python scripts/validate_node_frontmatter.py`
2. `python scripts/validate_cross_references.py`
3. `python scripts/validate_trust_zone_vocabulary.py`
4. `python scripts/validate_internal_links.py`

## Reviewer sign-off note

Include a short PR note:

> "Architecture invariants A1-A4 validated; no unresolved violations."
