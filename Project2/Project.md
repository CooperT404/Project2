# Dungeon Crawler Project Report

## Overview
This project expands upon a base server to create a dungeon crawler game with a structured combat system and interactive AI-driven dialogues.

## Files and Their Functions

### `dice_gold_tools.py`
- Generates gold and rolls dice for combat outcomes.
- Uses random number generators:
  - Gold: between 10 and 100 (awarded after defeating an enemy).
  - Dice: between 1 and 20 (rolled during combat).

### `Fighting.py`
- Core combat system, offering the player four choices:
  1. **Attack** – Uses dice roll to determine damage (1 to 20).
  2. **Defend** – Prevents damage for the turn.
  3. **Flee** – Allows escape but may fail, leading to future encounters.
  4. **Talk** – Uses `dm_ai_tool.py` for dynamic interactions.

- Enemy AI:
  - Chooses between attacking or defending, prioritizing defense as health decreases.
  - Gold is awarded upon victory.

### `dm_ai_tool.py`
- Uses a Retrieval-Augmented Generation (RAG) network alongside the server system for text responses.
- AI Model: Deepseek-r1:1.5b, allowing dynamic dialogues.
- Planned server integration for multiplayer interactions (stretch goal).

### `dndnetwork.py`
- Modified server starter to support turn-based mechanics.

### `Project_Main.py`
- Main entry point calling all other modules.
- Initially designed for multiplayer but currently modified for solo play.
- Commands:
  - `/combat` – Starts a fight.
  - `/quit` – Ends the program.

## Future Improvements
- Implementing multiplayer interactions.
- Enhancing AI dialogue depth.
- Refining game mechanics based on player feedback.




