"""
Mark Porraz
7/9/2024
guest list function.py
"""

# simplified guest list function.


def main():
    guest_names = inputs()
    outputs(guest_names)


def inputs():
    guests = []
    while True:
        new_guest = input('Type name & enter (hit enter twice to quit): ')
        if new_guest == '':
            break
        else:
            guests.append(new_guest)
    return guests


def outputs(guest_names):
    print('The guest names are:')
    for index,names in enumerate(guest_names):
        print(f'{index + 1}:{names}')


main()
