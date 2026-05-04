# Deep Review of `Sologa/sr-survey-prior-router`

Suggested repo path: `validation/chatgpt_deep_review_2026-05-04.md`  
Review date: 2026-05-04  
Reviewer stance: external reviewer of a draft-stage, knowledge-heavy agent skill / capability pack  
Scope source: user task request and constraints fileciteturn0file0

## 1. Executive summary

### Verdict

`sr-survey-prior-router` has a defensible architecture for a draft-stage, knowledge-heavy routing skill. Its strongest design choice is the explicit separation between:

- canonical source
- converted canonical Markdown
- manifest / index / locator
- derivative source card
- graph / navigation artifact
- validation note

The repo already encodes this boundary in `SKILL.md`, `source-map.md`, `evidence-rules.md`, and the coverage/registry files. `SKILL.md` describes the pack as a route-first knowledge-resource router, not an execution workflow, and explicitly says not to bulk-load raw/Markdown corpora or treat source cards, indexes, summaries, or graph output as canonical truth fileciteturn6file0. `evidence-rules.md` similarly requires canonical Markdown/raw verification for direct support and treats source cards and indexes as derivative or locator artifacts fileciteturn41file0.

### Main conclusions

| Area | Judgment | Action |
|---|---:|---|
| Overall architecture | reasonable / above-average for a draft skill | keep route-first progressive-disclosure design |
| Full canonical Markdown in repo | acceptable, with caveats | keep `canonical_sources/md/`; do not add raw PDF/HTML/DOCX to main branch |
| Raw canonical files | should remain outside normal main branch | use manifest plus LFS/release/object storage if distribution is needed |
| Current source cards | useful but too coarse | do not use as evidence; replace/augment with `source_cards_v2` |
| Canonical Markdown conversion quality | mixed | add conversion QA flags, especially for web UI/nav/cookie captures and stubs |
| Section locator availability | partially broken for GitHub-only review | mark `sections/by_source/*.jsonl` as local-only or commit a small public locator layer |
| Distillation | recommended | build derivative distilled layer with strict provenance and QA gates |
| Licensing/reuse | nontrivial | add per-source reuse/license risk fields before broad redistribution |

### Highest-priority issues

1. **GitHub-only locator break:** `section_index_manifest.jsonl` advertises per-source files under `references/corpus_index/sections/by_source/<source_id>.jsonl`, but direct GitHub fetches for selected examples such as `prisma_2020.jsonl` and `openai_codex_skills.jsonl` returned 404. This is consistent with `source-map.md` saying split section locators are local/rebuildable backing data, but `SKILL.md`, `route-source-index.yaml`, and validation docs still operationally point agents to those files without always saying they are not in the public GitHub surface. The public review pathway should be made explicit.

2. **Some converted Markdown is canonical-but-noisy:** PRISMA, PRISMA-S/TARCiS, PRISMA-ScR, AMSTAR2, ROBIS, SANRA, SWiM checklist, PubMed E-utilities, OpenAlex, Crossref, and TACL are generally usable. JBI, GRADE, Nature Reviews, ISCA Archive, GitHub-rendered pages, and some developer-doc pages contain UI/nav/cookie/footer artifacts. These can still support claims, but they need QA flags and distilled cards to keep agents from over-reading boilerplate.

3. **Family-level source cards are not enough:** Current `references/source_inventory/source_cards/*.md` are useful for route selection, but they do not consistently attach each key point to a canonical Markdown path and exact locator. That is acceptable for family guidance, but inadequate for a knowledge-heavy prior router that must support claim verification.

4. **Blocked/bad sources are handled correctly, but should be louder:** `press`, `cacm_author_guidelines`, and `state_of_art_review_2022` are correctly marked as blocked or bad capture in inventory/coverage docs. Any routing text that mentions them should say “inventory target / local unavailable / not direct evidence” at the first point of use.

5. **Distillation should be added, not substituted:** A derivative distilled layer is warranted, but it must never replace canonical Markdown. The distilled layer should provide route-specific decision aids, source cards v2, and claim ledgers with mandatory canonical paths and support status.

---

## 2. External evidence review

### 2.1 What comparable skill systems usually store

#### OpenAI / Codex skill packaging

OpenAI’s public `openai/skills` repo defines Agent Skills as folders containing instructions, scripts, and resources that Codex can use to improve task performance fileciteturn21file0. The repo’s skill-creator guidance is more explicit: a skill may contain `SKILL.md` plus optional `scripts/`, `references/`, and `assets/`, but `SKILL.md` should stay concise; longer references should be loaded only as needed, and large reference files should include search guidance or tables of contents fileciteturn23file0. The local canonical OpenAI Codex skill documentation in this repo also emphasizes progressive disclosure: the model initially sees only name/description/path, then loads `SKILL.md` after selection, and can further load references/assets/scripts as needed fileciteturn18file0.

**Implication for this repo:** The current design is aligned with OpenAI-style progressive disclosure. However, a 201-file canonical Markdown corpus is heavier than ordinary public skills; it is reasonable only because the repo explicitly routes through registries, manifests, and indexes before opening selected canonical Markdown.

#### Anthropic / Claude plugin skills

Anthropic’s official Claude plugin examples define skills as model-invoked capabilities placed under `skills/<skill-name>/SKILL.md`, with optional README, references, examples, and scripts fileciteturn16file0. The plugin-structure skill describes standardized directories, optional `skills/`, and supporting references/scripts for richer capabilities fileciteturn17file0. The root README frames plugins as curated bundles, not unrestricted corpora, and warns users to exercise caution when installing plugins from the web fileciteturn14file0.

**Implication:** Skill-like repos usually include instructions and lightweight supporting references, not necessarily full raw corpora. This supports the repo’s `SKILL.md` + references + source cards + indexes pattern, but does not itself prove that all fulltext Markdown belongs in the repo.

#### `llms.txt` and LLM-readable Markdown

The `AnswerDotAI/llms-txt` project argues that context windows are too small to process entire websites, so sites should provide concise Markdown guidance and links to LLM-friendly Markdown versions of detailed pages fileciteturn35file0. It explicitly supports clean Markdown as a useful format for LLM consumption, while also distinguishing overview files from larger optional full representations.

**Implication:** There is explicit external evidence that Markdown is a good LLM-facing format and that a layered overview-plus-details design is desirable. This supports converted canonical Markdown as an agent-readable verification layer. It does not prove that every converted fulltext should be stored in the same Git repository.

#### Large corpora and source files

The ACL Anthology repo is a useful counterexample for large scholarly corpora. Its README says the repo contains metadata for papers/authors/venues, code, instructions, and a Python metadata package; when hosting a mirror, papers and attachments reside in a separate `ANTHOLOGYFILES` directory and are rsynced separately, with a warning that initial mirroring can take up to eight hours fileciteturn93file0. The ACL Anthology programmatic-access page also says the metadata is in GitHub while PDFs are hosted on ACL servers fileciteturn87file0.

**Implication:** Corpus-heavy scholarly projects commonly keep metadata/code in Git and keep large original fulltext/PDF assets in a separate serving or mirroring channel. This supports the current choice to keep `canonical_sources/raw/` out of normal GitHub review.

### 2.2 GitHub official guidance on large files and release channels

GitHub official docs state that GitHub warns for files above 50 MiB and blocks files above 100 MiB; repositories should ideally remain below 1 GiB and are strongly recommended below 5 GiB; for large files, GitHub recommends Git LFS or releases rather than tracking large binaries directly fileciteturn27file0. The same official data variables define `50 MiB` as the warning size and `100 MiB` as the maximum GitHub file size, with `2 GiB` as a large-file variable fileciteturn31file0. Git LFS stores pointer files in Git and file contents elsewhere, with plan-dependent file size limits fileciteturn28file0. GitHub Releases can distribute assets, with up to 1000 assets per release and per-file limits, and official docs describe releases as a way to package project versions and binary files fileciteturn29file0 fileciteturn32file0.

**Implication:** Do not add raw PDFs, raw HTML captures, DOCX, or full downloaded binary corpora to the main branch by default. The current approach—Markdown conversions tracked, raw captures outside GitHub unless LFS/release/object storage is chosen—is consistent with GitHub guidance.

