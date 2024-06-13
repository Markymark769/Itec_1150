import random
guest_names = []  # brackets are functions that hold items
# this value is an empty list that can have things added.
while True:
    user_input = input('Enter the guest names, or press enter to stop: ')
    if user_input:
        if user_input in guest_names:
            print('Name has already been recorded')
        else:
            guest_names.append(user_input)
    else:
        break

print('the guest names are:')

for index, task in enumerate(guest_names):
    print(f'{index + 1} is {task}')

print(f'there are {len(guest_names)} guests')
if guest_names:  # you don't need { } here. This will be true if there is at least one guest, false if guest_names is empty

    while True:
        print('Do you want to remove any guests? type "y" or "n" ')
        delete_guest = input()
        # ask for user_input here, use input()
        if delete_guest == 'y':
        # print('Which guests should be removed?')  # use input
            user_input = input('Which guest should be removed?')  # ask for one guest name
            # start by assuming the guest is in the list and remove them.
            # get this working, and then you can modify the program to only remove guests who are in the list
            guest_names.remove(user_input)  # is this the right variable name?
            print(guest_names)
            print(f"delete_guest {user_input} has been deleted")  # is this the right variable name?
        # think about how to stop this loop when the user is done deleting guests.
        # maybe an else will help?
        else:
            break


for index, name in enumerate(guest_names):
    print(f"name {index}: {name}")

print('How many prizes should there be?')
prizes = input()

options = guest_names
persons_choice = random.choices(options)
print(f'{persons_choice} will be given a prize')
