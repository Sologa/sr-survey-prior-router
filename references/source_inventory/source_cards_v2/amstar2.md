# AMSTAR 2 Source Card v2

```yaml
source_id: amstar2
source_family: sr_certainty_appraisal_bias_search
canonical_paths:
  - references/canonical_sources/md/amstar2/canonical.md
  - references/canonical_sources/md/amstar2/linked_1_bmj.j4008.full.pdf.md
  - references/canonical_sources/md/amstar2/linked_2_amstar-2.pdf.md
  - references/canonical_sources/md/amstar2/linked_3_amstar_202-guidance-document.pdf.md
canonical_urls:
  - https://www.amstar.ca/
  - https://www.bmj.com/content/358/bmj.j4008
  - https://www.amstar.ca/docs/AMSTAR-2.pdf
  - https://www.amstar.ca/docs/AMSTAR%202-Guidance-document.pdf
authority_level: canonical_appraisal_tool
version_or_access_date: "AMSTAR 2 article 2017; official site local corpus fetched 2026-05-04"
applies_to:
  - critical appraisal of systematic reviews of healthcare interventions
  - appraisal of reviews including randomized studies, non-randomized studies, or both
  - overview-of-reviews appraisal support
not_for:
  - appraising primary studies directly
  - replacing systematic review conduct guidance
  - review-level risk-of-bias assessment when ROBIS is the intended tool
  - certainty grading of effect estimates
  - reporting guideline compliance
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: low for the 2017 AMSTAR 2 article and captured tool/guidance; verify the official AMSTAR site for newer training materials or updated downloads before relying on current website wording.
reuse_or_license_risk: BMJ and AMSTAR tool/guidance terms apply; verify source-specific reuse terms before redistributing substantial excerpts or raw tool files.
qa_status: seed_verified_by_worker_c_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: AMSTAR 2 is a critical appraisal tool for systematic reviews that include randomized or non-randomized studies of healthcare interventions, or both.
  supporting_canonical_paths:
    - references/canonical_sources/md/amstar2/canonical.md
    - references/canonical_sources/md/amstar2/linked_1_bmj.j4008.full.pdf.md
  support_type: direct
  verification_note: Use the official AMSTAR landing page and the BMJ article title/abstract for the review-appraisal scope.
  quote_or_locator: canonical.md:12-14; section_id=amstar2__canonical__s0002_amstar_2; linked_1_bmj.j4008.full.pdf.md:13-15,132-144; section_id=amstar2__linked_1_bmj_j4008_full_pdf__s0002_page_1
- claim: AMSTAR 2 has 16 items, uses critical domains for overall appraisal, and is not intended to generate an overall score.
  supporting_canonical_paths:
    - references/canonical_sources/md/amstar2/linked_1_bmj.j4008.full.pdf.md
    - references/canonical_sources/md/amstar2/linked_3_amstar_202-guidance-document.pdf.md
  support_type: direct
  verification_note: Use the BMJ key-points box and guidance document before turning AMSTAR 2 into a numeric scale.
  quote_or_locator: linked_1_bmj.j4008.full.pdf.md:138-142,783-808; section_ids=amstar2__linked_1_bmj_j4008_full_pdf__s0002_page_1, amstar2__linked_1_bmj_j4008_full_pdf__s0007_page_6; linked_3_amstar_202-guidance-document.pdf.md:23-27; section_id=amstar2__linked_3_amstar_202_guidance_document_pdf__s0002_page_1
- claim: AMSTAR 2 appraises many review-conduct domains, including critical domains that can affect review validity and confidence in review findings.
  supporting_canonical_paths:
    - references/canonical_sources/md/amstar2/linked_1_bmj.j4008.full.pdf.md
  support_type: direct
  verification_note: Use the critical-domain discussion when deciding whether a review flaw should affect the overall appraisal.
  quote_or_locator: linked_1_bmj.j4008.full.pdf.md:602-646,941-943; section_ids=amstar2__linked_1_bmj_j4008_full_pdf__s0006_page_5, amstar2__linked_1_bmj_j4008_full_pdf__s0008_page_7
- claim: AMSTAR 2 differs from ROBIS because AMSTAR 2 gives a broad quality appraisal for reviews of healthcare interventions, while ROBIS focuses specifically on risk of bias introduced by review conduct.
  supporting_canonical_paths:
    - references/canonical_sources/md/amstar2/linked_1_bmj.j4008.full.pdf.md
  support_type: direct
  verification_note: Use this boundary before routing review-level bias questions to AMSTAR 2 instead of ROBIS.
  quote_or_locator: linked_1_bmj.j4008.full.pdf.md:904-928; section_id=amstar2__linked_1_bmj_j4008_full_pdf__s0008_page_7
- claim: AMSTAR 2 may help as a brief teaching aid or checklist, but it does not explain the logic and methods of conducting systematic reviews in detail.
  supporting_canonical_paths:
    - references/canonical_sources/md/amstar2/linked_1_bmj.j4008.full.pdf.md
  support_type: direct
  verification_note: Preserve the appraisal-tool versus conduct-manual boundary when using AMSTAR 2 in routing.
  quote_or_locator: linked_1_bmj.j4008.full.pdf.md:809-814,937-940; section_ids=amstar2__linked_1_bmj_j4008_full_pdf__s0007_page_6, amstar2__linked_1_bmj_j4008_full_pdf__s0008_page_7
```

## Operational rules

- Use `amstar2` for critical appraisal of systematic reviews, especially reviews of healthcare interventions that include randomized and/or non-randomized studies.
- Do not turn AMSTAR 2 item responses into an additive quality score.
- Route review-level risk-of-bias questions to `robis` when the user asks specifically about risk of bias in a systematic review.
- Route certainty-of-evidence questions to `grade_working_group` or `grade_handbook`; AMSTAR 2 is not a GRADE certainty framework.

## Common misuses

- Applying AMSTAR 2 directly to primary studies.
- Treating AMSTAR 2 as a full systematic review conduct manual.
- Treating AMSTAR 2 as a reporting guideline or PRISMA substitute.
- Collapsing AMSTAR 2 responses into a single score without accounting for critical domains.

## Evidence limits

This card is a router aid. Final claims about AMSTAR 2 must cite the official site, BMJ article, AMSTAR 2 tool, or guidance Markdown directly. Source manifests, route registries, section indexes, and this card are locator-only for substantive claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=amstar2`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=amstar2`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=amstar2`.
- Optional local section locators: `references/corpus_index/sections/by_source/amstar2.jsonl`.

## Unresolved gaps

- The official site may expose newer training videos or download wording than the local 2026-05-04 capture.
- Local Markdown preserves content but not original PDF layout; inspect the raw PDF when exact tool form layout matters.
