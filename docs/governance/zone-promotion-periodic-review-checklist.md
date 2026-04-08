---
object_type: trust_zone_promotion_checklist
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-08 to standardize recurring promotion reviews across proposed, inferred, and learning-sidecar artifacts."
reason_for_inclusion: "Provide a lightweight periodic checklist so trust-zone promotions (for example proposed -> canonical) are explicit, repeatable, and auditable."
---

# Trust-Zone Promotion Periodic Review Checklist

Review cadence recommendation: run monthly and before any release-tag or major merge window.

## 1) Queue assembly

- Collect candidate artifacts currently in `proposed`, `inferred`, and `learning-sidecar`.
- Group candidates by destination request (`canonical`, `tradition-scoped`, or remain non-canonical).
- Verify each candidate has required governance metadata:
  - `object_type`
  - `trust_zone`
  - `lifecycle_status`
  - `provenance_note`
  - `reason_for_inclusion`

## 2) Evidence and provenance gate

- Confirm provenance note is specific (what source, when, by whom/what process).
- Confirm the artifact cites or links to reviewable evidence.
- Confirm evidence trust is equal or higher than the candidate’s target trust zone.
- Reject promotion if source evidence is ambiguous, inferred-only, or missing.

## 3) Dependency direction gate

- For each candidate, inspect outbound references/links.
- If target zone is `canonical`, ensure dependencies are canonical only.
- If target zone is `tradition-scoped`, ensure dependencies are tradition-scoped or canonical.
- Block promotion when any dependency direction violates `architecture-invariants.md` (A1).

## 4) Role-separation and identity gate

- Verify doctrine topic/view/assessment roles are not collapsed.
- Verify identity fields are stable and independent from labels.
- If identity changed, require an explicit migration/deprecation note.

## 5) Decision and recording gate

- Record reviewer, date, decision, and rationale.
- If promoted, update trust zone and add a backlink to evidence.
- If not promoted, retain in-place and add a short remediation action list.
- If superseded, mark deprecated rather than deleting.

## 6) Post-review validation commands

- `python3 scripts/validate_governance_metadata.py`
- `python3 scripts/validate_trust_zone_vocabulary.py`
- `python3 scripts/validate_cross_references.py`
- `python3 scripts/validate_internal_links.py`

## Promotion log stub

| Date | Artifact | From zone | To zone | Reviewer | Decision | Notes |
|---|---|---|---|---|---|---|
