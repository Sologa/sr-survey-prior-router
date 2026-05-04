# Source Cards v2 Full Coverage Validation

Date: 2026-05-05
Status: passed
Artifact type: validation note
Canonical evidence status: not canonical evidence

## Scope

This pass completed `references/source_inventory/source_cards_v2/` coverage for every `source_id` in `references/source_inventory/source_manifest.jsonl`.

Coverage result:

```text
source_manifest_sources: 65
source_cards_v2 cards: 65
missing source cards: 0
extra source cards: 0
```

## Subagent Split

- Worker 1: PRISMA extension, PRESS, EQUATOR PRISMA, PROSPERO, Cochrane Library, Epistemonikos, PubMed E-utilities, Europe PMC, ClinicalTrials.gov API, WHO ICTRP.
- Worker 2: Cochrane chapters 9 and 12, York narrative synthesis guidance, state-of-art review 2022, narrative review writing 2011.
- Worker 3: Nature/Scientific Reviews, Nature Reviews, IEEE ComST, CACM, ACM DL, IEEE Xplore API, Papers with Code.
- Worker 4: ACL Anthology, ACL Anthology GitHub, ACL ARR, ACL formatting, TACL, Computational Linguistics, ISCA Archive, Interspeech policy.
- Worker 5: DBLP, Crossref, Semantic Scholar, CORE, Lens, Dimensions, Scite, OpenCitations, arXiv.

Each worker wrote a disjoint set of card files and did not commit or push.

## Validation Commands

Run from the skill root:

```sh
python3 -m pip install -r requirements.txt
find . -name '._*' ! -path './.git/*' -delete
rm -rf .omx validation/__pycache__
python3 validation/validate_source_cards_v2.py
python3 validation/validate_graphify_navigation.py
git diff --check -- . ':!validation/chatgpt_deep_review_2026-05-04'
```

Observed result:

```text
source_cards_v2 validation: PASS
checked_cards: 65
source_manifest_sources: 65

graphify navigation validation: PASS
```

## Validator Hardening

This pass tightened `validation/validate_source_cards_v2.py` so it now:

- ignores generated `._*.md` files while selecting card candidates, then reports them through the macOS metadata sidecar check instead of crashing on invalid UTF-8
- fails when any `source_manifest.jsonl` `source_id` lacks a matching `source_cards_v2/<source_id>.md`

## Known Boundaries Preserved in Cards

- `press` and `cacm_author_guidelines` are blocked local inventory targets and cannot be used as local canonical evidence.
- Superseded by `live_recapture_2026-05-05.md`: `state_of_art_review_2022` now has local article-body Markdown, and `clinicaltrials_api` now has local OpenAPI/version captures. Both remain scoped sources, not universal methodology authorities.
- Registry, API, database, venue, and exemplar cards are locator/context sources, not SR or survey methodology authorities.
- Commercial/API sources keep freshness, access, rate-limit, subscription, and reuse caveats.
- Venue and formatting cards support venue-specific expectations only; they are not cross-domain writing methods.

## Boundary

These cards are derivative routing artifacts. They help agents choose the right canonical Markdown files and locators. They are not canonical evidence for methodology, reporting, tool behavior, API availability, venue policy, licensing, or source freshness claims.