### 2.3 Do similar projects put original fulltext directly in repo?

**Observed evidence:**

- OpenAI and Anthropic skill examples include `SKILL.md`, references, scripts, examples, and resources, but their official pattern stresses progressive disclosure and concise core instructions rather than raw fulltext corpora fileciteturn16file0 fileciteturn21file0 fileciteturn23file0.
- ACL Anthology stores metadata/code in GitHub and keeps papers/PDFs on external servers or mirror file directories fileciteturn93file0.
- GitHub official docs recommend LFS/releases for large files, not regular Git tracking of large binaries fileciteturn27file0.
- `llms.txt` supports clean Markdown for LLM consumption, with concise overview files linking to detailed Markdown pages, not indiscriminate raw fulltext in a repo fileciteturn35file0.

**Answer:** Other projects usually do **not** put raw original fulltext binaries directly into a main Git branch. They usually put metadata, manifests, indexes, clean docs, source cards, summaries, or selected reference files. If they distribute large or original assets, the usual channels are Git LFS, release assets, object storage, website hosting, or a separately documented mirror path.

### 2.4 Is there evidence supporting “converted Markdown fulltext in repo”?

**Supported by evidence:**

- OpenAI/Anthropic skills allow references/resources as part of skills, and OpenAI skill-creator guidance says references can be loaded as needed fileciteturn16file0 fileciteturn23file0.
- `llms.txt` explicitly supports Markdown as a human- and LLM-readable format for content that would otherwise be hard for LLMs to parse efficiently fileciteturn35file0.
- GitHub size guidance permits ordinary text files when repo size remains reasonable; the concern is large binaries and repository bloat, not small/medium Markdown files per se fileciteturn27file0.

**Inferred / not directly proven:**

- There is no official evidence found here that says “convert hundreds of official PDFs/HTML pages to Markdown and commit all of them into a skill repo.” That is a repo-specific design inference.
- It is reasonable in this draft because the repo needs claim verification and has explicit routing/index boundaries, but it should remain conditional on license/reuse review and repository size monitoring.

### 2.5 Is there evidence supporting LLM-generated derivative summaries / distilled cards?

**Direct evidence:**

- OpenAI skill guidance emphasizes progressive disclosure, concise `SKILL.md`, and reference files loaded on demand; large references should include search guidance rather than being forced into core prompts fileciteturn23file0.
- `llms.txt` argues for concise expert-level information plus links to detailed Markdown pages because entire websites do not fit in context windows fileciteturn35file0.
- The repo’s own `SKILL.md`, `evidence-rules.md`, `source-map.md`, and validation note already require source cards/indexes to be derivative locator aids rather than canonical truth fileciteturn6file0 fileciteturn41file0 fileciteturn39file0 fileciteturn92file0.

**Inference:**

- The external evidence supports derivative summaries as a progressive-disclosure layer. It does **not** specifically require that summaries be LLM-generated. The decision to use LLM-based distillation is a practical inference from this repo’s scale, the mixed conversion quality, and the need for route-specific operational guidance.
- Any LLM-generated summary must be validated against canonical Markdown and must carry provenance fields. It should never be cited as direct evidence.

---

## 3. Repository architecture review

### 3.1 Architecture strengths

1. **Route-first design.** `SKILL.md`, `route-registry.md`, `task-routing.md`, and `route-source-index.yaml` collectively define a route-first workflow: start with the smallest applicable route, select source families/source IDs, then load indexes/locators before opening canonical Markdown. This is aligned with OpenAI/Anthropic progressive-disclosure conventions fileciteturn6file0 fileciteturn38file0 fileciteturn42file0 fileciteturn40file0.

2. **Evidence boundary is explicit.** `evidence-rules.md` requires source packets with source ID, doc ID, span/page, support type, confidence, freshness, claim type, and canonical verification. It says blocked/bad/no-local rows cannot support direct claims and that source cards/indexes are derivative fileciteturn41file0.

3. **GitHub vs local boundary is mostly understood.** `source-map.md` explicitly says Markdown conversions under `canonical_sources/md/` are tracked for reviewable source access, while raw captures and split section locators are local/rebuildable backing data unless distributed via LFS, release assets, object storage, or other large-file channel fileciteturn39file0.

4. **Coverage status is transparent.** `local_corpus_index.md` and `coverage_report.md` mark sources as `available`, `partial`, `blocked`, `bad_capture`, or `no_local_docs`, including examples such as `press`, `cacm_author_guidelines`, and `state_of_art_review_2022` fileciteturn10file0 fileciteturn44file0.

5. **Validation already tests routing behavior.** `validation/agent_qa_validation_2026-05-04.md` tests route selection, source boundaries, evidence locator use, blocked-source handling, and GitHub/full-corpus boundary. It explicitly notes that factual claim validation still requires selected canonical spans fileciteturn92file0.

### 3.2 Architecture weaknesses and risks

1. **Public locator availability is ambiguous.** `section_index_manifest.jsonl` reports 63 section index files and large per-source section counts, including PRISMA 2020, Cochrane, ISCA, JBI, and OpenAI/Codex sources fileciteturn51file0. However, direct GitHub fetches for selected `references/corpus_index/sections/by_source/*.jsonl` paths returned 404. `source-map.md` explains these are local backing data, but `SKILL.md` and `route-source-index.yaml` should state this more explicitly for GitHub-only agents.

2. **Absolute local raw paths are exposed in converted Markdown and manifest.** Many canonical Markdown files show local raw paths such as `/Volumes/My Book/...` or `docs/agent_capability_packs/...`. This is useful for a local vault but not portable. It may also leak local directory naming. Normalize to relative repo paths or a placeholder variable such as `${RAW_CORPUS_ROOT}`.

3. **Converted Markdown quality varies.** Some files are clean item-level checklists. Others contain navigation chrome, cookie notices, GitHub UI content, generated page controls, or huge conference program listings. The repo needs a conversion QA layer with explicit flags such as `clean_item_text`, `web_ui_noise`, `registry_locator_only`, `stub`, `bad_capture`, `requires_manual_check`.

4. **Family-level cards lack claim-level provenance.** Current source cards are useful as route labels and source-family guidance, but they should not be used for claim support. A v2 source card schema should require every key point and operational rule to list canonical Markdown paths and, where available, exact headings/pages/items.

5. **Licensing/reuse risk is underdeveloped.** Some sources are CC-BY or CC0, but others are publisher pages, manuals, venue instructions, commercial API documentation, or source files with specific terms. The repo already says licensing restrictions apply, but source cards should include `reuse_risk` and `redistribution_note`.

---

## 4. Canonical Markdown corpus audit

### 4.1 Corpus scale and index alignment

`local_corpus_index.md` reports 65 source IDs and status categories; `coverage_report.md` reports 201 Markdown paths/docs and notes two blocked source IDs (`press`, `cacm_author_guidelines`) plus a bad capture (`state_of_art_review_2022`) fileciteturn10file0 fileciteturn44file0. `document_index.jsonl` provides per-document metadata including source ID, family, route tags, canonical URL, Markdown path, bytes, line counts, heading counts, and status fileciteturn11file0. This is the right shape for a corpus index.

`section_index_manifest.jsonl` provides a second-layer section index manifest and marks some sources as `locator_only`, `browser_check_only`, or `bad_capture` fileciteturn51file0. This is conceptually useful, but the advertised split section files are not present in the GitHub review surface. Since `source-map.md` says split locators are local/rebuildable, the public docs should say: “GitHub-only agents should use `document_index.jsonl`, `local_corpus_index.md`, and direct selected Markdown search; local agents may additionally use `sections/by_source/*.jsonl`.”

### 4.2 PRISMA / EQUATOR / PRISMA-S / PRISMA-ScR / PRISMA-P

