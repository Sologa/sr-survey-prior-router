# RAMESES Realist Source Card v2

```yaml
source_id: rameses_realist
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md
canonical_urls:
  - https://www.equator-network.org/reporting-guidelines/rameses-publication-standards-realist-syntheses/
authority_level: canonical_reporting_guideline
version_or_access_date: "2013 standards; EQUATOR record last updated 2022-01-13; local corpus fetched 2026-05-04"
applies_to:
  - routing realist synthesis reporting questions
  - identifying RAMESES realist synthesis bibliographic metadata and applicability from the local EQUATOR record
  - distinguishing realist synthesis standards from ordinary narrative or scoping review guidance
not_for:
  - meta-narrative review reporting
  - ordinary narrative reviews or scoping reviews
  - taxonomy-driven field surveys without an explicit realist synthesis method
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
- claim: The local RAMESES realist source is an EQUATOR reporting-guideline page for reporting realist syntheses.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md
  support_type: direct
  verification_note: Use this page for source identity and route selection before opening any RAMESES full-report source.
  quote_or_locator: references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md:47,53-57; section_id=rameses_realist__canonical_rameses_publication_standards_realist_syntheses__s0003_rameses_publication_standards_realist_syntheses
- claim: The EQUATOR record identifies Wong, Greenhalgh, Westhorp, Buckingham, and Pawson as authors of the RAMESES publication standards for realist syntheses.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md
  support_type: direct
  verification_note: Use this as bibliographic metadata; do not infer standards items from the citation line alone.
  quote_or_locator: references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md:59-63; section_id=rameses_realist__canonical_rameses_publication_standards_realist_syntheses__s0003_rameses_publication_standards_realist_syntheses
- claim: The EQUATOR record points to a RAMESES project full report and website, but the local card's canonical path is the registry page.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md
  support_type: direct
  verification_note: Treat the full-report and project website lines as locators until those sources are locally captured and verified.
  quote_or_locator: references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md:67-73; section_id=rameses_realist__canonical_rameses_publication_standards_realist_syntheses__s0003_rameses_publication_standards_realist_syntheses
- claim: The EQUATOR record gives the acronym as RAMESES for realist syntheses and classifies the study design as systematic reviews/meta-analyses/reviews/HTA/overviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md
  support_type: direct
  verification_note: Use this only as route and source metadata.
  quote_or_locator: references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md:75-77; section_id=rameses_realist__canonical_rameses_publication_standards_realist_syntheses__s0003_rameses_publication_standards_realist_syntheses
- claim: The EQUATOR record says the RAMESES realist synthesis standards apply to the whole report.
  supporting_canonical_paths:
    - references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md
  support_type: direct
  verification_note: Whole-report applicability does not make RAMESES a generic narrative-review checklist.
  quote_or_locator: references/canonical_sources/md/rameses_realist/canonical_rameses-publication-standards-realist-syntheses.md:79-81; section_id=rameses_realist__canonical_rameses_publication_standards_realist_syntheses__s0003_rameses_publication_standards_realist_syntheses
```

## Operational rules

- Route to this source only when the user names or clearly implies a realist synthesis.
- Use the local EQUATOR capture for source identity, citation, acronym, broad scope, and whole-report applicability.
- Do not use this card to populate RAMESES standards items; capture and verify the article/full report first.
- Keep RAMESES realist synthesis separate from RAMESES meta-narrative unless the task explicitly compares the two.

## Common misuses

- Collapsing realist synthesis into ordinary narrative or scoping review guidance.
- Treating the RAMESES project full-report locator as if the local full report were already available.
- Reusing meta-narrative claims for realist syntheses without a comparative source.

## Evidence limits

The local canonical Markdown is an EQUATOR registry page. It supports route selection and bibliographic/source metadata, but not detailed standards-item claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=rameses_realist`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=rameses_realist`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=rameses_realist`.
- Optional local section locators: `references/corpus_index/sections/by_source/rameses_realist.jsonl`.

## Unresolved gaps

- Local fulltext for the RAMESES realist synthesis article or NIHR full report is not included in this card's canonical paths, so detailed publication-standards item claims remain unresolved.
