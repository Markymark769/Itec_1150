""" M. Bock 6/18/2019 this program summarizes cost of a list
of books, giving each book a number.

starter file collects book prices into a list, and totals, averages & displays the info

TO DO:
The revised program has to add a feature to collect the book titles into a parallel list, for
improved display. * functions: main, inputs, processing, outputs & get_pos_int, with exception
handling & restart in main(). """

print('This program summarizes a book list.')  # print intro

def main():  # call functions and save results under key variable names.
    try:  # generic exception handling - turn off during development
        num_books, price_list, booklist = inputs()
        total, average = processing(price_list)
        outputs(num_books, price_list, booklist, total, average)
        restart = input('Need more books? Enter y or n: ')  # restart feature
        if restart == 'y':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:  # turn off during development
        print(err)  # turn off during development


def inputs():  # collect info needed from the user.
    booklist=[]
    print('Enter the number of books that you need ')  # user sets the list length/ repetitions of the for loop
    num_books = get_pos_int()  # call validation function to collect int > 0
    price_list = []  # create list to save prices
    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
        print(index)
        booklist.append(input(f'Enter the title of book #{index+1}: '))
        print(f'Enter the cost of book #{index +1}, to the nearest dollar: ')
        book_cost = get_pos_int()  # call validation function to collect int > 0
        price_list.append(book_cost)  # build price list
    return num_books, price_list, booklist


def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


def processing(price_list):  # use the list to calculate summary data
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(num_books, price_list, booklist, total, average):  # display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book #":<10}{"Book Title":<20}{"Price":>10}')
    for index in range(len(price_list)):
        print(f'{index + 1:>2d}{booklist[index]:>20}\t\t\t${price_list[index]:>8.2f}')
    print()
    print()
    print(f'{"Total":<10} ${total:>8.2f}')
    print(f'{"Average":<10} ${average:>8.2f}')


main()  # call main to start or restart program.
