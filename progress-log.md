# Progress Log

Weekly Tier-0 assessments: timed, solo, no AI, docs allowed. Graded afterward by Claude against a rubric. Logged honestly — including incomplete attempts and failures. An upward trend matters more than any single score.

| Week | Date | Assessment | Time | Result | Notes |
|------|------|------------|------|--------|-------|
| 0 | 2026-07-14 | Baseline: word frequency counter | ~80 min (60 + 20 over) | **3/5** | First-ever unassisted program. Full algorithm correct — read/normalize/regex-strip/split/unique-list/nested-count/lambda-sorted top-5. All 5 words correct + correct order. One bug: final print used a parallel counter (`counta`) for the count instead of the sorted index (`item`), so 3 of 5 counts printed wrong. Diagnosed the bug himself in plain English ("lock and key mismatch") before seeing the analysis. Used regex + lambda sort keys unprompted on day one. |
| 1 | 2026-07-14 | Mini eval scorer | tutored (Tier 1) | **not graded** | Started solo, hit a wall on dictionaries ~30 min in and switched to Tier 1 tutoring — correct call, logged honestly. Built a dynamic dict-based eval scorer (no hardcoded categories): file parsing, the group-and-tally pattern, per-category + overall accuracy, `sorted()` with a lambda key (understood this time, not copied), then refactored two loops into one single-pass version with a validation guard. Wrote every line himself. Concepts learned: dicts, group-and-tally, `sum(d.values())`, `sorted`/`key`/`lambda`, guard clauses, and variable ordering/scope ("can't use an ingredient before the line that makes it"). |
| 2 | 2026-07-14 | Enrollment rate scorer (3-status variant) | semi-assisted | **not graded** | Second independent build of the same pattern, reskinned, with a new twist: `status` had three values (`enrolled`/`waitlisted`/`declined`) and only `enrolled` counts as success while all three count toward the total — handled correctly. All three parts correct including the stretch sort. Sorted by true rate, not count (dataset was rigged so count-order ≠ rate-order — he got it right, the exact bug he had at the start of the night). Wrote every line, but referred to the Week 1 solution heavily and asked conceptual dict questions (`totals[program]`, formal dict definition) mid-way — so not a cold solo rep. Pattern is becoming his; next bar is reproducing it with the reference closed. |
| 3 | 2026-07-14 | Support resolution rate (mastery check) | ~30 min (of 60), cold solo | **5/5** | Mastery check: reproduce the dict group-and-tally pattern with all references closed. Passed cleanly — all three parts correct incl. the stretch sort, in half the allotted time. Correctly sorted by rate not count on a dataset rigged so the two orders diverge. Single-pass, both tally dicts inside the comma guard, success-gate correct. First fully cold, correct, unassisted solo rep of the pattern — the curve from Week 0 (couldn't do a word counter) to here in one session. NOTE: this is 5/5 on *reproduction* of a now-familiar pattern; next bar is *transfer* — a non-isomorphic problem (e.g. averaging a numeric field instead of a success-rate) to test applying dicts to a new shape. |

## Grading scale

- **5** — Correct, clean, handled edge cases, finished with time to spare
- **4** — Correct on main cases, minor issues or rough edges
- **3** — Core working, notable bugs or an incomplete part
- **2** — Substantial progress, doesn't run correctly end-to-end
- **1** — Attempted, fundamental blockers
- **0** — Could not start / did not attempt
