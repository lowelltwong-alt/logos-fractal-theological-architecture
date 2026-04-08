---
object_type: operations_runbook
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-08 to operationalize safe branch consolidation and GitHub self-checking controls."
reason_for_inclusion: "Provide a repeatable process to clean branch sprawl while preserving unmerged value and enforcing coherent repository checks."
---

# Branch Cleanup and Protection Runbook

## Goal
Safely reduce branch sprawl while preserving important unmerged work and enforcing coherent GitHub self-checks.

## Safety first
1. Protect `main` before cleanup.
2. Create a backup tag on the current `main` tip.
3. Only delete a branch after merge confirmation or archival tagging.

## Step-by-step process

### 1) Establish protections in GitHub
In **GitHub → Settings → Rules → Rulesets**, create/update an active ruleset targeting `refs/heads/main`.

Required rule settings:
- Require pull request before merge.
- Require at least **1 approval**.
- Require status checks to pass.
- Require branch to be up to date before merge.
- Require conversation resolution before merge.
- Disallow force pushes.
- Restrict direct pushes.

Required status checks:
- `Metadata schema validator`
- `Trust-zone policy validator`
- `Docs link/lint check`

Reference machine-readable policy: `.github/rulesets/main-canonical-ruleset.json`.

### 2) Enable automatic branch cleanup
In **GitHub → Settings → General**, enable **Automatically delete head branches**.

### 3) Snapshot backup
From a synchronized local checkout:
```bash
git checkout main
git pull --ff-only
git tag backup/pre-cleanup-YYYY-MM-DD
git push origin backup/pre-cleanup-YYYY-MM-DD
```

### 4) Inventory branches
Use:
```bash
git fetch --all --prune
git branch -r --sort=-committerdate
```
Classify each branch as:
- merge-now
- keep-active
- archive
- delete

### 5) Merge discipline
- Merge in small batches.
- Keep governance and validation changes in dedicated PRs.
- Resolve conflicts by preserving canonical governance constraints.

### 6) Archive before delete
For any unmerged branch with potential future value:
```bash
git tag archive/<branch>-YYYY-MM-DD <sha>
git push origin archive/<branch>-YYYY-MM-DD
```
Then delete the branch.

### 7) Enforce self-checking CI
Require these checks on PRs to `main`:
- `Metadata schema validator` (runs `scripts/validate_governance_metadata.py`)
- `Trust-zone policy validator` (runs `scripts/validate_trust_zone_vocabulary.py`)
- `Docs link/lint check` (runs `scripts/validate_internal_links.py --all-markdown`)

## Suggested branch cadence
- Weekly branch review.
- Auto-delete branches after merge.
- Keep branch naming explicit: `feat/`, `fix/`, `docs/`, `governance/`.

## Definition of done
- Branch inventory completed.
- All risky branches archived or merged.
- Protected branch rules live.
- Required validation checks enforced.
- Worktree clean.

## Decision ledger backlink

Justification record: `DL-PR-0019` in `docs/governance/pr-decision-ledger-2026-04-08.md`.
