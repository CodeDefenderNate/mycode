#!/usr/bin/python3

round = 0
answer = " "

while round < 3 and (answer != "Brian" and answer != "Shrubbery"):
    round += 1        # increases round count by 1
    answer = input("Finish the movie title, \"Monty Python's The life of ____: ")
    answer = answer.capitalize() # this line will make all user input start with uppercase
    if answer == "Brian":  # checks for correct answer
        print("Corect!")
    elif answer == "Shrubbery":
        print("You gave the super secret answer!")
    elif round == 3:  # makes sure the round hasn't reached 3
        print("Sorry, the answer is Brian.")
    else:             # if the answer is wrong
        print("Sorry! Try again!")
