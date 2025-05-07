import random

def roll_d20():
    """
    Roll a 20-sided die and return the result (an integer between 1 and 20).
    """
    return random.randint(1, 20)

def random_gold(min_gold=10, max_gold=100):
    """
    Return a random amount of gold between min_gold and max_gold.
    
    By default, this function returns an amount between 10 and 100.
    You can adjust the range by passing different values.
    """
    return random.randint(min_gold, max_gold)

# Additional helper: you might want to roll multiple dice at once.
def roll_multiple_dice(num_dice, sides=20):
    """
    Roll the specified number of dice with the given number of sides.
    Returns a list of results.
    
    :param num_dice: The number of dice to roll.
    :param sides: The number of sides on each die. Defaults to 20.
    """
    return [random.randint(1, sides) for _ in range(num_dice)]

if __name__ == "__main__":
    # Example usage
    print("Rolling one d20:", roll_d20())
    print("Rolling three d20s:", roll_multiple_dice(3))
    print("Random gold amount:", random_gold())
