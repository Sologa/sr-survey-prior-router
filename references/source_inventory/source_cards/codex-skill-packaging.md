# Source Card: Codex Skill Packaging

source_ids: `openai_codex_skills`, `openai_codex_agents_md`

## Summary

OpenAI Codex docs support the pack architecture: keep `SKILL.md` focused, use progressive disclosure, and load references or scripts only when needed. AGENTS.md is for persistent project instructions; skills package repeatable workflows plus optional references/scripts.

## Decision Boundary

Use these sources to justify the router/registry/references split. Do not use them as evidence for SR or survey-writing methodology.

## Supported Uses

- Keep `SKILL.md` short and route-oriented.
- Put longer source inventories and source cards under `references/`.
- Avoid loading all domain material into every task.

## Gaps

- These docs do not define how to conduct or write reviews.
- They do not decide which SR/survey methodology sources are canonical.

last_reviewed: 2026-05-04
