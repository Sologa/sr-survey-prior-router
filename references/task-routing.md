# Task Routing

Use routing to minimize loaded context. The router chooses the smallest knowledge route that can inform the user's task, then reads only that route's listed reference files.

## Navigation Heuristics

- Restate the task as one knowledge-routing question.
- Match the question to one `route_id` in `route-registry.md`.
- If two routes match, prefer the route with the narrowest useful reference set.
- If the task asks for grounded writing but evidence support is missing, consult `evidence_grounding` before `synthesis_writing`.
- If the task asks how a new knowledge layer should be organized, consult `general_domain_prior` before discussing retrieval or skill bundles.
- Scoping-review route conflict rule: formal scoping-review reporting, conduct, checklist, JBI, or PRISMA-ScR tasks route to `sr_writing_prior`; broad literature mapping, taxonomy, or survey-organization tasks may route to `survey_writing_prior`.
- Report missing context rather than silently widening scope.

## Route Boundaries

- `general_domain_prior`: knowledge architecture for turning large resources into agent-usable prior.
- `survey_writing_prior`: survey/related-work resources, taxonomy, source cards, claim ledgers, and broad literature mapping or organization tasks that are not formal scoping-review reporting/conduct/checklist work.
- `sr_writing_prior`: systematic-review and scoping-review writing authority, methodology, reporting, conduct, checklist, JBI, PRISMA, and PRISMA-ScR routing.
- `evidence_grounding`: claim-to-source support and evidence packets.
- `source_audit`: source role, provenance, authority, and freshness checks.
- `synthesis_writing`: source-grounded writing knowledge after evidence support exists.

## Routing Examples

- "我有一堆 survey writing resources，如何變成 prior？" -> `survey_writing_prior`
- "幫我判斷 PRISMA 2020 在這個 SR 寫作任務中應該當什麼 authority" -> `sr_writing_prior`
- "Covidence 能不能當 SR methodology source of truth？" -> `sr_writing_prior`
- "這個 claim 有沒有 source 支持？" -> `evidence_grounding`
- "references 太多，什麼時候該升級成 wiki/RAG？" -> `general_domain_prior`
- "router 太胖時要如何拆分 reference domains？" -> `general_domain_prior`

## Expansion Criteria

- Add a route when the same task type appears repeatedly and needs a distinct reference set or risk boundary.
- Add optional notes when agents repeatedly miss a knowledge distinction and a short checklist would reduce mistakes.
- Split the reference domain only when the router becomes too broad, route-specific references exceed a practical read size, or repeated usage shows a stable separate knowledge domain.
