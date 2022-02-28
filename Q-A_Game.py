from time import sleep
from sys import stdout

class Q:
    Q_count = 0

def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.03)
    print(" ")

def question_maker(Question, cor_ans):
    Q.Q_count += 1
    print_slow(f"\nQuestion No. {Q.Q_count}:")
    sleep(1)
    print_slow(f"{Question}")
    sleep(1.2)
    while True:
        user_ans = input("\nYour answer: ").lower()
        if user_ans in cor_ans:
            print_slow("\nCorrect answer!")
            sleep(1)
            print_slow("Let's move on to the next question.")
            sleep(1)
            break
        else:
            print_slow("Wrong answer, please try again.")
            sleep(1.2)

def no_more_questions():
    print_slow("\nOops, looks like that's all for now.")
    sleep(1)
    print_slow(f"You answered {Q.Q_count-1} questions so far.")
    sleep(1.2)
    print_slow("\nThank you for playing!")
    sleep(0.6)
    print_slow("\nThe script will now exit.")
    sleep(1)

print_slow("Welcome to a game under progress.")
sleep(1)
ready = input("Are you ready to play?(y/n): ").lower()

if ready == "y":
    question_maker("How many colours are there in the rainbow?", ["7", "seven"])
    question_maker("What is my name?", ["mubashir", "ahmed", "mubashir ahmed"])
    question_maker("How many days are there in a year?", ["365", "three sixty five", "three-sixty-five"])
    question_maker("What is the name of the highest peak/mountain?",["everest", "mount everest"])
    question_maker("Who is called the father of computers?", ["charles babbage"])
    no_more_questions()