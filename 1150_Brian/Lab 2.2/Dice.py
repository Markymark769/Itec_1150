"""
Mark Porraz
Dice.py

In this program we are modifying some code provided;
1) it rolls two dice at the same time,
2) prints both die values on the same line. The program should let the user
roll the dice as many times as they want, until they want to quit.
3) congrats you rolled a double -->> extra points!!

code to modify:

import random
want_to_quit = "" # Empty strings are False

while not want_to_quit:
    dice_value = random.randint(1, 6)
    print("You rolled a " + str(dice_value))
    # Not typing anything and pressing <ENTER> will return an empty string
    want_to_quit = input("Press <ENTER> to roll again, any other key to quit ")

"""

import random

#want_to_quit = " "  # Empty strings are False
# this variable is set to quit the program by setting an empty string.

while True:
    want_to_quit = ''  # if the user does not want to quit, run the program
    # step 1
    dice_value1 = random.randint(1, 6)  # first dice roll value
    dice_value2 = random.randint(1, 6)  # second dice roll value

    # step 2
    print(f'You rolled a {dice_value1} and a {dice_value2}')
    # print("You rolled a " + str(dice_value1))
    # print("You rolled a " + str(dice_value2))

    # step 3
    if dice_value1 == dice_value2:
        print('congrats you rolled a double -->> extra points!!')

    else:
        print()
        # Not typing anything and pressing <ENTER> will return an empty string
        want_to_quit = input('Press <ENTER> to roll again, any other key to quit')


# this program needs an if else statement, if we roll a die --> show the values
# else we quit the program
