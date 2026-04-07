---
object_type: reading_guide
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created on 2026-04-07 to make pilot doctrine networks legible to maintainers and future users."
reason_for_inclusion: "Help readers understand the difference between topic, view, assessment, and relationship object so the network remains useful rather than merely complex."
---

# How To Read A Doctrine Network

## Four core object layers

### Doctrine Topic
A doctrine topic is the stable thing under discussion.

Example:
- Trinity

A topic should not carry approval or rejection language by itself.

### Doctrine View
A doctrine view is one concrete formulation of the topic.

Examples under Trinity include:
- Nicene core
- Latin filioque
- Eastern monarchy of the Father
- Arian

A view is not yet a judgment.
It is a formulation.

### Doctrine Assessment
A doctrine assessment is a judgment applied to a specific view under an explicit baseline.

Examples:
- Nicene core affirmed under project-christian-core
- Arian rejected under project-christian-core

Assessments belong to views, not to the topic identity.

### Relationship Object
A relationship object is a governed record that connects two objects through an explicit relationship type.

Examples:
- topic has_view view
- view assessed_by assessment
- view grounded_in_passage passage
- view contrasts_with another view
- view neighboring_view another view

## Why the separation matters

Without separation, doctrine files become unstable.
The topic itself gets overloaded with one tradition's judgment, the view loses clarity, and the reasoning trail becomes hard to inspect.

This structure prevents that collapse.

## How to read the Trinity pilot

Start with the topic:
- Trinity

Then inspect the available views.

Then inspect the assessments under a stated baseline.

Then inspect the relationship objects to see:
- which views belong under the topic
- which assessments judge which views
- which passages ground a given view
- which views contrast with or neighbor other views

## What this architecture makes possible

This architecture makes it possible to:

- preserve rejected views without erasing them
- represent disagreement honestly
- attach scriptural grounding to specific views
- compare neighboring formulations without collapsing them
- scale later into coherence mapping and AI retrieval

## What this architecture does not yet do

This reading model does not yet compute doctrinal tension automatically.
It does not yet tell you which view is correct by itself.
It gives you a governed structure in which those judgments can be represented, traced, and expanded.
