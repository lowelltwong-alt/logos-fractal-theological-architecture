# Benchmark and Evaluation Layer

## Purpose

This folder holds the benchmark and evaluation surface for the Logos project.

It exists so ontology, dependency, profile, and routing changes can be tested against a stable question corpus rather than judged only by ad hoc impressions.

The benchmark layer should help answer questions like:

- did a profile change improve or degrade route quality?
- did a dependency change break distinction handling?
- did a canon, doctrine, scripture, or lexical update improve grounding?
- did a new ordering or weighting profile distort scope handling?
- did a graph or concordance change create regressions downstream?

## Core principle

A benchmark corpus is not just a list of prompts.

It is a governed regression surface for:
- exegetical answers
- dogmatic answers
- historical theology answers
- pastoral theology answers
- ethics and public theology answers

## Current contents

- `data/benchmarks/question-corpus-v1.yaml` — initial cross-route benchmark corpus

## Recommended use

Use the corpus:
1. before and after major ontology changes
2. before and after profile changes
3. before and after dependency-atlas changes
4. before promoting new benchmark answer sets or gold outlines
5. when comparing tradition-specific response behavior

## Evaluation dimensions

The initial benchmark corpus tracks these scoring dimensions:

- text grounding
- scope correctness
- distinction handling
- tradition fairness
- theological coherence
- pastoral tone
- citation and provenance discipline
- uncertainty honesty

## Build discipline

This layer should remain connected to:
- `README.md`
- `docs/roadmap/repository-integration-map.md`
- `docs/governance/README.md`

It should not become a side folder for random prompts.

The benchmark corpus should stay:
- route-aware
- dependency-aware
- tradition-sensitive
- stable enough for regression use
- extensible enough for later gold-answer outlines, benchmark runs, and impact reports
