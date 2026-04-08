# Logos Exceptions Lake Pack

This directory adds a governed exceptions / learning-loop layer to the Logos Fractal Theological Architecture repository.

It treats exceptions as structured pressure signals tied to a canonical 9-layer address:

`root.domain.capability.entity.instance.state.expectation.exception.adaptation`

The pack includes:

- architecture notes and an ADR
- JSON Schema contracts for the core learning-loop objects
- example records for every object type
- validation and scoring tools
- generated sample priority artifacts

## Core design choices

- **Stable operating locus:** layers 1-7 capture where the work lives
- **Failure and learning suffix:** layers 8-9 capture deviation and adaptation
- **AIRCA bridge:** architect, inform, rank, commit, act map directly to the record types
- **Governance layering:** worldview, institutional, operating, human, technical are first-class enums
- **Pressure vector:** theological, psychological, moral, political, economic, cultural lenses are scored per exception
- **Append-only promotion path:** local fixes can be promoted to rule, taxonomy, ontology, policy, or authority changes

## Layout

```text
exceptions-lake/schema/      JSON Schema contracts
exceptions-lake/examples/    sample records and a stitched demo dataset
exceptions-lake/tools/       validation and scoring scripts
exceptions-lake/docs/        architecture notes and ADRs
exceptions-lake/build/       generated artifacts
```

## Quickstart

```bash
python exceptions-lake/tools/validate_examples.py
python exceptions-lake/tools/build_priority_report.py
```
