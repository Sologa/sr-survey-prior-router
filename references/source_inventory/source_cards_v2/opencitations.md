# OpenCitations Source Card v2

```yaml
source_id: opencitations
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/opencitations/canonical_home_canonical_home.md
  - references/canonical_sources/md/opencitations/official_querying_data_querying.md
  - references/canonical_sources/md/opencitations/official_api_selector_official_api_selector.md
  - references/canonical_sources/md/opencitations/official_index_api_v2_v2.md
  - references/canonical_sources/md/opencitations/official_meta_api_v1_v1.md
canonical_urls:
  - https://opencitations.net/
  - https://opencitations.net/querying/
  - https://api.opencitations.net/
  - https://api.opencitations.net/index/v2
  - https://api.opencitations.net/meta/v1
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local corpus fetched 2026-05-04"
applies_to:
  - open citation graph checks
  - open bibliographic metadata lookup
  - REST SPARQL and dump routing
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - full-text retrieval
  - universal citation coverage
  - proprietary citation graph replacement without coverage checks
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: medium to high for API versions, rate limits, token recommendations, endpoint availability, and dump formats; verify live OpenCitations docs before implementation.
reuse_or_license_risk: OpenCitations data is captured as CC0, but website text, software, access tokens, API limits, and downstream identifiers have separate terms.
qa_status: seed_verified_from_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: OpenCitations provides open infrastructure for global scholarly bibliographic and citation data.
  supporting_canonical_paths:
    - references/canonical_sources/md/opencitations/canonical_home_canonical_home.md
  support_type: direct
  verification_note: Use for open citation metadata, not for full text or SR methodology.
  quote_or_locator: canonical_home_canonical_home.md:65-85
- claim: OpenCitations services include data search, downloadable dumps, and APIs for querying data.
  supporting_canonical_paths:
    - references/canonical_sources/md/opencitations/canonical_home_canonical_home.md
  support_type: direct
  verification_note: Choose dumps for scale and APIs for targeted lookup.
  quote_or_locator: canonical_home_canonical_home.md:89-100
- claim: OpenCitations offers SPARQL endpoints, REST APIs, and search/browse interfaces.
  supporting_canonical_paths:
    - references/canonical_sources/md/opencitations/official_querying_data_querying.md
  support_type: direct
  verification_note: Keep REST, SPARQL, and search UI routes distinct in workflows.
  quote_or_locator: official_querying_data_querying.md:65-89
- claim: OpenCitations Meta REST API returns bibliographic metadata and documents a rate limit of 180 requests per minute per IP, recommending dumps for large-scale retrieval.
  supporting_canonical_paths:
    - references/canonical_sources/md/opencitations/official_meta_api_v1_v1.md
  support_type: direct
  verification_note: Verify current rate limits and dump routes before batch jobs.
  quote_or_locator: official_meta_api_v1_v1.md:24-40
- claim: OpenCitations datasets are available under CC0, while website text and software use separate licenses.
  supporting_canonical_paths:
    - references/canonical_sources/md/opencitations/canonical_home_canonical_home.md
    - references/canonical_sources/md/opencitations/official_querying_data_querying.md
  support_type: direct
  verification_note: Separate data reuse from documentation/software reuse.
  quote_or_locator: canonical_home_canonical_home.md:106-108; official_querying_data_querying.md:95-97
```

## Operational rules

- Use OpenCitations for open citation and bibliographic metadata lookups when coverage is sufficient for the task.
- Prefer dumps over APIs for high-volume retrieval.
- Use access tokens where recommended and record current rate-limit assumptions.
- Do not use OpenCitations as a full-text source or as review-method guidance.

## Common misuses

- Treating OpenCitations as a universal citation graph.
- Treating citation metadata availability as full-text access.
- Ignoring API rate limits or token recommendations.
- Collapsing CC0 data rights with documentation or software licenses.

## Evidence limits

This card supports open citation metadata routing. It does not prove complete coverage for any domain, journal family, or SR corpus.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=opencitations`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=opencitations`.
- Canonical Markdown: `references/canonical_sources/md/opencitations/`.
- Optional section locators: `references/corpus_index/sections/by_source/opencitations.jsonl`.

## Unresolved gaps

- Verify current index/meta API versions and dump formats before implementation.
- Add coverage benchmarks if OpenCitations becomes a decision source for corpus completeness.
