# ROBINS-I Source Card v2

```yaml
source_id: robins_i
source_family: sr_certainty_appraisal_bias_search
canonical_paths:
  - references/canonical_sources/md/robins_i/canonical_home.md
canonical_urls:
  - https://www.riskofbias.info/welcome/home
authority_level: canonical_appraisal_tool
version_or_access_date: "original 2016 version; V2 draft notice dated 2025-11-30; local corpus fetched 2026-05-04"
applies_to:
  - primary-study risk-of-bias assessment for non-randomized studies of interventions
  - routing between original 2016 ROBINS-I material and the V2 draft notice
not_for:
  - randomized trials
  - risk of bias in systematic reviews
  - systematic review reporting guidance
  - certainty or confidence grading
  - non-intervention exposure or measurement-error tools
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: high; the captured page announces a ROBINS-I V2 draft notice dated 2025-11-30, so live verification is needed before choosing between original 2016 and V2 materials.
reuse_or_license_risk: ROBINS-I is stated with the same CC BY-NC-ND 4.0 notice as the other risk-of-bias tools on the captured page; verify terms for any linked tool, template, or guidance file.
qa_status: seed_verified_by_worker_f_with_local_locators_partial_capture
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: ROBINS-I is identified as a risk-of-bias tool for non-randomized studies of interventions.
  supporting_canonical_paths:
    - references/canonical_sources/md/robins_i/canonical_home.md
  support_type: direct
  verification_note: Use ROBINS-I routing for non-randomized intervention studies, not randomized trials.
  quote_or_locator: canonical_home.md:96-100; section_id=robins_i__canonical_home__s0003_risk_of_bias_in_non_randomized_studies_of_interventions
- claim: The captured page announces a ROBINS-I V2 draft notice dated 30 November 2025.
  supporting_canonical_paths:
    - references/canonical_sources/md/robins_i/canonical_home.md
  support_type: direct
  verification_note: Treat version selection as freshness-sensitive and verify the live page or captured V2 material before applying detailed guidance.
  quote_or_locator: canonical_home.md:102; section_id=robins_i__canonical_home__s0003_risk_of_bias_in_non_randomized_studies_of_interventions
- claim: The captured page points to original 2016 ROBINS-I materials, including detailed guidance, tool, and template entries.
  supporting_canonical_paths:
    - references/canonical_sources/md/robins_i/canonical_home.md
  support_type: direct
  verification_note: The home page names these materials but this local canonical Markdown file does not contain the detailed contents.
  quote_or_locator: canonical_home.md:56-68,104; section_ids=robins_i__canonical_home__s0001_robins_i_tool, robins_i__canonical_home__s0003_risk_of_bias_in_non_randomized_studies_of_interventions
- claim: The local canonical Markdown is too thin to support ROBINS-I domain, signaling-question, or judgment-algorithm claims by itself.
  supporting_canonical_paths:
    - references/canonical_sources/md/robins_i/canonical_home.md
  support_type: indirect
  verification_note: Use this card only to route to ROBINS-I; inspect captured or live detailed guidance/tool files before making operational ROBINS-I assessment claims.
  quote_or_locator: canonical_home.md:96-104; section_id=robins_i__canonical_home__s0003_risk_of_bias_in_non_randomized_studies_of_interventions
- claim: The captured page states RoB 2, ROBINS-I, ROBINS-E, and ROB-ME are licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License and notes limits on help-desk and Excel-tool support.
  supporting_canonical_paths:
    - references/canonical_sources/md/robins_i/canonical_home.md
  support_type: direct
  verification_note: Check license and support text before redistributing linked files or relying on tool implementations.
  quote_or_locator: canonical_home.md:108; section_id=robins_i__canonical_home__s0003_risk_of_bias_in_non_randomized_studies_of_interventions
```

## Operational rules

- Use ROBINS-I only for primary-study risk-of-bias questions involving non-randomized studies of interventions.
- Verify whether the task should use original 2016 ROBINS-I material or newer V2 draft material before giving detailed assessment guidance.
- For randomized trials, route to `rob2` instead.
- For risk of bias in systematic reviews, route to `robis`; for review quality appraisal, route to `amstar2`; for reporting and certainty claims, route to PRISMA/GRADE-family sources.
- Do not use this local home-page capture alone for domain-level ROBINS-I judgments or algorithmic scoring.

## Common misuses

- Applying ROBINS-I to randomized trials.
- Treating ROBINS-I as a review-level appraisal tool, reporting guideline, or certainty framework.
- Treating the local home-page capture as if it contains the full 2016 detailed guidance, tool, or template.
- Ignoring the V2 draft notice when version choice matters.

## Evidence limits

This card is a router aid. The local canonical Markdown for `robins_i` is a thin home page capture with purpose/version locators and license text. It is not enough to support detailed ROBINS-I assessment domains, signaling questions, judgment algorithms, or implementation templates without additional captured or live source verification.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=robins_i`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=robins_i`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=robins_i`.
- Optional local section locators: `references/corpus_index/sections/by_source/robins_i.jsonl`.

## Unresolved gaps

- The local corpus does not include separate Markdown captures for the original 2016 detailed guidance, tool, or template.
- The V2 draft notice is present only as a home-page notice here; add a separate captured source or claim ledger before using V2 details.
