"""
Mark Porraz
dollar.py
1/16/2024

This program asks the user if they meet the following qualifications to be a senator:

Article I, Section 3 of the United States Constitution sets out three qualifications for senators:
(1) they must be at least 30 years old,
(2) they must have been citizens of the United States for at least the past nine years, and
(3) they must live in the state they seek to represent at the time of their election.
"""

# define variables
state = input('What is the state you want to be a senator in?')
age = int(input('what is your age?'))
us_citizen = int(input('Have you been a citizen of the US for at least 9 years?'))
current_state = input('what is the state that you currently live in?')

# validation


# print statements
while True:
    if age >= 30:  # and -----# and
        print('You meet the requirement of being at least 30 years old.')
    else:
        print('You do not meet the requirement of being at least 30 years old.')

    if us_citizen >= 9:
        print('You meet the requirements of living in the US for at least 9 years.')
    else:
        print('Ineligible, you have not lived in the US for at least 9 years.')

    if current_state == state:
        print('You meet the requirement of living in the state you would like to represent.')
    else:
        print('You do not meet the requirement of living in the state you would like to represent.')
    break

