# ChatGPT Deep Review Alignment Check

Date: 2026-05-05
Status: aligned with scoped caveats
Artifact type: validation note
Canonical evidence status: not canonical evidence

## Scope

This check compares the current `sr-survey-prior-router` pack against the imported ChatGPT review under:

`validation/chatgpt_deep_review_2026-05-04/`

It focuses on current live files, not historical validation notes. Older validation files from 2026-05-04 remain useful audit history, but some of their blocked/bad-capture statements are superseded by later recapture work.

## Alignment Summary

| ChatGPT review requirement | Current status | Evidence |
| --- | --- | --- |
| Keep raw canonical files outside normal GitHub review surface. | Aligned. Raw files remain ignored by `.gitignore`; tracked review surface uses Markdown, manifests, indexes, cards, and validation notes. | `.gitignore`, `references/canonical_sources/README.md` |
| Keep `SKILL.md` concise and use progressive disclosure. | Aligned. `SKILL.md` routes through registry, local corpus index, document/section indexes, selected source cards, then selected canonical Markdown. | `SKILL.md`, `references/route-source-index.yaml` |
| Make GitHub/public checkout fallback explicit for split `sections/by_source/` locators. | Aligned. Current docs say split section locators are local/rebuildable and public checkouts should fall back to `document_index.jsonl`, source cards v2, and targeted Markdown search. | `SKILL.md`, `references/source-map.md`, `references/route-source-index.yaml`, `references/source_inventory/source_cards_v2/README.md` |
| Add source cards v2 with canonical paths, support types, scope boundaries, freshness, and reuse risk. | Aligned. There is one v2 card for every manifest source ID, and the validator enforces card coverage, required metadata, route IDs, canonical paths, support types, and sidecar cleanliness. | `references/source_inventory/source_cards_v2/`, `validation/validate_source_cards_v2.py` |
| Do not let derivative summaries replace canonical Markdown. | Aligned. Evidence boundary is repeated in the schema, route index, source map, distillation plan, and validation notes. | `references/evidence-rules.md`, `references/source_inventory/source_cards_v2/README.md`, `references/distillation-plan.md` |
| Distillation should be added, not substituted. | Aligned as draft. `references/distillation-plan.md` exists and frames distilled artifacts as derivative routing aids only. | `references/distillation-plan.md` |
| Keep blocked/bad captures visible. | Aligned, with updated status. `state_of_art_review_2022` and `clinicaltrials_api` were repaired/augmented; `press` and `cacm_author_guidelines` now have manual browser PDF Markdown captures but retain scripted-fetch 403 caveats. | `source_manifest.jsonl`, `local_corpus_index.*`, `manual_browser_capture_2026-05-05.md` |
| Do not substitute ACM DL user guide for CACM author guidelines. | Aligned. CACM has its own manual browser captures; the ACM DL card explicitly remains scoped to DL/user-guide behavior. | `source_cards_v2/cacm_author_guidelines.md`, `source_cards_v2/acm_dl.md` |
| Treat APIs/registries/databases as locators or infrastructure, not methodology authorities. | Aligned. ClinicalTrials.gov now has OpenAPI/version captures but remains API/schema/currentness locator only. | `source_cards_v2/clinicaltrials_api.md`, `source_inventory/source_manifest.jsonl` |
| Track authority boundaries to avoid authority creep. | Aligned. Source cards and family cards keep methodology, conduct, reporting, appraisal, venue, registry, and API roles separate. | `source_cards_v2/*`, `source_cards/*.md`, `source_registry.yaml` |

## Important Supersessions Since The ChatGPT Review

- `state_of_art_review_2022`: no longer bad capture; local article-body Markdown is available and scoped to SotA review methodology.
- `clinicaltrials_api`: no longer just a sparse 12-line entry point; local OpenAPI v2 and version endpoint captures are available, but it is still not a review-method authority.
- `press`: no longer no-local-content; manual browser PDF captures exist for the hub, detail page, and official E&E PDF. Scripted fetch remains blocked, so refreshes may require browser/manual capture.
- `cacm_author_guidelines`: no longer no-local-content; manual browser PDF captures exist for CACM author guidelines and ACM author pages. Use only as venue/publisher guidance.

## Remaining Caveats

The current pack is aligned with the ChatGPT review's architecture and source-boundary requirements. It is not "finished" as a mature knowledge-heavy skill in these narrower senses:

- Source cards v2 are still derivative summaries. High-stakes methodology, venue, API, or licensing claims must open canonical Markdown or live official URLs.
- PRESS/CACM manual captures are browser print/PDF captures and include navigation/date/cookie artifacts. They are usable, but not as clean as direct official HTML/XML captures.
- Scripted refresh for PRESS/CACM still fails with 403-style blocks.
- Fine-grained claim ledgers and item-level source-card locators are still future work beyond the ChatGPT review's minimum alignment gate.

## Fresh Validation Commands

Run from the skill root:

```sh
python3 validation/validate_source_cards_v2.py
python3 validation/validate_graphify_navigation.py
git diff --check -- . ':!validation/chatgpt_deep_review_2026-05-04'
python3 - <<'PY'
import json
from pathlib import Path
for path in [
    'references/source_inventory/source_manifest.jsonl',
    'references/canonical_sources/download_manifest.jsonl',
    'references/corpus_index/document_index.jsonl',
    'references/corpus_index/section_index_manifest.jsonl',
]:
    rows = [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]
    print(f'{path}: {len(rows)} rows ok')
PY
```

Observed current counts:

```text
source_manifest.jsonl: 65 rows
download_manifest.jsonl: 254 rows
document_index.jsonl: 210 rows
section_index_manifest.jsonl: 65 rows
source_cards_v2 cards: 65
```

## Conclusion

The current pack is aligned with the imported ChatGPT deep review for the draft-publication standard: route-first architecture, progressive disclosure, public/local artifact boundary, complete source-card-v2 coverage, canonical evidence boundary, and repaired status for previously blocked/bad high-value sources.

Do not describe it as complete domain knowledge. Describe it as a reviewable, provenance-preserving draft knowledge router with local canonical Markdown coverage and remaining freshness/claim-ledger work.
