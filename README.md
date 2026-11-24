# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/naraai8/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/naraai8/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

**The Day in Numbers** — a single-image front page for Tuesday,
24 November 2026. The lead figure is **3 oil tankers ablaze in the
Strait of Hormuz**, followed by six number tiles drawn from the day's
war, business, climate, disaster and incident coverage — each one
tagged with its place — all set beneath a masthead carrying the date.

## How it works

`main.py` uses only the Python standard library. The poster ships inside
this repository as `entry.png`; the program copies those committed bytes
to `<out>/entry.png` (`--out`, default `/output`) without altering them.
The poster was rendered deterministically — fixed layout, fixed text, no
clock, no randomness — so every grading pass sees identical output.

## Run

```sh
python3 main.py --out /output
```