| Source family | Audit result |
|---|---|
| PRISMA 2020 landing page | Readable but shallow. It correctly states PRISMA 2020 includes statement paper, checklist, expanded checklist, abstract checklist, and flow diagrams, and advises reading the statement with the explanation/elaboration paper fileciteturn52file0. Use as family overview, not item-level evidence. |
| PRISMA 2020 checklist | Clean and directly usable for item-level reporting claims. Items 1–27 are readable, including information sources, search strategy, selection process, data collection process, risk of bias, certainty assessment, registration/protocol, support, conflicts, and data/code availability fileciteturn69file0. |
| PRISMA-S / TARCiS | The sampled TARCiS checklist is clean and directly usable for citation-search reporting terminology and items such as seed references, search directionality, dates, iterations, citation indexes/tools, deduplication, screening method, and flow-diagram reporting fileciteturn70file0. |
| PRISMA-ScR | The checklist is clean and directly usable for scoping-review reporting items, including rationale for scoping-review approach, PCC-like elements, evidence sources, data charting, critical appraisal if done, and synthesis of charted results fileciteturn71file0. |
| EQUATOR registry pages | Useful as registry/locator pages but often not enough for item-level claims. Use linked checklists or article fulltexts for direct reporting-item claims. |
| PRISMA-P | Not deeply sampled in this pass, but inventory says available. It should be prioritized for distillation because protocol-reporting guidance is distinct from completed-review reporting. |

**Priority:** PRISMA 2020, PRISMA-S/TARCiS, PRISMA-ScR, and PRISMA-P should be first-wave source cards v2 because they are central to routing and have exact checklist items.

### 4.3 Cochrane / JBI / Campbell / AMSTAR / ROBIS / GRADE

| Source | Audit result |
|---|---|
| Cochrane Handbook chapter 4 | Strong conduct authority for searching/selecting studies. The Markdown is readable and very detailed, with useful key points and MECIR boxes, but long and navigation-heavy at the top. It directly supports claims about information specialist involvement, comprehensive searches, CENTRAL/MEDLINE/Embase, trials registers, sensitivity, peer review of searches, and the difference between studies and reports fileciteturn72file0. |
| JBI Manual overview | Useful conduct/manual authority for systematic and scoping reviews, but the captured Markdown includes Confluence/cookie/UI artifacts. It supports high-level claims about JBI methodology scope and online/PDF version caveats, but chapter-specific claims should use chapter/PDF spans where available fileciteturn73file0. |
| AMSTAR 2 | Clean converted checklist. Directly supports critical appraisal claims about PICO, protocol, comprehensive search, duplicate selection/extraction, excluded studies, risk of bias, synthesis methods, publication bias, funding, and conflicts fileciteturn74file0. |
| ROBIS | Readable full article, with minor conversion artifacts in names. Directly supports claims that ROBIS assesses risk of bias in systematic reviews, has three phases, and domain structure covering eligibility, identification/selection, data collection/appraisal, and synthesis/findings fileciteturn75file0. |
| GRADE Working Group | Useful for high-level GRADE definition, domains, evidence tables, and requirements for claiming GRADE use. It also has long site/footer/news content and should not be used as a detailed handbook substitute unless exact relevant sections are located fileciteturn76file0. |
| Campbell | Inventory shows short canonical page. It likely functions as standards/locator unless the full standards document is available and clean. |
| PRESS | Correctly blocked. It should remain an unresolved audit target and not be inferred from other search-QA sources. |

**Priority:** Distill Cochrane chapter 4/12/14, JBI scoping/systematic chapters, AMSTAR2, ROBIS, and GRADE into source cards v2. Do not distill PRESS until canonical text is retrieved.

### 4.4 Survey writing / narrative review / taxonomy / SANRA / SWiM / ENTREQ / RAMESES

| Source | Audit result |
|---|---|
| SANRA | High-quality converted source. It supports claims that SANRA is a six-item critical appraisal scale for narrative review articles, rated 0–2, covering importance, aims, literature search, referencing, scientific reasoning/evidence level, and endpoint data. It also supports cautions: further validity testing is desirable, training is recommended, no established cross-setting cutoffs, and SANRA is a critical appraisal tool rather than a full reporting guideline fileciteturn80file0. |
| SWiM registry page | EQUATOR page is a useful locator. It states SWiM is for reporting synthesis without meta-analysis in systematic reviews of interventions and provides linked checklist/fulltext fileciteturn77file0. |
| SWiM checklist | Clean item-level evidence. It states SWiM complements PRISMA and includes nine reporting items covering grouping, standardized metrics, synthesis methods, prioritization criteria, heterogeneity, certainty, data presentation, results, and limitations fileciteturn78file0. |
| ENTREQ | Current sampled canonical file is an EQUATOR registry page. It supports high-level locator claims about qualitative synthesis reporting, but not item-level ENTREQ checklist claims. Need linked article/checklist for direct evidence fileciteturn79file0. |
| Nickerson taxonomy | Strong and readable but long. It directly supports taxonomy-development claims: taxonomies/classifications organize domain objects, many IS taxonomies are ad hoc, and the method combines conceptual and empirical approaches with properties such as conciseness, robustness, comprehensiveness, and extendibility fileciteturn81file0. |
| RAMESES | Not deeply sampled in this pass. Should be treated as realist/meta-narrative reporting standards source; distillation should be manually QA’d because these standards are specialized. |
| Narrative review writing 2011 / York narrative synthesis | Inventory says available. They should be distilled after SANRA/SWiM/Nickerson because their operational use is more nuanced and field-dependent. |
| `state_of_art_review_2022` | Marked bad capture by inventory/coverage; do not use as evidence until re-captured. |

**Priority:** First-wave survey-side distillation should cover SANRA, SWiM checklist, Nickerson taxonomy method, and PRISMA-ScR. ENTREQ/RAMESES should be second wave after locating item-level fulltext.

### 4.5 Scholarly databases and APIs

| Source | Audit result |
|---|---|
| OpenAlex | Clean enough. Supports claims that OpenAlex is an open catalog of scholarly entities and relationships, exposes a REST API and monthly snapshot, and has an LLM documentation index. It also contains dynamic pricing/usage text, so freshness risk is high fileciteturn82file0. |
| Crossref REST API | Clean enough despite navigation/blog noise. Supports claims about Crossref metadata retrieval, JSON REST API endpoints, deposited scholarly metadata, identifiers, no sign-up for REST API, and caveats about abstracts copyright fileciteturn83file0. |
| PubMed / NCBI E-utilities | Strong. Supports API base URL, request limits, API keys, registered tool/email policies, E-utilities list, Entrez history server, UID behavior, and copyright/disclaimer caveats fileciteturn84file0. |
| Semantic Scholar | Useful but contains web UI and marketing/testimonial content. Supports services (Academic Graph, Recommendations, Datasets), API key/rate-limit information, and dataset availability, but freshness risk is high fileciteturn85file0. |
| OpenCitations | Clean high-level page. Supports claims about open bibliographic/citation data, CC0 data, APIs/dumps, and linked open data, but more detailed API endpoint claims need API-specific pages fileciteturn86file0. |
| ClinicalTrials API | Inventory indicates only a 12-line file. Treat as stub/entrypoint only, not as full API documentation. |
| Europe PMC / CORE / Lens / Dimensions / Scite / IEEE Xplore | Not deeply sampled here. Inventory flags some as partial/stub/restricted. They need per-source conversion QA before any direct operational claims. |

**Priority:** OpenAlex, Crossref, PubMed E-utilities, Semantic Scholar, and OpenCitations should get source cards v2 because they are likely used often for paper retrieval/routing. Every card should say “metadata/discovery infrastructure, not SR methodology authority.”

### 4.6 Venue / exemplar / journal guidance

| Source | Audit result |
|---|---|
| ACL Anthology API | Clean and concise. Supports claims that ACL metadata is in a GitHub repo, PDFs are hosted on servers, and the Python package provides access; also gives ACL licensing/reuse distinctions before/after 2016 fileciteturn87file0. |
| ACL Anthology GitHub page capture | Noisy if using GitHub-rendered page captures. Prefer actual README/API docs or raw GitHub content over captured GitHub HTML. External README is cleaner and shows the repo contains metadata/code/package while paper files are served/mirrored separately fileciteturn93file0. |
| ISCA Archive | Current canonical sample is a huge Interspeech 2025 program/listing. It is useful as corpus/venue exemplar metadata, but poor as methodology guidance and high freshness risk fileciteturn88file0. |
| TACL submission guidelines | Strong venue guidance. Supports claims about submission format, double-blind policy, dual submission, ethics, resubmission windows, and a specific “Survey Papers – a Note” saying surveys must meet the same originality/significance/technical/relevance bar and provide new insights rather than a descriptive enumeration fileciteturn89file0. |
| Nature Reviews submission | Good venue/editorial guidance with footer/nav noise. Supports claims about Nature Reviews article types, writing tips, LLM authorship/use disclosure, and that Nature Reviews does not publish original research, case studies, meta-analyses, or systematic reviews fileciteturn90file0. |
| IEEE/ACM-related sources | Not deeply sampled here. Treat as venue or database guidance, not method authority, unless exact author-guideline or article-format files are cleanly captured. |
| CACM author guidelines | Blocked. Do not substitute ACM DL user guide. |

**Priority:** TACL and Nature Reviews should be distilled as venue/exemplar constraints, not as universal survey-writing methodology. ISCA should be reclassified as dynamic venue corpus/exemplar index, not methodology.

### 4.7 Codex / OpenAI skill packaging sources

The repo’s canonical OpenAI Codex skills file supports the central packaging logic: skills are instructions/resources/scripts; discovery uses name/description/path; `SKILL.md` is loaded after selection; references/assets/scripts are optional and loaded as needed fileciteturn18file0. External OpenAI skill-creator guidance adds strong support for keeping `SKILL.md` concise, splitting references, avoiding duplication, and using progressive disclosure for large references fileciteturn23file0.

**Priority:** This source should get a v2 source card because it grounds the pack’s architecture.

---

## 5. Non-canonical alignment audit

### 5.1 Findings table

| file | claim_or_section | alignment_status | supporting_canonical_sources | issue | recommended_change |
|---|---|---:|---|---|---|
| `SKILL.md` | “staged draft knowledge-resource router”; route-first, no runtime execution | aligned | OpenAI/Codex skills canonical; OpenAI/Anthropic skill examples fileciteturn18file0 fileciteturn16file0 | None. This is the repo’s strongest architectural claim. | Keep. Add one sentence that this is a prior router, not a source of final claims. |
| `SKILL.md` | Do not bulk-load raw/md; source cards/indexes/summaries/graph output are not canonical truth | aligned | Evidence rules and canonical/source-map boundary fileciteturn41file0 fileciteturn39file0 | None. | Keep and repeat in source_cards_v2 README. |
| `SKILL.md` | Use section indexes before canonical Markdown | partially aligned | `section_index_manifest.jsonl` exists fileciteturn51file0 | `sections/by_source/*.jsonl` appear local-only / missing from GitHub. | Add “local-only if absent in GitHub; GitHub fallback is document_index + selected canonical Markdown search.” |
| `references/source-map.md` | Markdown conversions tracked; raw captures remain local or distributed via LFS/release/object storage | aligned | GitHub large-file docs fileciteturn27file0; Git LFS/release docs fileciteturn28file0 fileciteturn29file0; ACL metadata/PDF split fileciteturn93file0 | None. | Keep. Add explicit size/licensing policy. |
| `references/source-map.md` | Split section locators are local/rebuildable backing data | aligned, but under-communicated | `section_index_manifest.jsonl` plus missing by_source files fileciteturn51file0 | Other docs assume section indexes are accessible. | Add cross-reference in `SKILL.md`, `route-source-index.yaml`, and `coverage_report.md`. |
| `references/route-registry.md` | Route registry and graphify are navigation only | aligned | `graphify-navigation.md` and evidence rules fileciteturn43file0 fileciteturn41file0 | None. | Keep. |
| `references/route-source-index.yaml` | `canonical_verification`: important claims require canonical md/raw, not only index/card | aligned | PRISMA, Cochrane, SWiM, API examples show need for exact source spans fileciteturn69file0 fileciteturn72file0 fileciteturn78file0 | None. | Keep. |
| `references/route-source-index.yaml` | `press` as SR search peer review authority | partially aligned | No local canonical PRESS; coverage says blocked fileciteturn44file0 | Correct route label, but cannot support claims. | Mark in route entry as `inventory_target_only until canonical retrieved`. |
| `references/route-source-index.yaml` | Scholarly APIs as retrieval/discovery sources | aligned | OpenAlex, Crossref, PubMed, Semantic Scholar, OpenCitations canonical docs fileciteturn82file0 fileciteturn83file0 fileciteturn84file0 fileciteturn85file0 fileciteturn86file0 | Potential overreach if called methodology authorities. | Add `not_methodology_authority: true` to database/API source family. |
| `references/evidence-rules.md` | Locator/index/source card cannot be direct evidence | aligned | Supported by repo architecture and validation note fileciteturn41file0 fileciteturn92file0 | None. | Keep. |
| `references/graphify-navigation.md` | Graph output is derivative/locator-only | aligned | Graphify doc and evidence rules fileciteturn43file0 fileciteturn41file0 | None. | Keep. |
| `references/source_inventory/coverage_report.md` | “201 Markdown paths/docs; 65 source IDs; blocked/bad statuses” | aligned, but local/public distinction needs clarity | `local_corpus_index.md`, `document_index.jsonl`, validation checks fileciteturn10file0 fileciteturn11file0 fileciteturn92file0 | Raw and split locators are local; public GitHub has md corpus but not raw/by_source. | Split metrics into `public_github`, `local_raw`, `local_section_indexes`. |
| `references/source_inventory/source_registry.yaml` | Source cards cannot replace canonical; inventory not exhaustive | aligned | Registry promotion policy fileciteturn45file0 | None. | Keep. Add source_card_v2 artifact class. |
| `references/source_inventory/source_cards/sr-method-authorities.md` | PRISMA reporting, Cochrane/JBI conduct, GRADE certainty, PRESS search-QA | mostly aligned | PRISMA checklist, Cochrane ch4, JBI overview, GRADE, AMSTAR/ROBIS fileciteturn69file0 fileciteturn72file0 fileciteturn73file0 fileciteturn76file0 | Family-level summary lacks exact canonical path per claim; PRESS blocked. | Convert to source_cards_v2 and label PRESS unresolved. |
| `references/source_inventory/source_cards/survey-writing-methods.md` | No single official cross-domain survey rulebook; combine narrative review, taxonomy, scoping, synthesis sources | partially aligned | SANRA, Nickerson, SWiM, PRISMA-ScR fileciteturn80file0 fileciteturn81file0 fileciteturn78file0 fileciteturn71file0 | “No single official rulebook” is a reasonable synthesis but not a single canonical claim. | Mark as reviewer synthesis / route prior, not direct evidence. |
| `references/source_inventory/source_cards/scholarly-databases.md` | Crossref/OpenAlex/PubMed/etc. as metadata/discovery baseline | partially aligned | API docs support capabilities and limits fileciteturn82file0 fileciteturn83file0 fileciteturn84file0 | “Best baseline” is evaluative. API docs do not prove optimality. | Reword to “configured candidate baseline; choose per task/coverage/license/rate limits.” |
| `references/source_inventory/source_cards/nlp-speech-cs-exemplars.md` | ACL/ISCA/TACL/Nature/IEEE/ACM as venue/exemplar guidance, not methodology | aligned | ACL API, ISCA archive, TACL, Nature Reviews fileciteturn87file0 fileciteturn88file0 fileciteturn89file0 fileciteturn90file0 | ISCA archive is a dynamic program listing, not stable guidance. | Add `dynamic_exemplar_index` and freshness risk. |
| `references/source_inventory/source_cards/codex-skill-packaging.md` | Progressive disclosure and skill reference design | aligned | OpenAI Codex canonical docs and skill-creator fileciteturn18file0 fileciteturn23file0 | Current family card should include exact paths. | Add v2 source card for `openai_codex_skills`. |
| `validation/agent_qa_validation_2026-05-04.md` | Navigation behavior passes; factual correctness still requires canonical spans | aligned | Validation note itself and canonical audit fileciteturn92file0 | Good. It did not validate factual claims from canonical source content. | Keep. Add this review as next validation layer. |

