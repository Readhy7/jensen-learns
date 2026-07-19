# Week 4 Assessment — Average Deal Size (Transfer Test)

**This is a transfer test, not a reproduction.** Weeks 1–3 asked "what fraction were a success?" This one asks a **different question about a different kind of data** — you're averaging a *number*, not counting successes. The dictionary skeleton you know still applies, but you'll have to adapt *what* you accumulate, and deal with a wrinkle the earlier problems didn't have. Figuring out that adaptation is the whole point.

**Rules:** 60 minutes. No AI, including me. Python docs and web search allowed. Try it with your prior solutions **closed** — you've proven you know the pattern; the new parts are yours to work out. If you get stuck, run the unsticking ladder (error → print → narrate → shrink → docs → search → break) before asking. Write your solution in `solution.py` in this folder. When you finish or time runs out, stop, save, and say so.

## The data

`deals.txt` — one closed sales deal per line, format `rep,dealsize`:

```
bob,1000
alice,5000
carol,2000
```

Three reps — `bob`, `alice`, `carol` — mixed together. `dealsize` is the dollar value of that deal.

## What to build

**Part 1 — Overall average deal size.** Across every deal, print the average dollar value.

**Part 2 — Average deal size per rep.** For each rep, print the average size of *their* deals.

**Part 3 (stretch — only if time remains).** Print the reps sorted with the **highest** average on top (best closer first).

## Expected output (Parts 1–2)

```
Overall average deal size: 2400.0 (24000/10)
bob: 1000.0 (5000/5)
alice: 5000.0 (10000/2)
carol: 3000.0 (9000/3)
```

The two numbers in parentheses are the total dollars and the number of deals that went into each average. If your numbers match, Parts 1–2 are correct. Rep order doesn't matter for Parts 1–2.

## One heads-up

Think carefully about what `dealsize` *is* when you read it out of the file, versus what you need it to be in order to add and average it. If something misbehaves, that's your first clue — read the error, and print the thing to see what it actually is.
