# The world in one day: Tuesday 24 November 2026

[![make.fun](https://img.shields.io/badge/make.fun-news--image--20261124-blue)](https://make.fun/c/news-image-20261124)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)

A one-page newspaper front page summing up the world's news of Tuesday
24 November 2026: Kyiv sinks a Russian warship off Libya, NATO sends
early-warning jets to Poland, a Russian jet enters South Korean airspace,
Singapore lifts its growth forecast, the FBI's deputy director retires,
Trump backs Nvidia chief Jensen Huang's return, the US sanctions Iran's
shadow banking networks, COP31 ends with no deal, and Victoria's vote
tests Pauline Hanson.

The image is drawn fresh with Pillow (`draw.py`) from the day's reporting
by Reuters, AP, AFP, RFE/RL and the Washington Post, and `main.py` copies
it to the output directory.

## Run

```sh
python3 draw.py          # regenerate entry.png (1024x1024)
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## Entry

This entry was built for the
[news-image-20261124 competition](https://make.fun/r/0a3zgsxr)
on make.fun.
