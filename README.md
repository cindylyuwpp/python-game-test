# Gaming Test

Python practice project: data analysis and simple games built on CSV data.

## Files

- `creatures.csv` – made-up creature stats (name, type, HP, attack, defense, speed, rarity)
- `creature_game.py` – data practice (filter, sort, group) plus a random creature battle
- `ai_usage_log.csv` – log of my AI image/video model usage (Firefly, Nano Banana, GPT Image, Gemini Omni Flash, Runway Gen-4)
- `analyze_usage.py` – analysis of my AI usage: most-used models, ratings, keep rate, credits

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```
python creature_game.py
python analyze_usage.py
```

## Ideas for later

- Let the player pick a creature with `input()`
- "Model Battle" and "Guess the Model" games using my AI usage data
- Connect to Firefly to log usage automatically
