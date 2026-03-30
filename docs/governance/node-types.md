# Node Types

## Purpose

Node types define the major structural families used in the Logos repository.

They help keep the project recursive, comparable, and ontology-ready without turning every file into a one-off format.

A node type is not just a label. It signals what kind of object the file is, what role it plays in the architecture, and how it should relate to other nodes.

## Core rule

Prefer existing node types before inventing new ones.

A new node type should be added only when the new object cannot fit an existing type without meaningful distortion.

## Approved node types

### `canon_thinker`
Use for major thinker nodes in the canon layer.

Examples:
- Augustine
- Aquinas
- Calvin
- Athanasius

Typical role:
- identify why the thinker belongs in the project
- map major theological contributions
- define concept-level child nodes
- support alignment and tension mapping

### `doctrine_node`
Use for stable doctrine-level objects.

Examples:
- anthropology
- grace
- creation
- sin
- ecclesiology

Typical role:
- define a major theological object
- support tradition comparison
- serve as upstream grounding for applied reasoning

### `concept_node`
Use for reusable conceptual objects that recur across thinkers, doctrines, or traditions.

Examples:
- imago Dei
- ordered love
- institutions
- vocation
- natural law

Typical role:
- make repeated concepts independently retrievable
- support cross-thinker comparison
- prepare repeated concepts for ontology promotion

### `tradition_node`
Use for major tradition-level objects.

Examples:
- patristic
- catholic
- reformed
- orthodox
- evangelical

Typical role:
- describe shared emphases and constraints in a tradition
- map internal variety without erasing common structure
- support later comparison across traditions

### `comparison_node`
Use for direct comparison between thinkers, doctrines, concepts, or traditions.

Examples:
- Augustine vs Aquinas on order
- Calvin vs Wesley on formation
- Reformed vs Orthodox on grace

Typical role:
- make agreement and tension explicit
- identify alignment, disalignment, and translation needs
- reduce buried comparison in prose-only form

### `synthesis_node`
Use for integrative nodes that pull multiple upstream nodes together into a project-level argument.

Examples:
- Christian AI anthropology map
- AI governance limits
- theology-to-governance translation map

Typical role:
- integrate multiple node families
- support practical theological reasoning
- connect source architecture to downstream use

### `governance_node`
Use for project-internal rule documents.

Examples:
- ontology discipline
- anchor conventions
- tag registry
- relationship registry
- node types

Typical role:
- stabilize the architecture itself
- guide contributors
- reduce structural and vocabulary drift

### `application_node`
Use for applied downstream examples, worked cases, or use-case buildouts.

Examples:
- nonprofit governance example
- AI hiring workflow example
- public-institution use case

Typical role:
- show how the architecture behaves in practice
- connect theology to workflow or governance design
- remain downstream of canon, doctrine, and synthesis layers

### `crosswalk_node`
Use for translation or mapping files between major systems.

Examples:
- Logos to LAIRCA
- LAIRCA to AIRCA
- doctrine to governance crosswalk

Typical role:
- map one system into another
- preserve lineage and traceability
- show how upstream claims become downstream constraints or actions

## Optional future node types

These should not be used until the project actually needs them.

### `weighting_profile`
Use when the project begins creating formal weighting maps for traditions, institutions, or use cases.

### `ordering_profile`
Use when the project begins creating explicit priority or consultation order maps.

### `derivation_node`
Use when a file’s main purpose is to trace a concept from source theology into downstream implications.

## When not to add a new node type

Do not add a new node type just because:
- a file feels special
- a concept is interesting
- a contributor prefers a new label
- two files differ in style but not in function

If the function is already covered by an approved node type, reuse the existing type.

## Naming rule

Node type names should be:
- lowercase
- underscore-separated
- stable
- function-based rather than fashionable

## Extension note

For scripture, interpretation, translation, manuscript, original-language, and boundary-source node-type extensions, see:

- `node-types-scripture-and-boundary-extension.md`

## Summary principle

Use as few node types as necessary, but enough to keep the architecture clear.

Too few node types flatten real distinctions.
Too many node types create taxonomy drift.

The goal is disciplined recursive growth.
