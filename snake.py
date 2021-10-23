import random

def roll_dice():
    i = random.randint(1,6)
    j = random.randint(1,6)
    #print(f"You have rolled a {i} and a {j}.")
    return i, j

roll_dice()