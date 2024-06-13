""" Mark Porraz,4/5/2023, attempt1_author_book.py
This program dispalys a command menu and let/'s the user view, add, edit, and delete dictionary enteries.

The variable 'readings' are used for dicitonary data type. The index is initialized with 3 authors and book titles.
The readings used are 1) HP LoveCraft, The Call of Cthulu, 2) Stephen King, The Shining, J.R.R Tolken, The Hobbit.
"""


def main():

    try:
        readings = {'H.P. Lovecraft': 'The Call of Cthulu','Stephen King':'The Shining', 'J.R.R. Tolken': 'The Hobit'}
        # since python only recognizes the first letter as a title case, does not recognize other caps in the string.
        # add dot between every capital ensures that python recognizes every capital
        display_menu()
        while True:
            command = input('Command: ')
            command = command.lower()  # converts what the user puts in lowercase and puts it in the correct string
            if command == 'view':  # the code for command entered.
                view(readings)  # lets the user view possible books
            elif command == 'add':  # lets the user add a book to the collection
                add(readings)
            elif command == 'edit':  # lets the user edit a book in the collection
                edit(readings)
            elif command == 'del':  # lets the user delete a book in the collection
                delete(readings)
            elif command == 'exit':  # exit lets the user exit the program
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')  # validation for error
    except KeyError:  # this is raised when trying to access a key that is not in a dictionary.
        print('Key Error ')


def display_menu(): # the display menu of commands, tells user options
    print('COMMAND MENU')
    print('view - View a reading')
    print('add - Add a reading')
    print('edit - Edit a reading')
    print('del - Delete a reading')
    print('exit - Exit program')
    print()


def view(readings):
    display_readings(readings)
    author_name = input('Enter author\'s name to view: ')
    author_name = author_name.title() # author name is converted into title case for consistency.
    if author_name in readings:
        book_title = readings[author_name] # lets the user view the key, which is author.
        print('Book title: ' + book_title + '.\n')  # lets the user view the value, book title
    else:
        print('There is no author with that name. \n')


def add(readings):
    display_readings(readings)
    author_name = input('Enter a new author\'s to add: ')  # the user is prompted to add a new author
    author_name = author_name.title()  # the input is converted into title case for consistency
    if author_name in readings: # if the author name already exists it goes through a validation check.
        book_title = readings[author_name]
        print(book_title + ' is already using this name. \n')
    else:
        book_title = input('Enter the book title name: ')
        book_title = book_title.title()  # input is converted into a title case
        readings[author_name] = book_title  # author name and book title are added to the dictionary as a key+value pair
        print(book_title + ' was added. \n')


def edit(readings): # defines the function edit(readings)
    display_readings(readings)
    author_name = input('Enter the author\'s name to edit: ')
    author_name = author_name.title()  # the input is converted into title case for consistency.
    if author_name in readings:
        new_title = input('Enter the new name of the title you want: ')
        new_title = new_title.title()  # input is converted into title case.
        readings.update({author_name: new_title})  # the author name is edited with the update method.
        # updating the value ## think of +/-

        print(new_title + ' was edited. \n')  # tells the user which title was edited.
    else:
        print('There is no author with that name. \n')  # tells the author that there is no author asked to edit is not
        # there.


def delete(readings):
    display_readings(readings)
    author_name = input('Enter the author\'s name to delete: ')
    author_name = author_name.title() # the input is converted to title case for consistency.
    if author_name in readings:
        readings.pop(author_name) # the pop method deletes the author name in index
        print(author_name + ' was deleted. \n')  # displays which author was deleted
    else:
        print('There is no author with that name. \n')


def display_readings(readings):
    author_names = list(readings.keys())  # displays the key of the program, which is author.
    author_names.sort()   ## sorts the authors names that are listed
    line = 'Author names and their book titles: \n '
    for author_name in author_names:
        line += author_name + ', '
    print(line)


if __name__ == '__main__':  # ensures that main() is called when the program is run as the main script.
    main()


