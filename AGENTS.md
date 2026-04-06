---
object_type: repository_governance_contract
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-05 from the maintainer's governing contract provided in chat."
reason_for_inclusion: "Keep the working contract on disk at the repo root so future edits follow the same governance rules."
---

# AGENTS.md

## Project intent
This repository is a governed theological ontology project.
Optimize for structural clarity, provenance, and future scalability.
Be strict on structure and light on ceremony.

## Current operating mode
Solo-maintainer mode.
Assume one maintainer currently performs:
- author
- reviewer
- promoter
- publisher

## Non-negotiable rules
- Do not invent new top-level folders unless necessary.
- Keep identity separate from labels.
- Do not let inferred or AI-generated material overwrite canonical material.
- Keep doctrine topic, doctrine view, and doctrine assessment separate.
- Preserve history through deprecation rather than deletion.

## Required metadata for meaningful additions
Every meaningful addition should declare:
- object type
- trust zone
- lifecycle status
- short provenance note
- reason for inclusion

If a change cannot satisfy those five things, keep it in notes/backlog instead of governed core.

## Trust zones
Allowed trust zones:
- canonical
- tradition-scoped
- proposed
- inferred
- deprecated
- learning-sidecar

Lower-trust zones may reference higher-trust zones.
Higher-trust zones may not depend on lower-trust zones.

## File placement
- Governance docs go in `docs/governance/`
- Phase docs go in `docs/`
- Examples go in `examples/`
- Machine-readable manifests go beside the relevant module or example

## Working style
- Prefer small, reviewable edits
- Prefer explicit file creation over broad rewrites
- Explain why a file belongs before adding it
- Keep commit messages short and concrete

## Definition of done
Before finishing:
- check file placement
- check required metadata
- check trust zone correctness
- check provenance note presence
- leave the worktree clean
