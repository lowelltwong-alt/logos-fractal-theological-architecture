# Fractal Rules

## Purpose

This file defines what it means for the repository to be genuinely fractal rather than merely nested.

A fractal repository does not just contain many folders. It repeats the same structural logic at multiple levels, with scale changing but the governing pattern remaining recognizably the same.

This file should be read together with:
- `ontology-discipline.md`
- `anchor-conventions.md`
- `tag-registry.md`
- `relationship-registry.md`
- `node-types.md`
- `scripture-taxonomy-and-ontology.md`
- `textual-traditions-translation-and-noncanonical-sources.md`
- `translation-trust-and-sectarian-classification.md`
- `noncanonical-and-heresy-classification.md`

## Core principle

Human contributors should record local, immediate structure.
Machines may infer larger recursive structure from governed local assertions.

That means the repository should prefer:
- direct parent relationships over manually listing every ancestor
- direct child relationships over manually listing every descendant
- direct broader or narrower relations over hand-written transitive chains
- explicit local provenance over vague historical implication

## What makes the repository fractal

The same structural shell should recur across levels such as:
- repository root
- major branch or domain root
- folder-level README
- node file
- graph or concordance object
- relationship object where needed

The level changes.
The grammar should not change casually.

## Fractal shell rule

Where appropriate, each serious branch should eventually be able to express the same structural dimensions:
- identity
- classification
- relationships
- content
- provenance
- review state
- downstream machine-readable connection points

The exact fields may vary by layer, but the pattern should remain recognizable.

## Local-direct structure rule

Contributors should prefer immediate, local structure over bloated global listing.

Preferred:
- direct `parents`
- direct `children`
- direct `broader`
- direct `narrower`
- direct typed edges such as `grounds`, `constrains`, `aligns_with`, or `derived_from`

Avoid when not necessary:
- manually listing every upstream ancestor
- manually listing every downstream descendant
- filling nodes with pseudo-global graph state that could be inferred more reliably by machines

## Human vs machine rule

### Human-authored layer
Humans should author:
- the local node
- the immediate structural and semantic relationships
- the rationale and provenance
- the confidence and trust boundaries where relevant

### Machine-derived layer
Machines may infer:
- ancestor chains
- descendant chains
- transitive broader/narrower traversals
- concordance expansion
- local-to-global graph maps
- cross-branch clustering where governed relations already exist

This keeps the authored layer lean while preserving rich machine traversal.

## Self-similar README rule

Every serious new branch should aim to have:
- a local README
- a clear statement of purpose
- the branch's relation to the wider repository
- examples of what belongs in the branch
- the branch's key controlled terms, if needed

Examples of branches that should ideally follow this pattern:
- canon
- scripture
- original languages
- translations
- manuscripts
- noncanonical
- graph/concordance domains

## Promotion rule

Fractal growth happens by promotion, not by uncontrolled duplication.

When the same concept, edge, or substructure recurs often enough, promote it into a more reusable node.

That means:
- repeated concepts become concept nodes
- repeated passage clusters become text or pericope nodes
- repeated interpretive methods become hermeneutic nodes
- repeated high-value edges may become relationship objects
- repeated branch patterns may justify local templates or schemas

See also:
- `promotion-thresholds.md`

## Branch recursion rule

A new branch should not invent a totally new structural grammar unless the existing shell cannot represent it without meaningful distortion.

Before adding a new branch, ask:
1. can this be expressed as an existing node type?
2. can this live inside an existing branch with clearer tags and anchors?
3. does it need a new branch because the object type or governance burden is genuinely different?

If a new branch is needed, it should still inherit the repo's larger discipline.

## Edge escalation rule

Not every link should become a first-class relationship object.

Use simple local typed edges by default.
Escalate to a relationship object when the edge itself needs:
- provenance
- rationale
- trust review
- dispute handling
- reuse across multiple contexts
- later supersession

## Trust and boundary recursion rule

Boundary logic should also be fractal.

That means the same discipline should recur across layers where trust matters:
- translation trust
- manuscript confidence
- noncanonical status
- doctrinal alignment
- graph-edge review

The repository should not have one safe layer and several ungoverned side channels.

## Layer integration rule

No branch should become a silent parallel project.

When a major new branch is added, it should normally be integrated in at least three places where relevant:
- governance
- roadmap or integration guidance
- the branch's own local README

This prevents architectural drift through side additions.

## Fractal audit questions

A contributor or reviewer should periodically ask:
- does this branch use the same address logic as the rest of the repository?
- are local relationships immediate rather than bloated?
- are new terms registered?
- are repeated concepts being promoted rather than endlessly duplicated?
- does the branch have clear provenance and review expectations?
- does this branch feel like part of the same repository grammar?

## Summary principle

A fractal repository is not just deeply nested.
It is self-similar, governable, and machine-legible across scales.

The deeper it grows, the more it should still feel like the same architecture.
