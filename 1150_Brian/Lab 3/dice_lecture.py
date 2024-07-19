"""
Mark Porraz
Examples from class
"""

# example 1
import random

number_of_dice = int(input('How many dice to roll? '))
number_of_sides = int(input('How many sides per die?'))
print(f'About to roll {number_of_dice} and {number_of_sides}')

for dice in range(number_of_dice):
    dice_value = random.randint(1, number_of_sides)
    print(dice_value)

