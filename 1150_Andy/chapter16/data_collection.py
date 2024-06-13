"""
Mark Porraz, 5/12/2023, data_collection.py
This program accepts input from the user and creates a
csv file that holds the name, email, and a phone number
of each contact.

The add function adds the name, email, and a phone number
of each contact in that format. The view function reads
from the csv file and displays the data in columns, with
appropriate headings.
"""

import csv


def main():
    try:
        ref_file()
        display_menu()
        while True:
            command = input('Command: ').lower()  # accepts input in lowercase
            if command == 'view':  # view cmd
                view()
            elif command == 'add':  # add to program cmd
                add()
            elif command == 'exit':  # exit program cmd
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again.\n')  # validation for valid command
    except KeyError:
        print('Key Error')


def ref_file():  # the reference file to be viewed
    # Open file with 'with' statement to ensure it's always closed
    with open('directory.csv', 'w', newline='') as contact_file:
        contact_writer = csv.writer(contact_file)  # formats to write in the file
        # Uses descriptive header
        contact_writer.writerow(['Name', 'Email', 'Phone'])  # sets header
        # List of tuples for better syntax
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
    print('exit - Exit Program\n')


def view():  # function for viewing
    with open('directory.csv', newline='') as contact_file:  # opens the file as contact file variable
        contact_reader = csv.DictReader(contact_file)  # dictionary reader function to open reference file
        # print('NAME\t\t\tEMAIL\t\t\tPHONE')
        # print('{"NAME":<30}{"EMAIL":<30}{"PHONE":<20}')
        print(f'{"NAME":<30}{"EMAIL":<30}{"PHONE":<20}')  # prints name, email, and phone with 3 tabs
        for row in contact_reader:
            # an attempt to use f-strings for cleaner syntax
            # print(f"{row['Name']}\t\t\t{row['Email']}\t\t\t{row['Phone']}")
            print('{:<30}{:<30}{:<20}'.format(row['Name'], row['Email'], row['Phone']))
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
