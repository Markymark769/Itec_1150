"""
Mark Porraz
2/14/2024

"""

# imports from the random library code, which is built into python but not in the program
# a library is a collection of functions taht have already been written that we can
# use in our program
import random  # this adds the ability to generate random numbers to our program


number_of_dice = int(input('How many dice to roll? '))


# todo move the dice rolling code into a function with one parameter, the number of dice to roll

# the function does not need to return anything
# Loop here, based on the number the user enters.
# repeats once for each dice roll. if the user enters 4 then loop repeats 4 times.
# with loops we have to think about how many times to repeat AND what is the task that is repeated?
for dice_counter in range(number_of_dice):  # this controls how many times to repeat

    dice_value = random.randint(1, 6)  # this line is picking the random number
# random is used from the import, randint means random integer
    # input function argument is the 1 and the ending argument is 6
    # the smallest number we want is 1 and the largest number is 6 we want to generate
    print(f'The dice rolled a {dice_value}')  # Optional TODO can you use the dice_counter to print messages like 'Dice 1 rolled a 5'

# this is after the loop - not intended, only runs one time
print('That is all the dice')