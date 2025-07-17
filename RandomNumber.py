"""
Filename: RandomNumber
File-type: .py
Author: Andrei Alexandru
Date: 13.06.2022
About: A program that uses random module to generate a number in range 1 to 99 that asks the user to guess the
       number.
"""

# Importing random module.
import random

# List in range 1-99
n_list = list(range(1, 100))
# List that stores input numbers as integers
number = []
n = random.choice(n_list)


# Starting message
def main():
    print("Welcome to 'Guess the number'!")
    print("If you are feeling lucky, try to guess the number in less than 5 attempts!")


main()


# Function for invalid values.
def invalid_values():
    if not i.isnumeric():
        print("Invalid value!")
    else:
        if int(i) not in range(1, 100):
            print("Please insert a number between 1 and 100!")


# Function for values close to the number that needs to be guessed.
def input_value():
    if int(i) < n != int(i) and (n - int(i)) <= 10:
        print("Close, try a bit higher.")
    elif int(i) > n != int(i) and (int(i) - n) <= 10:
        print("Close, try a bit lower.")
    else:
        print("Keep trying!")


while True:
    # Declaring "i" as input.
    i = input(str("Enter your guess here: "))
    # If the condition is met the number is going to be inserted in "number" list.
    if i.isdigit() and int(i) in range(1, 100):
        number.append(int(i))
        l_num = len(number)
        # If the user guess the number of attempts is going to pop
        # along with a message that is asking the user if he wants to try again.
        if int(i) == n:
            print("Correct!")
            print("Your number of attempts is: {}".format(l_num))
            while True:
                answer = str(input("Try again? (y/n): "))
                # If the answer is "y" the program will restart.
                if answer == "y":
                    number.clear()
                    n = random.choice(n_list)
                    print("The number has been regenerated. Good luck!")
                    main()
                    break
                # If the answer is "n" the program will shut down.
                elif answer == "n":
                    print("Thank you for playing!")
                    quit()
                # If the answer is other than "y/n" the program will shut down.
                else:
                    if answer not in ("y", "n"):
                        print("Invalid value!")
        # If the input is not the correct number the following function will execute.
        else:
            input_value()
    # If the input is not a valid value the following function will execute.
    else:
        invalid_values()
