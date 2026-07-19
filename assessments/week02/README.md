# Week 2 Assessment — Enrollment Rate Report

**Rules:** 60 minutes. No AI of any kind, including me — once you start, I won't answer questions or look at code until you're done or time's up. Python docs and web search are allowed (reading explanations is fine; copying a solution is not). **Don't open your Week 1 solution** — the whole point is to see whether the pattern is yours now, not whether you can transcribe it. If you genuinely get stuck and peek, that's okay — just tell me so when you report. Write your solution in `solution.py` in this folder. When you finish or time runs out, stop, save, and say so.

This is the same shape of problem as the mini eval scorer, reskinned, with one twist (see below). You've done every piece of this before — this time, solo.

## The data

`results.txt` — one enrollment inquiry per line, format `program,status`:

```
business,enrolled
nursing,declined
data-science,waitlisted
```

Three programs appear — `business`, `nursing`, `data-science` — mixed together in no order.

**The twist:** unlike last time, `status` has **three** possible values: `enrolled`, `waitlisted`, or `declined`. Only `enrolled` counts as a success. `waitlisted` and `declined` are both non-successes — but they still count toward a program's **total** (they're real inquiries). So: every row adds to the total; only `enrolled` rows add to the success count.

## What to build

**Part 1 — Overall enrollment rate.** Read the file. Print the percentage of all inquiries that ended in `enrolled`, across everything.

**Part 2 — Per-program enrollment rate.** For each program, print its enrollment rate — enrolled out of that program's own total.

**Part 3 (stretch — only if time remains).** Print the programs sorted from lowest rate to highest, so the program that most needs attention is on top.

## Expected output (Parts 1–2)

```
Overall enrollment rate: 60.0% (12/20)
business: 60.0% (6/10)
nursing: 75.0% (3/4)
data-science: 50.0% (3/6)
```

If your numbers match, Parts 1–2 are correct. Program order doesn't matter for Parts 1–2.
