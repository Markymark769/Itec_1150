""" Mark Porraz,4/5/2023, attempt1_author_book.py
This program dispalys a command menu and let/'s the book view, add, edit, and delete dictionary enteries.
The variable readings are used for dicitonary data type. The index is initialized with 3 authors and book titles.
The readings used are 1) HP LoveCraft, The Call of Cthulu, 2) Stephen King, The Shining, J.R.R Tolken, The Hobbit.
"""

def main():
    try:
        readings = {'HP Lovecraft': 'The Call of Cthulu','Stephen King':'The Shining', 'JRR Tolken': 'The Hobit'}
        display_menu()
        while True:
            command = input('Command: ')
            if not command:
                continue
            command = command.lower()
            if command == 'view':
                view(readings)
            elif command == 'add':
                add(readings)
            elif command == 'edit':
                edit(readings)
            elif command == 'del':
                delete(readings)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')

def display_menu():
    print('COMMAND MENU')
    print('view - View Readings')
    print('add - Add a Reading')
    print('edit - Edit Reading')
    print('del - Delete a Readings')
    print('exit - Exit program')
    print()


def display_books(readings):
    print('Readings')
    for book in readings:
        print(book)


def view(readings):
    display_books(readings)
    book = input('Enter a reading to view: ')
    book = book.title()
    if book in readings:
        book_name = readings[book]
        print('The book name for '+ book + 'is'+ book_name + '\n')
    else:
        print('There is reading with that name. \n')


def add(readings):
    display_books(readings)
    book = input('Enter new book name to add: ')
    book = book.title()
    if book in readings:
        book_name = readings[book]
        print('The book name ' + book + ' is already in use by ' + book_name + '\n')
    else:
        book_name = input('Enter full name as shown: Surname, Given_name ')
        book_name = book_name.title()
        readings[book] = book_name
        print(book_name + ' was added with book name ' + book + '\n')


def edit(readings):
    display_books(readings)
    book = input('Enter book name to edit: ')
    book = book.title()
    book_name = readings[book].title()

    if book in readings:

        new_book_name = input('Enter new full name as shown: Surname, Given_name ').title()
        new_book_name = new_book_name.title()
        readings[book] = new_book_name
        print(book_name + f' was edited to {new_book_name}. \n')
    else:
        print(book_name + ' is already using that name. \n')
def delete(readings):
    display_books(readings)
    book = input('Enter name to delete: ')
    book = book.title()

    if book in readings:
        book_name = readings.pop(book)
        print(book_name + ' was deleted. \n')
    else:
        print('There is no book with that name. \n')
        
if __name__ == '__main__':
        main()

#TODO: find author (key) then find the book associated with the key (value)
#TODO: figure out why edit crashes
#TODO: make sure that del actually deletes what the book deletes
#TODO: