---
name: sr-survey-prior-router
description: Staged knowledge-resource router for prepared research resources, domain prior, literature corpora, survey/SR writing prior, evidence grounding, source audit, and source-grounded synthesis in this repo. Use to choose the smallest relevant reference knowledge; this staged draft does not execute workflows or mutate runtime state.
---

# SR/Survey Prior Router

This copy is a staged draft knowledge-resource router while it remains under `docs/agent_capability_packs/`. It is not installed or active until it is copied into an agent skill root by a separate, explicit action; once installed, `agents/openai.yaml` controls whether Codex may also invoke it implicitly from the skill description.

Its job is navigation: point the agent to the smallest relevant reference knowledge and keep source/provenance boundaries visible. It is not an execution workflow, automation harness, or multi-step prompt pack.

## Coverage Status

This staged pack now includes a seed source inventory under `references/source_inventory/`, a first local full-document corpus under `references/canonical_sources/`, and lazy-load locator indexes under `references/corpus_index/`. Treat the corpus as the local read path for downloaded official/method sources, not as proof of exhaustive coverage: broad APIs, commercial sources, blocked URLs, and source-specific licensing still need route-by-route checks.

Before claiming substantive survey-writing or SR-writing coverage, consult `references/source_inventory/coverage_report.md`, verify the relevant `source_manifest.jsonl` / `source_registry.yaml` rows, then use `references/route-source-index.yaml`, `references/source_inventory/local_corpus_index.*`, and `references/corpus_index/` to locate the smallest relevant local Markdown section. Prefer local `canonical_sources/md/<source_id>/` files only after this source/document/section selection is done. Split `corpus_index/sections/by_source/<source_id>.jsonl` files may exist locally as generated backing locators but are not part of the ordinary GitHub review surface; if absent, fall back to `corpus_index/document_index.jsonl`, source cards v2 locators, and targeted search inside the selected canonical Markdown file. If a graphify graph exists for this pack, use `references/graphify-navigation.md` only as an optional navigation adapter after route selection; graph output is never canonical evidence.

## Use When

- The user asks how prepared research resources, survey-writing material, SR-writing resources, or broader domain material should become agent prior.
- The task needs knowledge routing across a literature corpus, source registry, evidence packet, citation audit, retrieval layer, or source-grounded synthesis question.
- The task must keep long knowledge out of the prompt while still making the agent read the right prepared source.

## Do Not Use When

- The task is ordinary coding, shell usage, or writing unrelated to prepared research resources.
- The user asks for a current fact that needs live web or a specific external source not represented in the prepared corpus.
- The user asks to install, activate, or mutate an agent runtime. This staged pack only describes behavior.

## Reference Navigation

1. Read `references/route-registry.md` first.
2. Select exactly one smallest route unless the task clearly crosses route boundaries.
3. Read only the reference files listed for that route.
4. If the route needs local full-document evidence, read `references/route-source-index.yaml`, then choose source IDs through `references/source_inventory/local_corpus_index.md` or `.json`.
5. Use `references/corpus_index/document_index.jsonl` and, when available locally, the selected `references/corpus_index/sections/by_source/<source_id>.jsonl` file to find line/page locators before opening any canonical Markdown file. If split section locators are unavailable in a public checkout, use `references/source_inventory/source_cards_v2/<source_id>.md` and targeted search in the selected canonical Markdown file as the fallback.
6. Use graphify only when the selected route still needs relationship navigation or candidate narrowing. Follow `references/graphify-navigation.md`, then return to document/section locators and canonical verification.
7. Consult optional notes only when they clarify a knowledge distinction.
8. If a source, registry, locator, graph, or corpus is missing, say what is missing instead of guessing.

## Safety Rules

- Do not modify frozen SRs: `2307.05527`, `2409.13738`, `2511.13936`, or `2601.19926`.
- Do not bulk-load `references/canonical_sources/raw/`, `references/canonical_sources/md/`, or every `corpus_index/sections/by_source/*.jsonl` file.
- Do not treat compiled wiki, RAG output, graphify output, source cards, indexes, or summaries as canonical truth.
- Do not present unsupported claims as conclusions.
- Keep repo rules, source provenance, and read/write boundaries visible in the answer.

## Answer Guidance

For audit-heavy or evidence-sensitive answers, make these distinctions visible when they matter:

- `read`: files, registries, or sources actually consulted.
- `supported`: claims or actions supported by the consulted sources.
- `uncertain`: missing evidence, weak support, stale information, or unresolved routing.
- `next_smallest_action`: the next bounded action that would reduce uncertainty.

Do not force this shape for simple answers. Use it only when it helps preserve provenance or uncertainty.
