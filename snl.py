import random


position = 1
print("You are on square ", position)

def roll_die():
    i = random.randint(1,6)
    print("You rolled a ", i)
    return i

def move(roll_die, position):
    position = roll_die + position
    print(f"Move forward {roll_die} space(s), to square {position}.")
    return position

roll_die()
print(position)
