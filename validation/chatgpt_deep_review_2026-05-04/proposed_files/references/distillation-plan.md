# Distillation plan for `sr-survey-prior-router`

Status: proposed  
Created: 2026-05-04  
Artifact type: derivative planning document  
Canonical evidence status: not canonical evidence

## 1. Why distillation is needed

`sr-survey-prior-router` is a knowledge-heavy route-first skill. It contains a tracked converted canonical Markdown corpus under `references/canonical_sources/md/`, manifests and indexes, family-level source cards, route registries, and validation notes.

Distillation is needed because:

1. The canonical Markdown corpus is too large and heterogeneous to load directly in routine agent context.
2. The corpus mixes clean checklists, long manuals, registry pages, API docs, venue guidance, stubs, blocked sources, bad captures, and web UI artifacts.
3. Current source cards are useful for source-family navigation but are not precise enough for claim-level verification.
4. Several high-value sources require operational rules, common misuses, and explicit `not_for` boundaries.
5. Agents need compact route priors, but final claims still need canonical verification.

Distillation must not replace canonical Markdown. It should create a provenance-preserving derivative layer that helps agents choose what to open, what claims are likely supported, and what should be treated as locator-only or unresolved.

## 2. External evidence

The design is consistent with external patterns observed in agent-skill and documentation-heavy repositories:

1. Skill repositories commonly keep the main skill file concise and place supporting material in references, scripts, or assets.
2. Progressive disclosure is favored for agent skills: load the route/skill entrypoint first, then load references only when needed.
3. LLM-friendly documentation conventions such as `llms.txt` recommend a concise Markdown entrypoint plus links to more detailed Markdown pages, including optional full-context versions.
4. GitHub documentation discourages normal Git history as a channel for very large binary/raw files and recommends LFS or release assets for large downloadable artifacts.
5. Scholarly corpus infrastructure such as ACL Anthology keeps metadata/code in GitHub while papers/PDFs remain hosted separately or mirrored through a dedicated path.

These examples support a layered architecture: concise entrypoint, manifest/index, source cards, selected canonical Markdown, and raw files outside normal Git where needed.

## 3. Repo-specific evidence

The current repo already shows the need for distillation:

1. `SKILL.md` and `evidence-rules.md` correctly warn that source cards, indexes, summaries, graph output, and validation notes are not canonical evidence.
2. `references/canonical_sources/md/` provides valuable converted canonical text, but quality varies by source.
3. Clean item-level checklists exist for PRISMA 2020, PRISMA-S/TARCiS, PRISMA-ScR, AMSTAR 2, SWiM, and several API docs.
4. Some sources are noisy but usable, including JBI, GRADE, Nature, Crossref, PubMed, and Semantic Scholar pages with navigation/footer/cookie artifacts.
5. Some sources are not usable as evidence until repaired, including `state_of_art_review_2022`; some are blocked or unavailable, including `press` and `cacm_author_guidelines`.
6. The public repo tracks `section_index_manifest.jsonl`, but per-source section indexes may be local/rebuildable rather than available in GitHub, so source cards should include fallback canonical paths.

## 4. Canonical-vs-derivative policy

### 4.1 Canonical source

A canonical source is the official or methodologically authoritative source identified by URL, DOI, publisher, venue, database provider, or official documentation owner.

Examples:

- PRISMA statement/checklist pages and PDFs
- Cochrane Handbook chapters
- JBI Manual pages/PDF
- AMSTAR 2 tool/PDF/paper
- ROBIS paper/tool
- GRADE Working Group and handbook pages
- Official PubMed/NCBI, Crossref, OpenAlex, Semantic Scholar, OpenCitations docs
- Official venue policies from ACL/TACL/ISCA/Nature/IEEE/ACM
- Official OpenAI/Codex skill documentation

### 4.2 Converted canonical Markdown

Converted canonical Markdown is a local representation of canonical source text under:

`references/canonical_sources/md/<source_id>/...`

It is allowed for claim verification, subject to quality status. It is not a new authority independent of its source URL.

### 4.3 Manifest, index, and locator

The following are locator and audit artifacts, not evidence by themselves:

- `references/canonical_sources/download_manifest.jsonl`
- `references/source_inventory/local_corpus_index.md`
- `references/corpus_index/document_index.jsonl`
- `references/corpus_index/section_index_manifest.jsonl`
- `references/source_inventory/source_manifest.jsonl`

They can establish existence, paths, checksums, status, and retrieval quality. They cannot support methodological claims without opening canonical Markdown or raw source.

### 4.4 Derivative summary

A derivative summary includes source cards, route notes, claim ledgers, family maps, and graph/navigation artifacts. It may guide routing and source selection. It must not be cited as final evidence unless the claim is about the derivative artifact itself.

### 4.5 Validation note

