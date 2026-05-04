# Source Card: SR Method Authorities

source_ids: `prisma_2020`, `prisma_extensions`, `prisma_s`, `prisma_p`, `prisma_scr`, `cochrane_handbook`, `cochrane_mecir`, `jbi_manual_2024`, `campbell_standards`, `grade_working_group`, `grade_handbook`, `grade_cerqual`, `amstar2`, `robis`, `rob2`, `robins_i`, `press`

related_source_ids: `equator_prisma`, `prospero`

## Summary

SR-writing prior requires a stack rather than one source. PRISMA-family sources are reporting authorities; Cochrane, MECIR, JBI, and Campbell are conduct/manual authorities; GRADE/CERQual support certainty/confidence; AMSTAR 2 and ROBIS appraise reviews; RoB 2 and ROBINS-I assess primary-study bias; PRESS supports search strategy peer review when accessible. PROSPERO and EQUATOR PRISMA are related registry/locator sources, not methodology truth.

## Decision Boundary

Do not collapse reporting, conduct, appraisal, bias, search QA, and registry sources into one authority type. Each source supports only claims within its scope.

## Supported Uses

- Identify which authority applies to a review type or writing section.
- Prevent PROSPERO or databases from being treated as conduct guidance.
- Route search-reporting claims to PRISMA-S and to PRESS only when usable PRESS content has been captured or otherwise access-approved.
- Route certainty and confidence claims to GRADE/CERQual.

## Gaps

- Local raw and Markdown snapshots now exist for retrieved authorities under `../../canonical_sources/`; use `source_manifest.jsonl` `local_documents` entries to locate them.
- PRESS official hub/detail/E&E locators were browser-live verified on 2026-05-05, but the pack still has no local canonical PRESS Markdown and scripted fetch remains blocked; it needs browser/manual retrieval or an access-approved route.
- EQUATOR PRISMA is locally captured as a registry record and linked PRISMA materials; use it as a locator/update monitor, not as a substitute for primary PRISMA method text.
- Direct BMJ PDF endpoints for PRISMA 2020 returned 403; PRISMA/PLOS/PMC full-text alternatives are locally captured for statement and explanation/elaboration coverage.
- Individual source cards still need page/section locators.
- Review-type-specific branches need more examples before broad automation.

last_reviewed: 2026-05-05
