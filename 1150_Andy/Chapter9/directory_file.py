"""
Mark Porraz, 5/3/2023, directory.py
This program allows users to contribute and view a text file
containing usernames and emails.
It references the starter file from chapter 5, giving the user 3 options:
view, add, and exit.
"""
# unused code for list
# from pathlib import Path
# p = Path('directory.txt')
# p.write_text('mmouse mickeymouse@gmail.com')
# p.read_text()


def main():
        try:
            directory_file = open('directory.txt', 'w')  # opens the directory txt file in write mode
            directory_file.write('mmouse mickeymouse@gmail.com\n')  # writes a preloaded Username
            directory_file.close()  # closes the file
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


def display_menu():  # display for the cmd menu
    print('COMMAND MENU')
    print('view - View Username & Email')
    print('add - Add a Username & Email')
    print('exit - Exit program')
    print()


# creates view command
def view():
    directory_file = open('directory.txt', 'r')  # opens the directory file
    directory = directory_file.read()  # reads the directory file
    print(directory)
    directory_file.close()  # close is usually the last function


def add():
    print('You have chosen to add usernames & emails to the directory...')
    user_input = input('Use this format... username email@address.com, username email@address.com, ... ')
    user_input_list = user_input.split(',')  # change to a list
    user_input_fixed = ''  # a new string to hold the fixed items, so they can be written to the file
    directory_file = open('directory.txt', 'a')  # appends/writes to the dictionary txt
    for i in range(len(user_input_list)):
        guest_fixed = user_input_list[i].strip()  # strips the whitespace from input text
        user_input_fixed += guest_fixed + '\n'  # concatenate instead of overwriting
        directory_file.write(user_input_fixed)
    directory_file.close()  # close is usually the last function


main()
