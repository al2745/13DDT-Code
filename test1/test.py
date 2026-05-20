import time
import sys
from colorama import Fore, Style, init

print(Fore.YELLOW + "Welcome to the Game Centre!\n" + Style.RESET_ALL)
target = "Balin"

print("Please answer the following questions:")
name = input("What is your name? ")

if name == target:
    print("Hi Balin, you're not on our list.") #there is no list balin
    time.sleep(1.2)
    print("which means...")
    time.sleep(1.2)
    print("you are not allowed on the program.")
    sys.exit()
else:
    print("Hi", name, "you have been found on our list.")


def quiz():
    lives = 3
    heart = "❤︎"
    score = 0
    print(f"Current Lives: {heart * lives}")
    #question 1
    answer = input(Fore.RED + "How many planets are in the solar system? " + Style.RESET_ALL)

    if answer == "8":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: 8\n")
        print("You need to revise more.\n")
        lives -= 1

        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")
    
    #question 2
    answer = input(Fore.RED + "Whats the biggest island in the world? " + Style.RESET_ALL)

    if answer == "Greenland":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: Greenland\n")
        lives -= 1

        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")

    #question 3
    answer = input(Fore.RED + "What item is purchased most commonly at Walmart? " + Style.RESET_ALL)

    if answer == "Banana":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: Banana\n")
        lives -= 1

        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")

    #question 4
    answer = input(Fore.RED + "Which bird has the largest wingspan? " + Style.RESET_ALL)

    if answer == "Albatross":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: Albatross\n")
        lives -= 1

        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")

    #question 5
    answer = input(Fore.RED + "What is the brightest star in the sky? " + Style.RESET_ALL)

    if answer == "Sirius":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: Sirius\n")
        lives -= 1

        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")

    #question 6
    answer = input(Fore.RED + "What does Ph.D stand for? " + Style.RESET_ALL)

    if answer == "Doctor of Philosophy":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: Doctor of Philosophy\n")
        lives -= 1

        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")

    #question 7
    answer = input(Fore.RED + "What is the most common toilet paper colour in France? " + Style.RESET_ALL)

    if answer == "Pink":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: Pink\n")
        lives -= 1


        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")

    #question 8
    answer = input(Fore.RED + "What colour is a giraffe's tongue? " + Style.RESET_ALL)

    if answer == "Blue":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: Blue\n")
        lives -= 1

        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")

    #question 9
    answer = input(Fore.RED + "Who invented the word vomit? " + Style.RESET_ALL)

    if "Shakespeare" in answer:
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer had to include: Shakespeare\n")
        lives -= 1

        if lives <= 0:
            print("GG you ran out of lives!")
            quit()
    print("Your score is:", score)
    print(f"Lives: {heart * lives}")

    #question 10
    answer = input(Fore.RED + "What is the total number of dots on a pair of dice? " + Style.RESET_ALL)

    if answer == "42":
        print("Congrats on getting the correct answer!\n")
        score += 1
    else:
        print("Sorry, the correct answer was: 42\n")
        lives -= 1
        print(f"Lives: {heart * lives}")
        
        if lives <= 0:
            print("GG you ran out of lives!" + Style.RESET_ALL)
            quit()
    print('Loading')
    for i in range(3):
        time.sleep(.5)
        sys.stdout.write('.')
        sys.stdout.flush()
    print(Fore.BLUE + "\nYour final score is:", score, "/ 10" + Style.RESET_ALL)
    print(f"Lives: {heart * lives}")
    
    if lives == 3:
        print("Perfect score and no mistakes! Well done!" + Style.RESET_ALL)

    if lives == 1:
        print("Wow, that was a close one!" + Style.RESET_ALL)

age = input("Enter your age: ")

if int(age) >= 18:
    print(Fore.BLUE + "Welcome to the program. Answers are case sensitive, answer with the first letter in capital. If an answer has multiple words, answer the important words in capital." + Style.RESET_ALL)
    quiz()

else:
    print("Sorry, you are not old enough to access the program.")
    sys.exit()

while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input.lower() == "exit":
        print("Closing program...")
        time.sleep(3)
        break
    sys.exit()
