# Crossref REST API Source Card v2

```yaml
source_id: crossref_api
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/crossref_api/canonical_rest-api.md
canonical_urls:
  - https://www.crossref.org/documentation/retrieve-metadata/rest-api/
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local corpus fetched 2026-05-04"
applies_to:
  - DOI metadata retrieval
  - publisher-deposited bibliographic metadata checks
  - funding license relation and identifier metadata lookup
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - full-text access
  - complete citation graph guarantees
  - clinical trial registry evidence
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for endpoints, filters, polite-pool behavior, rate limits, and Metadata Plus access; verify live Crossref docs before implementation.
reuse_or_license_risk: most Crossref metadata is reusable, but some abstracts may be copyrighted and Crossref documentation is CC BY 4.0.
qa_status: seed_verified_from_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The Crossref REST API exposes scholarly metadata deposited by Crossref members and trusted sources.
  supporting_canonical_paths:
    - references/canonical_sources/md/crossref_api/canonical_rest-api.md
  support_type: direct
  verification_note: Use for DOI metadata provenance, not for method or reporting rules.
  quote_or_locator: canonical_rest-api.md:179-183
- claim: Crossref REST metadata includes funding data, license information, post-publication updates, identifiers, and abstracts when deposited.
  supporting_canonical_paths:
    - references/canonical_sources/md/crossref_api/canonical_rest-api.md
  support_type: direct
  verification_note: Metadata completeness depends on deposits and trusted-source enrichment.
  quote_or_locator: canonical_rest-api.md:181-183
- claim: The public REST API requires no sign-up, but abstracts may be subject to publisher or author copyright.
  supporting_canonical_paths:
    - references/canonical_sources/md/crossref_api/canonical_rest-api.md
  support_type: direct
  verification_note: Treat abstract reuse separately from bibliographic metadata reuse.
  quote_or_locator: canonical_rest-api.md:185
- claim: Crossref documents endpoints for works, journals, members, funders, types, licenses, and DOI lookups.
  supporting_canonical_paths:
    - references/canonical_sources/md/crossref_api/canonical_rest-api.md
  support_type: direct
  verification_note: Endpoint behavior and filters are operationally freshness-sensitive.
  quote_or_locator: canonical_rest-api.md:189-245
```

## Operational rules

- Use Crossref for DOI-centered metadata, publisher-deposit checks, funder/license/relation metadata, and source-audit triangulation.
- Prefer Crossref canonical docs or live Swagger docs for endpoint-level implementation.
- Record whether a field is absent because it was not deposited versus because the query failed.
- Do not use Crossref API docs as evidence for SR conduct, reporting, appraisal, or survey-writing methodology.

## Common misuses

- Treating a Crossref metadata record as proof of full-text access.
- Treating missing abstracts, references, or relations as proof the work lacks them.
- Reusing abstracts without checking copyright.
- Ignoring polite-pool, rate-limit, or Metadata Plus constraints in batch designs.

## Evidence limits

This card routes DOI metadata work. It does not establish completeness of Crossref deposits, permission to reuse abstracts, or final API limits.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=crossref_api`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=crossref_api`.
- Canonical Markdown: `references/canonical_sources/md/crossref_api/canonical_rest-api.md`.
- Optional section locators: `references/corpus_index/sections/by_source/crossref_api.jsonl`.

## Unresolved gaps

- Re-check current polite-pool and Metadata Plus limits before any high-volume job.
- Add separate tested query recipes if this pack starts using Crossref as an executable retrieval adapter.
