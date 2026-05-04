# Future Split Notes

This note is not part of normal knowledge-router navigation. Use it only if the staged router is later split into smaller knowledge domains.

## Possible Context Fields

- `task_type`: selected route or future child-skill task.
- `corpus_scope`: allowed files, registries, review ids, or source subsets.
- `authority_paths`: canonical policies, guidelines, registries, or source maps to consult.
- `read_only/write_allowed`: explicit mutation boundary.
- `expected_artifacts`: outputs to produce or update, if any.
- `provenance_expectation`: evidence or source-tracing expectation.

## Boundary Notes

- Preserve repo safety boundaries from the router.
- Do not widen `corpus_scope` without reporting the reason.
- Return unsupported, missing, or stale evidence explicitly.
- Return enough provenance for later synthesis or audit.

## Possible Future Domains

- `evidence-extraction`: evidence packet knowledge.
- `source-grounding-audit`: source role, freshness, and provenance knowledge.
- `synthesis-writing`: grounded prose and outline knowledge.
- `research-memory-update`: durable-decision recording after user-approved memory/documentation policy exists.