### 5.2 Claims supported by canonical Markdown

The following non-canonical claims are well-supported:

- **PRISMA 2020 as completed-SR reporting authority:** supported by PRISMA landing/checklist docs fileciteturn52file0 fileciteturn69file0.
- **PRISMA-S/TARCiS as search/citation-search reporting authority:** supported by TARCiS checklist fileciteturn70file0.
- **PRISMA-ScR as scoping-review reporting authority:** supported by PRISMA-ScR checklist fileciteturn71file0.
- **Cochrane chapter 4 as conduct/search-selection authority for intervention SRs:** supported by Cochrane chapter 4 fileciteturn72file0.
- **AMSTAR2/ROBIS as appraisal/risk-of-bias-in-review tools rather than reporting guidelines:** supported by AMSTAR2 and ROBIS sources fileciteturn74file0 fileciteturn75file0.
- **GRADE as certainty/recommendation framework, not search/screening authority:** supported by GRADE Working Group source fileciteturn76file0.
- **SWiM as PRISMA-complementary reporting guideline for synthesis without meta-analysis:** supported by SWiM checklist fileciteturn78file0.
- **SANRA as critical appraisal scale for narrative reviews, not a broad reporting guideline:** supported by SANRA source fileciteturn80file0.
- **Nickerson as taxonomy-development method source:** supported by Nickerson taxonomy article fileciteturn81file0.
- **OpenAlex/Crossref/PubMed/Semantic Scholar/OpenCitations as API/discovery infrastructure:** supported by sampled API docs fileciteturn82file0 fileciteturn83file0 fileciteturn84file0 fileciteturn85file0 fileciteturn86file0.
- **TACL/Nature as venue/editorial guidance, not general methodology:** supported by TACL and Nature Reviews submission docs fileciteturn89file0 fileciteturn90file0.

### 5.3 Claims that are over-generalized or only route labels

- “Best baseline” for database/API selection is not directly proven by API docs. It is a route prior.
- “No single official cross-domain survey rulebook” is likely true as a synthesis judgment, but not a direct claim from a single canonical source.
- “NLP/speech exemplar source family” is a route label. ACL/ISCA/TACL docs support source existence and venue norms, not universal survey-writing methodology.
- `press` and `cacm_author_guidelines` are source inventory targets, not available evidence.
- `state_of_art_review_2022` is explicitly bad capture and should not support claims.

### 5.4 Places where locator/summary/graph may be mistaken for evidence

- `route-source-index.yaml` should avoid language that makes source IDs look like evidence themselves. Add `evidence_role: locator|derivative|canonical`.
- Current source cards should be renamed or front-mattered as `artifact_type: derivative_family_card`.
- `coverage_report.md` and `local_corpus_index.md` should state that coverage rows only establish retrieval/corpus status, not source claims.
- `graphify-navigation.md` correctly says graph output is derivative, but route docs should repeat that graph traversal cannot substitute for canonical path verification.

---

## 6. Distillation decision

### Decision

Build a derivative distilled layer now.

This decision is based on both external conventions and repo-specific audit results:

- External skill conventions favor progressive disclosure, concise entrypoints, and optional references loaded as needed fileciteturn16file0 fileciteturn23file0.
- `llms.txt` supports concise LLM-readable Markdown and links to detailed Markdown because context windows cannot handle entire websites efficiently fileciteturn35file0.
- The repo has 201 Markdown docs and large per-source section counts, including sources with hundreds or thousands of sections/lines fileciteturn44file0 fileciteturn51file0.
- The canonical Markdown corpus contains clean checklists, long manuals, stubs, registry-only pages, web UI artifacts, and dynamic venue listings. A route-level agent needs a distilled triage layer.
- Current source cards are family-level and intentionally derivative; they need v2 provenance to become safe operational aids.

### Should the repo retain complete canonical Markdown?

Yes. Do **not** delete `references/canonical_sources/md/`.

The canonical Markdown layer is valuable because:

1. It gives GitHub/cloud agents reviewable access to canonical source text without raw binary downloads.
2. It allows claim verification to stay inside the repo.
3. It supports checksum/manifest/index alignment.
4. It is consistent with LLM-friendly Markdown conventions when kept behind progressive-disclosure routing.

The key caveats:

- It is converted canonical Markdown, not original raw source.
- It may contain conversion noise.
- It may carry licensing/reuse restrictions from the original source.
- Important claims must still verify against exact canonical paths and, when necessary, original source URL/raw capture.

### What derivative artifacts are needed?

| Artifact type | Purpose | Granularity | Can support direct claim? |
|---|---|---:|---:|
| `source_cards_v2/*.md` | per-source operational summary with provenance | per-source | no |
| `family_notes/*.md` | compare sources within a family | per-family | no |
| `route_notes/*.md` | route-specific source ordering and authority boundaries | per-route | no |
| `claim_ledgers/*.jsonl` | canonical-backed claims with support status | per-claim | only if claim ledger includes exact canonical path/span and is verified |
| `conversion_qa/*.jsonl` | conversion quality flags | per-document | no |
| `reuse_ledger/*.jsonl` | license/reuse redistribution constraints | per-source/doc | no |

### Recommended granularity

1. **Per-source v2 cards** for high-use canonical sources.
2. **Per-route notes** for `sr_writing_prior`, `survey_writing_prior`, `scholarly_database_routing`, and `codex_skill_packaging`.
3. **Per-claim ledgers** only for claims that the router is likely to reuse repeatedly, such as “PRISMA item 7 requires full search strategies” or “Cochrane chapter 4 recommends working with an information specialist.”
4. **Per-family overview** only after per-source cards exist, to avoid over-generalized family claims.

### Sources that should not be replaced by summaries

- PRISMA/PRISMA-S/PRISMA-ScR/PRISMA-P checklists and flow diagrams
- AMSTAR2 checklist
- ROBIS tool/guidance
- GRADE minimum requirements and handbook sections
- OpenAPI/Swagger/schema files
- API rate-limit/license/terms pages
- Venue submission policies and author instructions
- Legal/reuse/license text
- Blocked, bad-capture, or stub sources
- Any source used to make a direct claim about exact item wording

### How to avoid summary replacing canonical evidence

Add this policy to every derivative artifact:

> This card is derivative. It is for routing and triage only. It cannot be cited as direct evidence. Any user-facing methodological or factual claim must be verified against the listed canonical Markdown path and, when necessary, the original source URL or raw capture.

---

## 7. Proposed changes

### 7.1 Must-do changes

1. Add `references/distillation-plan.md`.
2. Add `references/source_inventory/source_cards_v2/README.md`.
3. Add first-wave v2 source cards:
   - `references/source_inventory/source_cards_v2/prisma_2020.md`
   - `references/source_inventory/source_cards_v2/sanra.md`
   - `references/source_inventory/source_cards_v2/openai_codex_skills.md`
4. Update `SKILL.md` to state that `sections/by_source/*.jsonl` may be local-only and GitHub-only agents should fall back to `document_index.jsonl` plus selected canonical Markdown search.
5. Update `route-source-index.yaml` with an `evidence_role` or equivalent for source families:
   - `canonical`
   - `converted_canonical`
   - `locator`
   - `derivative`
   - `blocked_inventory_target`
   - `bad_capture`
6. Update `coverage_report.md` to split public GitHub coverage from local raw/section-index coverage.
7. Add `conversion_quality` and `reuse_risk` fields to source registry or document index.
8. Normalize local raw paths in converted Markdown headers and manifest.

### 7.2 Should-do changes

1. Add first-wave source cards for:
   - Cochrane chapter 4
   - PRISMA-S/TARCiS
   - PRISMA-ScR
   - SWiM checklist
   - AMSTAR2
   - ROBIS
   - GRADE Working Group
   - OpenAlex
   - Crossref REST API
   - PubMed E-utilities
   - TACL submission guidelines
