# Cochrane MECIR Source Card v2

```yaml
source_id: cochrane_mecir
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/cochrane_mecir/canonical_mecir-manual.md
canonical_urls:
  - https://www.cochrane.org/authors/handbooks-and-manuals/mecir-manual
authority_level: canonical_conduct_manual
version_or_access_date: "Version August 2023; local corpus fetched 2026-05-04"
applies_to:
  - Cochrane Intervention Review conduct standards
  - planning and conduct standards for Cochrane review updates
  - Cochrane protocol, search, selection, data, bias, synthesis, and summary-of-findings standard routing
not_for:
  - treating Cochrane-specific standards as universal requirements for all systematic reviews
  - replacing the Cochrane Handbook chapter explanations
  - generic PRISMA reporting checklist claims outside Cochrane reporting expectations
  - non-intervention or non-Cochrane review conduct without adaptation
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: moderate because MECIR says the online version will be kept up to date; verify live pages for current Cochrane publication standards.
reuse_or_license_risk: Cochrane terms apply; verify permissions before redistributing standards text or generated PDFs.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: MECIR stands for Methodological Expectations of Cochrane Intervention Reviews and the local capture is Version August 2023.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_mecir/canonical_mecir-manual.md
  support_type: direct
  verification_note: Use the MECIR landing page for version and scope before opening any generated section PDF.
  quote_or_locator: canonical_mecir-manual.md:86-90; section_ids=cochrane_mecir__canonical_mecir_manual__s0005_methodological_expectations_of_cochrane_intervention_reviews_mecir, __s0006_standards_for_the_conduct_of_new_cochrane_intervention_reviews_and_the_planning_
- claim: MECIR presents standards for the conduct of new Cochrane Intervention Reviews and for planning and conduct of updates.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_mecir/canonical_mecir-manual.md
  support_type: direct
  verification_note: Preserve the Cochrane Intervention Review scope when applying these standards.
  quote_or_locator: canonical_mecir-manual.md:90,126-158; section_ids=cochrane_mecir__canonical_mecir_manual__s0006_standards_for_the_conduct_of_new_cochrane_intervention_reviews_and_the_planning_, __s0012_mecir
- claim: MECIR is a guide to the conduct of Cochrane Intervention Reviews and links to Cochrane Training resources, the Cochrane Handbook, and other resources.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_mecir/canonical_mecir-manual.md
  support_type: direct
  verification_note: Use MECIR for standards and the Handbook for explanatory method detail.
  quote_or_locator: canonical_mecir-manual.md:102-106; section_id=cochrane_mecir__canonical_mecir_manual__s0011_4_professor_of_evidence_synthesis_centre_for_reviews_and_dissemination_universit
- claim: The MECIR conduct standard groups cover protocol development, question and eligibility criteria, outcomes, planned methods, searching, study selection, data collection, risk of bias, synthesis, and summarizing evidence.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_mecir/canonical_mecir-manual.md
  support_type: direct
  verification_note: Use this as a map to the relevant C-number standard group, not as the exact standard wording.
  quote_or_locator: canonical_mecir-manual.md:126-152; section_id=cochrane_mecir__canonical_mecir_manual__s0012_mecir
- claim: The MECIR online version is intended to be kept up to date and links to the most up-to-date Handbook chapters.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_mecir/canonical_mecir-manual.md
  support_type: direct
  verification_note: Recheck the live MECIR page before current compliance claims.
  quote_or_locator: canonical_mecir-manual.md:104-106; section_id=cochrane_mecir__canonical_mecir_manual__s0011_4_professor_of_evidence_synthesis_centre_for_reviews_and_dissemination_universit
```

## Operational rules

- Use MECIR for Cochrane-specific standards, especially when the user asks what is expected, required, or publishable in a Cochrane Intervention Review.
- Pair MECIR with the Handbook when method rationale or implementation detail is needed.
- Do not generalize MECIR standards to all SRs without labeling the transfer and checking the target review family.
- Use PRISMA-family sources for generic reporting-guideline claims unless the claim is specifically about Cochrane reporting expectations.

## Common misuses

- Treating MECIR as a universal SR checklist for every discipline or review type.
- Treating a MECIR heading as the full standard text without opening the relevant standard section or generated PDF.
- Using MECIR alone to explain detailed methods that are better grounded in the Handbook chapters.

## Evidence limits

This local MECIR capture is a compact landing-page conversion. It gives version, scope, and section routing, but does not expose every standard's detailed text in the card itself. Final answers should verify the relevant MECIR section or official Cochrane page when compliance wording matters.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=cochrane_mecir`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=cochrane_mecir`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=cochrane_mecir`.
- Optional local section locators: `references/corpus_index/sections/by_source/cochrane_mecir.jsonl`.

## Unresolved gaps

- The local Markdown capture primarily exposes the MECIR landing page and section map; detailed C- and U-standard text may require live-page or generated-PDF verification.
- Mandatory versus highly desirable status is not fully represented in the local MECIR landing-page span used here.
