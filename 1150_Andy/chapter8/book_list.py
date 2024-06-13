""" Mark Porraz, 4/11/2023 this program asks the user how many books they would
like to enter, asks the user for a price of each book, then summarizes the list
of books. The main variable in this program is book_list"""

import pyinputplus as pyip


def main():
    try:
        book_names, price_list, num_books = inputs()  # input variables
        total, average = processing(price_list)  # process the price_list and return total and average
        outputs(num_books, price_list, book_names, total, average)  # process the outputs
        restart = input('Continue? Enter y or n: ')
        if restart == 'y':
            print('OK, let\'s process more books.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
        print(err)


def inputs():
    num_books = pyip.inputInt(prompt="Enter the number of books you need: ")  # inputInt is used instead of inputNum as
    book_names = []  # To display all the book names, they are stored in a list then loop through list to display them
    price_list = []  # To display prices, they are stored in a list then loop through list to display them
    for index in range(num_books):  # puts the following in an index
        book_name = pyip.inputStr(f'Enter the title of the book # {index + 1}:')
        book_price = pyip.inputFloat('Enter the cost of the book: ')
        book_names.append(book_name)  # adds the book names to the list above.
        price_list.append(book_price)  # adds the price to a list as shown above.
    return book_names, price_list, num_books


def get_pos_int():
    # performing a check to make sure it is a positive int
    pos_int = input('Please enter a whole number: ')  # need to define a positive int. pos int = whole number
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a whole number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


# Calculations:
def processing(price_list):
    #  formulas for processing
    total = sum(price_list)  # summed of the price list
    average = round(total / len(price_list), 2)  # divide total by price list & round total
    return total, average


def outputs(num_books,price_list, book_names, total, average):
    print(f'Info on {num_books} Books Needed')  # displays the number of books needed by user
    print(f'{"Book Name":<10}{"Price":>10}')  # formats the book name and price in 10 characters
    for index in range(len(price_list)):  # calls for the index of the book price in the list
        print(f'{book_names[index]:<10} ${price_list[index]:>8.2f}')  # formats book names and prices
        # in a list with 10 characters.
    print(f'{"Total":<10} ${total:>8.2f}')
    print(f'{"Average":<10} ${average:>8.2f}')


main()
