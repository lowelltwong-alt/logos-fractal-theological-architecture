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

Create branch `feature/human-person-formation-core-slice` from live `main` after running the standard live-main startup protocol from `AGENTS.md`.

## Non-negotiable boundary

This branch is main-project theology/governance architecture only.

Do not add Christian counseling content, diagnosis/treatment guidance, therapy workflows, crisis material, or pastoral-care product logic.

## First task: inspect existing files

Before editing, inspect the current README, AI front door, agent instructions, theological roadmap, repository integration map, anthropology doctrine file, existing concept files for imago Dei, sin, stewardship, and vocation, the canon README, the Augustine canon README, and the claims README.

Search for existing files or anchors before creating any of these:

- personhood
- human agency
- fallenness
- ordered love
- suffering and lament
- hope
- formation
- grace
- Athanasius
- Willard
- Nouwen
- Keller
- Calvin
- Luther

Do not duplicate an existing node under a different label.

## Implementation option A: safest seed-only PR

Create only the staged research files in this packet:

- packet README
- research packet
- claim inventory YAML
- graph object plan JSON
- Codex handoff

This is the lowest-risk PR and should pass as staged research if metadata is valid.

## Implementation option B: research + small concept buildout

After option A, add only three to five proposed concept nodes if no duplicates exist.

Recommended first candidates:

- personhood
- human agency
- ordered love
- formation
- grace

Do not add all concepts in one pass unless validation and review remain easy.

For fallenness, first decide whether the existing sin concept should be deepened instead of creating a separate fallenness concept file.

For suffering and lament and hope, consider staging them as future follow-up if the branch becomes too large.

## Implementation option C: thinker-anchor audit only

Do not create large canon thinker nodes yet unless asked.

Instead, create a small staged thinker-anchor map in this packet.

Use it to map:

- Augustine -> ordered love, fallenness, grace, institutions
- Athanasius -> incarnation, image renewal, human restoration
- Willard -> formation, heart/will, apprenticeship, agency
- Nouwen -> servant leadership, vulnerability, non-dominating power
- Keller -> vocation/work, service, public faithfulness
- Calvin/Luther -> later deepening for grace, work, calling, fallenness

## Suggested PR title

`Seed human person and formation core slice`

## Suggested PR description content

Summary: seed the Human Person and Formation Core Slice as staged research for the next theological architecture buildout.

Boundary statement: this PR does not promote counseling content, create therapy workflows, or add crisis/diagnosis/treatment guidance.

Invariant impact statement: preserves repository invariants by staging multi-claim theological research before promotion into doctrine, concept, claim, or graph layers.

Trust zone declaration: touched trust zone is `incoming_research`; optionally `proposed` if concept nodes are added. No canonical or higher-trust theological zone depends on lower-trust material.

Provenance note update: every added staged file includes a metadata/provenance note. No existing canonical provenance note is changed unless a concept-node audit patch is explicitly included.

Deprecation plan: no structures are deprecated.

Drift check: staged material does not silently become doctrine or graph truth.

Validation: run the repo's existing validation commands or document why a command was not available.

## Validation commands

Use the repo's existing validation commands. At minimum, try:

- `git status`
- list the files in the staged research packet
- run the metadata validator if available
- run the cross-reference validator if available
- run the trust-zone validator if available
- run the overnight maintenance dry run if available

If a validation script name differs, inspect the workflows and use the scripts referenced there.

## Stop conditions

Stop and report instead of forcing the change if:

- concept files already exist under different names;
- tag registry rejects proposed tags;
- node type or trust-zone metadata is unclear;
- validation fails for existing unrelated files;
- changes require editing schema/validators;
- branch grows into counseling or agent-runtime content.
