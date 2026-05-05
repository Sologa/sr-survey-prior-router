# Source Alignment Fix Validation

Date: 2026-05-04

## Publication Note

Historical snapshot. Current live status is tracked in `validation/source_integrity_tracker.md`. Superseded points: PRESS/CACM manual captures now exist, `state_of_art_review_2022` was recaptured, and graphify outputs were refreshed where relevant.

Scope: organized/index layer under `docs/agent_capability_packs/sr-survey-prior-router`.

This validation checks the remediation requested after `source_alignment_audit_2026-05-04.md`. It treats `references/canonical_sources/raw/` and `references/canonical_sources/md/` as the backing corpus and does not use them as route-level context.

## Fix Summary

- Downgraded `state_of_art_review_2022` to a non-evidence local capture:
  - `local_bundle_status=bad_capture_browser_check_only`
  - `local_content_status=bad_capture`
  - `validation_status=local_capture_invalid_browser_check`
  - document/section locator rows carry `status=bad_capture` and `content_quality=browser_check_only`
- Marked `press` as blocked/candidate-only:
  - `source_manifest.jsonl` now records `local_access_blocked_403` and `blocked_403_no_local_content`
  - `local_corpus_index.*` records zero local docs and six blocked attempts
  - coverage/source-card prose no longer treats PRESS as local canonical evidence
- Reclassified `equator_prisma` as a registry locator:
  - moved from `sr_certainty_appraisal_bias_search` to `scholarly_databases_and_apis`
  - local/document/section locator rows now use `family=scholarly_databases_and_apis`
  - `evidence_use=locator_only` and `content_quality=registry_or_linked_locator`
  - SR method source card lists it only as `related_source_ids`
- Added API stub evidence gates:
  - `core_api`: `conversion_depth=mixed_full_and_entry_stub`
  - `scite_api`: `conversion_depth=mixed_entry_stub_and_openapi`
  - `evidence-rules.md` now prevents `entry_point_stub` / stub conversion-depth rows from being treated as `direct` evidence unless a non-stub/current official source span is selected
- Added cross-family traceability:
  - source cards now use `related_source_ids` plus explicit caveats for registry/metadata/venue sources
- Rebuilt graphify locator output from the updated indexes.

## Validation Results

### Local Structural Validation

Command: custom Python consistency check over `source_manifest.jsonl`, `local_corpus_index.json`, `source_registry.yaml`, `document_index.jsonl`, `section_index_manifest.jsonl`, and selected split section indexes.

Result: PASS

Key counts:

- `source_manifest.jsonl`: 65 source IDs
- `local_corpus_index.json`: 65 source IDs
- `document_index.jsonl`: 201 rows
- `section_index_manifest.jsonl`: 63 source rows

Checked conditions:

- `state_of_art_review_2022` is `bad_capture` / `browser_check_only` / `not_supported`.
- `press` is blocked and candidate-only until recaptured.
- `equator_prisma` is assigned only to `scholarly_databases_and_apis` in registry, manifest, local corpus index, document locators, and section locators.
- `core_api` and `scite_api` expose explicit mixed/stub conversion depth.
- `evidence-rules.md` contains blocked/bad-capture and stub locator-only gates.
- No AppleDouble `._*` files are present.

### Graphify Validation

Commands:

```sh
python3 scripts/build_graphify_index_graph.py
python3 validation/validate_graphify_navigation.py
rg -n "references/canonical_sources/(raw|md)/|references/corpus_index/sections/by_source/|refs_old/|upstream_repo/" graphify-out
```

Results:

- `build_graphify_index_graph.py`: PASS
  - nodes: 363
  - edges: 1336
  - communities: 44
  - scope: `router_index_graph`
- `validate_graphify_navigation.py`: PASS
- forbidden-path `rg`: PASS, no matches

### OMX Read-only Cross-check

Command: `codex-omx-exec --ephemeral --sandbox read-only --skip-git-repo-check -m gpt-5.3-codex-spark -c 'model_reasoning_effort="xhigh"'`

Result: PASS

OMX validated seven audit requirements:

1. `state_of_art_review_2022` is consistently non-usable local evidence.
2. `press` is blocked/candidate-only and not treated as Strong Seed Coverage local evidence.
3. `equator_prisma` is a `scholarly_databases_and_apis` registry locator with SR-card caveats.
4. `core_api` and `scite_api` have conversion-depth/stub locator-only rules.
5. Cross-family references have `related_source_ids` and caveats.
6. `graphify-out` is rebuilt, locator-only, and has no forbidden full-corpus path strings.
7. No `._*` sidecars exist.

## Residual Boundaries

- `state_of_art_review_2022` still needs a real article-body recapture before it can be used as method evidence.
- PRESS still needs browser/manual or access-approved retrieval before local canonical evidence can be claimed.
- API/database rows with stub captures still require a richer local document or current official source span before detailed capability claims can be marked `direct`.
