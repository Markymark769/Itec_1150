"""
Mark Porraz
DAte: 2/5/2024
some program.py

This program explains the while true statments of a function
"""

while True:
    try:
        n1 = float(input('Enter your number, int or float: '))
    except ValueError:
        print('When I ask for a number, give me a number.')
    else:
        break
print("your number is: ", n1)



 # try two decimal points
 # try hyphen at the end of a number
 # big numbers
 # small numbers
# Greetings Python People!
# Here are 2 simple validation functions that will help you in you mipo based programs:

def int_check(number): # add comments
    if number.isnumeric() is True:
        return True
    else:
        return False

def float_check(number): # add comments
       try:
           number = float(number)
           return True
       except ValueError:
           return False
# In the Area program (for example), you might do the following to get an integer, calling one of those functions:

width = input('Enter width: ')
while int_check(width) is False:
    print("Width must be an integer")
    width = input('Try again: ')
else:
    width = int(width)

# or you might do this to get a float:

height = input('Enter height: ')
while float_check(height) is False:
    print("Height must be an float or integer")
    height = input('Try again: ')
else:
    height = float(height)
