# RoB 2 Source Card v2

```yaml
source_id: rob2
source_family: sr_certainty_appraisal_bias_search
canonical_paths:
  - references/canonical_sources/md/rob2/canonical_rob-2-0-tool.md
canonical_urls:
  - https://www.riskofbias.info/welcome/rob-2-0-tool
authority_level: canonical_appraisal_tool
version_or_access_date: "parallel-group version 2019-08-22; cluster and crossover versions revised 2021-03-18; local corpus fetched 2026-05-04"
applies_to:
  - primary-study risk-of-bias assessment for randomized trials
  - individually randomized parallel-group trials
  - cluster-randomized trials
  - crossover trials
not_for:
  - non-randomized studies of interventions
  - risk of bias in systematic reviews
  - systematic review reporting guidance
  - certainty or confidence grading
  - search strategy peer review
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate; the captured version dates are stable local evidence, but live tool pages, templates, Excel support, and archived/current status should be rechecked before operational use.
reuse_or_license_risk: RoB tools are stated as CC BY-NC-ND 4.0 on the captured page; verify terms for any linked tool, template, or redistribution.
qa_status: seed_verified_by_worker_f_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: RoB 2 is a revised Cochrane tool for assessing risk of bias in randomized trials.
  supporting_canonical_paths:
    - references/canonical_sources/md/rob2/canonical_rob-2-0-tool.md
  support_type: direct
  verification_note: Use this source for randomized-trial primary-study risk-of-bias routing, not for non-randomized studies or review-level appraisal.
  quote_or_locator: canonical_rob-2-0-tool.md:98,102,120; section_id=rob2__canonical_rob_2_0_tool__s0003_a_revised_cochrane_risk_of_bias_tool_for_randomized_trials
- claim: The captured page identifies a current individually randomized parallel-group version dated 22 August 2019 and cluster-randomized and crossover versions revised 18 March 2021.
  supporting_canonical_paths:
    - references/canonical_sources/md/rob2/canonical_rob-2-0-tool.md
  support_type: direct
  verification_note: Match the trial design before choosing a RoB 2 variant.
  quote_or_locator: canonical_rob-2-0-tool.md:106-110; section_id=rob2__canonical_rob_2_0_tool__s0003_a_revised_cochrane_risk_of_bias_tool_for_randomized_trials
- claim: The page maintains archives of previous RoB 2.0 versions, and the archived cluster and crossover sections say revised versions should be used in preference to archived versions.
  supporting_canonical_paths:
    - references/canonical_sources/md/rob2/canonical_rob-2-0-tool.md
  support_type: direct
  verification_note: Do not route to archived tools unless the task explicitly needs historical 2016 material.
  quote_or_locator: canonical_rob-2-0-tool.md:112,132-135,152-155,178-198; section_id=rob2__canonical_rob_2_0_tool__s0003_a_revised_cochrane_risk_of_bias_tool_for_randomized_trials
- claim: The local canonical Markdown identifies RoB 2 tool variants and citations but does not capture detailed domain-level scoring instructions from embedded tool files.
  supporting_canonical_paths:
    - references/canonical_sources/md/rob2/canonical_rob-2-0-tool.md
  support_type: indirect
  verification_note: Treat this card as a routing aid for selecting the source; retrieve or inspect the actual tool/guidance files before making detailed RoB 2 scoring or domain claims.
  quote_or_locator: canonical_rob-2-0-tool.md:102-110,132-198; section_id=rob2__canonical_rob_2_0_tool__s0003_a_revised_cochrane_risk_of_bias_tool_for_randomized_trials
- claim: The captured page states RoB 2, ROBINS-I, ROBINS-E, and ROB-ME are licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License and notes limits on help-desk and Excel-tool support.
  supporting_canonical_paths:
    - references/canonical_sources/md/rob2/canonical_rob-2-0-tool.md
  support_type: direct
  verification_note: Check license and support text in the specific file or page before redistributing material or relying on Excel implementations.
  quote_or_locator: canonical_rob-2-0-tool.md:202; section_id=rob2__canonical_rob_2_0_tool__s0003_a_revised_cochrane_risk_of_bias_tool_for_randomized_trials
```

## Operational rules

- Use RoB 2 only for primary-study risk-of-bias questions involving randomized trials.
- Choose the tool variant by trial design: individually randomized parallel-group, cluster-randomized, or crossover.
- Prefer current/revised variants over archived 2016 variants unless the user specifically asks for historical RoB 2.0 material.
- For non-randomized studies of interventions, route to `robins_i` instead.
- For risk of bias in systematic reviews, route to `robis`; for review quality appraisal, route to `amstar2`; for reporting and certainty claims, route to PRISMA/GRADE-family sources.

## Common misuses

- Applying RoB 2 to non-randomized studies.
- Treating RoB 2 as a reporting guideline, certainty framework, or review-level appraisal tool.
- Making detailed domain/scoring claims from this local page capture alone.
- Using archived versions when a current/revised variant is the relevant source.

## Evidence limits

This card is a source-selection aid. The canonical Markdown capture is a website page with version and routing information, not the full detailed tool/guidance content. Final answers about RoB 2 domains, signaling questions, algorithms, or scoring should cite the actual tool or guidance file after it is captured or inspected.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=rob2`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=rob2`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=rob2`.
- Optional local section locators: `references/corpus_index/sections/by_source/rob2.jsonl`.

## Unresolved gaps

- The local capture does not include separate current tool, guidance, template, or implementation files for RoB 2 variants.
- Add a detailed claim ledger only after the relevant RoB 2 tool/guidance files are captured or manually verified.
