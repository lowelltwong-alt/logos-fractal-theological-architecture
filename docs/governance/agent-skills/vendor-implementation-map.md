---
object_type: vendor_implementation_map
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: model_vendor_mapping_guidance
provenance_note: "Created 2026-05-01 as a draft map from registry concepts to model/tool-specific implementations."
reason_for_inclusion: "Preserve model-agnostic governance while acknowledging that Codex, Claude, OpenAI-style agents, local models, and future tools may expose different implementation surfaces."
---

# Vendor Implementation Map

## Principle

The registry card is canonical. Vendor/tool files are adapters.

## Adapter examples

| Registry object | Possible adapter |
|---|---|
| skill card | Claude Skill, Codex prompt, local model task profile |
| subagent card | Claude Code subagent, OpenAI-style agent config |
| monitoring agent card | scheduled runtime monitor later |
| orchestrator card | future runtime orchestrator config |
| edge vocabulary | derived graph/index relationships |

## Claude Code

Claude Code subagents and Skills may be useful later, but project files should not be created before registry governance.

## Codex

Codex is appropriate for repo edits, PR preparation, validation, and route-template updates.

## Local/free models

Local/free models may support low-risk tasks, but they must obey the same source, route, audit, and tool-permission boundaries.

## Future frontier models

New model providers should map to the same registry fields:

- model policy;
- tool permissions;
- side-effect level;
- audit level;
- source boundaries;
- theological profile boundary;
- review cadence.