2. Add a `conversion_qa_report.md` with specific flags:
   - `clean_checklist`
   - `long_manual`
   - `web_ui_noise`
   - `registry_locator_only`
   - `stub`
   - `bad_capture`
   - `dynamic_listing`
   - `license_sensitive`
3. Add `claim_ledgers/sr_reporting.jsonl`, `claim_ledgers/survey_writing.jsonl`, and `claim_ledgers/scholarly_apis.jsonl`.

### 7.3 Nice-to-have changes

1. Add a small public `section_locator_compact.jsonl` for top sources only if the full section indexes remain local.
2. Add CI checks:
   - every source card v2 canonical path exists
   - every `source_id` in v2 cards exists in `source_registry.yaml`
   - no card has `support_type: direct`
   - no blocked/bad source card claims direct support
3. Add a README subsection explaining why raw sources are excluded.

---

## 8. Files to add or edit

| Path | Action | Rationale |
|---|---|---|
| `validation/chatgpt_deep_review_2026-05-04.md` | add | This report. |
| `references/distillation-plan.md` | add | Formal policy and workflow for derivative layer. |
| `references/source_inventory/source_cards_v2/README.md` | add | Schema and QA contract. |
| `references/source_inventory/source_cards_v2/prisma_2020.md` | add | SR reporting example card. |
| `references/source_inventory/source_cards_v2/sanra.md` | add | Narrative/survey-writing example card. |
| `references/source_inventory/source_cards_v2/openai_codex_skills.md` | add | Skill-packaging example card. |
| `SKILL.md` | edit | Clarify local-only section indexes and GitHub fallback. |
| `references/route-source-index.yaml` | edit | Add evidence-role fields and blocked/bad state. |
| `references/source_inventory/coverage_report.md` | edit | Split public vs local coverage metrics. |
| `references/source_inventory/source_registry.yaml` | edit | Add v2 source card artifact class, conversion/reuse fields. |
| `references/corpus_index/section_index_manifest.jsonl` | edit or document | Mark by-source paths as local-only if not tracked. |
| `references/canonical_sources/download_manifest.jsonl` | edit | Normalize local raw paths or add placeholder root. |

---

## 9. Exact Markdown contents for proposed new files

The following blocks are ready for Codex to add. They are also written out as separate downloadable files in this review bundle.

### 9.1 `references/distillation-plan.md`

<!-- BEGIN FILE: references/distillation-plan.md -->
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

<!-- END FILE: references/distillation-plan.md -->

### 9.2 `references/source_inventory/source_cards_v2/README.md`

<!-- BEGIN FILE: references/source_inventory/source_cards_v2/README.md -->
# Source cards v2

Status: proposed  
Artifact type: derivative source briefing schema  
Canonical evidence status: not canonical evidence

Source cards v2 are compact, provenance-preserving summaries for sources in `sr-survey-prior-router`. They help agents choose which canonical Markdown files to open and what claims are likely supported.

They must never replace canonical Markdown verification for final answers.

## Directory

Recommended path:

`references/source_inventory/source_cards_v2/`

File naming:

`<source_id>.md`

Examples:

- `prisma_2020.md`
- `cochrane_handbook.md`
- `sanra.md`
- `openalex.md`
- `openai_codex_skills.md`

## Schema

Each card should use the following top-level fields.

```yaml
source_id: ""
source_family: ""
canonical_paths: []
canonical_urls: []
authority_level: ""
version_or_access_date: ""
applies_to: []
not_for: []
route_relevance: []
freshness_risk: ""
reuse_or_license_risk: ""
qa_status: ""
last_reviewed: ""
```

Then include Markdown sections:

1. `## Key points`
2. `## Operational rules`
3. `## Common misuses`
4. `## Evidence limits`
5. `## Verification paths`
6. `## Unresolved gaps`

## Required key-point format

Every key point must include canonical grounding.

```yaml
- claim: ""
  supporting_canonical_paths: []
  support_type: "direct | indirect | locator_only | blocked | unsupported"
  verification_note: ""
  quote_or_locator: ""
```

Rules:

- Use `direct` only when the canonical Markdown directly states the claim.
- Use `indirect` when the canonical source supports the inference but not the exact operational rule.
- Use `locator_only` for registry pages, indexes, source cards, graph output, or manifests that only tell the agent where to look.
- Use `blocked` for sources known to exist but not locally captured.
- Use `unsupported` for tempting but not grounded claims.

## Authority levels

Recommended values:

- `canonical_reporting_guideline`
- `canonical_conduct_manual`
- `canonical_appraisal_tool`
- `canonical_certainty_framework`
- `canonical_database_api_doc`
- `canonical_venue_policy`
- `canonical_skill_packaging_doc`
- `locator_only`
- `blocked_inventory_target`
- `bad_capture_do_not_use`
- `derivative_not_canonical`

## Evidence boundary

A source card v2 may be cited only for statements about the card itself. For claims about methodology, reporting, API behavior, venue rules, or skill packaging, the answer must cite or quote the relevant canonical Markdown path or source URL.

## QA checklist

Before committing a source card v2:

1. Confirm `source_id` exists in the inventory.
2. Confirm at least one `canonical_paths` entry exists or mark the card as blocked/bad capture.
3. Confirm every key point has `supporting_canonical_paths`.
4. Confirm no key point is supported only by an older source card.
5. Confirm `not_for` boundaries are explicit.
6. Confirm blocked/partial/bad-capture status is not hidden.
7. Confirm licensing/reuse risk is stated.
8. Confirm freshness risk is stated for API, venue, pricing, and policy sources.

<!-- END FILE: references/source_inventory/source_cards_v2/README.md -->

### 9.3 `references/source_inventory/source_cards_v2/prisma_2020.md`

<!-- BEGIN FILE: references/source_inventory/source_cards_v2/prisma_2020.md -->
# Source card v2: PRISMA 2020

```yaml
source_id: prisma_2020
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/prisma_2020/canonical_prisma-2020.md
  - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  - references/canonical_sources/md/prisma_2020/subpage_statement_prisma-2020-statement.md
  - references/canonical_sources/md/prisma_2020/subpage_checklist_prisma-2020-checklist.md
  - references/canonical_sources/md/prisma_2020/pmc_bmj_statement_printable_html_pmc8005924.md
canonical_urls:
  - https://www.prisma-statement.org/prisma-2020
  - https://static1.squarespace.com/static/65b880e13b6ca75573dfe217/t/67ad313f1c80aa5235fce0d0/1739403584136/PRISMA_2020_checklist.pdf
authority_level: canonical_reporting_guideline
version_or_access_date: PRISMA 2020; local capture reviewed 2026-05-04
applies_to:
  - reporting completed systematic reviews
  - reporting systematic reviews with or without meta-analysis
  - methods and results reporting completeness checks
not_for:
  - designing the entire conduct method without Cochrane/JBI/manual guidance
  - assessing methodological quality of systematic reviews
  - rating certainty of evidence
  - venue-specific survey-writing advice
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
freshness_risk: low to medium; reporting guideline is stable, but official site/download URLs can change.
reuse_or_license_risk: checklist states CC BY 4.0; still verify source-specific license before redistributing large derived text.
qa_status: draft_v2_example
last_reviewed: 2026-05-04
```

## Key points

```yaml
- claim: "PRISMA 2020 is a reporting guideline for completed systematic review reports, not a full conduct manual."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/canonical_prisma-2020.md
  support_type: direct
  verification_note: "The PRISMA 2020 page describes the statement paper, checklist, expanded checklist, abstract checklist, and flow diagrams."
  quote_or_locator: "Open canonical_prisma-2020.md and verify the paragraph beginning 'PRISMA 2020 consists of a statement paper...'."

- claim: "A report should identify itself as a systematic review in the title."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: "Checklist item 1 states this requirement."
  quote_or_locator: "Page 1, TITLE / Title / Item 1."

- claim: "The Methods section should report eligibility criteria, information sources, full search strategies, selection process, data collection process, risk-of-bias assessment, synthesis methods, reporting-bias assessment, and certainty assessment."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: "Checklist items 5-15 cover these reporting elements."
  quote_or_locator: "Page 1, METHODS, items 5-15."

- claim: "The Results section should report the search/selection process, ideally using a flow diagram."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: "Checklist item 16a asks for numbers from records identified to included studies, ideally with a flow diagram."
  quote_or_locator: "Page 2, RESULTS / Study selection / Item 16a."

- claim: "PRISMA 2020 asks reports to disclose registration/protocol information, support, competing interests, and availability of data/code/materials."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: "Checklist items 24a-27 cover these other-information elements."
  quote_or_locator: "Page 2, OTHER INFORMATION, items 24a-27."
```

