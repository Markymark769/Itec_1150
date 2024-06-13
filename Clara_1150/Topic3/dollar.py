"""
Mark Porraz
dollar.py
1/16/2024

This program asks the user how many cents (penny coins) they have.
Do you have a dollar? Write a program that asks the user how many cents (penny coins) they have.

Do you have a dollar?
If they have less than 100 cents, print the message 'you have less than a dollar'.
Or, the user could have exactly 100 cents, so print the message 'you have exactly one dollar'
Or, they could have more than 100 cents, so print the message 'you have more than one dollar'

"""


# define variables
pennies = int(input('How many coins (pennies) do you have?'))


# validation block
if (int(pennies) is False) or (int(pennies) < 0):
    print('Sorry, please put in a whole number.')

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
