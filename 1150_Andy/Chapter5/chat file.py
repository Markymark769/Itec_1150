def main():
    try:
        users = {'DRM': 'drmouse', 'MRM': 'mrmouse', 'MSM': 'mrsmouse'}
        display_menu()
        while True:
            command = input('Command: ')
            if not command:
                continue
            command = command.lower()
            if command == 'view':
                view(users)
            elif command == 'add':
                add(users)
            elif command == 'edit':
                edit(users)
            elif command == 'del':
                delete(users)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')


def display_menu():
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
    user_code = user_code.upper()
    if user_code in users:
        fullname = users[user_code]
        print('The username for code ' + user_code + ' is ' + fullname + '\n')
    else:
        print('There is no user with that code. \n')


def add(users):
    display_codes(users)
    user_code = input('Enter new user code to add: ')
    user_code = user_code.upper()
    if user_code in users:
        fullname = users[user_code]
        print('The user code ' + user_code + ' is already in use by ' + fullname + '\n')
    else:
        fullname = input('Enter full name as shown: Surname, Given_name ')
        fullname = fullname.title()
        users[user_code] = fullname
        print(fullname + ' was added with user code ' + user_code + '\n')


def edit(users):
    display_codes(users)
    user_code = input('Enter user code to edit: ')
    user_code = user_code.upper()

    if user_code in users:
        fullname = users[user_code]
        fullname = fullname.title()
        new_fullname = input('Enter new full name as shown: Surname, Given_name ')
        new_fullname = new_fullname.title()
        users[user_code] = new_fullname
        print(fullname + ' was edited. \n')
    else:
        print(fullname + ' is already using that name. \n')

    def delete(users):
        display_codes(users)
        user_code = input('Enter name to delete: ')
        user_code = user_code.upper()

        if user_code in users:
            fullname = users.pop(user_code)
            print(fullname + ' was deleted. \n')
        else:
            print('There is no user with that name. \n')

if __name__ == '__main__':
    main()