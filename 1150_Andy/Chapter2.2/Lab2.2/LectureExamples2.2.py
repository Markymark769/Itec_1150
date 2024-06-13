"""answer = input('When did Apollo 11 land on the moon? ')
while answer != '1969':		# if this is True, go into the loop
    print('Wrong, try again')
    answer = input('Enter the year when Apollo 11 landed on the moon: ')
print('You are correct!')"""

while True:
    print('Welcome to the coffee shop.')
    total = 0.0
    items = int(input('How many items is the customer buying? '))
    for item in range(items):
        price = int(input(f'Enter price in whole dollars for item #{item + 1}: '))
        total = total + price
    print(f'Running subtotal = ${total :<.2f}')
    print(f'Grand total = ${total :<.2f}')
    close = input('Time to close? Enter y or n:')
    if close == 'y':
        break
print('Thanks for using the program')

