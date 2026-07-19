# Week 3 Assessment — Support Resolution Rate (Mastery Check)

**This one is the mastery check.** Same shape as Week 2 — the point is not a new puzzle, it's whether you can build the pattern **from your own understanding, with every reference closed.**

**Rules:** 60 minutes. No AI, including me. Python docs and web search are allowed. **Do NOT open your Week 1 or Week 2 solutions** — that's the whole test. If you get genuinely stuck, sit with it a while before anything else; if you still need help, you can ask, but then it converts to a tutored run (no shame — just tell me so I log it honestly). Write your solution in `solution.py` in this folder. When you finish or time runs out, stop, save, and say so.

## The data

`results.txt` — one support ticket per line, format `channel,outcome`:

```
phone,resolved
email,escalated
chat,abandoned
```

Three channels appear — `phone`, `email`, `chat` — mixed together in no order. `outcome` has three possible values: `resolved`, `escalated`, or `abandoned`. **Only `resolved` counts as a success.** `escalated` and `abandoned` are non-successes but still count toward a channel's total.

## What to build

**Part 1 — Overall resolution rate.** Print the percentage of all tickets that ended in `resolved`, across everything.

**Part 2 — Per-channel resolution rate.** For each channel, print its resolution rate — resolved out of that channel's own total.

**Part 3 (stretch — only if time remains).** Print the channels sorted from lowest rate to highest, so the channel that most needs attention is on top.

## Expected output (Parts 1–2)

```
Overall resolution rate: 50.0% (11/22)
phone: 60.0% (6/10)
email: 25.0% (2/8)
chat: 75.0% (3/4)
```

If your numbers match, Parts 1–2 are correct. Channel order doesn't matter for Parts 1–2.
