"""
Mark Porraz
6/13/2024
variables.py
- This program asks for your name, and the number of credits you are taking this
semester
- explains the difference between print and input
"""

# using the print statement
print('Sam is taking 7 credits this semester.')
print('Miriam is taking 9 credits this semester.')

# using input statements
sam_credits = input('how many credits is sam taking this semester?')
miriam_credits = input('how many credits is miriam taking this semester?')

print(f'Sam is taking {sam_credits} credits this semester')
print(f'Miriam is taking {miriam_credits} credits this semester.')

# -- or --
print('Sam is taking' + sam_credits + 'credits this semester.')
print('Miriam is taking' + miriam_credits + 'credits this semester.')