## Operational rules

1. Use PRISMA 2020 first for reporting-completeness claims about completed systematic reviews.
2. Pair with Cochrane Handbook or JBI Manual for conduct/method-design claims.
3. Pair with GRADE/CERQual for certainty/confidence claims.
4. Pair with PRISMA-S/TARCiS for detailed search/citation-search reporting.
5. For item-level claims, open the checklist Markdown, not only the PRISMA landing page.

## Common misuses

1. Treating PRISMA as proof that a review was well conducted.
2. Treating PRISMA as a substitute for a protocol, conduct manual, or certainty framework.
3. Using an EQUATOR registry page as if it contained the full checklist item wording.
4. Applying PRISMA 2020 unchanged to scoping reviews when PRISMA-ScR is the better reporting source.

## Evidence limits

- PRISMA 2020 supports reporting claims, not full conduct prescriptions.
- The landing page is a locator and overview; the checklist and statement/E&E files are better for item-level evidence.
- Some PRISMA files are partial or linked downloads; verify the specific Markdown path before final answers.

## Verification paths

1. `references/canonical_sources/md/prisma_2020/canonical_prisma-2020.md`
2. `references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md`
3. `references/canonical_sources/download_manifest.jsonl`
4. `references/source_inventory/local_corpus_index.md`

## Unresolved gaps

- Confirm whether all PRISMA linked PDFs/DOCX files convert cleanly after any future retrieval update.
- Add quote-level line or page locators for statement and explanation/elaboration papers after public section indexes are available or rebuilt.

<!-- END FILE: references/source_inventory/source_cards_v2/prisma_2020.md -->

### 9.4 `references/source_inventory/source_cards_v2/sanra.md`

<!-- BEGIN FILE: references/source_inventory/source_cards_v2/sanra.md -->
# Source card v2: SANRA

```yaml
source_id: sanra
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  - references/canonical_sources/md/sanra/linked_1_s41073-019-0064-8.pdf.md
canonical_urls:
  - https://link.springer.com/article/10.1186/s41073-019-0064-8
authority_level: canonical_appraisal_tool
version_or_access_date: 2019 article; local capture reviewed 2026-05-04
applies_to:
  - quality assessment of narrative review articles
  - narrative review writing prior
  - distinguishing narrative review appraisal from systematic review reporting
not_for:
  - systematic review reporting
  - systematic review methodological quality appraisal
  - formal taxonomy development methodology
  - database/API source selection
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
freshness_risk: low; original article is stable, but publisher page layout may change.
reuse_or_license_risk: article is open access; verify license and linked instrument terms before redistributing forms.
qa_status: draft_v2_example
last_reviewed: 2026-05-04
```

## Key points

```yaml
- claim: "SANRA was developed for assessing the quality of narrative review articles."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The abstract and background state the gap and purpose."
  quote_or_locator: "Abstract / Background and Conclusions."

- claim: "SANRA consists of six items scored from 0 to 2, with a maximum sum score of 12."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The Methods section lists the six revised scale items and scoring."
  quote_or_locator: "Methods section beginning 'The six items that form the revised scale...'."

- claim: "The six SANRA domains cover importance, aims, literature search, referencing, scientific reasoning/evidence level, and endpoint data."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The Methods section states the six topics."
  quote_or_locator: "Methods section discussing Fig. 1 and the six items."

- claim: "SANRA is a critical appraisal tool, not a reporting guideline."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The Discussion explicitly states SANRA is a critical appraisal tool and not a reporting guideline."
  quote_or_locator: "Discussion / Validity."

- claim: "SANRA should not be used as a strict universal grading scale because the article warns about validity limits, lack of established cut-offs, and the need for rater training."
  supporting_canonical_paths:
    - references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md
  support_type: direct
  verification_note: "The Discussion notes rater training, limitations, and caution around cross-setting comparisons/cutoffs."
  quote_or_locator: "Discussion / Inter-rater reliability, Validity, and Limitations."
```

## Operational rules

1. Use SANRA when the user asks about narrative review quality or how to improve a non-systematic review.
2. Do not apply SANRA to systematic reviews as a replacement for PRISMA, AMSTAR 2, ROBIS, or Cochrane/JBI.
3. Use SANRA to flag narrative-review quality dimensions: aim, search description, referencing, scientific reasoning, and endpoint data.
4. When a survey is closer to an NLP/CS literature survey than a biomedical narrative review, use SANRA as partial guidance only and pair it with taxonomy/survey-writing and venue/exemplar sources.

## Common misuses

1. Treating SANRA as a formal reporting guideline.
2. Treating SANRA score thresholds as universally validated.
3. Using SANRA to rate systematic review conduct.
4. Ignoring the article’s caution that validity and reliability depend on setting, raters, and training.

## Evidence limits

- SANRA was developed and tested in a medical editorial context.
- It is not enough for taxonomy-building methodology; pair with Nickerson/Kundisch taxonomy sources.
- It does not supply database search reporting standards comparable to PRISMA-S or TARCiS.
- It is not venue policy.

## Verification paths

1. `references/canonical_sources/md/sanra/canonical_s41073-019-0064-8.md`
2. `references/canonical_sources/md/sanra/linked_1_s41073-019-0064-8.pdf.md`
3. `references/canonical_sources/download_manifest.jsonl`
4. `references/source_inventory/local_corpus_index.md`

## Unresolved gaps

- Add a quote-level locator for the exact six-item list after section indexes are rebuilt or made available.
- Confirm whether the linked instrument/download has separate reuse conditions.

<!-- END FILE: references/source_inventory/source_cards_v2/sanra.md -->

### 9.5 `references/source_inventory/source_cards_v2/openalex.md`

<!-- BEGIN FILE: references/source_inventory/source_cards_v2/openalex.md -->
# Source card v2: OpenAlex API

```yaml
source_id: openalex
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/openalex/canonical.md
  - references/canonical_sources/md/openalex_snapshot/official_snapshot_data_format_snapshot-format.md
  - references/canonical_sources/md/openalex_snapshot/official_api_overview_introduction.md
canonical_urls:
  - https://developers.openalex.org/
authority_level: canonical_database_api_doc
version_or_access_date: local capture reviewed 2026-05-04
applies_to:
  - scholarly entity metadata retrieval
  - works/authors/sources/institutions/topics/publishers/funders discovery
  - open scholarly graph and snapshot access
  - retrieval pipeline planning
not_for:
  - systematic review conduct authority
  - reporting guideline authority
  - certainty appraisal
  - venue policy
route_relevance:
  - paper_retrieval_prior
  - survey_writing_prior
  - scholarly_database_selection
  - source_audit
freshness_risk: high; API pricing, limits, endpoints, and authentication can change.
reuse_or_license_risk: OpenAlex describes dataset openness/CC0; verify current terms before large-scale redistribution or commercial use.
qa_status: draft_v2_example
last_reviewed: 2026-05-04
```

## Key points

```yaml
- claim: "OpenAlex is an open catalog of the global research system covering scholarly works, authors, institutions, sources, topics, publishers, and funders."
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: direct
  verification_note: "The overview page describes OpenAlex and its entity types."
  quote_or_locator: "Overview / Documentation Index and Data sections."

- claim: "OpenAlex offers both a REST API and a downloadable data snapshot."
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: direct
  verification_note: "The overview page states that the documentation covers the API and data snapshot."
  quote_or_locator: "Overview / Access section."

- claim: "OpenAlex can support retrieval and metadata expansion, but it is not itself a methodology authority for SR conduct."
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: indirect
  verification_note: "The source describes data/API access, not review methods. The non-methodology boundary is inferred from source type."
  quote_or_locator: "Overview / Data and Access sections."

- claim: "OpenAlex freshness risk is high because the local capture includes current API access/pricing language."
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex/canonical.md
  support_type: direct
  verification_note: "The page mentions API key, free usage, paid plan, and snapshot update cadence; these are operational details that can change."
  quote_or_locator: "Overview / Access section."
```

