"""
Mark Porraz
7/9/2024
guest list function.py
"""

# More complex function.
# this calls and returns the guest list because that is what is being processed and updated.


def main():
    guest_list = inputs()
    guest_list = add_guests(guest_list)  # processing the old guest list and setting it equal to a new guest list
    guest_list = delete_guests(guest_list)  # processing the old guest list and deleting names in the old list,
    # we are setting it equal to a new list
    outputs(guest_list)  # outputting the finial list when completed.


def inputs():  # the input def from main
    guest_list = []  # setting an empty list
    while True:
        new_guest = input('Type name & enter (hit enter twice to quit): ')
        if new_guest == '':  # an empty string breaks the list
            break  # command used to break the input
        else:
            guest_list.append(new_guest)  # we are going to add the guest to a list
    return guest_list  # returning a list to def main


def add_guests(guest_list):  # block for adding guests already to an established list
    while True:
        guest_add = input('Enter the name of the guest you would like to add or press <ENTER> to continue: ')
        if guest_add == '':
            break
        elif guest_add not in guest_list:
            guest_list.append(guest_add)
        else:
            print('That name is already in the guest list.')
    return guest_list  # we are sending a new guest list back to main


def delete_guests(guest_list):  # block for deleting guests to already to an established list
    delete = input('Would you like to delete any guests (yes/no)? ')
    if delete.lower() in ['yes','y']:
        while True:
            guest = input('Enter the name of the guest to delete or press <ENTER> to continue: ')
            if guest == '':
                break
            elif guest in guest_list:
                print(f'Deleting {guest} from the list ...')
                guest_list.remove(guest)
                if len(guest_list) == 0:
                    print('That was the last remaining guest on the list')
                    break
            else:
                print(f'{guest} is not in the guest list.')
    else:
        print('No guests deleted.')
    return guest_list


def outputs(guest_names):
    print('The guest names are:')
    for index, name in enumerate(guest_names):
        print(f'{index + 1}: {name}')


main()
