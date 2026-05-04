# IEEE Xplore API Source Card v2

```yaml
source_id: ieee_xplore_api
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/ieee_xplore_api/canonical_docs_home_docs.md
  - references/canonical_sources/md/ieee_xplore_api/official_metadata_api_overview_ieee_xplore_metadata_api_overview.md
  - references/canonical_sources/md/ieee_xplore_api/official_metadata_api_details_metadata_api_details.md
  - references/canonical_sources/md/ieee_xplore_api/official_searching_metadata_api_searching_the_ieee_xplore_metadata_api.md
  - references/canonical_sources/md/ieee_xplore_api/official_metadata_api_responses_metadata_api_responses.md
canonical_urls:
  - https://developer.ieee.org/docs
  - https://developer.ieee.org/docs/read/IEEE_Xplore_Metadata_API_Overview
  - https://developer.ieee.org/docs/read/Metadata_API_details
  - https://developer.ieee.org/docs/read/Searching_the_IEEE_Xplore_Metadata_API
  - https://developer.ieee.org/docs/read/Metadata_API_responses
authority_level: canonical_database_api_doc
version_or_access_date: "official API docs; local corpus fetched 2026-05-04"
applies_to:
  - IEEE Xplore API source routing
  - metadata search and API-response field checks
  - licensed IEEE open-access or full-text API planning
not_for:
  - open bulk corpus assumptions
  - systematic review or survey methodology
  - unrestricted full-text reuse
  - current access, quota, or terms claims without live verification
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for API endpoints, authentication, quotas, result limits, access tiers, and terms of use; verify live IEEE developer docs before implementation.
reuse_or_license_risk: IEEE Xplore API access is key-based and license-sensitive; metadata, open-access, and full-text endpoints have different access and reuse boundaries.
qa_status: seed_verified_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The captured IEEE developer home lists Metadata Search API, IEEE Open Access API, IEEE Full-Text Access API, and DOI API as available API categories.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_xplore_api/canonical_docs_home_docs.md
  support_type: direct
  verification_note: API availability and naming are freshness-sensitive.
  quote_or_locator: canonical_docs_home_docs.md:20-36
- claim: The Metadata Search API is documented for metadata records, including abstracts, across IEEE Xplore content and supports simple and Boolean searches.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_xplore_api/canonical_docs_home_docs.md
  support_type: direct
  verification_note: This supports metadata-discovery routing, not full-text access or reuse.
  quote_or_locator: canonical_docs_home_docs.md:22-24
- claim: The local query-basics page shows the search endpoint pattern and says an API key must be appended to every query.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_xplore_api/official_searching_metadata_api_searching_the_ieee_xplore_metadata_api.md
  support_type: direct
  verification_note: Recheck endpoint and authentication details live before coding.
  quote_or_locator: official_searching_metadata_api_searching_the_ieee_xplore_metadata_api.md:20-34
- claim: The local docs distinguish metadata retrieval from full-text retrieval and indicate full-text access requires article-number based subsequent requests and access-type handling.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_xplore_api/official_searching_metadata_api_searching_the_ieee_xplore_metadata_api.md
    - references/canonical_sources/md/ieee_xplore_api/official_metadata_api_responses_metadata_api_responses.md
  support_type: direct
  verification_note: Do not treat metadata search as permission or ability to retrieve full text.
  quote_or_locator: official_searching_metadata_api_searching_the_ieee_xplore_metadata_api.md:28,40; official_metadata_api_responses_metadata_api_responses.md:44-50,146-178
- claim: The captured metadata details include query fields, boolean free-text search, insert-date parameters, paging, and a maximum-results note.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_xplore_api/official_metadata_api_details_metadata_api_details.md
  support_type: direct
  verification_note: Operational limits must be verified against current docs before production use.
  quote_or_locator: official_metadata_api_details_metadata_api_details.md:70,96,110-124
```

## Operational rules

- Use this card for IEEE API routing and for deciding which official API Markdown file to open.
- Separate metadata search, open-access full text, full-text access, and DOI lookup.
- Treat every endpoint, quota, field list, and access rule as freshness-sensitive.
- Confirm API key, subscription, and terms assumptions before any automated workflow.

## Common misuses

- Treating IEEE Xplore API docs as review-method guidance.
- Assuming metadata access implies full-text access.
- Assuming open-access endpoint behavior applies to subscription-only full text.
- Building bulk collection logic without current API terms and institutional licensing checks.

## Evidence limits

The local bundle is official IEEE developer documentation captured on 2026-05-04. It supports API-source routing and preliminary implementation planning only. It does not grant access rights, establish current quotas, or authorize bulk reuse.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=ieee_xplore_api`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=ieee_xplore_api`.
- Canonical Markdown: `references/canonical_sources/md/ieee_xplore_api/`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=ieee_xplore_api`.

## Unresolved gaps

- Verify current terms of use, quota, key registration, and subscription requirements before implementation.
- Add a separate implementation note only if the project starts using IEEE Xplore API fields in a repeatable pipeline.
