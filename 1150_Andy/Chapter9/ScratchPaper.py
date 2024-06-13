def main():
    try:
        directory_file = open('directory.txt', 'w')
        directory_file.write('mmouse mickeymouse@gmail.com\n')
        directory_file.close()
        display_menu()
        while True:
            command = input('Command: ')
            command = command.lower()
            if command == 'view':
                view()
            elif command == 'add':
                add()
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')

def display_menu():
    print('COMMAND MENU')
    print('view - View Username & Email')
    print('add - Add a Username & Email')
    print('exit - Exit program')
    print()

# create view command
def view():
    directory_file = open('directory.txt', 'r')
    directory = directory_file.read()
    print(directory)
    directory_file.close()  # close is usually the last function

def add():
    print('You have chosen to add usernames & emails to the directory...')
    user_input = input('Use this format... username email@address.com, username email@address.com, ... ')
    user_input_list = user_input.split(',')  # change to a list
    user_input_fixed = ''  # a new string to hold the fixed items, so they can be written to the file
    directory_file = open('directory.txt', 'a')
    for i in range(len(user_input_list)):
        guest_fixed = user_input_list[i].strip()
        user_input_fixed += guest_fixed + '\n'  # concatenate instead of overwriting
        directory_file.write(user_input_fixed)
    directory_file.close()  # close is usually the last function

main()
