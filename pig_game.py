import random

def roll():
    return random.randint(1, 6)

while True:
    players = input("Enter the number of the players 2-4: \n")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a valid number 2 - 4")
    else:
        print("Please enter a number")
max_score = 15
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for i in range(len(player_scores)):
        if max(player_scores) < max_score:
            while True:
                r = input(f"Player {i+1} Do you want to roll? enter 'y': ").lower().strip()
                if r == "y":
                    num = roll()
                    print("itssss: ", num)
                    if num != 1:
                        player_scores[i] = num + player_scores[i]
                        print(f"Player {i+1} current score is: \n", player_scores[i])
                        if player_scores[i] >= max_score:
                            print(f"Player {i+1} won the game")
                            break
                    else:
                        print("Oops! You rolled a 1 so turn done")
                        player_scores[i] = 0
                        print(f"Player {i+1} current score is: \n", player_scores[i], "\nNext player: \n\n")
                        break
                else:
                    print(f"Player {i+1} current score is: \n", player_scores[i], "\nNext player: \n\n")
                    break
        else:
            break