# Lens API Source Card v2

```yaml
source_id: lens_api
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/lens_api/canonical_docs_home_canonical_docs_home.md
  - references/canonical_sources/md/lens_api/official_scholarly_request_schema_request-scholar.html.md
  - references/canonical_sources/md/lens_api/official_scholarly_response_schema_response-scholar.html.md
  - references/canonical_sources/md/lens_api/official_scholarly_examples_examples-scholar.html.md
  - references/canonical_sources/md/lens_api/official_swagger_yaml_swagger.yaml.md
canonical_urls:
  - https://docs.api.lens.org/
  - https://docs.api.lens.org/request-scholar.html
  - https://docs.api.lens.org/response-scholar.html
  - https://docs.api.lens.org/examples-scholar.html
  - https://api.lens.org/swagger.yaml
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local docs report Lens API 2.19.3 and last update 2026-04-17"
applies_to:
  - Lens scholarly works lookup
  - patent-linked literature enrichment
  - scholarly and patent metadata field audit
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - low-friction open public backbone
  - unrestricted bulk replication
  - license-free reuse of Lens data
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for API version, schema version, access plans, tokens, quotas, and attribution requirements; verify live Lens docs before implementation.
reuse_or_license_risk: Lens API access requires plans/tokens and terms; attribution requirements and scholarly/patent API terms must be reviewed before reuse.
qa_status: seed_verified_from_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: Lens API documentation covers scholarly works and patent API resources through a versioned REST API.
  supporting_canonical_paths:
    - references/canonical_sources/md/lens_api/canonical_docs_home_canonical_docs_home.md
  support_type: direct
  verification_note: Use Lens for scholarly/patent metadata routing, not SR or survey methodology.
  quote_or_locator: canonical_docs_home_canonical_docs_home.md:57-72
- claim: New Lens Scholarly API users must provide identity, organization address, official email, and intended-use information, and API users must follow attribution requirements.
  supporting_canonical_paths:
    - references/canonical_sources/md/lens_api/canonical_docs_home_canonical_docs_home.md
  support_type: direct
  verification_note: Treat access and attribution as implementation blockers until verified.
  quote_or_locator: canonical_docs_home_canonical_docs_home.md:76-78
- claim: Lens scholarly requests support query, sort, include/exclude projection, pagination, scroll, stemming, and regex controls.
  supporting_canonical_paths:
    - references/canonical_sources/md/lens_api/official_scholarly_request_schema_request-scholar.html.md
  support_type: direct
  verification_note: Use schema docs for request-building, with current API version verification.
  quote_or_locator: official_scholarly_request_schema_request-scholar.html.md:63-130
- claim: Lens scholarly responses include external identifiers, references, scholarly citation counts, patent citations, and patent citation counts.
  supporting_canonical_paths:
    - references/canonical_sources/md/lens_api/official_scholarly_response_schema_response-scholar.html.md
    - references/canonical_sources/md/lens_api/official_scholarly_examples_examples-scholar.html.md
  support_type: direct
  verification_note: Patent-linked fields are enrichment metadata, not review-method evidence.
  quote_or_locator: official_scholarly_response_schema_response-scholar.html.md:111-207; official_scholarly_examples_examples-scholar.html.md:81-103
```

## Operational rules

- Use Lens when patent-linked scholarly metadata or cross-domain scholarly/patent enrichment is explicitly needed.
- Treat access-plan approval, token management, attribution, and terms as part of any implementation plan.
- Keep Lens API field evidence separate from the underlying publisher record and from systematic-review methodology sources.
- Do not use Lens documentation as a survey writing or SR conduct authority.

## Common misuses

- Treating Lens as an unrestricted open metadata backbone.
- Treating patent-citation enrichment as proof of clinical or SR relevance.
- Ignoring attribution and access-plan requirements.
- Assuming captured schema versions are current.

## Evidence limits

This card supports Lens API routing and field awareness. It does not certify access, quotas, commercial reuse, or current schema versions.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=lens_api`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=lens_api`.
- Canonical Markdown: `references/canonical_sources/md/lens_api/`.
- Optional section locators: `references/corpus_index/sections/by_source/lens_api.jsonl`.

## Unresolved gaps

- Verify current API plan, token, quota, attribution, and terms before executable use.
- Decide whether patent and scholarly Lens surfaces need separate future cards if workflows diverge.
