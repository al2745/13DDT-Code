import time
import sys
from colorama import init, Style, Fore, Back

init(autoreset=True)

w = float(input("Enter your weight (kg): "))

h = float(input("Enter your height (m): "))

BMI = w / (h * h)

print(Fore.BLUE + f"Your body weight index: {BMI}" + Style.RESET_ALL)


def Calculation():
    if BMI > 0:
        if BMI <= 16:
            print(Fore.RED + "You are severely underweight." + Style.RESET_ALL)
        elif BMI <= 18.5:
            print(Fore.YELLOW + "You are underweight." + Style.RESET_ALL)
        elif BMI <= 25:
            print(Fore.GREEN + "You are healthy." + Style.RESET_ALL)
        elif BMI <= 30:
            print(Fore.YELLOW+ "You are overweight." + Style.RESET_ALL)
        else:
            print(Fore.RED + "You are severely overweight." + Style.RESET_ALL)
    else:
        print("Invalid data, please check details.")

Calculation()