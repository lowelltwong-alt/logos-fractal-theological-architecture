# Logos repo cleanup runbook

## Goal
Clean the repository in a private/local staging workspace first, then merge a single cleanup branch back into the current public repo unless a privacy audit forces a reset.

## Working assumptions
- Public repo stays canonical.
- Cleanup happens on one consolidation branch, not across many direct-to-main merges.
- Old branches are deleted only after their work is either merged, cherry-picked, or explicitly discarded.
- History is audited before any destructive public cleanup.

## Phase 0 — Freeze and snapshot
1. Stop merging new feature branches into `main`.
2. Fetch everything and create a safety tag.
3. Create one cleanup branch from `main`.
4. Export branch and PR inventory before touching anything.

### Suggested commands
```bash
git fetch origin --prune --tags
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
git tag -a "pre-cleanup-$STAMP" -m "Snapshot before repo cleanup"
git push origin "pre-cleanup-$STAMP"
git switch -c cleanup/repo-consolidation origin/main
```

If you use GitHub Desktop, create an annotated tag first, then create `cleanup/repo-consolidation` from `main`.

## Phase 1 — Privacy and history audit
Run this before any public restructuring.

### Check for a private companion or submodule
```bash
git submodule status || true
if [ -f .gitmodules ]; then cat .gitmodules; else echo "No .gitmodules file found"; fi
```

### Check for likely sensitive patterns in tracked history
```bash
git log --all --name-only --pretty=format: | sort -u > tracked-paths.txt
rg -n "(\.env|secret|token|credential|private|report)" tracked-paths.txt || true
```

### Check for likely secret strings in history
```bash
git log -S'OPENAI_API_KEY' --all || true
git log -S'ANTHROPIC_API_KEY' --all || true
git log -S'-----BEGIN' --all || true
```

### Check ignored local-only artifacts
```bash
cat .gitignore
```

If you find secrets in Git history, stop and either:
- rewrite history with `git filter-repo`, then force-push carefully, or
- create a clean new public repo from a sanitized export.

If you do **not** find sensitive history, keep the current repo and clean it in place.

## Phase 2 — Triage what actually needs cleanup
Do not treat this as a content-expansion cycle. Treat it as a normalization cycle.

### Structural decisions to make once
1. `docs/doctrine/` remains canonical.
2. `docs/doctrines/` becomes redirect-only until links are migrated, then gets retired.
3. `schemas/` is the canonical machine-contract root.
4. `schema/` remains deprecated legacy template territory.
5. `docs/schemas/` remains prose/reference only.
6. `ontology/` remains a non-canonical draft/reference layer in this wave; do not migrate it yet.
7. Separate governed nodes from meta/governance prose so validators are not checking the wrong files.

### Validation problems to close
- Wire validators to the actual JSON schema files.
- Decide whether governance/roadmap docs should get full frontmatter or be excluded from node validation.
- Fix broken internal links.
- Remove or soften README links that point to runtime-only paths.
- Make required branch checks match the workflows that actually matter.

## Phase 3 — Open PR triage
Review every open PR and decide one of three actions:
- **Cherry-pick into cleanup branch**
- **Supersede and close**
- **Leave for later after cleanup**

### Suggested current triage posture
- `Normalize layer and node metadata...` → cherry-pick only after canonical path and schema-folder decisions are locked.
- `Add Codex merge-alignment spine...` → mine for useful documentation only.
- `Reinforce exceptions-lake...` and `Add exceptions lake import pack` → keep only if exceptions-lake remains a priority in this cleanup wave.
- `Add canonical external mapping grammar...` → review after schema/ontology boundaries are settled.
- `feat: add trinity network layer...` → postpone until cleanup is merged; avoid mixing major content expansion into a structural cleanup.

## Phase 4 — Consolidate onto one branch
Build the cleanup branch in waves.

### Wave A — path normalization
- Keep `docs/doctrine/` as the canonical doctrine editing surface.
- Keep `docs/doctrines/` as redirect stubs only.
- Treat `schemas/` as the canonical machine-readable contract root.
- Leave `schema/` in place as deprecated legacy templates.
- Leave `docs/schemas/` in place as prose/reference-only schema docs.
- Leave `ontology/` untouched apart from governance wording about path authority.
- Add README notes where necessary so old paths do not invite new edits.

### Wave B — validation alignment
- Make frontmatter and claim validation consume the canonical schema definitions.
- Adjust validation scope for governance/meta docs.
- Add a simple validator summary artifact to CI.

### Wave C — link and README cleanup
- Fix broken markdown links.
- Replace runtime-only README references with one of:
  - a note that the directory is generated at runtime, or
  - committed placeholder `.gitkeep` directories, or
  - documentation that clearly labels those paths as generated outputs.

### Wave D — ruleset cleanup
- Confirm required checks match actual workflow job names.
- Add structure and cross-reference validation to required checks if you want them to block merges.
- Keep code-owner review on governed paths.

## Phase 5 — Merge and prune
1. Open one PR: `cleanup/repo-consolidation` → `main`.
2. Merge it only after CI is green.
3. Close open PRs that have been superseded.
4. Delete their head branches.
5. Turn on automatic deletion of head branches.
6. Delete stale remote branches after confirming they are merged or intentionally abandoned.

## Phase 6 — Post-cleanup hardening
- Tag the post-cleanup state.
- Publish a short release note or changelog entry describing path normalization and validation changes.
- Keep future work on short-lived branches only.
- Prefer one active cleanup or feature wave at a time.

## Recommended branch policy after cleanup
- Keep: `main`
- Optional temporary: `staging` or `release/*`
- Delete: superseded `codex/*` and stale feature branches

## Definition of done
You are done when:
- there is one canonical folder for doctrine content,
- there is one canonical schema folder,
- validators use the real schema contracts,
- broken links are reduced to intentional exceptions only,
- open PRs are either merged, cherry-picked, or closed,
- most branches are gone,
- `main` is protected and boring.
