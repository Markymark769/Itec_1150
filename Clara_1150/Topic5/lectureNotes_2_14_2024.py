"""
Mark
Dice roll
"""

import random


def main():
    number_of_dice = int(input('How many dice to roll? '))
    roll_dice(number_of_dice)  # call the roll_dice function
    print('That is all the dice')


def roll_dice(number_of_dice):
    # dice rolling code moved into a function with one parameter, the number of dice to roll
    # the function does not need to return anything
    for dice_counter in range(number_of_dice):
        dice_value = random.randint(1, 6)
        print(f'The dice rolled a {dice_value}')   # Optional TODO can you use the dice_counter to print messages like 'Dice 1 rolled a 5' ?


main()  # don't forget!