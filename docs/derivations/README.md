# Derivations

This branch holds the logic chains that turn theology into ethics, governance, LAIRCA configuration, and institutional application.

## Why derivations matter

A theological architecture is not yet useful merely because it contains doctrines, sources, and conceptual categories. It becomes operationally meaningful when it can show how one layer gives rise to the next.

That is the work of derivation.

A derivation chain makes visible how:
- theological claims generate moral implications
- moral implications generate governance requirements
- governance requirements shape decision architecture
- decision architecture constrains or enables institutional applications

Without derivation, a repository like this can become a library. With derivation, it becomes an architecture.

## Canonical derivation chain

The standard chain for this project is:

`theology -> ethics -> governance -> LAIRCA -> institutional application`

This chain is intentionally directional.
It resists the temptation to begin with a desired application and retrofit theology afterward.

## What each layer does

### Theology
This layer identifies the doctrinal source material, metaphysical assumptions, and theological commitments that shape the rest of the framework.

### Ethics
This layer translates theology into moral implications. It asks what kinds of conduct, limits, obligations, and goods follow from the theological claims.

### Governance
This layer translates ethical implications into structures of authority, review, accountability, escalation, and boundary-setting.

### LAIRCA
This layer shows how theological and governance commitments configure Architect, Inform, Rank, Commit, and Act in a Christian decision architecture.

### Institutional application
This layer shows how the framework behaves in a real use case such as nonprofit governance, ministry leadership, AI review, or policy design.

## Design rules for derivation files

1. Start upstream, not downstream.
2. Name the theological sources explicitly.
3. Preserve intermediate steps instead of jumping from doctrine to application.
4. Show where prudential judgment is required.
5. Record what remains fixed and what is context-sensitive.
6. Make the derivation inspectable by both humans and machines.

## Questions every derivation should answer

1. Which doctrines and sources are doing the work?
2. What ethical claims follow from them?
3. What governance structures become necessary?
4. How does this alter LAIRCA stages?
5. What practical institutional behavior follows?
6. What are the known risks, tensions, or unresolved questions?

## Why derivation is crucial for AI governance

AI systems often compress or hide intermediate reasoning. A derivation file does the opposite. It slows the architecture down enough to preserve accountability.

This matters because Christian institutions should be able to explain not only what they did, but why that action followed from a coherent theological and moral structure.

## Typical failure modes derivation is meant to prevent

- theology being reduced to branding language
- ethics being asserted without doctrinal grounding
- governance rules appearing arbitrary
- technical systems being adopted because they are available rather than justified
- institutions skipping directly from desire to implementation

## Recommended first derivation

The first full derivation in this repository should be:

`anthropology -> ethics of dignity and responsibility -> AI governance requirements -> LAIRCA configuration -> institutional review workflow`

That derivation is especially important because anthropology is where Christian claims about personhood, agency, dignity, and answerability most directly confront AI-era temptations toward depersonalization and automation drift.

## Related files to build next

- anthropology doctrine node
- AI governance derivation example
- nonprofit governance derivation example
- derivation schema or sidecar template
