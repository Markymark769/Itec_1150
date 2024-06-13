# Slide 7
# inputChoice()Ensures the user enters one of the provided choices
# Adding a default and a limit parameter
# Test with good and bad data

import pyinputplus as pyip
myChoice = pyip.inputChoice(['Apple', 'Pomegranate', 'Tea-leaf'], default="BANANA", limit=2)
print('My choice is: ', myChoice)


