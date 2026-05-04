# Source card v2: OpenAlex API

```yaml
source_id: openalex
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/openalex/canonical.md
  - references/canonical_sources/md/openalex_snapshot/official_snapshot_data_format_snapshot-format.md
  - references/canonical_sources/md/openalex_snapshot/official_api_overview_introduction.md
canonical_urls:
  - https://developers.openalex.org/
authority_level: canonical_database_api_doc
version_or_access_date: local capture reviewed 2026-05-04
applies_to:
  - scholarly entity metadata retrieval
  - works/authors/sources/institutions/topics/publishers/funders discovery
  - open scholarly graph and snapshot access
  - retrieval pipeline planning
not_for:
  - systematic review conduct authority
  - reporting guideline authority
  - certainty appraisal
  - venue policy
route_relevance:
  - paper_retrieval_prior
  - survey_writing_prior
  - scholarly_database_selection
  - source_audit
freshness_risk: high; API pricing, limits, endpoints, and authentication can change.
reuse_or_license_risk: OpenAlex describes dataset openness/CC0; verify current terms before large-scale redistribution or commercial use.
qa_status: draft_v2_example
last_reviewed: 2026-05-04
```

## Key points

```yaml
- claim: "OpenAlex is an open catalog of the global research system covering scholarly works, authors, institutions, sources, topics, publishers, and funders."
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: direct
  verification_note: "The overview page describes OpenAlex and its entity types."
  quote_or_locator: "Overview / Documentation Index and Data sections."

- claim: "OpenAlex offers both a REST API and a downloadable data snapshot."
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: direct
  verification_note: "The overview page states that the documentation covers the API and data snapshot."
  quote_or_locator: "Overview / Access section."

- claim: "OpenAlex can support retrieval and metadata expansion, but it is not itself a methodology authority for SR conduct."
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: indirect
  verification_note: "The source describes data/API access, not review methods. The non-methodology boundary is inferred from source type."
  quote_or_locator: "Overview / Data and Access sections."

- claim: "OpenAlex freshness risk is high because the local capture includes current API access/pricing language."
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: direct
  verification_note: "The page mentions API key, free usage, paid plan, and snapshot update cadence; these are operational details that can change."
  quote_or_locator: "Overview / Access section."
```

## Operational rules

1. Use OpenAlex for open scholarly graph metadata, entity expansion, and broad discovery.
2. Verify API limits, authentication, pricing, and snapshot cadence live or from the latest canonical Markdown before implementation decisions.
3. Pair OpenAlex with PubMed/Europe PMC/Crossref/Semantic Scholar/OpenCitations depending on domain, metadata need, and citation-link need.
4. Do not cite OpenAlex as proof that a search strategy is systematic or comprehensive.

## Common misuses

1. Treating OpenAlex coverage claims as a substitute for database-selection guidance from Cochrane/JBI/search-method sources.
2. Treating API availability as proof of canonical bibliographic completeness.
3. Using old local API limits without freshness checks.
4. Confusing source metadata coverage with venue/methodological authority.

## Evidence limits

- Supports claims about OpenAlex data/API/snapshot access.
- Does not support PRISMA, Cochrane, JBI, AMSTAR, ROBIS, or GRADE claims.
- Operational details may be stale.

## Verification paths

1. `references/canonical_sources/md/openalex/canonical.md`
2. `references/canonical_sources/md/openalex_snapshot/official_snapshot_data_format_snapshot-format.md`
3. `references/canonical_sources/download_manifest.jsonl`
4. `references/source_inventory/local_corpus_index.md`

## Unresolved gaps

- Add latest live verification step for API limits, pricing, and authentication before release.
- Add route-specific comparison table with Crossref, PubMed, Semantic Scholar, OpenCitations, and Europe PMC.
