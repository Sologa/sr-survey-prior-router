# ENTREQ Source Card v2

```yaml
source_id: entreq
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/entreq/canonical_entreq.md
canonical_urls:
  - https://www.equator-network.org/reporting-guidelines/entreq/
authority_level: canonical_reporting_guideline
version_or_access_date: "statement 2012; EQUATOR record last updated 2014-01-24; local corpus fetched 2026-05-04"
applies_to:
  - reporting synthesis of qualitative research
  - routing qualitative evidence synthesis reporting questions
  - identifying ENTREQ bibliographic metadata and applicability from the local EQUATOR record
not_for:
  - quantitative synthesis or synthesis without meta-analysis
  - realist synthesis or meta-narrative review publication standards
  - broad narrative reviews without qualitative-synthesis methods
  - ENTREQ checklist item claims unless local fulltext or checklist text is captured
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate because the local capture is a 2014 EQUATOR registry entry for a 2012 statement; verify current links/fulltext before detailed checklist use.
reuse_or_license_risk: EQUATOR record plus article terms apply; do not redistribute substantial guideline text without checking the source license.
qa_status: worker_d_verified_against_local_canonical_markdown_registry_only
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: ENTREQ is represented locally by an EQUATOR reporting-guideline page for enhancing transparency in reporting qualitative research synthesis.
  supporting_canonical_paths:
    - references/canonical_sources/md/entreq/canonical_entreq.md
  support_type: direct
  verification_note: Use this as the source identity and scope locator before making qualitative-synthesis reporting claims.
  quote_or_locator: references/canonical_sources/md/entreq/canonical_entreq.md:47,53-57; section_id=entreq__canonical_entreq__s0003_enhancing_transparency_in_reporting_the_synthesis_of_qualitative_research_entreq
- claim: The EQUATOR record gives the ENTREQ bibliographic reference as Tong, Flemming, McInnes, Oliver, and Craig, BMC Medical Research Methodology 2012.
  supporting_canonical_paths:
    - references/canonical_sources/md/entreq/canonical_entreq.md
  support_type: direct
  verification_note: Use this citation locator for source identification only; it does not provide the full ENTREQ checklist text.
  quote_or_locator: references/canonical_sources/md/entreq/canonical_entreq.md:59-63; section_id=entreq__canonical_entreq__s0003_enhancing_transparency_in_reporting_the_synthesis_of_qualitative_research_entreq
- claim: The EQUATOR record lists the reporting guideline acronym as ENTREQ and classifies the study design as qualitative research plus systematic reviews/meta-analyses/reviews/HTA/overviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/entreq/canonical_entreq.md
  support_type: direct
  verification_note: Use this classification for route selection, not for detailed checklist-item claims.
  quote_or_locator: references/canonical_sources/md/entreq/canonical_entreq.md:65-67; section_id=entreq__canonical_entreq__s0003_enhancing_transparency_in_reporting_the_synthesis_of_qualitative_research_entreq
- claim: The EQUATOR record says ENTREQ applies to narrative sections and procedure/method sections.
  supporting_canonical_paths:
    - references/canonical_sources/md/entreq/canonical_entreq.md
  support_type: direct
  verification_note: Keep this as section-routing metadata because the local page is an EQUATOR record, not a captured full checklist.
  quote_or_locator: references/canonical_sources/md/entreq/canonical_entreq.md:69-71; section_id=entreq__canonical_entreq__s0003_enhancing_transparency_in_reporting_the_synthesis_of_qualitative_research_entreq
- claim: The local ENTREQ capture should not be used for item-level checklist claims without an additional local fulltext or checklist source.
  supporting_canonical_paths:
    - references/canonical_sources/md/entreq/canonical_entreq.md
  support_type: indirect
  verification_note: The captured canonical Markdown section contains registry fields for scope, reference, acronym, study design, applicability, and update date; it does not contain checklist item text.
  quote_or_locator: references/canonical_sources/md/entreq/canonical_entreq.md:53-71; section_id=entreq__canonical_entreq__s0003_enhancing_transparency_in_reporting_the_synthesis_of_qualitative_research_entreq
```

## Operational rules

- Route to ENTREQ only when the task is about qualitative evidence synthesis reporting.
- Use the local EQUATOR page for source identity, scope, bibliographic reference, acronym, and applicability metadata.
- Do not generate ENTREQ checklist-item recommendations from this local capture alone.
- If item-level ENTREQ reporting advice is needed, first capture and verify local fulltext or checklist Markdown.

## Common misuses

- Treating ENTREQ as a general survey-writing rulebook.
- Applying ENTREQ to quantitative systematic reviews or SWiM scenarios.
- Inventing ENTREQ checklist items from memory or from other qualitative-review guidance.

## Evidence limits

The current local canonical Markdown is an EQUATOR registry page. It supports source location and high-level scope, but it is insufficient for exact ENTREQ checklist item claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=entreq`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=entreq`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=entreq`.
- Optional local section locators: `references/corpus_index/sections/by_source/entreq.jsonl`.

## Unresolved gaps

- Local fulltext/checklist Markdown for the ENTREQ article has not been captured in this card's canonical paths, so item-level checklist claims remain unresolved.
