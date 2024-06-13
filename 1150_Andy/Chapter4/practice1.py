# """ Mark Porraz, 2/26/2023 this program summarizes cost of a list
# of books, giving each book a number. """
#
# print('This program summarizes a book list.')  # print intro
# def main():
#     try:
#         book_list, num_books, price_list = inputs()
#         total, average = processing(price_list)
#         outputs(num_books, book_list, price_list, total, average)
#         restart = input('Need more books? Enter y or n: ')
#         if restart == 'y':
#             print('OK, let\'s create a new list.')
#             main()
#         else:
#             print('Thanks for using the program.')
#     except Exception as err:
#         print(err)
#
#
# def inputs():print('Enter the number of books that you need ')
#
#     num_books = get_pos_int()
#
#     book_list = []
#     price_list = []
#     for index in range(num_books):
#         book_name = input(f'Enter the title of the book # {index + 1}:')
#         book_cost = get_pos_int()
#         book_title = get_book_title(book_name)
#         price_list.append(book_cost)
#         book_list.append(book_title)
#
#     return book_list, num_books, price_list
#
#
# def get_pos_int():
#     pos_int = input('Please enter a whole number: ')
#     while pos_int.isnumeric() is False or int(pos_int) == 0:
#         pos_int = input('Enter a number greater than 0: ')
#     pos_int = int(pos_int)
#     return pos_int
#
#
# def get_book_title(book_title):
#     while type(book_title) != str or str(book_title) == '':
#         book_title = input('We don\'t have all day, put in a damn book.')
#     book_title = str(book_title)
#     return book_title
#
#
# def processing(price_list):
#     total = sum(price_list)
#     average = round(total / len(price_list), 2)
#     return total, average
#
#
# def outputs(num_books, book_list, price_list, total, average):
#     print(f'Info on {num_books} Books Needed')
#     print(book_list)
#     print(f'{"Book Name":<10}{"Price":>10}')
#     for index in range(len(price_list)):
#         print(f'{index + 1:>2d}\t\t   ${price_list[index]:>8.2f}')
#     print(f'{"Total":<10} ${total:>8.2f}')
#     print(f'{"Average":<10} ${average:>8.2f}')
# main()
