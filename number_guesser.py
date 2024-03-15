import random

print("Welcome to Number Guesser")

playing = input("Do you want to play? ")

if playing.lower().strip() != "yes":
    quit()

else:
    start = 0

    while True:
        end = input("Enter a number range")
        if end.isdigit():
            end = int(end)
            if end>0:
                break
            else:
                print("Please enter a number larger than zero")
        else:
            print("The entered value is not a number, please enter a number")

    num_guess = 0
    num = random.randrange(start, end)

    if num <= end and num >= start:
        while True:
            num_guess += 1
            guess = input(f"Guess the number between {start} to {end} ")
            if guess.isdigit():
                guess = int(guess)
            else:
                print("The entered value is not a number, please enter a number")
                continue

            if guess > num:
                print("lower than your quess")
            elif guess < num:
                print("Higher that your guess")
            else:
                print("Yay! correct guess")
                break

print(f"You got the answer in {num_guess} guesses")