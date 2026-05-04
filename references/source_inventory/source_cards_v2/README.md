# Source Cards v2

Status: active draft schema
Artifact type: derivative source briefing schema
Canonical evidence status: not canonical evidence

Source cards v2 are compact, provenance-preserving summaries for individual sources in `sr-survey-prior-router`. They help agents choose which canonical Markdown files to open and what claims are likely supported.

They must never replace canonical Markdown verification for final answers.

## Directory

Path:

`references/source_inventory/source_cards_v2/`

File naming:

`<source_id>.md`

Rules:

- Use exactly one live inventory `source_id` per card.
- Do not merge multiple source IDs into one v2 card, even when they belong to the same source family.
- Keep family-level comparisons in future `family_cards_v2/`, not in source cards v2.

Examples:

- `prisma_2020.md`
- `cochrane_handbook.md`
- `sanra.md`
- `openalex.md`
- `openalex_snapshot.md`
- `openai_codex_skills.md`
- `openai_codex_agents_md.md`

## Schema

Each card should start with one fenced YAML metadata block.

```yaml
source_id: ""
source_family: ""
canonical_paths: []
canonical_urls: []
authority_level: ""
version_or_access_date: ""
applies_to: []
not_for: []
route_relevance: []
freshness_risk: ""
reuse_or_license_risk: ""
qa_status: ""
last_reviewed: ""
```

Then include Markdown sections:

1. `## Key points`
2. `## Operational rules`
3. `## Common misuses`
4. `## Evidence limits`
5. `## Verification paths`
6. `## Unresolved gaps`

## Required Key-Point Format

Every key point must include canonical grounding.

```yaml
- claim: ""
  supporting_canonical_paths: []
  support_type: "direct | indirect | locator_only | blocked | unsupported"
  verification_note: ""
  quote_or_locator: ""
```

Rules:

- Use `direct` only when canonical Markdown directly states the claim.
- Use `indirect` when the canonical source supports the inference but not the exact operational rule.
- Use `locator_only` for registry pages, indexes, source cards, graph output, or manifests that only tell the agent where to look.
- Use `blocked` for sources known to exist but not locally captured.
- Use `unsupported` for tempting but not grounded claims.

## Authority Levels

Recommended values:

- `canonical_reporting_guideline`
- `canonical_conduct_manual`
- `canonical_appraisal_tool`
- `canonical_certainty_framework`
- `canonical_database_api_doc`
- `canonical_venue_policy`
- `canonical_skill_packaging_doc`
- `locator_only`
- `blocked_inventory_target`
- `bad_capture_do_not_use`
- `derivative_not_canonical`

## Evidence Boundary

A source card v2 may be cited only for statements about the card itself. For claims about methodology, reporting, API behavior, venue rules, or skill packaging, the answer must cite or quote the relevant canonical Markdown path or source URL.

`references/corpus_index/sections/by_source/<source_id>.jsonl` entries are locator aids, not evidence. They may be available in a local workspace even when excluded from the public GitHub review surface. A v2 card should therefore include enough `canonical_paths`, line ranges, or section IDs for a reviewer to find the same span without relying only on split section indexes.

## QA Checklist

Before committing a source card v2:

1. Confirm `source_id` exists in `source_inventory/source_manifest.jsonl`.
2. Confirm the card filename is `<source_id>.md`.
3. Confirm all `route_relevance` values exist in `route-registry.md`.
4. Confirm at least one `canonical_paths` entry exists, unless the card is explicitly blocked, bad capture, or locator-only.
5. Confirm every key point has `supporting_canonical_paths`.
6. Confirm no key point is supported only by an older source card, graph output, section index, or registry row.
7. Confirm `not_for` boundaries are explicit.
8. Confirm blocked/partial/bad-capture status is not hidden.
9. Confirm licensing/reuse risk is stated.
10. Confirm freshness risk is stated for API, venue, pricing, and policy sources.
