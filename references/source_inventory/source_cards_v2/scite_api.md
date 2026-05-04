# scite API Source Card v2

```yaml
source_id: scite_api
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/scite_api/official_api_docs_docs_7da8d680.md
  - references/canonical_sources/md/scite_api/official_openapi_json_openapi.json.md
canonical_urls:
  - https://api.scite.ai/docs
  - https://api.scite.ai/openapi.json
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local corpus fetched 2026-05-04"
applies_to:
  - citation context enrichment
  - smart citation tallies by DOI
  - scite API and assistant capability routing
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - open public metadata backbone
  - source-of-record bibliographic metadata
  - reusable full-text corpus construction
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for token requirements, endpoint restrictions, premium/MCP access, rate limits, model lists, and licensing; verify live scite docs or agreement before implementation.
reuse_or_license_risk: scite search, recommendations, reference check, citation graph, and advanced API use can require tokens, paid licenses, or separate agreements.
qa_status: mixed_entry_stub_and_openapi_local_capture
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The scite API provides access to citation data, scite tallies, related paper metadata, and reference check capabilities.
  supporting_canonical_paths:
    - references/canonical_sources/md/scite_api/official_openapi_json_openapi.json.md
  support_type: direct
  verification_note: Use for citation-context enrichment, not as source-of-record metadata or methodology evidence.
  quote_or_locator: official_openapi_json_openapi.json.md:7; openapi info.description
- claim: scite distinguishes citation statements, tallies, paper metadata, search, reference check, and reference pairs in its API terminology.
  supporting_canonical_paths:
    - references/canonical_sources/md/scite_api/official_openapi_json_openapi.json.md
  support_type: direct
  verification_note: Keep these fields separate from traditional bibliography and SR evidence concepts.
  quote_or_locator: official_openapi_json_openapi.json.md:7; Overview and Terminology block
- claim: Most scite endpoints require tokens, and unauthenticated use has documented default rate limits while some endpoints are uncapped.
  supporting_canonical_paths:
    - references/canonical_sources/md/scite_api/official_openapi_json_openapi.json.md
  support_type: direct
  verification_note: Token access and bypassing rate limits require current scite contact/terms verification.
  quote_or_locator: official_openapi_json_openapi.json.md:7; Authentication and Rate Limiting blocks
- claim: scite Search and Recommendations APIs can require separate licenses for commercial or research use.
  supporting_canonical_paths:
    - references/canonical_sources/md/scite_api/official_openapi_json_openapi.json.md
  support_type: direct
  verification_note: Treat license status as an access blocker, not a minor caveat.
  quote_or_locator: official_openapi_json_openapi.json.md:7; tags Search and Paper recommendations
```

## Operational rules

- Use scite only for citation-context, smart-citation, tallies, assistant, or reference-check enrichment when access rights are known.
- Treat token scopes, separate licenses, premium/MCP access, and paid features as first-class requirements.
- Keep scite citation classifications separate from inclusion/exclusion decisions unless a review protocol explicitly defines their role.
- Do not use scite API documentation as SR or survey-writing methodology authority.

## Common misuses

- Treating scite classifications as direct quality appraisal or certainty evidence.
- Treating API availability as permission to search or reuse at research/commercial scale.
- Ignoring token scopes, paid license requirements, or endpoint-specific restrictions.
- Treating the short local HTML docs capture as sufficient for detailed API implementation.

## Evidence limits

The useful local canonical source is the OpenAPI JSON converted into one long Markdown line. It supports routing and caveats, but detailed implementation should use live OpenAPI/docs and the applicable scite agreement.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=scite_api`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=scite_api`.
- Canonical Markdown: `references/canonical_sources/md/scite_api/`.
- Optional section locators: `references/corpus_index/sections/by_source/scite_api.jsonl`.

## Unresolved gaps

- Confirm which scite endpoints and scopes are actually available in the user's account.
- Capture a more readable OpenAPI-derived section index if this source becomes operationally important.
