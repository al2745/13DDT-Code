import time
import sys

print("hi")

target = "Balin"

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
    lives = 3

    score = 0
    #question 1
    answer = input("How many planets are in the solar system? ")

    if answer == "8":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)
    
    #question 2
    answer = input("Whats the biggest island in the world? ")

    if answer == "Greenland":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)

    #question 3
    answer = input("What item is purchased most commonly at Walmart? ")

    if answer == "Banana":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)

    #question 4
    answer = input("Which bird has the largest wingspan? ")

    if answer == "Albatross":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)

    #question 5
    answer = input("What is the brightest star in the sky? ")

    if answer == "Sirius":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)

    #question 6
    answer = input("What does Ph.D stand for? ")

    if answer == "Doctor of Philosophy":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)

    #question 7
    answer = input("What is the most common toilet paper colour in France? ")

    if answer == "Pink":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)

    #question 8
    answer = input("What colour is a giraffe's tongue? ")

    if answer == "Blue":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)

    answer = input("What is the most common toilet paper colour in France? ")

    #question 9
    if answer == "Pink":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your score is:", score)
    print("Remaining lives:", lives)

    answer = input("What is the total number of dots on a pair of dice? ")

    #question 10
    if answer == "42":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry thats incorrect, you need to revise more.\n")
        lives -= 1
    print("Your final score is:", score, "/10")
    print("Remaining lives:", lives)
    
    if lives < 2:
        print("Wow, that was a close one!")

    if lives == 0:
        print("GG you lost!")
        sys.exit()

age = input("Enter your age: ")

if int(age) >= 18:
    print("Welcome to the program.")
    quiz()

else:
    print("Sorry, you are not old enough to access the program.")
    sys.exit()

input("Press Enter to close")