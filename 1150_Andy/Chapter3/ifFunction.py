
def main():
    num_pennies = input('Enter the number of pennies in the jar: \n') #what are you trying to find
    dollar_amount = processing(num_pennies) #what is the amount you are trying to get
    # TODO: add get_post_int
    output(dollar_amount,num_pennies)

def inputs():
    print('Enter the number of pennies in the jar.')
    num_pennies = get_pos_int()
    return num_pennies

def get_pos_int():
    pos_int = input('Please enter a whole number only: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Please enter a real number: ')
    pos_int = int(pos_int)
    return pos_int

def processing(num_pennies):
    dollar_amount = float(num_pennies)/100.0
    return dollar_amount

def output(dollar_amount, num_pennies):
    if dollar_amount < 1.00:
        print(f'You have less than a dollar.')
        print(f'You have exactly {num_pennies} cents')
    elif dollar_amount == 1.00:
        print(f'You have exactly one dollar')
        print(f'You have exactly ${dollar_amount:,.2f}')
    elif dollar_amount > 1.00:
        print(f'You have more than a dollar.')
        print(f'You have ${dollar_amount:,.2f} to be exact.')
main()