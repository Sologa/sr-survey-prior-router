# OpenAI Codex AGENTS.md Source Card v2

```yaml
source_id: openai_codex_agents_md
source_family: codex_skill_packaging
canonical_paths:
  - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
canonical_urls:
  - https://developers.openai.com/codex/guides/agents-md
authority_level: canonical_skill_packaging_doc
version_or_access_date: "official docs; local corpus fetched 2026-05-04"
applies_to:
  - Codex project instructions
  - AGENTS.md discovery and layering
  - separating persistent repo guidance from lazy-loaded skill references
not_for:
  - SR or survey-writing methodology
  - reusable workflow packaging details handled by the skills doc
  - canonical evidence for source claims
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
- claim: Codex reads AGENTS.md files before doing work and can combine global guidance with project-specific overrides.
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
  support_type: direct
  verification_note: Use this source for persistent project-instruction behavior.
  quote_or_locator: canonical_agents-md.md:1007-1014; section_id=openai_codex_agents_md__canonical_agents_md__s0049_custom_instructions_with_agents_md
- claim: Codex discovers guidance through global scope, project scope, and root-to-current-directory merge order.
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
  support_type: direct
  verification_note: Use this for AGENTS.md precedence and scoping claims.
  quote_or_locator: canonical_agents-md.md:1015-1026; section_id=openai_codex_agents_md__canonical_agents_md__s0050_how_codex_discovers_guidance
- claim: Repository-level AGENTS.md files are for project norms while inheriting global defaults.
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
  support_type: direct
  verification_note: Keep project policy guidance separate from large source corpora.
  quote_or_locator: canonical_agents-md.md:1046-1055; section_id=openai_codex_agents_md__canonical_agents_md__s0053_layer_project_instructions
- claim: AGENTS.md project guidance and reusable skill workflows should remain separate layers in this pack.
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: indirect
  verification_note: This is repo architecture guidance inferred from pairing the AGENTS.md and skills docs.
  quote_or_locator: agents-md lines 1007-1026; skills lines 1013-1025
```

## Operational rules

- Use AGENTS.md for persistent repo norms and safety boundaries.
- Use the skill's `SKILL.md` and `references/` for reusable, route-specific workflow knowledge.
- Do not bury large SR/survey canonical corpora inside AGENTS.md-style always-loaded guidance.

## Common misuses

- Treating AGENTS.md as a replacement for a skill or source corpus.
- Using a stale AGENTS.md URL; this corpus records `https://developers.openai.com/codex/guides/agents-md`.
- Combining this source with `openai_codex_skills` in a one-source v2 card.

## Evidence limits

This source supports project-instruction discovery and layering. It does not support domain methodology or source-content claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=openai_codex_agents_md`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=openai_codex_agents_md`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=openai_codex_agents_md`.
- Optional local section locators: `references/corpus_index/sections/by_source/openai_codex_agents_md.jsonl`.

## Unresolved gaps

- Re-check current official docs before publishing claims about exact file-size caps, fallback filename behavior, or discovery knobs.
