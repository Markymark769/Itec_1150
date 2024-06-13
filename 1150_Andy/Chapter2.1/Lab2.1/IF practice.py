if (int(pennies) is False) or (int(pennies) < 0):

else:
    if dollars < 1.00:
        print(f'You have less than a dollar.')
        print(f'You have exactly {pennies} cents')
    elif dollars == 1.00:
        print(f'You have exactly one dollar')
        print(f'You have exactly ${dollars:,.2f}')
    elif dollars > 1.00:
        print(f'You have more than a dollar.')
        print(f'You have ${dollars:,.2f} to be exact.')
print("That's all folks.")