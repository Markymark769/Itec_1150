"""Mark Porraz, 9/25/2023, Loop 2

this program uses a loop and range function to print numbers counted
the list of number are added together from small to large
the total number is displayed in a print statement. """

print('Welcome to our counting program.')
print('It also adds up the digits that you count!')

small = input('Please enter a small number, 0 or higher: ')
while not(small.isnumeric()):
    small = input('That wasn\'t a positive number. Try again: ')
small = int(small)

large = input('Please enter a larger number that you want to count up to: ')
while not(large.isnumeric()):
    large = input('That wasn\'t a positive number. Try again: ')
large = int(large)


