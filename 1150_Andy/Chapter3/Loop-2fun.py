
"""Mark Porraz, 2/19/2023, Loop-2fun
this program adds up digits in a range that is counted.
"""


def main():  # main is the function # tells us what is happening inside loop
    try:
        small, large = input_prompt()  # output variables into small and large
        # check_large_number(large, small)
        total = processing(small, large)
        output(total)
        restart = input('continue? Enter Y or N: ')
        if restart == 'y':
            print('Ok, let\s count some more numbers.')
            main()
        else:
            print('Thank you for using the program.')

    except Exception as err:
        print(err)
    return


def input_prompt(): #TODO: create while loop for validation
    print('Please enter a small number, 0 or higher: ')
    small = get_pos_int()  # the same as number 9
    print('Now, enter a larger number that you want to count up to: ')
    large = get_pos_int()  # and check_large_number()
    return small, large  # returns small and large numbers to


def get_pos_int():  # A function check for errors
    pos_int = input('Please enter a whole number only: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Please enter a number greater than your start number: ')
    pos_int = int(pos_int)
    return pos_int  # returns to input prompt


def processing(small, large):
    total = 0
    for i in range(small, large + 1):
        total = total + i
        print(i)
    return total


def output(total):
    print(f'The total of all the numbers you counted is : {total}')


main()
