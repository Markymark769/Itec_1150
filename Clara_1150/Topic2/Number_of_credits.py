"""
Mark Porraz
Number_of_Credits.py
1/16/2024

This program asks the user their name and how many credits they are taking at school
"""

# define variables
# assignment statement, uses input to ask question and store the answer in a new variable
# called username. Whatever the user types in will be stored in the username variable.
name = input('what is your name?')

# Ask for  number of credits as before but "wrap" the input in an int() function call
# to convert the data to an int() variable. Otherwise, it will be a string and we cannot work with
# strings
credit = input('how many credits are you taking this semester?')
# note: the int is numeric data, we need to do math
# or decide if this m=number is larger or smaller than another number,
# number_of_credits must be an int (or float) to do these

# print statement
# print(f'{name} is taking {credit} credits this semester')  # f-strings - more advanced
print(name + ' is taking ' + str(credit) + ' credits this semester')
# with print statements we cannot mix and match. Therefore, we can get around this by adding the str
# to it. We are making a copy of this data and then turning it into a string
# To be more precise, str(number_of_credits) makes a copy of number_of_credits and converts that to a string

# # new example of adding to the previous code
# if credit >= 12:  # conditional code - only runs if the condition is true
#     print(" you are taking at least 12 credits")
# else:
#     print("You are taking less than 12 credits")
#
# # student registers for another class
#
# # student registers for ITEC 1110 which is 2 credits
#
# credit = credit + 2
# print('y' + credit + '')
name = input('what is your name?')
upper_text = name.upper()
for letter in upper_text:
    print(letter)

