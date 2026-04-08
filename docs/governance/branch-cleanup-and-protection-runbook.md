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
Configure branch protection or rulesets for `main`:
- Require pull requests before merge.
- Require status checks to pass.
- Require branch to be up to date before merge.
- Block force pushes and direct pushes.
- Require conversation resolution before merge.

### 2) Snapshot backup
From a synchronized local checkout:
```bash
git checkout main
git pull --ff-only
git tag backup/pre-cleanup-YYYY-MM-DD
git push origin backup/pre-cleanup-YYYY-MM-DD
```

### 3) Inventory branches
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

### 4) Merge discipline
- Merge in small batches.
- Keep governance and validation changes in dedicated PRs.
- Resolve conflicts by preserving canonical governance constraints.

### 5) Archive before delete
For any unmerged branch with potential future value:
```bash
git tag archive/<branch>-YYYY-MM-DD <sha>
git push origin archive/<branch>-YYYY-MM-DD
```
Then delete the branch.

### 6) Enforce self-checking CI
Require the `Governance Validation` GitHub Action check on PRs to `main`.
This check runs `scripts/run_ci_validations.sh`.

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
