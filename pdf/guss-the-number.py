import random

randomNumber = random.randrange(1, 200)
#print(randomNumber)

guessthenumber = int(input("Please input a number what you guess and see the result!: "))

if guessthenumber > randomNumber:
    print("Hola! Your input number is grater then the guess number!")
    print("Guess number was:", randomNumber)
elif randomNumber > guessthenumber:
    print("Ah! your input number is too low, try again!")
    print("Guess number was:", randomNumber)
else:
    print("Wow! your are legend. Matched!")