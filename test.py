import time
import sys

print("hi")

target = "balin"

name = input("What is your name? ")

if name == target:
    print("Hi balin you're not very tuff.")
    time.sleep(1.2)
    print("but...")
    time.sleep(1.2)
    print("you are still loved")
else:
    print("Hi", name, "you're so cool.")


def quiz():
    score = 0

    answer = input("How many planets are in the solar system? ")

    if answer == "8":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")

    print("Your score is:", score)


age = input("Enter your age: ")

if int(age) >= 18:
    print("Welcome to the program.")
    quiz()

else:
    print("Sorry, you are not old enough to access the program.")
    sys.exit()

input("Press Enter to close")