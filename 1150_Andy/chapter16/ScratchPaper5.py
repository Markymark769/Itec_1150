"""
Mark Porraz, 5/11/2023, ScratchPaper5.py

"""
import csv


def main():
    try:
        ref_file()
        display_menu()
        while True:
            command = input('Command: ')
            command = command.lower()  # accepts input in lowercase
            if command == 'view':  # view cmd
                view()
            elif command == 'add':  # add to program cmd
                add()
            elif command == 'exit':  # exit program cmd
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')  # validation for valid command
    except KeyError:
        print('Key Error ')


def ref_file():  # the reference file to be viewed
    # Open file with 'with' statement to ensure it's always closed
    with open('directory.csv', 'w', newline='') as contact_file:
        contact_writer = csv.writer(contact_file)   # formats to write in the file
        # Use descriptive header
        contact_writer.writerow(['Name', 'Email', 'Phone'])  # sets a header
        # Use list of tuples for better syntax
        contacts = [
            ('Mickey Mouse', 'mickeymouse@gmail.com', '123-456-7890'),  # 1st contact
            ('Donald Duck', 'dduck@gmail.com', '456-789-0123'),  # 2nd contact
            ('Road Runner', 'rrunner@gmail.com', '789-012-3456')  # 3rd contact
        ]
        contact_writer.writerows(contacts)  # always close the file


def display_menu():  # display options
    print('COMMAND MENU')
    print('view - View Contact File')
    print('add - Add Contact to the File')
    print('exit - Exit Program')
    print()


def view():  # function for viewing
    with open('directory.csv', newline='') as contact_file:  # opens the file as contact file variable
        contact_reader = csv.DictReader(contact_file)  # dictionary reader function to open reference file
        print('NAME\t\t\tEMAIL\t\t\tPHONE')  # prints name, email, and phone with 3 tabs
        for row in contact_reader:
            print(str(row['name']) + '\t' + str(row['email']) + '\t' + str(row['phone']))
            # for the rows in the reference file print name, email, and phone of each
    print()


def add():
    print('You have chosen to add usernames & emails to the directory...')
    user_input = input('Enter a contact in this format: name, email, phone: ')
    user_input_list = user_input.split(',')  # change to a list
    user_input_fixed = []  # a new list to hold the fixed items, so they can be written to the file
    for i in range(len(user_input_list)):
        guest_fixed = user_input_list[i].strip()  # strips the whitespace from input text
        user_input_fixed.append(guest_fixed)
    with open('directory.csv', 'a', newline='') as directory_file:  # use "with open" for automatic file closing
        directory_writer = csv.writer(directory_file)
        directory_writer.writerow(user_input_fixed)  # write the fixed user input to the file
    print('Contact added successfully.\n')


main()
