answer = input("Are you interested to play quize game? [Yes/No]")

if answer == "Yes":
    print("Welcome to the Game!")
    answer = input("Let's chose the pattern. Which animal you like? [Tiger/giraf]")
    if answer == "Tiger":
        print("Tiger can eat you so be carefull...")
        answer = input("Which way you would like to go? [Jangle/Road]")
        if answer == "Jangle":
            print("This is more dangerus way! You are already dead")
        elif answer == "Road":
            print("You are save and win as Road is safe way!")
    elif answer == "giraf":
        print("Giraf is nice animal")
else:
    print("You have closed the game. Thanks")