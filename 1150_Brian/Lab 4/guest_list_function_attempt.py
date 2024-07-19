"""
Mark Porraz
7/9/2024
guest list function.py
"""

# simplified guest list function.


def main():
    guest_list = inputs()
    guest_list = add_guests(guest_list)
    guest_list = delete_guests(guest_list)
    outputs(guest_list)


def inputs():
    guest_list = []
    while True:
        new_guest = input('Type name & enter (hit enter twice to quit): ')
        if new_guest == '':
            break
        else:
            guest_list.append(new_guest)
    return guest_list

def add_guests(guest_list):
    while True:  # a while true loop is needed to create names; we don't know how many
        guest_add = input('Enter the name of the guest you would like to add or press <ENTER> to continue: ')
        if guest_add not in guest_list:
            guest_list.append(guest_add)
        else:
            print('That name is already in the guest list.')
    return guest_list


def delete_guests(guests):
    delete = input('would you to delete any guests (yes/no)?')
    len_before_delete = len(guests)
    if delete.lower() in ['yes','y']:
        while True:
            guest = input('Enter the name of the guest to delete or press <ENTER> to continue: ')
            if guest:
                if guest in guests:
                    print(f'Deleting {guest} from the list ...')
                    guests.remove(guest)
                    if len(guests) == 0:
                        print('That was the last remaining guest on the list')
                        break
    else:
        if len_before_delete == len(guests):
            print('No guests deleted.')
        # break
    return guests

def outputs(guest_names):
    print('The guest names are:')
    for index,names in enumerate(guest_names):
        print(f'{index + 1}:{names}')

main()
