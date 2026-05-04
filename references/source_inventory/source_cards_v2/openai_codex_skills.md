# OpenAI Codex Skills Source Card v2

```yaml
source_id: openai_codex_skills
source_family: codex_skill_packaging
canonical_paths:
  - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
canonical_urls:
  - https://developers.openai.com/codex/skills
authority_level: canonical_skill_packaging_doc
version_or_access_date: "official docs; local corpus fetched 2026-05-04"
applies_to:
  - Codex skill packaging
  - progressive disclosure for skill instructions and references
  - staged router design as an indirect architecture precedent
not_for:
  - SR or survey-writing methodology
  - scholarly source authority
  - AGENTS.md project-instruction precedence
route_relevance:
  - general_domain_prior
  - source_audit
freshness_risk: high for current Codex product behavior; verify official docs before publishing stable tool claims.
reuse_or_license_risk: OpenAI docs terms apply.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: A skill packages instructions, resources, and optional scripts so Codex can follow a workflow reliably.
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: direct
  verification_note: Use this only for skill packaging behavior, not domain methodology.
  quote_or_locator: canonical_skills.md:1007-1025; section_id=openai_codex_skills__canonical_skills__s0049_agent_skills
- claim: Skills use progressive disclosure so Codex initially sees skill name, description, and file path, then loads full instructions when selected.
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: direct
  verification_note: This supports a lean router entrypoint and lazy-loaded references.
  quote_or_locator: canonical_skills.md:1019-1023; section_id=openai_codex_skills__canonical_skills__s0049_agent_skills
- claim: Codex can activate skills through explicit invocation or implicit matching against the skill description.
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: direct
  verification_note: Use route descriptions and trigger terms carefully because implicit matching depends on description text.
  quote_or_locator: canonical_skills.md:1046-1055; section_id=openai_codex_skills__canonical_skills__s0050_how_codex_uses_skills
- claim: A route-first, lazy-loaded SR/survey router is a repo-specific application of the skill packaging and progressive-disclosure pattern.
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: indirect
  verification_note: The OpenAI doc supports the packaging pattern; this repo's SR/survey design remains a local inference.
  quote_or_locator: canonical_skills.md:1013-1025,1056-1065; section_ids=openai_codex_skills__canonical_skills__s0049_agent_skills, __s0051_create_a_skill
```

## Operational rules

- Keep `SKILL.md` concise and load `references/` only after route selection.
- Keep scripts and reference material separate from the entrypoint when they are not always needed.
- Do not use this source to answer SR, PRISMA, survey-writing, or scholarly methodology claims.

## Common misuses

- Treating Codex skill packaging documentation as evidence for survey/SR methods.
- Combining this source with `openai_codex_agents_md` in one source-specific v2 card.
- Listing `skill_packaging` as a route ID; it is a source family, not a live route.

## Evidence limits

This source is tool documentation. It can support claims about Codex skill packaging and progressive disclosure. It cannot support claims about SR/survey methodology.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=openai_codex_skills`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=openai_codex_skills`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=openai_codex_skills`.
- Optional local section locators: `references/corpus_index/sections/by_source/openai_codex_skills.jsonl`.

## Unresolved gaps

- Product behavior is freshness-sensitive; re-check the official docs before relying on details such as activation behavior, context budgets, or packaging conventions in external documentation.
