print("Welcom to Choose your own adventure Game")
playing = input("Do you want to play? ")
if playing != "yes":
    quit()
else:
    name = input("Please enter your name: ")
    print(f"Welcome {name} to this adventure!")
    answer = input("Your on a dirt road and at the end of the road two ways are there left and right road, where do you want to go? options \n right or left ").lower().strip()
    if answer == "right":
        answer = input("Now you came to a forest, you want to walk around it or walk through it? options \n around or through ")
        if answer == "around":
            print("you walked miles and you lost your way lost the game")
        elif answer == "through":
            print("Yay! Tarzan helped you cross the forest and you won the game")
        else:
            print("Not a valid option, You lose!")
    elif answer == "left":
        answer = input("You came to a river, you can walk around the river or swim through it. options \nswim or walk ")
        if answer == "swim":
            print("You swam through the reiver and eaten by the alligator. you lost the game")
        elif answer == "walk":
            print("Yay! You met Dora the explorar and had an wonderful adventure with her. you won the game")
        else:
            print("Not a valid option, You lose!")
    else:
        print("Not a valid option, You lose!")