import random
import dice_gold_tools  # Import the gold rolling tool

def enemy_turn():
    """Enemy randomly chooses between 'attack' or 'defend'."""
    return random.choice(["attack", "defend"])

def player_turn():
    """Prompt the player until a valid move is chosen."""
    valid_moves = ["attack", "defend", "flee", "talk"]
    while True:
        move = input("Choose your move (attack, defend, flee, talk): ").strip().lower()
        if move in valid_moves:
            return move
        else:
            print("Invalid move. Please choose from attack, defend, flee, or talk.")


def combat_round(player_move, enemy_move, enemy_hp, player_hp):
    """
    Process one round of combat and update HP values dynamically using dice rolls.
    
    Returns:
        Updated enemy_hp, player_hp, a result message, and a flag if the player fled.
    """
    result_message = ""

    # 🎲 Roll dice for attack damage
    player_attack_damage = dice_gold_tools.roll_d20()  # Randomized player damage
    enemy_attack_damage = dice_gold_tools.roll_d20()  # Randomized enemy damage
    half_damage = player_attack_damage // 2  # Half damage for successful defense

    # Evaluate the player's move.
    if player_move == "attack":
        if enemy_move == "attack":
            enemy_hp -= player_attack_damage
            player_hp -= enemy_attack_damage
            result_message += f"Both you and the enemy attack fiercely! You deal {player_attack_damage} damage, but take {enemy_attack_damage} in return! "
        elif enemy_move == "defend":
            enemy_hp -= half_damage
            result_message += f"You attack, but the enemy defends and reduces the impact! You deal only {half_damage} damage. "
    elif player_move == "defend":
        if enemy_move == "attack":
            player_hp -= half_damage
            result_message += f"You defend against the enemy's attack, taking reduced damage ({half_damage}). "
        elif enemy_move == "defend":
            result_message += "Both defend cautiously. No damage is dealt this round. "
    elif player_move == "flee":
        # Flee has a 50% chance to succeed.
        if random.random() < 0.5:
            result_message += "You successfully flee from the battle! "
            return enemy_hp, player_hp, result_message, True
        else:
            # On failed flee, enemy lands a free attack.
            player_hp -= enemy_attack_damage
            result_message += f"You failed to flee! The enemy capitalizes with a free attack, dealing {enemy_attack_damage} damage! "
    elif player_move == "talk":
        # Talking might confuse the enemy—simulate a chance to weaken them.
        if random.random() < 0.4:
            enemy_hp -= 3
            result_message += "Your words pierce the enemy's resolve, weakening them (-3 HP). "
        else:
            result_message += "Your attempt to talk falls on deaf ears. "

    # If not processing flee or if enemy attacked already, check enemy move.
    if player_move not in ["flee", "talk"]:
        if enemy_move == "attack" and player_move == "talk":
            player_hp -= enemy_attack_damage
            result_message += f"While you try to talk, the enemy attacks! You take {enemy_attack_damage} damage! "

    return enemy_hp, player_hp, result_message, False


player_gold = 0  # Initialize player's gold

def combat():
    """Main combat function with gold rewards."""
    global player_gold  # Track gold across combat sessions
    print("\nAn enemy fighter approaches! Prepare for battle!")
    
    enemy_hp = 20
    player_hp = 30

    while enemy_hp > 0 and player_hp > 0:
        print(f"\nYour HP: {player_hp} | Enemy HP: {enemy_hp} | Gold: {player_gold}")
        player_move = player_turn()
        enemy_move = enemy_turn()
        print(f"Enemy chooses to {enemy_move}!")
        enemy_hp, player_hp, outcome, fled = combat_round(player_move, enemy_move, enemy_hp, player_hp)
        print(outcome)
        
        if fled:
            print("You escaped the battle but gained no gold.")
            return
    
    if player_hp <= 0:
        print("\nYou have been defeated in battle!")
        return
    
    elif enemy_hp <= 0:
        print("\nEnemy defeated!")
        
        # 🎲 Roll for gold reward using dice_gold_tools
        gold_earned = dice_gold_tools.random_gold()  # Use the function from dice_gold_tools.py
        player_gold += gold_earned
        
        print(f"You loot {gold_earned} gold from the defeated enemy! You now have {player_gold} gold.")

        # Ask if the player wishes to fight another enemy.
        while True:
            replay = input("Do you want to fight another enemy? (yes/no): ").strip().lower()
            if replay in ["yes", "y"]:
                combat()  # Start combat again recursively.
                break
            elif replay in ["no", "n"]:
                print("You decide to rest and recover. Victory is yours for now!")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")


if __name__ == "__main__":
    combat()
