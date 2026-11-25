# One-Line Laugh-Off

[![make.fun · u-zkhiel-one-line-laugh-off-714618ae](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/DizellaCapital/u-zkhiel-one-line-laugh-off-714618ae/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/DizellaCapital/u-zkhiel-one-line-laugh-off-714618ae/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)

One funny line that lands on a cold read — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The line

> **At 6:47 a.m., Grandma's voicemail from 2019 played on the old Nokia, 'water the plant, love,' so I watered the empty pot again; dead four years, and still the only thing I've never disappointed.**

A scene, not a quip: a time anchor (6:47 a.m.), a named person (Grandma) and two concrete objects (the old Nokia, the empty pot), and a final clause that reframes the whole line — the plant has been dead four years, yet watering it is the one chore the narrator has never failed. Bittersweet, specific, and impossible to mistake for a generic joke.

## How it works

`main.py` (stdlib only) writes the line to `MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), validates it is a single line of 1–200 characters and at most 200 bytes, and verifies the write by reading it back. The entry is exactly 194 characters / 194 bytes, with no trailing newline.

```sh
python3 main.py
```
