""" Mark Porraz, 4/5/2023, username_fullname.py
This program dispalys a command menu and let/'s the user view, add, edit, and delete dictionary enteries.

The variable 'user' is used throughout the program. The key is a used is a user code and
the value user is the full name of the user.
. """


def main():
    try:
        users = {'DRM': 'Dr. Mouse', 'MRM': 'Mr. Mouse', 'MSM': 'Mrs. Mouse'}
        display_menu()
        while True:
            command = input('Command: ')
            if not command:
                continue
            command = command.lower() # converts what the user puts in lowercase and puts it in the correct string
            if command == 'view':
                view(users)  ## lets you view the possible users in the dictionary
            elif command == 'add':
                add(users)  ## lets you add a user to the dictionary
            elif command == 'edit':
                edit(users)  ## lets you edit user in the dictionary
            elif command == 'del':
                delete(users)  ## lets you delete a user in the dictionary
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n') # validation for errors
    except KeyError: # this is raised when trying to access a key that is not in a dictionary.
        print('Key Error ')


def display_menu():  # the display menu of commands, tells user options
    print('COMMAND MENU')
    print('view - View username')
    print('add - Add a user')
    print('edit - Edit a user')
    print('del - Delete a user')
    print('exit - Exit program')
    print()


def display_codes(users):
    print("User Codes:")
    for code in users:
        print(code)


def view(users):
    display_codes(users)
    user_code = input('Enter a username to view: ')
    user_code = user_code.upper()  # input is converted into upper case for consistency
    if user_code in users:
        fullname = users[user_code]  ## lets you view the key, which user code to be viewed.
        print('The username for code ' + user_code + ' is ' + fullname + '\n') # lets you view value,
        # which is the fullname
    else:
        print('There is no user with that code. \n')


def add(users):
    display_codes(users)
    user_code = input('Enter new user code to add: ')   # the user is prompted to enter a user code
    user_code = user_code.upper()  # the input is converted to uppercase for consistency.
    if user_code in users:  # if the user code already exists the user goes through a validation.
        fullname = users[user_code]
        print('The user code ' + user_code + ' is already in use by ' + fullname + '\n')
    else:
        fullname = input('Enter full name as shown: Surname, Given_name ')  # if user code does not exist
        # the function prompts to enter the fullname of the new user.
        fullname = fullname.title()  # input is converted into title case.
        users[user_code] = fullname  # user code and full name are added as a key+value
        # pair to the dictionary.
        print(fullname + ' was added with user code ' + user_code + '\n')  # message prints telling  user added


def edit(users):  # defines the function edit(users)
    display_codes(users)
    user_code = input('Enter user code to edit: ')   # the user is prompted to enter a user code to edit.
    user_code = user_code.upper()  # the input is converted to uppercase for consistency.
    if user_code in users:
        new_fullname = input('Enter new full name as shown: Surname, Given_name ')
        new_fullname = new_fullname.title()  # input is converted into title case.
        users.update({user_code:user_code})  # the user code is edited with the update method.
        # updating the value ## think of +/-

        print(new_fullname + ' was edited. \n')
    else:
        print(user_code + ' is already using that name. \n')  # if the user code already exists the user
        # goes through a validation.

def delete(users):
    display_codes(users)
    user_code = input('Enter name to delete: ')
    user_code = user_code.upper()  # the input is converted to uppercase for consistency.

    if user_code in users:
        fullname = users.pop(user_code)  # the pop method deletes the author name in index
        print(fullname + ' was deleted. \n')   # displays which author was deleted
    else:
        print('There is no user with that name. \n')


if __name__ == '__main__':   # ensures that main() is called when the program is run as the main script.
    main()


