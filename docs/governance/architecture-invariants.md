---
id: "gov.architecture_invariants"
anchor: "governance.architecture_invariants"
title: "Architecture Invariants"
node_type: "governance_invariant_spec"
status: "active"
review_status: "approved"
address: "docs/governance/architecture-invariants.md"
trust_zone: "canonical"
lifecycle_state: "active"
ai_usage_posture: "human_review_required"
object_type: "governance_invariant_spec"
lifecycle_status: active
provenance_note: "Authored on 2026-04-08 to operationalize non-negotiable architectural governance in reviewable form."
reason_for_inclusion: "Provide enforceable invariants and a lightweight PR gate for ongoing repository integrity."
---

# Architecture Invariants

This document defines non-negotiable repository architecture constraints in testable terms.

## Invariant A1 — Trust-zone dependency direction

**Invariant statement (testable):**
A higher-trust artifact MUST NOT depend on a lower-trust artifact.

Trust order for dependency checks:
1. `canonical`
2. `tradition-scoped`
3. `proposed`
4. `inferred`
5. `deprecated`
6. `learning-sidecar`

Allowed dependency direction:
- same trust -> same trust
- lower trust -> same or higher trust

Disallowed dependency direction:
- higher trust -> lower trust

**Rationale:**
Dependency direction preserves epistemic integrity so lower-certainty material cannot become an implicit foundation for higher-certainty content.

**Detection rule (what to scan for):**
- Scan links, references, or IDs in changed files and compare source/target `trust_zone` values.
- Flag any edge where source trust rank is higher than target trust rank.
- Practical check:
  - run `python scripts/validate_trust_zone_vocabulary.py`
  - run `python scripts/validate_cross_references.py`
  - perform targeted review of changed references for trust-direction violations.

**Remediation rule:**
- Reverse the dependency direction where architecturally appropriate.
- Promote the target artifact only through governed review if it truly belongs in a higher trust zone.
- Otherwise move the source artifact to an equal/lower trust zone and document the decision.

---

## Invariant A2 — Doctrine topic/view/assessment separation

**Invariant statement (testable):**
Doctrine topics, doctrine views, and doctrine assessments MUST remain separate objects and MUST NOT be collapsed into one artifact.

Minimum object-role expectations:
- Topic object: names scope of doctrinal question.
- View object: represents a specific doctrinal position under a topic.
- Assessment object: evaluates a view against a declared framework/profile.

**Rationale:**
Separation keeps representation legible and prevents category confusion between what is being discussed (topic), what is being proposed (view), and how it is judged (assessment).

**Detection rule (what to scan for):**
- Scan filenames, frontmatter/object metadata, and relationship files for mixed role signals in one object.
- Flag artifacts that claim more than one doctrine role or use cross-role naming patterns indicating collapse.
- Check for required relationship patterns such as topic->has-view and assessment->targets-view.
- Practical check:
  - inspect changed doctrine/object metadata for single-role clarity
  - inspect changed relationship artifacts for role-correct edges.

**Remediation rule:**
- Split mixed artifacts into separate topic/view/assessment objects.
- Add explicit relationship objects to reconnect split artifacts.
- Deprecate superseded mixed artifact; do not silently repurpose it.

---

## Invariant A3 — Identity vs label separation

**Invariant statement (testable):**
Stable identity fields (IDs/anchors/addresses) MUST be independent from human-readable labels/titles.

Required behavior:
- Label/title edits must not force identity changes.
- Identity changes must be treated as explicit migrations with provenance.

**Rationale:**
Separating identity from labels preserves durable references and prevents link breakage when wording is improved.

**Detection rule (what to scan for):**
- Scan diffs for simultaneous ID/address rewrites paired only with wording/label changes.
- Flag ID churn without migration intent records.
- Practical check:
  - run `python scripts/validate_node_frontmatter.py`
  - run `python scripts/validate_internal_links.py`
  - compare old/new IDs for unchanged conceptual objects.

**Remediation rule:**
- Revert unnecessary identity mutations and keep label-only edits.
- If identity must change, add migration/deprecation records and update all inbound references atomically.

---

## Invariant A4 — Deprecate-not-delete policy

**Invariant statement (testable):**
Canonical or referenced governed artifacts MUST be deprecated rather than deleted.

**Rationale:**
Deprecation preserves historical traceability, prior decisions, and graph continuity required for long-horizon theological governance.

**Detection rule (what to scan for):**
- Scan git diff for file deletions in governed paths (`docs/`, `ontology/`, `data/claims/`, `data/graph/`, `schemas/`, `schema/`).
- Flag deletions lacking an explicit replacement, deprecation marker, or migration note.
- Practical check:
  - review `git diff --name-status` for `D` entries
  - verify each retirement is represented by a deprecation artifact or lifecycle-status update.

**Remediation rule:**
- Restore deleted artifact when history is still relevant.
- Mark lifecycle as `deprecated` and add short migration guidance to successor artifact.
- Only physically remove generated/ephemeral artifacts that are explicitly non-governed.

---

## Enforcement posture

These invariants are mandatory for PR review and should be mirrored in validator automation over time.

The companion checklist is in:
- `docs/governance/pr-architecture-invariants-checklist.md`