## Operational rules

1. Use OpenAlex for open scholarly graph metadata, entity expansion, and broad discovery.
2. Verify API limits, authentication, pricing, and snapshot cadence live or from the latest canonical Markdown before implementation decisions.
3. Pair OpenAlex with PubMed/Europe PMC/Crossref/Semantic Scholar/OpenCitations depending on domain, metadata need, and citation-link need.
4. Do not cite OpenAlex as proof that a search strategy is systematic or comprehensive.

## Common misuses

1. Treating OpenAlex coverage claims as a substitute for database-selection guidance from Cochrane/JBI/search-method sources.
2. Treating API availability as proof of canonical bibliographic completeness.
3. Using old local API limits without freshness checks.
4. Confusing source metadata coverage with venue/methodological authority.

## Evidence limits

- Supports claims about OpenAlex data/API/snapshot access.
- Does not support PRISMA, Cochrane, JBI, AMSTAR, ROBIS, or GRADE claims.
- Operational details may be stale.

## Verification paths

1. `references/canonical_sources/md/openalex/canonical.md`
2. `references/canonical_sources/md/openalex_snapshot/official_snapshot_data_format_snapshot-format.md`
3. `references/canonical_sources/download_manifest.jsonl`
4. `references/source_inventory/local_corpus_index.md`

## Unresolved gaps

- Add latest live verification step for API limits, pricing, and authentication before release.
- Add route-specific comparison table with Crossref, PubMed, Semantic Scholar, OpenCitations, and Europe PMC.

<!-- END FILE: references/source_inventory/source_cards_v2/openalex.md -->

### 9.6 `references/source_inventory/source_cards_v2/openai_codex_skills.md`

<!-- BEGIN FILE: references/source_inventory/source_cards_v2/openai_codex_skills.md -->
# Source card v2: OpenAI Codex skills

```yaml
source_id: openai_codex_skills
source_family: codex_skill_packaging
canonical_paths:
  - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
canonical_urls:
  - https://developers.openai.com/codex/skills
  - https://developers.openai.com/codex/agents-md
authority_level: canonical_skill_packaging_doc
version_or_access_date: local capture reviewed 2026-05-04
applies_to:
  - skill packaging
  - progressive disclosure
  - route-first skill architecture
  - separating entrypoint, references, scripts, and validation artifacts
not_for:
  - systematic review methodology
  - survey-writing methodology
  - scholarly database/API content decisions
  - venue submission policy
route_relevance:
  - general_domain_prior
  - source_audit
  - skill_packaging
freshness_risk: medium to high; Codex/agent-skill docs can change.
reuse_or_license_risk: verify OpenAI documentation terms before large-scale redistribution.
qa_status: draft_v2_example
last_reviewed: 2026-05-04
```

## Key points

```yaml
- claim: "Codex skill packaging supports a concise skill entrypoint with optional supporting files."
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: direct
  verification_note: "Open the canonical skill documentation and verify the sections describing skill files and supporting assets/references."
  quote_or_locator: "canonical_skills.md; exact section locator should be added after section indexes are rebuilt."

- claim: "A route-first skill can keep detailed domain material under references rather than forcing every task to load the full corpus."
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
  support_type: indirect
  verification_note: "Progressive-disclosure packaging supports the architecture, but the exact SR/survey routing design is repo-specific."
  quote_or_locator: "canonical_skills.md; pair with SKILL.md and source-map.md for repo-specific policy."

- claim: "AGENTS.md or persistent project instructions are separate from repeatable skill workflows."
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
  support_type: direct
  verification_note: "Use this only for packaging/project-instruction boundaries, not research methodology."
  quote_or_locator: "canonical_agents-md.md; exact locator to be added."

- claim: "OpenAI/Codex skill docs do not decide which SR or survey-writing sources are canonical."
  supporting_canonical_paths:
    - references/canonical_sources/md/openai_codex_skills/canonical_skills.md
    - references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md
  support_type: indirect
  verification_note: "These are packaging docs, not methodology docs; this is an authority-boundary inference."
  quote_or_locator: "Verify source type and scope."
```

## Operational rules

1. Use this source to justify `SKILL.md` as a concise router and `references/` as lazy-loaded supporting material.
2. Use it to defend progressive disclosure and separation of instructions from supporting knowledge.
3. Do not use it to support SR, survey-writing, API, or venue claims.
4. Pair with this repo’s `SKILL.md`, `source-map.md`, and `evidence-rules.md` when explaining the pack architecture.

## Common misuses

1. Treating Codex skill-packaging docs as evidence for systematic review methods.
2. Treating packaging examples as proof that every canonical fulltext should be committed.
3. Ignoring license/reuse terms for copied documentation.
4. Overloading `SKILL.md` with full domain summaries instead of keeping it route-oriented.

## Evidence limits

- Supports packaging and workflow architecture.
- Does not support research methodology.
- Source freshness is important because Codex docs may evolve.

## Verification paths

1. `references/canonical_sources/md/openai_codex_skills/canonical_skills.md`
2. `references/canonical_sources/md/openai_codex_agents_md/canonical_agents-md.md`
3. `references/source_inventory/source_cards/codex-skill-packaging.md`
4. `references/source-map.md`
5. `references/evidence-rules.md`

## Unresolved gaps

- Add exact section locators from canonical skill docs after public section indexes are available or rebuilt.
- Add an explicit repo policy distinguishing packaging evidence from methodology evidence.

<!-- END FILE: references/source_inventory/source_cards_v2/openai_codex_skills.md -->


## 10. Open questions / risks

1. **Web search limitation:** This review used GitHub connector access to public repos and GitHub-hosted official docs. General web browsing was unavailable in the review environment, so non-GitHub official pages were inspected only through this repo’s converted canonical Markdown or GitHub-hosted docs. For fast-changing APIs/venue policies, a live browser re-check should be done before final release.

2. **License/reuse audit is incomplete:** The repo tracks Markdown conversions of sources with different licenses and terms. Some are CC-BY/CC0; others may have restrictive or ambiguous reuse terms. Add a reuse ledger before broad public distribution.

3. **Converted Markdown is not original source:** For exact forms, figures, tables, flow diagrams, schemas, and legal terms, verify raw/original sources. Converted Markdown may lose layout or table semantics.

4. **Public GitHub vs local vault mismatch:** The repo is intentionally bridged between local Obsidian/Codex/GitHub workflows. This is acceptable, but every workflow doc should explicitly say which files are public GitHub surface and which are local-only.

5. **Source freshness:** API docs, venue policies, OpenAI/Codex docs, Semantic Scholar/OpenAlex pricing/rate limits, and dynamic conference pages have high freshness risk. Cards should carry freshness risk and update dates.

6. **Authority creep:** The largest credibility risk is not missing sources but over-promoting a source’s role. Venue guidance is not methodology. API docs are not evidence-synthesis methodology. Reporting guidelines are not conduct manuals. Appraisal tools are not reporting guidelines. Cards should repeatedly enforce this.

7. **Distillation quality risk:** LLM-generated cards can hallucinate or over-compress. The QA gate must reject any key point without a canonical path and locator.

8. **Bad/blocked sources:** `press`, `cacm_author_guidelines`, and `state_of_art_review_2022` should remain visible as unresolved targets. Do not hide them, but do not let route text imply local evidence exists.

9. **Need claim ledgers for repeated claims:** For high-frequency claims, source cards alone may not be enough. Add claim ledgers with exact canonical paths, quotes, and verification dates.

10. **Need conversion QA automation:** Add a script or validation rule to flag extremely short files, navigation-heavy captures, bad/browser-check captures, missing source URLs, local absolute path leakage, and source cards with nonexistent canonical paths.
