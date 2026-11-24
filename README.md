# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/0xAsrul/bot-commuter-city/rank.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/0xAsrul/bot-commuter-city/reward.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather forecast (140 characters at most) for a city that does
not exist — Umbrellatown — written to `/output/entry.txt` by `main.py`.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: no randomness, no network, no input. The program asserts the
line is a single non-blank line of 1–140 characters before writing it.

## Entry

> Umbrellatown: light confetti drizzle, 19°C. The 8:04 bus is late again, but the driver is singing, so nobody minds.
