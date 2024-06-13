""" Mark Porraz, 2/26/2023 this program summarizes cost of a list
of books, giving each book a number. """


print('This program summarizes a book list.')  # print intro
def main():  # call functions and save results under key variable names.
    try:  # generic exception handling - turn off during development
        book_list, num_books, price_list = inputs()
        total, average = processing(price_list)
        outputs(book_name, num_books, book_list, price_list, total, average)
        restart = input('Need more books? Enter y or n: ')  # restart feature
        if restart == 'y':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:  # turn off during development
        print(err)  # turn off during development


def inputs():  # collect info needed from the user.
    print('Enter the number of books that you need ')  # user sets the list length/ repetitions of the for loop
    num_books = get_pos_int()  # call validation function to collect int > 0
    book_list = []  # creates a list to save prices
    price_list = []  # crates a list of to save price
    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
        book_name = input(f'Enter the title of the book # {index + 1}:')   # user sets the list length of
        # books print(Enter the cost of book #{index + 1}, to the nearest dollar)
        book_title = get_book_title(book_name)
        book_list.append(book_title)

    for index in range(num_books):
        book_cost = get_pos_int()
        price_list.append(book_cost)
    # for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
    #     book_cost = input(f'Enter the price for book # {index + 1}:')   # user sets the list length of
    #     book_cost = get_pos_int()
    #     price_list.append(book_cost)  # for loop runs user-specified number of times & collects info on each book
    return book_list, num_books, price_list  # what is expected to return, must be in the order called


# def get_pos_int():
#     pos_int = input('Please enter a whole number: ')
#     while pos_int.isnumeric() is False or int(pos_int) == 0:
#         pos_int = input('Enter a number greater than 0: ')  # this is where I ask for input of book cost
#     pos_int = int(pos_int)
#     return pos_int

def get_pos_int():
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a while number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


def get_book_title(book_title):  # collect and validate names as string
    while type(book_title) != str or str(book_title) == '':
        book_title = input('We don\'t have all day, put in a damn book.')
    book_title = str(book_title)
    return book_title


def processing(price_list):  # use the list to calculate summmary data
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(book_name, num_books, book_list, price_list, total, average):  # display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    print(book_list)
    print(f'{"Book Name":<10}{"Price":>10}')
    for index in range(len(price_list)):
        print(f'{book_name,index + 1:>2d}\t\t   ${price_list[index]:>8.2f}')
    print(f'{"Total":<10} ${total:>8.2f}')
    print(f'{"Average":<10} ${average:>8.2f}')
main()  # call main to start or restart program.
# Main has to follow the output order that is needed