Validation notes document QA behavior and audit outcomes. They can support claims about the repo’s internal QA process, not external methodology.

## 5. Proposed artifact types

### 5.1 Source card v2

Per-source card with required provenance fields and claim-level key points. This is the first layer to build.

Path:

`references/source_inventory/source_cards_v2/<source_id>.md`

Primary use:

- compact source briefing
- authority boundary
- canonical path selection
- operational rules
- common misuses
- verification path

### 5.2 Route-specific distilled notes

Per-route notes that map user intents to source families and source IDs.

Path:

`references/route_notes/<route_id>.md`

Primary use:

- route-level decision support
- source priority order
- route-specific caveats

These should reference source card v2 IDs and canonical paths, not restate everything.

### 5.3 Claim ledger

Structured claim ledger for reusable claims.

Path:

`references/claim_ledgers/<family_or_route>.jsonl`

Primary use:

- explicit claim-to-source mapping
- support type
- canonical path and quote locator
- quality status

### 5.4 Family overview

Short family-level overview after per-source cards exist.

Path:

`references/source_inventory/family_cards_v2/<family>.md`

Primary use:

- compare sources within a family
- explain authority hierarchy
- flag gaps and blocked sources

## 6. Required fields

Every source card v2 must include:

- `source_id`
- `source_family`
- `canonical_paths`
- `canonical_urls`
- `authority_level`
- `version_or_access_date`
- `applies_to`
- `not_for`
- `key_points`
- `operational_rules`
- `common_misuses`
- `route_relevance`
- `evidence_limits`
- `verification_paths`
- `freshness_risk`
- `reuse_or_license_risk`
- `unresolved_gaps`
- `qa_status`
- `last_reviewed`

Every key point must include:

- `claim`
- `supporting_canonical_paths`
- `support_type`: `direct`, `indirect`, `locator_only`, `blocked`, or `unsupported`
- `verification_note`
- optional `quote_or_locator`

## 7. QA gates

A card passes only if:

1. It has at least one canonical Markdown path.
2. Every key point points to at least one canonical path or is explicitly marked unresolved.
3. It does not cite source cards, registries, route labels, or graph output as canonical evidence.
4. It distinguishes reporting guidance from conduct guidance, appraisal guidance, database/API guidance, and venue policy.
5. It marks blocked, partial, bad-capture, and locator-only sources explicitly.
6. It includes `not_for` boundaries.
7. It includes licensing/reuse risk where redistribution or downstream use may be restricted.
8. It is checked against `download_manifest.jsonl` and `local_corpus_index.md`.
9. It avoids stating current API limits, venue rules, pricing, or dates as final without freshness risk.
10. It preserves enough canonical paths for a later agent to verify the claim without rereading the entire corpus.

## 8. Non-goals

Distillation is not intended to:

1. Replace canonical Markdown.
2. Create final legal advice about licensing or redistribution.
3. Summarize every paragraph of every source.
4. Convert locator-only registry pages into evidence.
5. Turn database/API docs into methodology authorities.
6. Hide blocked/bad captures.
7. Produce route answers without canonical verification for final claims.
8. Put raw PDFs/HTML/DOCX into the main branch.

## 9. Update workflow

1. Run or update retrieval.
2. Update `download_manifest.jsonl`.
3. Update `local_corpus_index.md` and `document_index.jsonl`.
4. Flag source quality: `available`, `partial`, `blocked`, `bad_capture`, `stub`, or `locator_only`.
5. Generate or update source card v2 from selected canonical Markdown.
6. Run QA gates.
7. For every changed key point, verify canonical paths and support status.
8. Update route notes only after affected source cards pass QA.
9. Keep raw source captures outside normal Git unless a large-file channel is chosen.
10. Add a validation note documenting what changed and what remains unresolved.

## 10. Priority order

Start with sources that are both high-authority and high-route-impact:

1. PRISMA 2020
2. Cochrane Handbook
3. JBI Manual
4. PRISMA-S / TARCiS / PRISMA-ScR / PRISMA-P
5. AMSTAR 2 / ROBIS / GRADE
6. SANRA / SWiM / ENTREQ / RAMESES / taxonomy-method sources
7. PubMed / Crossref / OpenAlex / Semantic Scholar / OpenCitations
8. ACL / ISCA / TACL / Computational Linguistics / Nature / IEEE / ACM venue guidance
9. OpenAI / Codex / skill-packaging sources

## 11. Sources that should not be replaced by summaries

The following source types must remain directly consulted for final claims:

- checklist item wording
- reporting item wording
- scoring tool criteria
- risk-of-bias signaling questions
- GRADE criteria and certainty categories
- API limits, terms, authentication, endpoint, and rate-limit rules
- venue submission rules, anonymity rules, dual-submission policies, length limits, and licensing
- license/reuse/copyright text
- blocked, bad-capture, or stub sources
