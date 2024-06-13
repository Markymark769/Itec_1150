"""Mark Porraz, 3/20/2023, Pasty2, midterm
This program calculates the price of a purchase order. It calculates
the item_price, tax, subtotal, tip%, and total.
The results are printed in the column."""

print('Welcome to Mark\'s Cornish Pasties!')

## note) python likes to have two spaces between functions, grammatically
def main():  # the goal is to start with the main() ##use as a road map to continue the rest of function.
    try:
        item_price, tip = inputs()  #where you would need to pass a parameter
        item_price, tax, subtotal, tip, tip_total, total = processing(item_price, tip)  #is defined
        #within the processing functions
        output(item_price, tax, subtotal, tip, tip_total, total) #output must have the following defined to work
        restart = input('continue? Enter Y or N: ') # asks the user if they would like to restart the program
        if restart == 'y':
            print('OK, let\'s calculate the volume of another box.')
            main()
        else:
            print('Thank you for using the program.')
    except Exception as err:
        print(err)


def inputs(item_price, tip): # asks the user for input
    print('Enter the price of your pasties $:\n ') ## prompt given and stored into item price
    item_price = get_pos_int() # checks if item price is a positive integer ### sends to get pos function
    print('Enter tip % that you want to give Mark:\n ') ## prompt given and stored into tip
    tip = get_pos_int()  # checks if tip is a positive integer ### sends to get pos function
    return item_price, tip  # returns the variable item price and tip


def get_pos_int():  #performs a check to make sure the the int is positive
    pos_int = input('Please enter a whole number only: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Please enter a number greater than your start number: ')
    pos_int = int(pos_int)
    return pos_int  # returns the positive integer

def processing(item_price, tip):  # for data processing
    tax = item_price * 0.07025
    subtotal = item_price + tax
    tip_percentage = tip / 100
    tip_total = subtotal * tip_percentage
    total = item_price + tax + tip
    return item_price, tax, subtotal, tip, tip_total, total  # returns back to main() to be defined.

def output(item_price, tax, subtotal, tip, tip_total, total): # displays our output disired in columns
    print('Invoice Due')
    print('{:<12}{:<4}{:<4}{:12}'.format('Pasty Price', '', '$', f'{item_price :<.2f}.'))
    print('{:<12}{:<4}{:<4}{:12}'.format('Tax @ 7.025%', '', '$', f'{tax :<.2f}.'))
    print('{:<12}{:<4}{:<4}{:12}'.format('Subtotal', '', '$', f'{subtotal:<.2f}.'))
    print('{:<12}{:<4}{:<4}{:12}'.format(f'Tip @{tip}', '', '$', f'{tip_total:<.2f}.'))
    print('{:<12}{:<4}{:<4}{:12}'.format('Total', '', '$', f'{total:<.2f}.'))
    print('Thank you for enjoying pasties from Cornwall!')
    # aligns everything into a column# by 12 spaces, 4 spaces, 4 spaces, and by 12 spaces.
    #the first section of numbers must match the number of characters in the formatting section.
main()