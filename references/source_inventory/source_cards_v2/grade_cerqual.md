# GRADE-CERQual Source Card v2

```yaml
source_id: grade_cerqual
source_family: sr_certainty_appraisal_bias_search
canonical_paths:
  - references/canonical_sources/md/grade_cerqual/canonical.md
canonical_urls:
  - https://www.cerqual.org/
authority_level: canonical_certainty_framework
version_or_access_date: "site copyright 2018; local corpus fetched 2026-05-04"
applies_to:
  - confidence in findings from qualitative evidence syntheses
  - systematic reviews of qualitative evidence
  - qualitative evidence synthesis Summary of Qualitative Findings workflow
not_for:
  - quantitative effect certainty
  - AMSTAR 2 or ROBIS review appraisal
  - primary-study risk-of-bias assessment
  - replacing full published CERQual guidance when component-level rules are needed
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate; the local capture is an official landing page with links to most recent published guidance, but not the full guidance supplement itself.
reuse_or_license_risk: The captured page states all rights reserved; verify resource-specific terms before redistributing substantial excerpts or mirrored guidance resources.
qa_status: seed_verified_by_worker_c_with_local_locators_landing_page_only
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: GRADE-CERQual provides a transparent method for assessing confidence in evidence from reviews of qualitative research.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_cerqual/canonical.md
  support_type: direct
  verification_note: Use the "What is the GRADE-CERQual approach?" section for the main scope claim.
  quote_or_locator: canonical.md:70-74; section_ids=grade_cerqual__canonical__s0002_confidence_in_the_evidence_from_reviews_of_qualitative_research, grade_cerqual__canonical__s0003_what_is_the_grade_cerqual_approach
- claim: CERQual is intended for findings from systematic reviews of qualitative evidence.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_cerqual/canonical.md
  support_type: direct
  verification_note: Use this sentence for the qualitative-synthesis boundary before routing quantitative effect certainty elsewhere.
  quote_or_locator: canonical.md:74; section_id=grade_cerqual__canonical__s0003_what_is_the_grade_cerqual_approach
- claim: The iSoQ tool is an online platform designed to help review authors apply GRADE-CERQual to findings of qualitative evidence synthesis.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_cerqual/canonical.md
  support_type: direct
  verification_note: Use the landing page only as a locator for iSoQ, not as full iSoQ documentation.
  quote_or_locator: canonical.md:76-78; section_id=grade_cerqual__canonical__s0004_have_you_tried_our_online_tool_https_isoq_epistemonikos_org
- claim: The captured CERQual page links to the most recent published guidance for applying GRADE-CERQual.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_cerqual/canonical.md
  support_type: direct
  verification_note: Treat this as a locator to the guidance supplement; open the guidance itself for component-level rules.
  quote_or_locator: canonical.md:84; section_id=grade_cerqual__canonical__s0005_the_most_recent_published_guidance_for_applying_grade_cerqual_http_implementatio
- claim: Methodological limitations of evidence contributing to a review finding are one component of the GRADE-CERQual approach.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_cerqual/canonical.md
  support_type: direct
  verification_note: Use the component link as a locator; do not infer all CERQual component rules from this landing-page sentence.
  quote_or_locator: canonical.md:86-88; section_id=grade_cerqual__canonical__s0006_camelot_tool_for_assessing_methodological_limitations_https_www_cerqual_org_meth
- claim: CERQual development is being taken forward through the GRADE-CERQual Project Group, a subgroup of the GRADE Working Group.
  supporting_canonical_paths:
    - references/canonical_sources/md/grade_cerqual/canonical.md
  support_type: direct
  verification_note: Use the project-group line for governance/relationship claims.
  quote_or_locator: canonical.md:98-100; section_id=grade_cerqual__canonical__s0009_the_grade_cerqual_coordinating_team_https_www_cerqual_org_the_grade_cerqual_proj
```

## Operational rules

- Use `grade_cerqual` for confidence in findings from qualitative evidence syntheses.
- Route quantitative effect-certainty questions to `grade_working_group` or `grade_handbook`.
- Treat the local CERQual card as a landing-page source; open the linked published guidance for component-level CERQual methods.
- Do not use CERQual as an AMSTAR 2, ROBIS, RoB 2, or ROBINS-I substitute.

## Common misuses

- Applying CERQual to quantitative intervention effect estimates.
- Treating the landing page as the full CERQual guidance supplement.
- Treating CERQual confidence judgments as methodological-quality scores for whole reviews.
- Using CERQual to appraise primary qualitative studies without the CERQual review-finding context.

## Evidence limits

This card is a router aid. Final claims about CERQual must cite the captured CERQual page or the linked published guidance directly. Source manifests, route registries, section indexes, and this card are locator-only for substantive claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=grade_cerqual`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=grade_cerqual`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=grade_cerqual`.
- Optional local section locators: `references/corpus_index/sections/by_source/grade_cerqual.jsonl`.

## Unresolved gaps

- The local capture is only the CERQual landing page; full published guidance and component pages are not locally captured as canonical Markdown in this source_id bundle.
- Component-level rules for relevance, adequacy, coherence, and methodological limitations require opening the linked published guidance or adding local canonical captures.
