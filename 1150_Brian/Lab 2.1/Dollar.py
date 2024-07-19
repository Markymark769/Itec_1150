"""
Mark Porraz
Dollar.py

This program asks the user how many pennies they have.
- If they have less than a dollar's worth of pennies, print the message 'you have less than a dollar'.
- If they have exactly 100 pennies, print the message 'you have exactly one dollar'
- If they have more than 100 pennies, print the message 'you have more than one dollar'

"""

# input
pennies = input('how many pennies do you have?')

# formula
# validation block
if (int(pennies) is False) or (int(pennies) < 0) or pennies == str:  # if pennies is not an integer or 0 is greater
    print('Sorry, please put in a whole number.')  # print sorry

# print statement
else:
    dollars = float(pennies)/100.0  # sets the int as a float
    if dollars <= 1.00:
        print(f'You have less than a dollar.')
        print(f'You have exactly {pennies} cents')
    elif dollars == 1.00:
        print(f'You have exactly one dollar')
        print(f'You have exactly ${dollars:,.2f}')
    elif dollars > 1.00:
        print(f'You have more than a dollar.')
        print(f'You have ${dollars:,.2f} to be exact.')

