# Ordering Profiles

Ordering profiles explain how theological material should be sequenced when moving from source theology toward ethics, governance, and LAIRCA-style decision systems.

This branch exists because theology is not only a library of concepts. It is also an architecture of priorities. The same doctrines may be affirmed across traditions, while their practical ordering differs in ways that strongly affect institutional judgment, AI governance, leadership models, and application design.

## Why ordering matters

Two systems may affirm many of the same theological truths and still produce very different downstream decisions because they place those truths in a different practical order.

For example:
- a system that puts efficiency and execution too early can quietly subordinate personhood and prudence
- a system that foregrounds anthropology and moral accountability will be more cautious about automation and delegated agency
- a system that places Scripture and revelation late in the practical stack may drift toward cultural accommodation even while keeping orthodox vocabulary

Ordering therefore belongs to the architecture, not only to private interpretation.

## What ordering is not

Ordering is not the same thing as doctrine.

Doctrine identifies stable theological objects.
Ordering identifies the practical sequence in which those objects are consulted, interpreted, or activated in judgment.

Ordering is also not the same thing as weighting.
A doctrine can appear early in the sequence but receive less practical force in a particular use case, or it can appear later while still serving as a hard constraint.

## Design rules

1. Keep doctrine objects stable.
2. Treat ordering as an explicit interpretive layer.
3. Make the ordering inspectable by humans and machines.
4. Preserve room for comparative profiles rather than pretending there is only one possible Christian order.
5. Tie ordering choices to use cases so practical consequences are visible.
6. Document blind spots created by each ordering profile.

## Core ordering question

What must come first so that downstream reasoning is not silently distorted by optimization, institutional self-protection, ideology, or hidden metaphysical assumptions?

That question is central to the Logos project because AI-supported systems often smuggle in an order before the user realizes one has already been chosen.

## Recommended baseline sequence

The broad default order for this repository is:

1. Logos and truth
2. doctrine of God
3. Christology
4. revelation and Scripture
5. anthropology and human dignity
6. sin and fallenness
7. wisdom, prudence, and moral reasoning
8. justice, mercy, and neighbor-love
9. vocation, stewardship, and responsibility
10. authority, community, and institutional ordering
11. technology, tools, and mediation
12. application-specific optimization

This sequence is meant to keep technical design downstream of reality, revelation, personhood, moral seriousness, and institutional responsibility.

## Why this baseline works

### Logos and truth first
The project begins with Logos because the architecture assumes that reality is meaningful, ordered, and not reducible to human preference or model output. Truth is not whatever a system predicts most efficiently. Truth comes first, and the system must answer to it.

### God and Christ before human technique
Theology proper and Christology come before institutional design because Christian reasoning is not built from generic moral intuitions upward. It is received from a prior account of God, creation, redemption, and lordship.

### Revelation before interpretation drift
Revelation and Scripture appear early because the project assumes that Christian decision architecture must remain accountable to an authoritative source outside the institution itself.

### Anthropology before optimization
Anthropology comes before efficiency or tool design because the project rejects any architecture that treats persons as merely process inputs, preference bundles, or manageable units of compliance.

### Sin before techno-utopianism
A realistic doctrine of sin must appear before governance and automation become ambitious, otherwise the institution will overestimate neutrality, underestimate corruption, and delegate too much to systems that amplify existing distortions.

### Prudence before scale
Wisdom and prudence precede large-scale application because not every valid principle should be operationalized in the same way or at the same speed.

## Comparative profiles to build next

This repository should eventually include several alternative orderings for comparative work:

### Broad Christian default
A reusable ordering intended to be orthodox, ecumenically legible, and suitable for general Christian institutional use.

### Reformed default
An ordering that may place stronger emphasis on sovereignty, covenant, vocation, common grace, and principled institutional structure.

### Evangelical ministry default
An ordering that may foreground Scripture, conversion, discipleship, mission, and pastoral responsibility.

### Nonprofit governance default
An ordering that may emphasize dignity, stewardship, mission fidelity, transparency, service, and neighbor-love in organizational design.

### AI ethics default
An ordering that may foreground personhood, responsibility, truthfulness, accountability, and limits on delegated agency in machine-assisted environments.

## Risks and blind spots

Every ordering profile creates risks. These should be documented instead of hidden.

Examples:
- a heavily institutional ordering may overprotect hierarchy
- a heavily activist ordering may underweight prudence and formation
- a heavily technical ordering may convert moral problems into process problems
- a heavily abstract ordering may fail to guide real decisions

## Machine-readable implications

Each ordering profile should eventually have an artifact sidecar that records:
- ordering id
- parent framework
- assumptions
- source dependencies
- intended use cases
- exclusions
- hard constraints
- known blind spots
- review cadence
- related weighting profiles

## Recommended companion files in this branch

- `default-lairca-ordering.md`
- `alternative-orderings.md`
- `blind-spot-analysis.md`

## Near-term build sequence

1. complete the default LAIRCA ordering profile
2. create an AI ethics ordering profile
3. create a nonprofit governance ordering profile
4. compare where each profile changes the practical decision path
5. connect those differences to weighting and derivation files
