"""Mark Porraz, 2/12/2023
Homework 2_2, Yourname2."""

## This program runs an infinate loop until the user types the following:
"""you name"""

### a break statement is added

while True:
    print('Please type your name:')
    name = input()
    if name == 'your name':
        break
print('Thank you!')