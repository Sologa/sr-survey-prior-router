# Semantic Scholar Source Card v2

```yaml
source_id: semantic_scholar
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/semantic_scholar/canonical_product_api_api.md
  - references/canonical_sources/md/semantic_scholar/official_api_tutorial_tutorial.md
  - references/canonical_sources/md/semantic_scholar/official_graph_swagger_json_swagger.json.md
  - references/canonical_sources/md/semantic_scholar/official_datasets_swagger_json_swagger.json.md
  - references/canonical_sources/md/semantic_scholar/official_recommendations_swagger_json_swagger.json.md
canonical_urls:
  - https://www.semanticscholar.org/product/api
  - https://www.semanticscholar.org/product/api/tutorial
  - https://api.semanticscholar.org/graph/v1/swagger.json
  - https://api.semanticscholar.org/datasets/v1/swagger.json
  - https://api.semanticscholar.org/recommendations/v1/swagger.json
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local corpus fetched 2026-05-04"
applies_to:
  - scholarly discovery enrichment
  - paper author venue citation and recommendation metadata
  - Semantic Scholar dataset routing
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - publisher source-of-record metadata
  - dependable full-text corpus control
  - license-free reuse of abstracts or PDFs
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for rate limits, API-key requirements, endpoint schemas, dataset releases, and availability during heavy use; verify live docs before implementation.
reuse_or_license_risk: API metadata, abstracts, datasets, and open-access PDF links can have different legal constraints; verify Semantic Scholar terms and source licenses before reuse.
qa_status: seed_verified_from_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: Semantic Scholar provides REST API services for publication, author, citation, venue, recommendation, and dataset access.
  supporting_canonical_paths:
    - references/canonical_sources/md/semantic_scholar/canonical_product_api_api.md
    - references/canonical_sources/md/semantic_scholar/official_api_tutorial_tutorial.md
  support_type: direct
  verification_note: Use as discovery and enrichment infrastructure, not as a methodology authority.
  quote_or_locator: canonical_product_api_api.md:57-66; official_api_tutorial_tutorial.md:119-129
- claim: Many Semantic Scholar endpoints are publicly available but rate-limited, while some endpoints require an API key.
  supporting_canonical_paths:
    - references/canonical_sources/md/semantic_scholar/canonical_product_api_api.md
    - references/canonical_sources/md/semantic_scholar/official_api_tutorial_tutorial.md
  support_type: direct
  verification_note: Current limits and key tiers must be checked live before batch use.
  quote_or_locator: canonical_product_api_api.md:100-108; official_api_tutorial_tutorial.md:131-141
- claim: The Datasets API supports downloading Semantic Scholar datasets and maintaining them with incremental diffs.
  supporting_canonical_paths:
    - references/canonical_sources/md/semantic_scholar/official_api_tutorial_tutorial.md
    - references/canonical_sources/md/semantic_scholar/official_datasets_swagger_json_swagger.json.md
  support_type: direct
  verification_note: Dataset release identifiers and file links are operationally freshness-sensitive.
  quote_or_locator: official_api_tutorial_tutorial.md:71-75,141; official_datasets_swagger_json_swagger.json.md:7
- claim: Abstracts and open-access PDF links may be absent or license-qualified, even when a paper record exists.
  supporting_canonical_paths:
    - references/canonical_sources/md/semantic_scholar/official_recommendations_swagger_json_swagger.json.md
  support_type: direct
  verification_note: Do not treat Semantic Scholar metadata as permission to reuse full text.
  quote_or_locator: official_recommendations_swagger_json_swagger.json.md:7; BasePaper abstract and openAccessPdf fields
```

## Operational rules

- Use Semantic Scholar for citation/discovery enrichment, paper recommendations, author lookup, and optional dataset-based local querying.
- Use the Graph, Recommendations, and Datasets APIs as separate operational surfaces.
- Keep field lists small and use batch/bulk endpoints where the docs recommend them.
- Do not use Semantic Scholar API documentation to justify PRISMA, Cochrane, JBI, GRADE, appraisal, or survey-writing claims.

## Common misuses

- Treating Semantic Scholar as publisher source-of-record metadata.
- Assuming abstract or PDF availability is stable or legally reusable.
- Ignoring API keys, throttling, or shared unauthenticated rate limits.
- Treating recommendation outputs as neutral evidence of relevance without a separate screening or audit process.

## Evidence limits

The local Swagger captures are one-line JSON-in-Markdown documents. They are valid canonical captures for schema routing, but final endpoint behavior should be verified against live documentation before executable work.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=semantic_scholar`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=semantic_scholar`.
- Canonical Markdown: `references/canonical_sources/md/semantic_scholar/`.
- Optional section locators: `references/corpus_index/sections/by_source/semantic_scholar.jsonl`.

## Unresolved gaps

- Confirm current API-key tiers, endpoint-specific limits, and dataset license terms.
- Add a tested adapter contract before using Semantic Scholar data as a repeatable corpus-construction input.
