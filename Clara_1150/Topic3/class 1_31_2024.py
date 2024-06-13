"""Do you have a dollar?

Write a program that asks the user how many cents they have.

If they have less than a dollar's worth of cents, print the message 'you have less than a dollar'.
If they have exactly 100 cents, print the message 'you have exactly one dollar'
If they have more than 100 cents, print the message 'you have more than one dollar'

"""

# The number of cents is a number, and it's a whole number, so convert to int
cents = int(input('How many pennies do you have? '))

# There are three possible outcomes to choose between so use if elif else
# you can check in any order, so check if less than, elif equal to, else more than is also correct

# check if cents is more than 100 (so not 100 or more, actually more than 100)
if cents > 100:
    print('you have more than one dollar in cents.') # this only happens if cents is more than 100
elif cents == 100:  # next check if cents is exactly equal to 100, make sure to use == not =
    print('You have exactly one dollar in cents.')  # this only happens if cents is exactly 100
else:
    # if neither of the above are true, then the user must have less than 100. (they don't have more and the don't have exactly 100)
    # so the else block code runs. Don't need to write another condition after the word else.
    print('You have less than one dollar in cents.')

# Q2
# Collect data from user. Numerical data needs to be converted to a number data type, for example int
# float would work too, and support ages like 30.5
# ask 4 question - age as a number (int of float), citizenship time as a number (int or float)
# and the state of residence and state they want to be senator of.

age = int(input('What is your age? '))
years_of_citizenship = int(
    input('How many years have you been a US citizen? If you are not yet a US citizen, enter 0: '))
state_of_residence = input('What state do you live in? ')
state_represent = input('What state do you want to be the senator of? ')

# check if the user's age is greater or equal to 30
# AND the years of citizenship is greater or equal to 9
# AND the state they live in is equal to the state they want to represent

# There's an example in the last lectuer v

if age >= 30 and years_of_citizenship >= 9 and state_of_residence == state_represent:
    print('Congratulations! You are eligible to be a senator of ' + state_represent)
else:
    print('Sorry, you are not eligible to be a senator.')