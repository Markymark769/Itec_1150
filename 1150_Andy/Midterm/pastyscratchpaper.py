"""Mark Porraz, 3/20/2023, Pasty2, midterm
This program calculates the price of a purchase order. It calculates
the item_price, tax, subtotal, tip%, and total.
The results are printed in the column."""

print('Welcome to Mark\'s Cornish Pasties!')
def main():
    item_price = float(input('Enter the price of your pasties $:\n '))
    tip = float(input('Enter the price of your pasties $:\n '))
    price = processing(item_price, tip)
    output(price, tax, subtotal, tip, tip_total, total)

def inputs():
    print('Enter the price of your pasties $:\n ')
    item_price = get_pos_int()
    print('Enter tip % that you want to give Mark:\n ')
    tip = get_pos_int()
    return item_price, tip

def get_pos_int():
    pos_int = input('Please enter a whole number only: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Please enter a number greater than your start number: ')
    pos_int = int(pos_int)
    return pos_int

def processing(price, tip):
    tax = price * 0.07025
    subtotal = price + tax
    tip_percentage = tip / 100
    tip_total = subtotal * tip_percentage
    total = price + tax + tip
    return price, tax, subtotal, tip, tip_total, total

def output(price, tax, subtotal, tip, tip_total, total):
    print('Invoice Due')
    print('{:<12}{:<4}{:<4}{:12}'.format('Pasty Price', '', '$', f'{price :<.2f}.'))
    print('{:<12}{:<4}{:<4}{:12}'.format('Tax @ 7.025%', '', '$', f'{tax :<.2f}.'))
    print('{:<12}{:<4}{:<4}{:12}'.format('Subtotal', '', '$', f'{subtotal:<.2f}.'))
    print('{:<12}{:<4}{:<4}{:12}'.format(f'Tip @{tip}', '', '$', f'{tip_total:<.2f}.'))
    print('{:<12}{:<4}{:<4}{:12}'.format('Total', '', '$', f'{total:<.2f}.'))
    print('Thank you for enjoying pasties from Cornwall!')
main()