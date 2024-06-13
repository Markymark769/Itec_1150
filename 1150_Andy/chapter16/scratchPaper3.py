import csv


def main():
    try:
        ref_file()
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
    print('view - View Contact File')
    print('add - Add Contact to the File')
    print('exit - Exit Program')
    print()


def view():
    with open('directory.csv', newline='') as contact_file:
        contact_reader = csv.DictReader(contact_file)
        print('NAME\tEMAIL\t\t\tPHONE')
        for row in contact_reader:
            print(str(row['name']) + '\t' + str(row['email']) + '\t' + str(row['phone']))
    print()


def add():
    print('You have chosen to add usernames & emails to the directory...')
    user_input = input('Enter a contact in this format: name, email, phone: ')
    user_input_list = user_input.split(',')
    user_input_fixed = []
    for i in range(len(user_input_list)):
        guest_fixed = user_input_list[i].strip()
        user_input_fixed.append(guest_fixed)
    with open('directory.csv', 'a', newline='') as directory_file:
        directory_writer = csv.writer(directory_file)
        directory_writer.writerow(user_input_fixed)
    print('Contact added successfully.\n')


main()
