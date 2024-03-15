print("Welcome to computer quiz!")

playing = input("Do you want to play? ")
score = 0
if playing.lower().strip() != "yes":
    quit()
else:
    print("Okay! Let's play")
    questions = [
        "What does the CPU stands for? ",
        "What does the GPU stands for? ",
        "What does the RAM stands for? ",
    ]
    answers = [
        "central processing unit",
        "graphic processing unit",
        "random access memory"
    ]

    for i, q in enumerate(questions):
        answer = input(q)
        if answer == answers[i].lower().strip():
            print("Yay! you are correct, two more questions to go")
            score += 1
        else:
            print("Oops! wrong answer")

    print(f"You have scored {score} out of {len(questions)} and that is {(score/len(questions))*100}% out of 100%")