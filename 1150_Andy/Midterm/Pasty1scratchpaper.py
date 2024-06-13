"""Mark Porraz, 3/20/2023, Pasty1, midterm
This program calculates the price of a purchase order. It calculates
the item_price, tax, subtotal, tip%, and total.
The results are printed in the column."""

print('Welcome to Mark\'s Cornish Pasties!')

### Define variables
while True:         # Loop to check number of students input is an integer
    try:
        item_price = float(input('Enter the price of your pasties $:\n '))  # asks user for input, stores it in item price
        tip = float(input('Enter tip % that you want to give Mark:\n '))  # asks user for input, stores it in tip
    except ValueError:
        print('We need a whole NUMBER, we do not have time for your nonsense sir!')
    else:
        break ## break is used to leave the loop

### Calculate the item_price_sales, tax, subtotal, tip%, and total
tax = item_price * 0.07025
subtotal = item_price + tax
tip_percentage = tip/100
tip_total = subtotal * tip_percentage
total = item_price + tax + tip

### Display in table
print('Invoice Due')
print('{:<12}{:<4}{:<4}{:12}'.format('Pasty Price','','$',f'{item_price :<.2f}.'))
print('{:<12}{:<4}{:<4}{:12}'.format('Tax @ 7.025%','','$',f'{tax :<.2f}.'))
print('{:<12}{:<4}{:<4}{:12}'.format('Subtotal','','$',f'{subtotal:<.2f}.'))
print('{:<12}{:<4}{:<4}{:12}'.format(f'Tip @{tip}','','$',f'{tip_total:<.2f}.'))
print('{:<12}{:<4}{:<4}{:12}'.format('Total','','$',f'{total:<.2f}.'))
print('Thank you for enjoying pasties from Cornwall!')
# aligns everything into a column# by 12 spaces, 4 spaces, 4 spaces, and by 12 spaces.
# the first section of numbers must match the number of characters in the formatting section.