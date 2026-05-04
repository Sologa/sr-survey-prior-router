# Codex OMX/Subagent Synthesis

Date: 2026-05-04

Status: review synthesis; not canonical evidence.

## Imported Inputs

The relevant `~/Downloads` items from 2026-05-04 20:19 were:

- `/Users/xjp/Downloads/chatgpt_deep_review_2026-05-04.md`
- `/Users/xjp/Downloads/sr_survey_prior_router_deep_review_2026-05-04/`

The Finder metadata file `/Users/xjp/Downloads/.DS_Store` was not imported.

Imported destinations:

- `review.md`: main ChatGPT review.
- `proposed_files/references/distillation-plan.md`: proposed derivative distillation plan.
- `proposed_files/references/source_inventory/source_cards_v2/README.md`: proposed source-card-v2 schema.
- `proposed_files/references/source_inventory/source_cards_v2/{prisma_2020,sanra,openalex,openai_codex_skills}.md`: proposed example cards.

See `import_manifest.md` for source paths and SHA-256 hashes.

## What ChatGPT Concluded

- The current route-first, progressive-disclosure architecture is defensible.
- Tracking converted canonical Markdown under `references/canonical_sources/md/` is acceptable with caveats.
- Raw PDF/HTML/DOCX captures should stay outside the normal main branch unless Git LFS, release assets, object storage, or another large-file channel is chosen.
- The current family-level `source_cards/*.md` are useful but too coarse for claim-level grounding.
- A derivative distillation layer is recommended, but it must not replace canonical Markdown.
- Some converted Markdown is noisy and needs quality/freshness/reuse flags.
- Blocked or bad captures, especially `press`, `cacm_author_guidelines`, and `state_of_art_review_2022`, should be called out more loudly.

## Directly Usable Now

The proposed `source_cards_v2/README.md` is the safest file to promote first. It is a schema and QA contract rather than a source-specific evidence claim file.

The review inbox structure and import manifest are also directly usable as provenance for this ChatGPT review package.

## Useful But Needs Edits Before Promotion

`proposed_files/references/distillation-plan.md` is directionally useful, but it should be edited before becoming a live `references/distillation-plan.md` because it repeats ChatGPT's public-GitHub locator concern. In this local workspace the split section indexes exist; the real issue is public/local distribution clarity, not missing local locators.

`prisma_2020.md` and `sanra.md` are the strongest example cards. Their core claims are mostly supported by canonical Markdown, but they should be enriched with exact existing section/page locators before promotion.

`openai_codex_skills.md` needs revision before promotion:

- It mixes `openai_codex_skills` and `openai_codex_agents_md` in one per-source card.
- It uses `https://developers.openai.com/codex/agents-md`, while the live manifest records `https://developers.openai.com/codex/guides/agents-md`.
- It lists `skill_packaging`, which is not a current route ID.

`openalex.md` needs revision before promotion:

- It mixes `openalex` and `openalex_snapshot`, which are separate source IDs.
- It lists route IDs that do not exist in the current route registry: `paper_retrieval_prior` and `scholarly_database_selection`.
- API/pricing/authentication/snapshot cadence claims are freshness-sensitive and should be rechecked before release.

## Work Remaining

1. Apply or adapt `source_cards_v2/README.md` into `references/source_inventory/source_cards_v2/README.md`.
2. Decide whether to promote `distillation-plan.md`; if so, edit the public/local section-index language first.
3. Promote `prisma_2020.md` and `sanra.md` only after replacing prose locators with exact section/page IDs from `references/corpus_index/sections/by_source/`.
4. Split and rewrite mixed cards:
   - `openai_codex_skills.md`
   - `openai_codex_agents_md.md`
   - `openalex.md`
   - `openalex_snapshot.md`
5. Add validation checks for source-card-v2 invariants:
   - one card per `source_id`
   - all `route_relevance` values exist in `route-registry.md`
   - every canonical path exists
   - no card cites source cards, graph output, or indexes as direct evidence
   - freshness and reuse-risk fields are present
6. Add or update documentation to make the public GitHub vs local backing-corpus boundary explicit.
7. Add future checks for local-path leakage in canonical Markdown headers and manifests.

## Current Decision

Do not directly apply all ChatGPT proposed files into the live `references/` tree as-is. Treat them as high-quality draft input. The schema is close to ready; the concrete cards need source-ID, route-ID, URL, freshness, and locator cleanup first.

## Post-Review Implementation Status

Status after Codex + OMX + subagent follow-up on 2026-05-04:

- Promoted a revised live schema at `references/source_inventory/source_cards_v2/README.md`.
- Promoted a revised `references/distillation-plan.md` with corrected public/local locator language.
- Promoted six corrected v2 source cards:
  - `references/source_inventory/source_cards_v2/prisma_2020.md`
  - `references/source_inventory/source_cards_v2/sanra.md`
  - `references/source_inventory/source_cards_v2/openai_codex_skills.md`
  - `references/source_inventory/source_cards_v2/openai_codex_agents_md.md`
  - `references/source_inventory/source_cards_v2/openalex.md`
  - `references/source_inventory/source_cards_v2/openalex_snapshot.md`
- Rewrote the mixed ChatGPT examples as one card per live `source_id`.
- Replaced invalid route IDs with the current route registry values.
- Added `validation/validate_source_cards_v2.py`.
- Updated `SKILL.md`, `source-map.md`, `route-source-index.yaml`, `coverage_report.md`, and `evidence-rules.md` to document source-card-v2 and the public/local split-section-locator fallback.

Validation run:

- `python3 validation/validate_source_cards_v2.py`: PASS, 6 cards checked.
- `python3 validation/validate_graphify_navigation.py`: PASS.

Remaining work:

1. Add v2 cards for the next high-priority method authorities: Cochrane Handbook, JBI Manual, PRISMA-S/TARCiS, PRISMA-ScR, AMSTAR 2, ROBIS, GRADE, and key survey-writing methods.
2. Add route-specific distilled notes only after enough source cards v2 pass validation.
3. Add claim ledgers if repeated writing tasks need reusable claim-to-source mappings.
4. Re-check live official docs before treating freshness-sensitive API, pricing, venue-policy, or product-behavior claims as current.
5. Decide later whether split `corpus_index/sections/by_source/` files should stay local-only or be published through a separate large/rebuildable artifact channel.
