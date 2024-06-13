"""
Mark Porraz, 4/9/2023, idiot.py
This program runs a loop created by the while true statement.
"""

import pyinputplus as pyip
# This part imports pyinputplus, we use pyip for short due to pyinputplus being long

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
# The while True statement creates an infinate loop, that will go until the break
    # statement is encountered. we call pyip.inputYesNo() to ensure that this function call
    # won’t return until the user enters a valid answer
    if response == 'no':
        break
# the string keeps running in a loop until the user enters no to break out of loop.

print('Thank you, have a nice day.')
