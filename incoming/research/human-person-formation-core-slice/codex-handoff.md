---
object_type: codex_handoff
trust_zone: incoming_research
lifecycle_status: draft
provenance_note: "Created 2026-04-30 for Codex to implement the Human Person and Formation Core Slice after PR #38 live-main rule merge."
reason_for_inclusion: "Give Codex an exact, safe implementation sequence for a narrow feature branch."
review_status: unreviewed
ai_usage_posture: staging_only_not_auto_promote
---

# Codex Handoff: Human Person and Formation Core Slice

## Branch

```bash
git checkout main
git fetch origin --prune --tags
git pull --ff-only origin main
git status
git checkout -b feature/human-person-formation-core-slice
```

## Non-negotiable boundary

This branch is main-project theology/governance architecture only.

Do not add Christian counseling content, diagnosis/treatment guidance, therapy workflows, crisis material, or pastoral-care product logic.

## First task: inspect existing files

Before editing, inspect:

```text
README.md
AI_FRONT_DOOR.md
AGENTS.md
docs/roadmap/theological-buildout-roadmap.md
docs/roadmap/repository-integration-map.md
docs/doctrine/anthropology.md
docs/concepts/README.md
docs/concepts/imago-dei.md
docs/concepts/sin.md
docs/concepts/stewardship.md
docs/concepts/vocation.md
docs/canon/README.md
docs/canon/augustine/README.md
data/claims/README.md
```

Search for existing files or anchors before creating any of these:

```text
personhood
human agency
fallenness
ordered love
suffering and lament
hope
formation
grace
Athanasius
Willard
Nouwen
Keller
Calvin
Luther
```

Do not duplicate an existing node under a different label.

## Implementation option A: safest seed-only PR

Create only:

```text
incoming/research/human-person-formation-core-slice/README.md
incoming/research/human-person-formation-core-slice/research-packet.md
incoming/research/human-person-formation-core-slice/claim-inventory.yaml
incoming/research/human-person-formation-core-slice/graph-object-plan.json
incoming/research/human-person-formation-core-slice/codex-handoff.md
```

This is the lowest-risk PR and should pass as staged research if metadata is valid.

## Implementation option B: research + small concept buildout

After option A, add only 3-5 proposed concept nodes if no duplicates exist:

```text
docs/concepts/personhood.md
docs/concepts/human-agency.md
docs/concepts/ordered-love.md
docs/concepts/formation.md
docs/concepts/grace.md
```

Do not add all concepts in one pass unless validation and review remain easy.

For `fallenness`, first decide whether `docs/concepts/sin.md` should be deepened instead of creating `docs/concepts/fallenness.md`.

For `suffering-and-lament` and `hope`, consider staging as future follow-up if the branch becomes too large.

## Implementation option C: thinker-anchor audit only

Do not create large canon thinker nodes yet unless asked.

Instead, create a small staged note if useful:

```text
incoming/research/human-person-formation-core-slice/thinker-anchor-map.md
```

Use it to map:

- Augustine -> ordered love, fallenness, grace, institutions
- Athanasius -> incarnation, image renewal, human restoration
- Willard -> formation, heart/will, apprenticeship, agency
- Nouwen -> servant leadership, vulnerability, non-dominating power
- Keller -> vocation/work, service, public faithfulness
- Calvin/Luther -> later deepening for grace, work, calling, fallenness

## Suggested PR title

```text
Seed human person and formation core slice
```

## Suggested PR description

```md
## Summary

Seeds the Human Person and Formation Core Slice as staged research for the next theological architecture buildout.

This PR does not promote counseling content, create therapy workflows, or add crisis/diagnosis/treatment guidance.

## Files changed

- `incoming/research/human-person-formation-core-slice/README.md`
- `incoming/research/human-person-formation-core-slice/research-packet.md`
- `incoming/research/human-person-formation-core-slice/claim-inventory.yaml`
- `incoming/research/human-person-formation-core-slice/graph-object-plan.json`
- `incoming/research/human-person-formation-core-slice/codex-handoff.md`

## Invariant impact statement

Preserves repository invariants by staging multi-claim theological research before promotion into doctrine, concept, claim, or graph layers.

No architecture invariant is intentionally changed.

## Trust zone declaration

Touched trust zones:

- `incoming_research`
- optionally `proposed` if concept nodes are added

No canonical or higher-trust theological zone depends on lower-trust material.

## Provenance note update

Every added file includes a metadata/provenance note. No existing canonical provenance note is changed unless a concept-node audit patch is explicitly included.

## Deprecation plan

No structures are deprecated.

## Drift check

Old rule preserved: staged material does not silently become doctrine or graph truth.

Intentional change: adds a staged research packet and optional small concept-node candidates for the human-person/formation slice.

Unchanged surface: no counseling side quest activation; no runtime agent work; no claim/graph promotion unless separately reviewed.

## Validation

- [ ] Ran default validation or documented why not.
```

## Validation commands

Use the repo's existing validation commands. At minimum, try:

```bash
git status
find incoming/research/human-person-formation-core-slice -maxdepth 2 -type f -print
# If available in repo:
python scripts/validate_metadata.py
python scripts/validate_crossrefs.py
python scripts/validate_trust_zones.py
./scripts/overnight_maintenance.sh --dry-run
```

If a validation script name differs, inspect `.github/workflows/` and use the scripts referenced there.

## Stop conditions

Stop and report instead of forcing the change if:

- concept files already exist under different names;
- tag registry rejects proposed tags;
- node type or trust-zone metadata is unclear;
- validation fails for existing unrelated files;
- changes require editing schema/validators;
- branch grows into counseling or agent-runtime content.
