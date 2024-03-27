#!/usr/bin/python3

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }


question = trivia["question"] 
A = html.unescape(trivia["incorrect_answers"][0])
B = html.unescape(trivia["incorrect_answers"][1])
C = html.unescape(trivia["correct_answer"])
D = html.unescape(trivia["incorrect_answers"][2])


def main():
    answer = input(f"{question}\nA: {A} \nB: {B} \nC: {C} \nD: {D} \nEnter answer here: ").upper()
    print(f'{C} is the correct answer!')

    if answer == "C":
        print("You are correct! Great job!")

    else:
        print("Sorry! Please Try again!")

main()