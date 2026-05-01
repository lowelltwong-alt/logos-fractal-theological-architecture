---
object_type: settings_matrix
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: contributor_guidance_only
provenance_note: "Created 2026-04-30 to guide reasoning, internet, and permission settings for AI-assisted work."
reason_for_inclusion: "Provide route-sensitive guidance for reasoning effort, internet use, permissions, and work mode so AI-assisted contributors choose settings proportional to risk."
---

# AI Tool Settings Matrix

This matrix guides Codex, Claude Code, chat-based AI, and future tools.

## Default posture

- Reasoning effort: match route risk.
- Internet: off by default.
- Permissions: conservative by default.
- Mode: Explore or Plan unless the task explicitly authorizes edits.
- Side effects: never execute unless explicitly authorized.

## Reasoning effort

| Level | Use for |
|---|---|
| low | Typo fixes, formatting, tiny single-file edits. |
| medium | Roadmaps, source maps, staged research packets, chat handoffs. |
| high | Governance bridges, concept nodes, theologian/source profile cards, policy docs. |
| xhigh | Schemas, validators, source registries, claim objects, graph objects, ingestion, runtime planning, CI changes. |

## Internet policy

| Internet state | Use when |
|---|---|
| off | Default for repo-internal docs, concept work, claim drafts, graph drafts, route templates. |
| on for official docs | Needed for OpenAI, Anthropic, GitHub, W3C, or tool-provider documentation. |
| on for source/license verification | Needed for Bible source status, public-domain/open-license review, publication terms, or current source policy. |
| on for current facts | Needed for facts that may have changed. |

When internet is on, prefer official sources and preserve citations in PR notes where relevant.

## Permission posture

| Permission posture | Use when |
|---|---|
| read-only | Explore and audit work. |
| conservative edit | Normal docs, templates, maps, and staged research. |
| guarded edit | Claims, graph, source registry, schema, validators, and CI. |
| execute with explicit approval | Push, merge, deploy, send, delete, external mutation, or runtime side effects. |

## Task matrix

| Task | Reasoning | Internet | Permissions | Mode |
|---|---|---|---|---|
| Source document map | medium | off | conservative edit | Edit |
| Staged research addition | medium | off unless source verification needed | conservative edit | Edit |
| Governance bridge | high | off unless official docs needed | conservative edit | Edit |
| Concept promotion | high | off | conservative edit | Edit |
| Source profile cards | high | off unless source status needed | conservative edit | Edit |
| Bible source registry | xhigh | on only for source/license verification | guarded edit | Edit |
| Claim object pack | xhigh | off unless source status needed | guarded edit | Edit |
| Graph object pack | xhigh | off | guarded edit | Edit |
| Validation or CI | xhigh | off unless official tool docs needed | guarded edit | Edit |
| Ingestion pilot | xhigh | on for license verification | guarded edit | Plan first, then Edit |
| Runtime agent planning | xhigh | off unless official tool docs needed | conservative edit | Plan |
| Runtime execution | xhigh | case-by-case | explicit approval only | Execute |

## Codex notes

Use medium/high/xhigh reasoning according to task risk. Use conservative permissions and internet off unless the route requires current official documentation or source/license verification.

For long tasks, enable any available prevent-sleep or long-running task option.

## Claude Code notes

Use project settings to deny sensitive reads and dangerous git or shell actions. Use allow/ask/deny permission posture. Prefer read/list/search by default, ask before writes, and deny destructive git actions.

## Chat-based AI notes

Use chat-based AI for research, prompt drafting, PR descriptions, review checklists, and patch planning. Do not claim that chat-based tools pushed or merged unless live repo tools are actually available.
