# Week 1 Assessment — Mini Eval Scorer

**Rules:** 60 minutes. No AI of any kind, including me — once you start, I won't answer questions or look at code until you're done or time's up. Python docs and web search are allowed (reading explanations is fine; copying a solution to this exact problem is not). Write your solution in `solution.py` in this folder. When you finish or time runs out, stop, save, and say so — I'll grade it against the rubric and log it.

This is a step up from the baseline, so a lower score than you'd like is fine — the point is the solo rep. If you finish early, that's a good sign.

## The data

`results.txt` — one graded item per line, format `category,verdict`:

```
math,correct
reading,incorrect
science,correct
```

`verdict` is always `correct` or `incorrect`. Three categories appear — `math`, `reading`, `science` — mixed together in no particular order.

## What to build

**Part 1 — Overall accuracy.** Read the file. Count how many items are `correct` out of the total, and print the percentage.

**Part 2 — Per-category accuracy.** For each category, print its accuracy — correct out of that category's own total.

**Part 3 (stretch — only if time remains).** Print the categories sorted from lowest accuracy to highest, so the weakest area is on top.

## Expected output (Parts 1–2)

```
Overall accuracy: 80.0% (12/15)
math: 80.0% (4/5)
reading: 60.0% (3/5)
science: 100.0% (5/5)
```

If your numbers match, Parts 1–2 are correct. Category order doesn't matter for Parts 1–2.
