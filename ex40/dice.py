import random

coin = {
    "side1": "heads",
    "side2": "tails", 
}

def roll():
    rollA = random.randint(1,6)
    rollB = random.randint(1,6)
    print(f"""Die A shows a {rollA} and DieB shows a {rollB}.""")
    move = rollA + rollB
    print(f"You move {move} spaces.")
    return move
