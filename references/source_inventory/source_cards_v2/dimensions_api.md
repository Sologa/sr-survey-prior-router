# Dimensions API Source Card v2

```yaml
source_id: dimensions_api
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/dimensions_api/canonical_product_api_dimensions-api.md
  - references/canonical_sources/md/dimensions_api/official_api_access_api.html.md
  - references/canonical_sources/md/dimensions_api/official_dsl_docs_home_dsl.md
  - references/canonical_sources/md/dimensions_api/official_reasonable_use_corrected_usagepolicy.html.md
canonical_urls:
  - https://www.dimensions.ai/products/all-products/dimensions-api/
  - https://docs.dimensions.ai/dsl/api.html
  - https://docs.dimensions.ai/dsl/
  - https://docs.dimensions.ai/dsl/usagepolicy.html
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local corpus fetched 2026-05-04"
applies_to:
  - paid scholarly analytics enrichment
  - Dimensions DSL query planning
  - publications datasets grants patents clinical trials policy reports metadata
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - open public core registry
  - local-copy construction
  - unrestricted bulk harvesting
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for subscription access, API keys, request limits, query limits, and DSL version details; verify live Dimensions docs and contract before implementation.
reuse_or_license_risk: Dimensions is subscription/proprietary; local-copy construction is explicitly constrained by the captured reasonable-use docs.
qa_status: seed_verified_from_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: Dimensions API access is a subscription offering.
  supporting_canonical_paths:
    - references/canonical_sources/md/dimensions_api/canonical_product_api_dimensions-api.md
    - references/canonical_sources/md/dimensions_api/official_api_access_api.html.md
  support_type: direct
  verification_note: Treat Dimensions as optional paid enrichment, not an open backbone.
  quote_or_locator: canonical_product_api_dimensions-api.md:156-158,228-230; official_api_access_api.html.md:62-68
- claim: Dimensions API supports full-text search, retrieval, aggregation, sorting, and Dimensions-specific query language for complex analysis.
  supporting_canonical_paths:
    - references/canonical_sources/md/dimensions_api/canonical_product_api_dimensions-api.md
  support_type: direct
  verification_note: This is analytics capability, not SR methodology evidence.
  quote_or_locator: canonical_product_api_dimensions-api.md:160-172
- claim: Dimensions data surfaces include publications, datasets, grants, patents, clinical trials, policy documents, reports, source titles, researchers, and organizations.
  supporting_canonical_paths:
    - references/canonical_sources/md/dimensions_api/canonical_product_api_dimensions-api.md
  support_type: direct
  verification_note: Coverage and entitlement depend on the subscription and should be checked.
  quote_or_locator: canonical_product_api_dimensions-api.md:206-227
- claim: Dimensions API is not intended for creating local copies as an alternative to the API and has fixed technical limits such as 30 requests per IP per minute and query return limits.
  supporting_canonical_paths:
    - references/canonical_sources/md/dimensions_api/official_reasonable_use_corrected_usagepolicy.html.md
    - references/canonical_sources/md/dimensions_api/official_api_access_api.html.md
  support_type: direct
  verification_note: This is a hard access/reuse caveat for any local corpus plan.
  quote_or_locator: official_reasonable_use_corrected_usagepolicy.html.md:48-76; official_api_access_api.html.md:74-87
```

## Operational rules

- Use Dimensions only when paid analytics access is available and the task needs its enriched research-output graph.
- Check the subscription, API key, token flow, DSL version, and reasonable-use policy before any query plan.
- Do not design local replication or bulk mirroring workflows around Dimensions API output.
- Do not use Dimensions API docs as SR reporting, conduct, appraisal, certainty, or survey-writing authority.

## Common misuses

- Treating Dimensions as an open metadata source.
- Treating subscription access as permission to build a local replacement copy.
- Ignoring 30-request-per-minute and result-size limits.
- Treating Dimensions analytics fields as methodological guidance.

## Evidence limits

This card can guide paid-source routing and caveats. It cannot establish user entitlements, current contract terms, or permission to redistribute Dimensions data.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=dimensions_api`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=dimensions_api`.
- Canonical Markdown: `references/canonical_sources/md/dimensions_api/`.
- Optional section locators: `references/corpus_index/sections/by_source/dimensions_api.jsonl`.

## Unresolved gaps

- Verify the actual account/subscription entitlement before recommending Dimensions operationally.
- Capture contract-specific export/reuse constraints if Dimensions becomes a real workflow dependency.
