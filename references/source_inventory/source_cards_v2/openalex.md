# OpenAlex Source Card v2

```yaml
source_id: openalex
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/openalex/canonical.md
canonical_urls:
  - https://developers.openalex.org/
authority_level: canonical_database_api_doc
version_or_access_date: "official docs; local corpus fetched 2026-05-04"
applies_to:
  - scholarly metadata discovery
  - OpenAlex API/source audit routing
  - metadata graph context for survey or SR corpus construction
not_for:
  - systematic review reporting guidance
  - review conduct methodology
  - appraisal or certainty grading
  - guaranteed PDF/full-text access
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for API key, pricing, quota, rate-limit, and paid-plan claims; verify live docs before implementation.
reuse_or_license_risk: OpenAlex metadata reuse and linked-content reuse are separate; verify current OpenAlex and linked-source terms.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: OpenAlex is a fully open catalog of the global research system with scholarly works, authors, institutions, and related entities.
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: direct
  verification_note: Use this for metadata/discovery claims, not methodology claims.
  quote_or_locator: canonical.md:150-156; section_id=openalex__canonical__s0007_documentation_index
- claim: OpenAlex provides a REST API for programmatic access.
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: direct
  verification_note: API details are freshness-sensitive and must be rechecked for implementation.
  quote_or_locator: canonical.md:161-162; section_id=openalex__canonical__s0007_documentation_index
- claim: OpenAlex can support survey/SR corpus metadata discovery but is not an SR methodology authority.
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: indirect
  verification_note: The source describes metadata/API capabilities; the methodology boundary comes from this pack's source registry and authority rules.
  quote_or_locator: canonical.md:150-162 plus source_registry/source_manifest authority_class=registry_database/tool_documentation context
```

## Operational rules

- Use OpenAlex for metadata discovery, entity lookup, and source-audit context.
- Do not use OpenAlex API documentation to justify PRISMA, Cochrane, JBI, GRADE, or appraisal claims.
- Keep snapshot-specific claims in `openalex_snapshot.md`, not this API/homepage card.
- Treat quota, pricing, authentication, and access details as current-fact checks, not stable corpus facts.

## Common misuses

- Treating OpenAlex metadata availability as proof that full text or PDFs are available.
- Treating OpenAlex API docs as review-method guidance.
- Merging OpenAlex API and snapshot source IDs into one card.

## Evidence limits

This card supports metadata/API source routing only. It does not establish review quality, reporting requirements, or full-text rights.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=openalex`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=openalex`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=openalex`.
- Optional local section locators: `references/corpus_index/sections/by_source/openalex.jsonl`.

## Unresolved gaps

- Re-check live OpenAlex docs before operational API work.
- Add a separate claim ledger if this pack begins using OpenAlex metadata fields for repeatable corpus construction.
