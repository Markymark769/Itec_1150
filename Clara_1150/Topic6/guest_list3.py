"""
Mark Porraz
guest list.py
This program covers the rest of the parts in a function
"""
import random
# TODO: add the random library
guest_list = []


def main():
    while True:
        guest_name = input('Enter your guest name: ')
        if guest_name in guest_list:
            print('You have already added: ' + guest_name)
        else:
            guest_list.append(guest_name)
        more_names = input('Any more names? Y for more names, N to stop: ')
        if more_names.lower() == 'N':
            break
    output()


def delete():
    while True:
        cont = input('Would you like to delete names? y to continue or n to quit: ')
        if cont.lower() == 'y':
            guest_del = input('Enter a name that you want to delete: ')
            if guest_del in guest_list:
                guest_list.remove(guest_del)
            else:
                print('Name not found in the list.')
        else:
            print('Thanks for using the program.')
            break


def output():
    print('After adding all the names, your list is: ')
    for index, name in enumerate(guest_list, 1):
        print(index, name)


main()
