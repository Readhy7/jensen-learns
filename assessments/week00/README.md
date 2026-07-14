# Week 0 — Baseline Assessment: Word Frequency Counter

**Rules:** 60 minutes. No AI of any kind (no Claude, no Copilot, no ChatGPT). Python documentation and web search are allowed — reading explanations is fine, copying solution code is not. Write your solution in `solution.py` in this folder. When time is up, stop, commit whatever you have, and report back honestly.

This is a *baseline* — a low score is expected and useful. Its only job is to mark the starting point.

## The problem

Write a program that reads a text file and reports the most common words.

**Part 1 (core):** Read `sample.txt` (in this folder). Count how many times each word appears:
- Case-insensitive ("The" and "the" are the same word)
- Ignore punctuation attached to words ("dog." and "dog" are the same word)

**Part 2 (core):** Print the 5 most common words, one per line, in the format `word: count`, most frequent first. If two words have the same count, order those alphabetically.

**Part 3 (stretch — only if time remains):** Let the user run it as `python solution.py <filename> <N>` to choose the file and how many top words to show, defaulting to `sample.txt` and 5.

## Expected output for sample.txt (Parts 1–2)

```
the: 7
sales: 4
model: 3
data: 2
evaluation: 2
```

If your output matches, Parts 1–2 are correct.
