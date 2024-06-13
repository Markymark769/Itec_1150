# inputNum() Ensures the user enters a number and returns an int or float,
# depending on if the number has a decimal point in it
# inputInt() function is used to accept integer inputs
# inputFloat() function is used to accept float inputs

# Example 1
# this example repeats back to the user the integer they put in
# import pyinputplus as pyip
# myInt = pyip.inputInt(prompt="Enter a integer... ")
# print('My integer is:', myInt)

# Example 2

# almost the same as the previous example
# uses the variable myNum instead

# import pyinputplus as pyip
# myNum = pyip.inputNum(prompt="Enter a number... ")
# print('My number is:', myNum)

# Example 3
# this example uses a float to repeat back to the user

# import pyinputplus as pyip
# myFloat = pyip.inputFloat(prompt="Enter a float... ")
# print('My float is: ', myFloat)

# Example 4
# Experiment with the min and max parameters to set lower and upper bounds.
# The greaterThan and lessThan parameters are used to set the
# external bounds:

import pyinputplus as pyip
myInt = pyip.inputInt(prompt="Enter an Integer... ",
                      min=3, lessThan=20)   # a range from 3 to 19
print("My integer within range:", myInt)



