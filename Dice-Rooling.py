import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1, 6))
    playAgain = input("Do you want to play again? [y/n]")
    if playAgain == "y":
        continue
    else:
        print("Game Over")
        break