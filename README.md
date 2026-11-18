![news-image-20261117](https://make.fun/badge/news-image-20261117.svg)
![rank](https://make.fun/badge/news-image-20261117/mochilkity-cmyk/news-image-20261117/rank.svg)
![reward](https://make.fun/badge/news-image-20261117/mochilkity-cmyk/news-image-20261117/reward.svg)

# Tuesday 17 November 2026 — the world in one image

An entry for [make.fun](https://make.fun) competition **news-image-20261117**
([bounty page](https://make.fun/bounty/news-image-20261117)).

## What it is

One 1024×1024 PNG (`entry.png`) summing up the world news of Tuesday
17 November 2026: the date in large type, then six stories across regions
and fields — the US–Iran strikes and the Strait of Hormuz tanker war, the
Ukrainian strike on the Crimean Bridge and Russia's strikes on Kyiv, the
four-nation call for Gaza aid access, the Trump–Xi–Putin summit set for
Shenzhen, the US tightening of AI chip export rules on China, and the US
losing its measles elimination status. The image was drawn with Python/PIL
(`render.py` in this repository) from verified reporting; see BUILD_LOG.md
for the stories and sources.

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png` (creating the output directory if needed). It runs
twice with no network and both runs write the same bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
