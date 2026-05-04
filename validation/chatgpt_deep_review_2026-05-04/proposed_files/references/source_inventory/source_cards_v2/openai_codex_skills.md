# Source card v2: OpenAI Codex skills

```yaml
source_id: openai_codex_skills
source_family: codex_skill_packaging
canonical_paths:
  - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
canonical_urls:
  - https://developers.openai.com/codex/skills
  - https://developers.openai.com/codex/agents-md
authority_level: canonical_skill_packaging_doc
version_or_access_date: local capture reviewed 2026-05-04
applies_to:
  - skill packaging
  - progressive disclosure
  - route-first skill architecture
  - separating entrypoint, references, scripts, and validation artifacts
not_for:
  - systematic review methodology
  - survey-writing methodology
  - scholarly database/API content decisions
  - venue submission policy
route_relevance:
  - general_domain_prior
  - source_audit
  - skill_packaging
freshness_risk: medium to high; Codex/agent-skill docs can change.
reuse_or_license_risk: verify OpenAI documentation terms before large-scale redistribution.
qa_status: draft_v2_example
last_reviewed: 2026-05-04
```

## Key points

```yaml
- claim: "Codex skill packaging supports a concise skill entrypoint with optional supporting files."
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: direct
  verification_note: "Open the canonical skill documentation and verify the sections describing skill files and supporting assets/references."
  quote_or_locator: "canonical_skills.md; exact section locator should be added after section indexes are rebuilt."

- claim: "A route-first skill can keep detailed domain material under references rather than forcing every task to load the full corpus."
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: indirect
  verification_note: "Progressive-disclosure packaging supports the architecture, but the exact SR/survey routing design is repo-specific."
  quote_or_locator: "canonical_skills.md; pair with SKILL.md and source-map.md for repo-specific policy."

- claim: "AGENTS.md or persistent project instructions are separate from repeatable skill workflows."
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
  support_type: direct
  verification_note: "Use this only for packaging/project-instruction boundaries, not research methodology."
  quote_or_locator: "canonical_agents-md.md; exact locator to be added."

- claim: "OpenAI/Codex skill docs do not decide which SR or survey-writing sources are canonical."
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
    - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
  support_type: indirect
  verification_note: "These are packaging docs, not methodology docs; this is an authority-boundary inference."
  quote_or_locator: "Verify source type and scope."
```

## Operational rules

1. Use this source to justify `SKILL.md` as a concise router and `references/` as lazy-loaded supporting material.
2. Use it to defend progressive disclosure and separation of instructions from supporting knowledge.
3. Do not use it to support SR, survey-writing, API, or venue claims.
4. Pair with this repo’s `SKILL.md`, `source-map.md`, and `evidence-rules.md` when explaining the pack architecture.

## Common misuses

1. Treating Codex skill-packaging docs as evidence for systematic review methods.
2. Treating packaging examples as proof that every canonical fulltext should be committed.
3. Ignoring license/reuse terms for copied documentation.
4. Overloading `SKILL.md` with full domain summaries instead of keeping it route-oriented.

## Evidence limits

- Supports packaging and workflow architecture.
- Does not support research methodology.
- Source freshness is important because Codex docs may evolve.

## Verification paths

1. `references/canonical_sources/md/openai_codex_skills/canonical_skills.md`
2. `references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md`
3. `references/source_inventory/source_cards/codex-skill-packaging.md`
4. `references/source-map.md`
5. `references/evidence-rules.md`

## Unresolved gaps

- Add exact section locators from canonical skill docs after public section indexes are available or rebuilt.
- Add an explicit repo policy distinguishing packaging evidence from methodology evidence.
