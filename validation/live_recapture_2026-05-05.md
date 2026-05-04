# Live Recapture Validation 2026-05-05

Status: completed
Artifact type: browser/live-access validation note
Canonical evidence status: derivative audit note; verify final claims against canonical Markdown or live official URLs

## Superseded Status Update

This note records the pre-manual-capture state from the live browser/subagent pass. A later user-assisted manual browser PDF capture on 2026-05-05 added local Markdown for `press` and `cacm_author_guidelines`; see `manual_browser_capture_2026-05-05.md` and the current source cards for the updated local corpus state.

## Scope

This pass used parallel subagents with live browser/web access to revisit four sources previously marked as blocked, bad capture, or too sparse:

- `press`
- `cacm_author_guidelines`
- `state_of_art_review_2022`
- `clinicaltrials_api`

## Results

### PRESS

Result: browser-live verified, but still no local canonical content.

- Official PRESS hub was browser-accessible on 2026-05-05.
- The official detail page and E&E PDF locators were identified by browser access.
- Simple local scripted fetch still returned Cloudflare/403-style blocks.
- Repo status remains no-local-content until browser/manual or access-approved capture stores Markdown.

Recommended use now:

- Treat as a live locator and future capture target.
- Do not cite PRESS checklist or recommendation content from this pack yet.

### CACM Author Guidelines

Result: CACM-specific page still blocked; official fallback pages browser-live verified.

- `https://cacm.acm.org/author-guidelines` remained blocked for usable local capture.
- Official CACM overview and ACM author pages were browser-accessible through live web access.
- Simple local scripted fetch still returned Cloudflare/403-style blocks.
- These sources are venue/publisher guidance, not survey-methodology authority.

Recommended use now:

- Treat as no-local-content until official pages are captured.
- Use only after live verification for venue guidance; do not use for method claims.

### State-of-Art Review 2022

Result: repaired.

- The previous local file was a bad PMC browser-check capture.
- The article body was recaptured from an official PMC route on 2026-05-05 and converted to Markdown.
- The local Markdown now includes citation metadata, abstract, methods, SotA methodology, six-stage table/sections, discussion, and references.
- The title uses "six-step"; the body uses "six-stage". Preserve both.

Tracked capture:

- `references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md`

Recommended use now:

- Use as a scoped peer-reviewed method source for state-of-the-art reviews.
- Do not generalize it to all narrative, scoping, or systematic reviews.

### ClinicalTrials.gov API

Result: improved from sparse locator to partial official API documentation.

- Human docs remain partly SPA-rendered and are not robustly captured by simple HTML fetch.
- Official OpenAPI v2 YAML was captured from `https://clinicaltrials.gov/api/oas/v2`.
- Live version endpoint was captured from `https://clinicaltrials.gov/api/v2/version`.
- Browser subagent also reported that an advertised `ctg-oas-v2.yaml` path returned 404 on 2026-05-05; this discrepancy is recorded in the source card.

Tracked captures:

- `references/canonical_sources/md/clinicaltrials_api/official_openapi_v2.md`
- `references/canonical_sources/md/clinicaltrials_api/official_version_v2.md`
- Existing sparse locator: `references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md`

Recommended use now:

- Use the OpenAPI capture for endpoint/schema locators.
- Use the version endpoint capture only for currentness facts tied to 2026-05-05.
- Live-check before automation.

## Repo Updates Applied

- Updated `source_manifest.jsonl` rows for all four sources.
- Updated `download_manifest.jsonl` for the repaired PMC capture and new ClinicalTrials.gov OpenAPI/version captures.
- Updated `local_corpus_index.json` and `local_corpus_index.md`.
- Updated `document_index.jsonl` and local split section locators for changed sources.
- Rewrote source cards v2 for all four sources.
- Updated coverage and family source cards to remove stale bad-capture language.

## Final Status

- `state_of_art_review_2022`: available local method evidence, scoped to SotA review methodology.
- `clinicaltrials_api`: partial official API documentation, usable as API/schema/currentness locator.
- `press`: browser-live verified but no local canonical content; no local evidence use.
- `cacm_author_guidelines`: browser-live fallback verified but no local canonical content; no local evidence use.
