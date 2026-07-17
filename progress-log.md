# Progress Log

Weekly Tier-0 assessments: timed, solo, no AI, docs allowed. Graded afterward by Claude against a rubric. Logged honestly — including incomplete attempts and failures. An upward trend matters more than any single score.

| Week | Date | Assessment | Time | Result | Notes |
|------|------|------------|------|--------|-------|
| 0 | 2026-07-14 | Baseline: word frequency counter | ~80 min (60 + 20 over) | **3/5** | First-ever unassisted program. Full algorithm correct — read/normalize/regex-strip/split/unique-list/nested-count/lambda-sorted top-5. All 5 words correct + correct order. One bug: final print used a parallel counter (`counta`) for the count instead of the sorted index (`item`), so 3 of 5 counts printed wrong. Diagnosed the bug himself in plain English ("lock and key mismatch") before seeing the analysis. Used regex + lambda sort keys unprompted on day one. |
| 1 | 2026-07-14 | Mini eval scorer | tutored (Tier 1) | **not graded** | Started solo, hit a wall on dictionaries ~30 min in and switched to Tier 1 tutoring — correct call, logged honestly. Built a dynamic dict-based eval scorer (no hardcoded categories): file parsing, the group-and-tally pattern, per-category + overall accuracy, `sorted()` with a lambda key (understood this time, not copied), then refactored two loops into one single-pass version with a validation guard. Wrote every line himself. Concepts learned: dicts, group-and-tally, `sum(d.values())`, `sorted`/`key`/`lambda`, guard clauses, and variable ordering/scope ("can't use an ingredient before the line that makes it"). |

## Grading scale

- **5** — Correct, clean, handled edge cases, finished with time to spare
- **4** — Correct on main cases, minor issues or rough edges
- **3** — Core working, notable bugs or an incomplete part
- **2** — Substantial progress, doesn't run correctly end-to-end
- **1** — Attempted, fundamental blockers
- **0** — Could not start / did not attempt
