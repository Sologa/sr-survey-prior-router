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
- Maintain one card for every `source_id` in `references/source_inventory/source_manifest.jsonl`; `validation/validate_source_cards_v2.py` fails if any manifest source lacks a matching card.
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

Then include these required Markdown sections:

1. `## Key points`
2. `## Operational rules`
3. `## Common misuses`
4. `## Evidence limits`
5. `## Verification paths`
6. `## Unresolved gaps`

Cards may also include `## Local bundle provenance` when the local pack needs to record capture, repair, refresh, or validation state. Keep this section separate from `## Key points`.

## Required Key-Point Format

Every key point must describe a source claim and include canonical grounding. Do not put repo-local capture, repair, download, validation, or tracker-status claims in `## Key points`.

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

## Local Bundle Provenance Format

Use `## Local bundle provenance` for claims about this repository's local source bundle, such as manual browser PDF capture, scripted fetch blockage, repaired bad captures, refreshed manifests, validation status, or source-integrity tracker state. These entries are not canonical source claims and must not be used as evidence for methodology, reporting, API, venue, or writing-rule claims.

```yaml
- claim: ""
  supporting_provenance_paths: []
  support_type: "capture_provenance | repo_qa | locator_only"
  verification_note: ""
  locator: ""
```

Rules:

- Use `capture_provenance` for how local raw/Markdown files were obtained, converted, recaptured, or blocked.
- Use `repo_qa` for validation, repair, tracker, or manifest-consistency status.
- Use `locator_only` only when the entry points to where provenance can be checked but does not itself establish the status.
- Provenance entries may point to files such as `references/source_inventory/source_manifest.jsonl`, `references/canonical_sources/download_manifest.jsonl`, `validation/source_integrity_tracker.md`, `validation/manual_browser_capture_2026-05-05.md`, or `validation/prisma_2020_pdf_recapture_validation_2026-05-05.md`.
- Do not use `direct` or `indirect` for local bundle provenance, and do not cite validation notes or manifests as canonical source evidence.

## Authority Levels

Recommended values:

- `canonical_reporting_guideline`
- `canonical_conduct_manual`
- `canonical_appraisal_tool`
- `canonical_certainty_framework`
- `canonical_database_api_doc`
- `canonical_venue_policy`
- `canonical_publisher_corpus_doc`
- `canonical_skill_packaging_doc`
- `methodology_guideline`
- `peer_reviewed_method_paper`
- `venue_guidance`
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
11. Confirm local capture, repair, scripted-fetch, and validation-status claims live in `## Local bundle provenance`, not `## Key points`.
