"""Mark Porraz, 2/12/2023
Homework 2_2, how many guests."""
# this program asks the users name and how many guests

name = ''
while not name:
        print('Enter your name:')  # asks for the users name, but numbers work as well.
        name = input()  # no restrictions set # where the user will actually input info
print('How many guests will you have?')
numOfGuests = int(input())  # integer set, crashes when letters input
if numOfGuests:
        print('Be sure to have enough room for all your guests.')
print('Done')
