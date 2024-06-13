"""Mark Porraz 2/5/2023, This program calculates the number of
pennies in a jar. Uses Boolean expressions.
"""
pennies = input('Enter the number of pennies in the jar: ')

# validation block
# checks input as an integer and that input is a non-negative
# formula makes sure input is a whole number


# if (int(pennies) is False) or (int(pennies) < 0): <----- alternate solution

if pennies != int:
    print('Sorry, please put in a whole number.')

# print statements.

else:
    dollars = float(pennies)/100.0  # putting the int as a float
    if dollars < 1.00:  # coding for everything greater than a dollar
        print(f'You have less than a dollar.')
        print(f'You have exactly {pennies} cents')
    elif dollars == 1.00:  # coding for everything equal to a dollar
        print(f'You have exactly one dollar')
        print(f'You have exactly ${dollars:,.2f}')  # printing the dollar amount with two decimal points
    elif dollars > 1.00:  # coding for everything less than a dollar
        print(f'You have more than a dollar.')
        print(f'You have ${dollars:,.2f} to be exact.')  # printing the dollar amount with two decimal points
print("That's all folks.")
