# DBLP Source Card v2

```yaml
source_id: dblp
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/dblp/canonical.md
  - references/canonical_sources/md/dblp/linked_1_dblpxml.pdf.md
  - references/canonical_sources/md/dblp/linked_2_dblpxmlreq.pdf.md
canonical_urls:
  - https://dblp.org/
  - https://dblp.org/xml/docu/dblpxml.pdf
  - https://dblp.org/xml/docu/dblpxmlreq.pdf
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local corpus fetched 2026-05-04"
applies_to:
  - computer science bibliography lookup
  - CS venue and author metadata normalization
  - DBLP XML or RDF dump routing
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - full-text retrieval
  - native citation graph completeness
  - broad non-CS coverage
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: medium for publication counts, dump hosting, API behavior, and external-link integrations; verify live DBLP docs before implementation.
reuse_or_license_risk: DBLP metadata is captured as CC0/open data locally, but linked full text and external APIs have separate terms and privacy policies.
qa_status: seed_verified_from_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: DBLP provides open bibliographic information for major computer science journals and proceedings.
  supporting_canonical_paths:
    - references/canonical_sources/md/dblp/canonical.md
  support_type: direct
  verification_note: Use for CS bibliography and venue normalization, not review methodology.
  quote_or_locator: canonical.md:543-545
- claim: DBLP exposes raw metadata as a downloadable XML file and points to XML/API documentation.
  supporting_canonical_paths:
    - references/canonical_sources/md/dblp/canonical.md
  support_type: direct
  verification_note: XML dump and primitive query API details should be checked live before a downloader is built.
  quote_or_locator: canonical.md:561-563
- claim: DBLP metadata is released as open data under CC0 in the local capture.
  supporting_canonical_paths:
    - references/canonical_sources/md/dblp/canonical.md
  support_type: direct
  verification_note: This does not transfer rights for linked publisher content or external APIs.
  quote_or_locator: canonical.md:642-644
- claim: DBLP record pages can load references, citations, and OA links from external services, so those enrichments are not native DBLP evidence.
  supporting_canonical_paths:
    - references/canonical_sources/md/dblp/canonical.md
  support_type: direct
  verification_note: Treat Crossref, OpenCitations, Semantic Scholar, Unpaywall, and OpenAlex enrichments as separate source checks.
  quote_or_locator: canonical.md:601-640
```

## Operational rules

- Use DBLP for CS-focused metadata, author/venue disambiguation, and local bibliography checks.
- Use DBLP XML/RDF dump routes for repeatable CS metadata ingestion only after checking current dump URLs and terms.
- Keep DBLP metadata separate from full-text availability and from third-party reference/citation enrichments.
- Do not use DBLP as evidence for PRISMA, Cochrane, JBI, GRADE, appraisal, or survey-writing rules.

## Common misuses

- Treating DBLP as a full-text source.
- Treating third-party citation/reference panels on DBLP pages as DBLP-native data.
- Assuming DBLP covers non-CS scholarly literature comprehensively.
- Treating current counts in the captured page as stable.

## Evidence limits

This card supports routing to DBLP metadata documentation only. Any final claim about API behavior, dump cadence, coverage, counts, or terms needs canonical Markdown or current live documentation.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=dblp`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=dblp`.
- Canonical Markdown: `references/canonical_sources/md/dblp/`.
- Optional section locators: `references/corpus_index/sections/by_source/dblp.jsonl`.

## Unresolved gaps

- Confirm current XML/RDF dump hosting, update cadence, and API limits before operational use.
- Decide whether local workflows need the older XML documentation PDFs or only the current homepage/dump docs.
