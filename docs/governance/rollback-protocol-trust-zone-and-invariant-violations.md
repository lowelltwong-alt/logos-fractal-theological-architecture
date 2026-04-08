---
object_type: governance_runbook
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-08 to standardize rollback handling when a merge violates trust-zone or architecture-invariant rules."
reason_for_inclusion: "Provide a deterministic rollback path that restores canonical integrity and preserves auditability after governance-breaking merges."
---

# Rollback Protocol for Trust-Zone and Invariant Violations

## Trigger conditions
Run this protocol immediately when a merged change is found to do either of the following:
1. Violates trust-zone dependency constraints (for example, higher-trust artifacts depending on lower-trust artifacts).
2. Violates an architecture invariant defined in canonical governance.

## Severity classification
- **SEV-1 (immediate rollback):** Canonical branch integrity is currently broken.
- **SEV-2 (time-boxed rollback):** Violation is real but contained; rollback must complete within 24 hours.

## Mandatory response timeline
1. **Detect and declare (within 30 minutes):** Open an incident issue documenting violating merge commit(s), impacted files, and violated rule(s).
2. **Contain (within 60 minutes):** Pause additional merges to `main` until rollback completes or incident owner declares safe continuation.
3. **Rollback execution (SEV-1 immediately, SEV-2 within 24 hours):** Revert violating merge(s) on a dedicated rollback branch and open expedited PR.
4. **Re-validation before re-merge:** Run governance validations and confirm trust-zone and invariant compliance.
5. **Post-incident documentation (within 24 hours of rollback):** Record root cause and prevention actions in governance decision ledger.

## Execution procedure

### 1) Open incident record
Create issue title:
`Rollback Incident: <short violation summary> (<YYYY-MM-DD>)`

Issue body must include:
- violating PR/merge SHA
- violated trust-zone or invariant rule(s)
- impacted canonical artifacts
- severity (SEV-1 or SEV-2)
- incident owner

### 2) Prepare rollback branch
```bash
git checkout main
git pull --ff-only
git checkout -b rollback/<incident-id>
git revert -m 1 <merge_commit_sha>
```
If multiple merges are involved, revert in reverse chronological order.

### 3) Validate rollback branch
Run canonical checks before opening rollback PR:
- `python3 scripts/validate_governance_metadata.py`
- `python3 scripts/validate_trust_zone_vocabulary.py`
- `python3 scripts/validate_internal_links.py --all-markdown`

### 4) Open expedited rollback PR
PR title format:
`Rollback: <incident-id> trust-zone/invariant violation`

PR description must include:
- violated rule(s)
- reverted commit(s)
- confirmation of restored compliance
- follow-up hardening actions

### 5) Merge and lock confirmation
After merge:
1. Confirm `main` is compliant via CI checks.
2. Link merged rollback PR in incident issue.
3. Close incident only after decision-ledger entry is recorded.

## Follow-up hardening requirements
Within 7 days of incident closure:
- Add or tighten automated checks that would have prevented the violation.
- Update PR template guidance if human review criteria were ambiguous.
- Document policy clarifications in canonical governance docs.

## Definition of done
- Violating merge reverted from `main`.
- Canonical validations green.
- Incident issue closed with root cause and prevention plan.
- Decision ledger updated with final disposition.
