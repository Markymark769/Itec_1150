"""
inputStr() function accepts string inputs and provides
parameters such as prompt, blank, blockRegexes, and allowRegexes.
Experiment with the following.
See what is accepted and what is rejected. Edit and play with it.

"""
# Example 1
# this example only accepts capital letters, blanks, and words w/o aeiouy (brr,grr,pfft)
# import pyinputplus as pyip   # string input with additional parameters
# myString = pyip.inputStr(prompt="Enter a string... ", blank=True, blockRegexes='aeiou', allowRegexes='AEIOUY')
# print('My string:', myString)



 # Example 2
# #Experiment with the following function parameters:
# The default parameter is used to set the default value if time runs out or
# the number of tries is exceeded. The limit parameter is used to specify
# the maximum number of tries the user has for entering a valid input.

import pyinputplus as pyip
myInput = pyip.inputStr(prompt = "Enter an string... \n ", default = "A", limit = 2)
print('My default if left blank:' , myInput)

