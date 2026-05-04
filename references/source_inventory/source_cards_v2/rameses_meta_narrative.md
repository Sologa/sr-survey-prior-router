# RAMESES Meta-Narrative Source Card v2

```yaml
source_id: rameses_meta_narrative
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md
canonical_urls:
  - https://www.equator-network.org/reporting-guidelines/rameses-publication-standards-meta-narrative-reviews/
authority_level: canonical_reporting_guideline
version_or_access_date: "2013 standards; EQUATOR record last updated 2022-01-13; local corpus fetched 2026-05-04"
applies_to:
  - routing meta-narrative review reporting questions
  - identifying RAMESES meta-narrative bibliographic metadata and applicability from the local EQUATOR record
  - distinguishing meta-narrative review standards from ordinary narrative review guidance
not_for:
  - realist synthesis reporting
  - ordinary narrative reviews or scoping reviews
  - taxonomy-driven field surveys without an explicit meta-narrative method
  - RAMESES standards item claims unless local fulltext or standards text is captured
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate because the local capture is an EQUATOR registry entry for 2013 standards, last updated 2022; verify current RAMESES project/full-report links before detailed use.
reuse_or_license_risk: EQUATOR record and linked RAMESES project/full-report terms apply; verify license before redistributing standards text.
qa_status: worker_d_verified_against_local_canonical_markdown_registry_only
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: The local RAMESES meta-narrative source is an EQUATOR reporting-guideline page for reporting meta-narrative reviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md
  support_type: direct
  verification_note: Use this page for source identity and route selection before opening any RAMESES full-report source.
  quote_or_locator: references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md:47,53-57; section_id=rameses_meta_narrative__canonical_rameses_publication_standards_meta_narrative_reviews__s0003_rameses_publication_standards_meta_narrative_reviews
- claim: The EQUATOR record identifies Wong, Greenhalgh, Westhorp, Buckingham, and Pawson as authors of the RAMESES publication standards for meta-narrative reviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md
  support_type: direct
  verification_note: Use this as bibliographic metadata; do not infer standards items from the citation line alone.
  quote_or_locator: references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md:59-63; section_id=rameses_meta_narrative__canonical_rameses_publication_standards_meta_narrative_reviews__s0003_rameses_publication_standards_meta_narrative_reviews
- claim: The EQUATOR record points to a RAMESES project full report and website, but the local card's canonical path is the registry page.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md
  support_type: direct
  verification_note: Treat the full-report and project website lines as locators until those sources are locally captured and verified.
  quote_or_locator: references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md:67-73; section_id=rameses_meta_narrative__canonical_rameses_publication_standards_meta_narrative_reviews__s0003_rameses_publication_standards_meta_narrative_reviews
- claim: The EQUATOR record gives the acronym as RAMESES for meta-narrative reviews and classifies the study design as systematic reviews/meta-analyses/reviews/HTA/overviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md
  support_type: direct
  verification_note: Use this only as route and source metadata.
  quote_or_locator: references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md:75-77; section_id=rameses_meta_narrative__canonical_rameses_publication_standards_meta_narrative_reviews__s0003_rameses_publication_standards_meta_narrative_reviews
- claim: The EQUATOR record says the RAMESES meta-narrative standards apply to the whole report.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md
  support_type: direct
  verification_note: Whole-report applicability does not make RAMESES a generic narrative-review checklist.
  quote_or_locator: references/canonical_sources/md/rameses_meta_narrative/canonical_rameses-publication-standards-meta-narrative-reviews.md:79-81; section_id=rameses_meta_narrative__canonical_rameses_publication_standards_meta_narrative_reviews__s0003_rameses_publication_standards_meta_narrative_reviews
```

## Operational rules

- Route to this source only when the user names or clearly implies a meta-narrative review.
- Use the local EQUATOR capture for source identity, citation, acronym, broad scope, and whole-report applicability.
- Do not use this card to populate RAMESES standards items; capture and verify the article/full report first.
- Keep RAMESES meta-narrative separate from RAMESES realist synthesis unless the task explicitly compares the two.

## Common misuses

- Collapsing meta-narrative reviews into ordinary narrative reviews.
- Treating the RAMESES project full-report locator as if the local full report were already available.
- Reusing realist-synthesis claims for meta-narrative reviews without a comparative source.

## Evidence limits

The local canonical Markdown is an EQUATOR registry page. It supports route selection and bibliographic/source metadata, but not detailed standards-item claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=rameses_meta_narrative`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=rameses_meta_narrative`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=rameses_meta_narrative`.
- Optional local section locators: `references/corpus_index/sections/by_source/rameses_meta_narrative.jsonl`.

## Unresolved gaps

- Local fulltext for the RAMESES meta-narrative article or NIHR full report is not included in this card's canonical paths, so detailed publication-standards item claims remain unresolved.
