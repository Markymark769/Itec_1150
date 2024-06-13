# book_list.py: you can adapt your Chapter 4 book_list.py Lab program. The program summarizes costs of a book list.
# • It uses all of our standard mipo_ex features.
# • In this version of the program you must use pyInputPlus functions to perform all the input validation and
# for the main() loop decision.
# • Adjust your program to allow book prices to include $ and cents. Restrict individual book prices to $100 maximum.
# • Clearly document, with comments, your use of the pyip functions.


import pyinputplus as pyip

print('This program summarizes a book list.')  # print intro


def main():  # call functions and save results under key variable names.
    try:  # generic exception handling - turn off during development
        num_books, price_list, booklist = inputs()
        total, average = processing(price_list)
        outputs(num_books, price_list, booklist, total, average)
        restart = pyip.inputYesNo(prompt="Need more books? Enter yes or no: ")  # restart feature
        if restart.upper() == 'YES':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:  # turn off during development
        print(err)  # turn off during development


def inputs():  # collect info needed from the user.
    booklist=[]
    # num_books = get_pos_int()  # call validation function to collect int > 0
    num_books = pyip.inputInt(prompt="Enter the number of books that you need: ", min=0)
    price_list = []  # create list to save prices
    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
        bookstr = "Enter the title of book #"+str(index+1)+": "
        booklist.append(pyip.inputStr(prompt=bookstr, blank=False))
        bookpricestr = "Enter the cost of book "+str(index+1)+": $"
        # book_cost = get_pos_int()  # call validation function to collect int > 0
        price_list.append(round(pyip.inputFloat(prompt=bookpricestr, min=0), 2))  # build price list
        # did not see option for inputFloat to limit decimal places
    return num_books, price_list, booklist


def processing(price_list):  # use the list to calculate summary data
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(num_books, price_list, booklist, total, average):  # display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book #":<10}{"Book Title":<30}{"Price":>10}')
    for index in range(len(price_list)):
        print(f'{index + 1:>2d}{booklist[index]:>30}\t\t\t${price_list[index]:>8.2f}')
    print()
    print()
    print(f'{"Total":<10} ${total:>8.2f}')
    print(f'{"Average":<10} ${average:>8.2f}')


main()  # call main to start or restart program.
