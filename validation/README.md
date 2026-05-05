# Validation Status

This directory contains dated validation snapshots for `sr-survey-prior-router`.
For current publication/readiness status, start with:

- `source_integrity_tracker.md`

The tracker is the live progress board. Dated files in this directory are
evidence snapshots from earlier repair rounds and may contain findings that were
true when written but later superseded.

## Current Draft-Publication Status

As of 2026-05-05, the tracked nested-pack surface is conditionally ready for
draft Git publication:

- Source-card v2 coverage exists for all 65 `source_manifest.jsonl` source IDs.
- The local canonical Markdown corpus has 212 Markdown files and pack-root
  relative raw-file headers.
- Runtime locator paths are pack-root-relative in the checked manifest/index
  surfaces.
- `agents/openai.yaml` is explicit-only with `allow_implicit_invocation: false`.
- Graphify output is optional/rebuildable locator output, not canonical evidence.

This is not a final knowledge-heavy coverage claim. The pack is a staged router
with a seed source inventory, local canonical Markdown corpus, source cards, and
route/index boundaries.

## Superseded Snapshot Warnings

Some older snapshots still mention no-local-content or blocked/bad-capture
states that have since changed. In particular:

- `press` now has user-assisted manual browser PDF Markdown captures, but remains
  scripted-refresh-sensitive.
- `cacm_author_guidelines` now has user-assisted manual browser PDF Markdown
  captures, but remains scripted-refresh-sensitive.
- `state_of_art_review_2022` was recaptured from PMC and now has article-body
  Markdown.
- Graphify index refresh was completed after earlier deferred/stale notes.

When a dated snapshot conflicts with `source_integrity_tracker.md`, the tracker
is the current authority.

## Fresh Local Checks

Run from the pack root:

```sh
COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_source_cards_v2.py
COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py
COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py --require-generated
git diff --check
find . -path './.git' -prune -o -name '._*' -type f -print
```

Expected publish-prep result: validators pass, `git diff --check` is clean, and
no non-`.git` AppleDouble files are printed.
