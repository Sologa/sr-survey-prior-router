# CORE API Source Card v2

```yaml
source_id: core_api
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/core_api/canonical_services_api_api.md
  - references/canonical_sources/md/core_api/official_api_v3_docs_v3.md
  - references/canonical_sources/md/core_api/official_api_root_official_api_root.md
canonical_urls:
  - https://core.ac.uk/services/api
  - https://api.core.ac.uk/docs/v3
  - https://api.core.ac.uk/
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local corpus fetched 2026-05-04"
applies_to:
  - open-access metadata and full-text discovery
  - repository and journal OA aggregation checks
  - optional OA full-text retrieval planning
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - closed or paywalled literature completeness
  - broad citation graph backbone
  - unrestricted commercial-scale harvesting
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for API key registration, rate limits, commercial terms, v3 documentation, and corpus size claims; verify live CORE docs before implementation.
reuse_or_license_risk: CORE aggregates OA content from many providers; per-item full-text licenses and CORE terms must be checked before reuse or redistribution.
qa_status: mixed_full_and_entry_stub_local_capture
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: CORE API provides machine access to metadata and full texts from a large open-access research-paper corpus.
  supporting_canonical_paths:
    - references/canonical_sources/md/core_api/canonical_services_api_api.md
  support_type: direct
  verification_note: Use for OA discovery/retrieval planning, not closed-literature completeness.
  quote_or_locator: canonical_services_api_api.md:104-128,159-167
- claim: CORE asks users to register for an API key to start testing live examples.
  supporting_canonical_paths:
    - references/canonical_sources/md/core_api/canonical_services_api_api.md
  support_type: direct
  verification_note: Current registration and key behavior should be checked live before use.
  quote_or_locator: canonical_services_api_api.md:139-143,219-226
- claim: CORE states the API can be used commercially subject to terms, with licensing eligibility assessed during registration.
  supporting_canonical_paths:
    - references/canonical_sources/md/core_api/canonical_services_api_api.md
  support_type: direct
  verification_note: Commercial use is not license-free; terms and eligibility need current verification.
  quote_or_locator: canonical_services_api_api.md:145-147
- claim: CORE documents free access subject to rate limits, faster registered rates, and a basic limit of one batch request or five single requests per 10 seconds.
  supporting_canonical_paths:
    - references/canonical_sources/md/core_api/canonical_services_api_api.md
  support_type: direct
  verification_note: Treat the local v3 docs/root captures as entry-point stubs for detailed endpoint work.
  quote_or_locator: canonical_services_api_api.md:149-177; official_api_root_official_api_root.md:6-8; official_api_v3_docs_v3.md:1-6
```

## Operational rules

- Use CORE as an optional OA metadata/full-text layer, not as a universal literature or citation backbone.
- Verify per-record licenses before storing, redistributing, or quoting full text.
- Use current live v3 documentation for endpoint details because local `official_api_v3_docs` is only a short entry-point capture.
- Do not use CORE API documentation for SR reporting, conduct, appraisal, certainty, or survey-writing methodology claims.

## Common misuses

- Treating CORE as covering closed or paywalled literature.
- Treating OA aggregation as blanket permission to reuse every full text.
- Ignoring API registration, commercial terms, or rate limits.
- Building endpoint-specific claims from the local API-root stub.

## Evidence limits

The local bundle mixes a useful product/API page with short entry-point stubs. Detailed endpoint schemas, authentication flows, and rate tiers remain live-doc checks.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=core_api`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=core_api`.
- Canonical Markdown: `references/canonical_sources/md/core_api/`.
- Optional section locators: `references/corpus_index/sections/by_source/core_api.jsonl`.

## Unresolved gaps

- Capture richer CORE v3 endpoint documentation if this pack needs executable CORE queries.
- Confirm current commercial-license and rate-tier language before operational use.
