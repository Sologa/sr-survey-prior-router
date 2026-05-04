# Source cards v2

Status: proposed  
Artifact type: derivative source briefing schema  
Canonical evidence status: not canonical evidence

Source cards v2 are compact, provenance-preserving summaries for sources in `sr-survey-prior-router`. They help agents choose which canonical Markdown files to open and what claims are likely supported.

They must never replace canonical Markdown verification for final answers.

## Directory

Recommended path:

`references/source_inventory/source_cards_v2/`

File naming:

`<source_id>.md`

Examples:

- `prisma_2020.md`
- `cochrane_handbook.md`
- `sanra.md`
- `openalex.md`
- `openai_codex_skills.md`

## Schema

Each card should use the following top-level fields.

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

## Required key-point format

Every key point must include canonical grounding.

```yaml
- claim: ""
  supporting_canonical_paths: []
  support_type: "direct | indirect | locator_only | blocked | unsupported"
  verification_note: ""
  quote_or_locator: ""
```

Rules:

- Use `direct` only when the canonical Markdown directly states the claim.
- Use `indirect` when the canonical source supports the inference but not the exact operational rule.
- Use `locator_only` for registry pages, indexes, source cards, graph output, or manifests that only tell the agent where to look.
- Use `blocked` for sources known to exist but not locally captured.
- Use `unsupported` for tempting but not grounded claims.

## Authority levels

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

## Evidence boundary

A source card v2 may be cited only for statements about the card itself. For claims about methodology, reporting, API behavior, venue rules, or skill packaging, the answer must cite or quote the relevant canonical Markdown path or source URL.

## QA checklist

Before committing a source card v2:

1. Confirm `source_id` exists in the inventory.
2. Confirm at least one `canonical_paths` entry exists or mark the card as blocked/bad capture.
3. Confirm every key point has `supporting_canonical_paths`.
4. Confirm no key point is supported only by an older source card.
5. Confirm `not_for` boundaries are explicit.
6. Confirm blocked/partial/bad-capture status is not hidden.
7. Confirm licensing/reuse risk is stated.
8. Confirm freshness risk is stated for API, venue, pricing, and policy sources.
