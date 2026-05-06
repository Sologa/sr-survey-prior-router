# SR/Survey Prior Router

This repository is a draft/staged Codex skill for routing prepared systematic-review, survey-writing, domain-prior, and source-grounding resources. It is a knowledge-resource router only: it helps an agent choose the smallest relevant local reference material and preserve provenance boundaries.

It is not a final domain authority, a legal clearance decision, or an executor. It does not run workflows, mutate agent runtime state, or replace live verification when a task needs current facts.

## Install

Install the standalone skill from GitHub with:

```sh
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Sologa/sr-survey-prior-router \
  --path . \
  --name sr-survey-prior-router
```

`--path .` points at the repository root containing `SKILL.md`. The same files can also be read as a staged pack without installation. Restart Codex after installing so the new skill is discovered.

## How It Is Meant To Be Used

Start with `SKILL.md`. For evidence-sensitive work, route through `references/route-source-index.yaml`, `references/source_inventory/local_corpus_index.*`, and `references/corpus_index/` before opening a full source file.

The pack is intentionally lazy-loaded. Source cards, route files, indexes, and graph navigation are locator layers. They narrow the reading target; they do not replace source text or live source checks.

## Canonical vs Derivative

Within this repo, `references/canonical_sources/md/<source_id>/` is the local canonical read path relative to the router. "Canonical" here means "closest local converted copy used for evidence checking inside this pack." It does not mean the project owns the source, controls its license, or supersedes the publisher, standards body, API provider, or original author.

Derivative materials include route registries, source cards, corpus indexes, graphify outputs, coverage reports, validation notes, and README-style explanations. These are project-authored navigation and audit layers. Final claims should cite or verify the selected canonical source text and, when currentness or rights matter, the live upstream source.

## Third-Party Markdown Caveat

Markdown files under `references/canonical_sources/md/` are converted from third-party web pages, PDFs, DOCX files, API docs, or manually captured browser PDFs. They may contain conversion artifacts, navigation text, page-footers, cookie notices, stale content, or incomplete captures.

Those Markdown files are not project-authored content and are not covered by the project license. Use them as local review copies and evidence locators, quote sparingly, preserve attribution, and check upstream terms before public redistribution or substantial reuse. Raw captures and source records listed in `references/canonical_sources/download_manifest.jsonl` and `references/source_inventory/source_manifest.jsonl` have the same upstream-rights boundary.

## Publication Boundary

Project-authored code, docs, manifests, route files, and validation scaffolding are licensed only as stated in `LICENSE`. Third-party source material is excluded from that license. See:

- `NOTICE.md`
- `THIRD_PARTY_SOURCES.md`
- `references/source_inventory/redistribution_policy.yaml`
- `references/source_inventory/source_manifest.jsonl`
- `references/canonical_sources/download_manifest.jsonl`

The redistribution policy is conservative metadata for reviewers and automation. It is not legal advice and does not settle all source-specific questions.

## Repository Layout

- `SKILL.md`: behavior contract and routing entrypoint.
- `agents/openai.yaml`: optional Codex metadata for installed-skill discovery.
- `references/`: route docs, source inventory, local source conversions, and locator indexes.
- `validation/`: dated validation reports plus the live tracker and validation entrypoint.
- `scripts/`: maintenance scripts for generated navigation artifacts.

## Quick Checks

For a small publication-layer edit, run:

```sh
git diff --check
rg -n 'docs/agent_capability_packs|not installed or active until' SKILL.md
```
