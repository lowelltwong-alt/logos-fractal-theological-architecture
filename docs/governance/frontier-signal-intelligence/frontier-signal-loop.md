---
object_type: governance_process
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: frontier_signal_loop_guidance
provenance_note: "Created 2026-05-01 as the required loop for frontier signal monitoring and routing."
reason_for_inclusion: "Define a safe monitor-capture-score-route-review loop for high-leverage external discoveries."
---

# Frontier Signal Loop

## Purpose

The Frontier Signal Loop turns external discoveries into reviewable repo inputs.

It is not an autonomous improvement engine. It is a governed intake and routing process.

## Loop

### 1. Monitor

Watch defined source classes, including math, AI, algorithms, ontology/KG standards, source licensing, security research, and theological scholarship.

### 2. Capture

Record the signal as a watch item or staged research item. Preserve source, date, claim, uncertainty, and whether source status is verified.

### 3. Classify

Assign a signal type and affected repo surfaces.

Examples:

- `frontier_math`
- `formal_verification`
- `ai_capability`
- `source_licensing`
- `security_prompt_injection`
- `agent_skill_discovery`

### 4. Score

Score novelty, relevance, impact radius, source quality, verification quality, urgency, risk, and route fit.

### 5. Route

Route through the AI work router. Do not bypass the router.

### 6. Stage

Stage the signal under `incoming/research/` or another approved staging surface.

### 7. Review

Require human review before promotion. Require specialist review when the signal affects theology, Bible/source policy, claims, graph objects, schemas, validators, or agent/skill runtime behavior.

### 8. Promote, reject, or defer

Promotion must use the correct route. Rejection should preserve a short audit note when high signal. Deferral should name the trigger that would reopen the item.

### 9. Router update check

If the signal changes how AI work should be routed, update `AI_WORK_START_HERE.md`, the route table, the settings matrix, or templates.

### 10. Registry update check

If the signal affects source registries, skill registries, claim objects, graph objects, or validators, open a follow-up PR through the correct route.
