# Solo Maintainer Governance Baseline

This repository is currently governed in solo-maintainer mode.

That means the system is designed to be easy for one serious builder to operate now, while remaining upgradeable later.

## Principle

Use the lightest rule that preserves structural integrity.

Do not require committee-grade process before the project has committee-grade staffing.

## Current operating mode

For now, the maintainer may perform all four functions personally:

- author
- reviewer
- promoter
- publisher

This is permitted only because the repository is still in formative buildout.

## Minimum required checks in solo mode

Even in solo mode, every meaningful addition should still declare:

- object type
- trust zone
- lifecycle status
- short provenance note
- reason for inclusion

If a change cannot satisfy those five things, it should stay in notes or backlog rather than enter the governed core.

## Solo-mode promotion rule

A solo maintainer may promote material to canonical or tradition-scoped status when all of the following are true:

1. the item is typed correctly
2. the trust zone is declared
3. a provenance note is present
4. the maintainer can explain the promotion in plain language
5. the item does not silently depend on inferred or learning-sidecar content

## Lightweight review note

In solo mode, review may be satisfied by a short structured self-review note inside the commit, PR body, or adjacent markdown note.

Recommended format:

- what changed
- why it belongs
- what trust zone it belongs to
- what would make it need future review

## Deferred controls

The following controls are encouraged later, but are not required now:

- second-person approval
- CODEOWNERS enforcement by domain
- merge gates by trust zone
- formal release checklist
- schema migration board
- separate editorial and publication roles

## Upgrade path

When additional contributors arrive, the repository should upgrade in this order:

1. require PR review for schema changes
2. require second-person approval for canonical promotion
3. assign domain ownership by folder
4. add release gates for published artifacts
5. separate proposer, reviewer, and promoter roles

## Rule of mercy and clarity

The system should be strict on structure and light on ceremony.

The project should never become so process-heavy that the lone maintainer stops building.

The right early bias is:

- preserve ontology integrity
- preserve provenance
- keep promotion explainable
- avoid unnecessary friction
