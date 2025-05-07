# Dungeon Crawler Project Report

## Section 1: Scenario Descriptions
This system implements multiple gameplay scenarios to enhance player experience and interaction with AI-driven mechanics.

### Combat Scenarios
- **Standard Attack**: Player rolls dice to determine damage dealt to an enemy.
- **Defensive Strategy**: Player opts to defend, mitigating incoming damage.
- **Flee Attempt**: Player tries to escape combat but may fail, leading to further encounters.
- **Dynamic Dialogue**: Player interacts with enemies using AI-generated responses.

### AI Interaction Scenarios
- **Contextual AI Responses**: Enemies respond dynamically based on player dialogue choices.
- **Adaptive Enemy Behavior**: Enemies choose attacks or defense strategically based on health.

### Reward Mechanics
- **Gold Distribution**: Player is awarded randomized gold amounts upon victory.

## Section 2: AI Method - Retrieval-Augmented Generation (RAG)
- Implemented in `dm_ai_tool.py` to generate dynamic enemy dialogues.
- Uses Deepseek-r1:1.5b for AI-driven contextual responses.

## Section 3: AI Method - Randomization Techniques
- `dice_gold_tools.py` utilizes random number generation for combat dice rolls (1-20) and gold rewards (10-100).
- Ensures variability in combat outcomes and rewards.

## Section 4: AI Method - Decision-Based Enemy Behavior
- `Fighting.py` includes AI logic for enemy decisions:
  - Random attack or defend choices.
  - Prioritization of defense when health is low.

## Section 5: AI Method - Server-Based Interaction
- `dndnetwork.py` enables turn-based interaction within the game framework.
- Designed to support multiplayer expansion in future iterations.

## Section 6: AI Method - Modular Game Design
- `Project_Main.py` integrates all components cohesively.
- Modular structure allows future scalability.

---

### Future Plans
- Expanding multiplayer capabilities.
- Refining AI interactions for enhanced immersion.
- Improving overall gameplay balance.
