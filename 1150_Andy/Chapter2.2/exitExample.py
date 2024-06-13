"""Mark Porraz, 2/12/2023
Homework 2_2, exit Example."""
# This program prints exit to exit or loop will continue.
# The program repeats back to the user what they typed.


# import sys function
#

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')