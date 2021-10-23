from operator import pos
import dice
from dice import roll, coin

Player1Pos = 1

print(f"Player 1 starts on square number {Player1Pos}. Now, roll the dice.")

P1move = roll()
Player1Pos = Player1Pos + P1move

print(f"You are now on spuare {Player1Pos}")

print(coin['side2'])