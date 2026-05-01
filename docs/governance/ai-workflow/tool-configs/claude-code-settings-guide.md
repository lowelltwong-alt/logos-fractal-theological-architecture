---
object_type: tool_settings_guide
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: contributor_guidance_only
tool: claude_code
---

# Claude Code Settings Guide

## Default posture

Claude Code should follow the same route and scope rules as Codex.

Use project or local settings to prefer:

- read/search/list allowed;
- file writes ask unless the task is explicitly Edit mode;
- git push ask;
- destructive git actions denied;
- secrets and private local files denied;
- internet/web fetch denied unless the route allows source or tool-documentation verification.

## Recommended deny examples

Deny access to:

- `.env` files;
- secrets folders;
- private keys;
- credential files;
- destructive shell commands;
- force-push commands;
- reset/rebase commands unless explicitly authorized.

## Recommended ask examples

Ask before:

- editing files;
- writing new files;
- pushing branches;
- merging;
- running broad scripts;
- changing validation or CI.

## Recommended allow examples

Allow:

- read/list/search tools;
- git status;
- git diff;
- git log;
- git branch;
- git fetch;
- targeted validation commands.

## Hooks

Hooks can be useful later, but this repository should not add active Claude Code hooks or agents until there is a reviewed runtime-agent route and approval boundary.

## Clean-room note

Do not copy private prompts, leaked code, or leak-derived repositories. Only clean-room architectural patterns may inform planning.
