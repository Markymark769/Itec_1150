quarters = input('Enter the number of quarters in the jar: ')

#validation block

q_total = int(quarters)* 0.25

#checks input as an integer and that input is a non-negative
#formula makes sure input is a whole number
if (int(quarters) is False) or (int(quarters) < 0):
    print('Sorry, please put in a whole number.')

#print statements
else:
    dollars = float(quarters)/100.0 # putting the int as a float
    if dollars < 10.00:
        print(f'You have less than ten dollars.')
        print(f'You have exactly {quarters} quarters')
    elif dollars == 10.00:
        print(f'You have exactly ten dollars')
        print(f'You have exactly ${dollars:,.2f}')
    elif dollars > 10.00:
        print(f'You have more than ten dollars.')
        print(f'You have ${dollars:,.2f} to be exact.')
print(f'You have a grand total of {q_total}')
print("That's all folks.")