import random

print("Welcome to ROCK, PAPER, SCISOR Game")

playing = input("Do you want to play? ")

if playing.lower().strip() != 'yes':
    quit()
else:
    while True:
        rounds = input("Please enter maximum points in number ")
        if rounds.isdigit():
            rounds = int(rounds)
            break
        else:
            print("entered value is not a number")
    sps = ['rock', 'paper', "scissor"]

    comp_win = 0
    user_win = 0
    while True:
        if comp_win != rounds and user_win !=rounds:
            comp_input = sps[random.randint(0,2)]
            user_input = input("Enter rock, paper, scisor or q to quit ").lower().strip()
            if user_input not in sps:
                print("Please enter a valid option")
                continue
            if user_input == comp_input:
                print("Draw! no points")
                continue
            elif user_input == "paper" and comp_input == "rock":
                print(f"me: {comp_input} \nyou: {user_input} \nYay! you won one point")
                user_win +=1
            elif user_input == "rock" and comp_input == "scissor":
                print(f"me: {comp_input} \nyou: {user_input} \nYay! you won one point")
                user_win +=1
            elif user_input == "scissor" and comp_input == "paper":
                print(f"me: {comp_input} \nyou: {user_input} \nYay! you won one point")
                user_win +=1
            elif user_input == 'q':
                break
            else:
                print(f"me: {comp_input} \nyou: {user_input} \nI won one point")
                comp_win +=1

        elif comp_win > user_win:
            print(f"Sorry! you lost. {comp_win} points for me and {user_win} points for you")
            break
        else:
            print(f"Yay! you won. {comp_win} points for me and {user_win} points for you")
            break

print("Thank You for playing, GoodBye!")