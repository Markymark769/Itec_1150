""" Mark Porraz, 4/11/2023 this program asks the user how many books they would
like to enter, asks the user for a price of each book, then summarizes the list
of books. The main variable in this program is book_list"""

import pyinputplus as pyip
# main and input functions
num_books = pyip.inputInt(prompt="Enter the number of books you need: ")  # inputInt is used instead of inputNum as
# validation. Int is more concise for validation.
book_names = []  # To display all the book names, they are stored in a list then loop through list to display them
price_list = []  # To display prices, they are stored in a list then loop through list to display them

for index in range(num_books): # puts the following in an index
    book_name = pyip.inputStr(f'Enter the title of the book # {index + 1}:')
    book_price = pyip.inputFloat('Enter the cost of the book: ')
    book_names.append(book_name)  # adds the book names to the list above.
    price_list.append(book_price)  # adds the price to a list as shown above.

# calculations
total = sum(price_list)
average = round(total / len(price_list), 2)

# displays in a table.
print(f'Info on {num_books} Books Needed')  # diplays the number of books needed by user
print(f'{"Book Name":<10}{"Price":>10}')  # formats the book name and price in 10 characters
for index in range(len(price_list)):  # calls for the index of the book price in the list
    print(f'{book_names[index]:<10} ${price_list[index]:>8.2f}') # formats book names and prices
    # in a list with 10 characters.
print(f'{"Total":<10} ${total:>8.2f}')
print(f'{"Average":<10} ${average:>8.2f}')
