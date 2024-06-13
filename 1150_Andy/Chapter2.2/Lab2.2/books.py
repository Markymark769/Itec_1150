"""Mark Porraz, 2/12/2023, Textbook
This program asks how many books you are going to buy
and do validation on a postive number to make it a positive
number.
"""


print('Welcome to the My Bookstore.')

total_cost = 0.0
for books_needed in range(books):
    books = int(input('How many textbooks do you have to buy?'))
    print()

for textbook in range(books_needed):         # loops through the range of all books bought
    price = float(input(f'Enter the price in whole dollars for book #{book+1}:'))
    total_cost = total_cost + price  # shorthand version ... total_cost+= price

print(f'\tRunning subtotal = ${total_cost :<.2f}.')  # displays the running total
print(f'Grand total = ${total_cost :<.2f}.')  # this means round two decimal places
