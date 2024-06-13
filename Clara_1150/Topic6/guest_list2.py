"""
Mark Porraz
guest list.py
This program covers parts 1-5 on the steps to complete the program
"""

guest_list = []  # part 1 create the empty list

# write a loop to ask user for guest names, and add to tlist
# add one name at a time.

# what kind of loop?
# how many guests are there? counting loop/for loop/while loop
# we do not know how many times our loop is going to repeat, so we will use a while loop
# in this scenario while --->>> a for loop if we knew how many times repeated

# loop will ask for one guest name (done)
# add the guest to the list (done)
# ask user if there are more names - stop loop if not (done)
# check for duplicates

# part 2, ask user for guest names, one by one
# we don't know how many guests there are - how many names will the user enter?
# so we can't a for loop, but we can use a while loop

while True:  # part 2: Uses a while loop to ask the user for the names of guests
    # before we add the name to the list, need to check if user is done with names,
    # The user presses enter when they are done, their input 'guest_name' us an empty string
    # so check

    # if guest_name == '':  # is the length 0? is it equal to empty string?
    #     break
    # check for duplicates before adding name
    # use if and else since we need to make a choice between two tasks
    # - EITHER print message OR add guest
    guest_name = input('Enter your guest name: ')
    # part 2: rejecting duplicate names
    if guest_name in guest_list:  # this is true if the name is already in the list
        print(' you have already added: ' + guest_name)
    else:  # name is new, not in a list
        guest_list.append(guest_name)
    guest_list.append(guest_name)
    more_names = input('Any more names? Y for more names, N to stop')
    if more_names == 'N':
        break

# wrong! DOES NOT WORK!
# for index in range(guest_name,guest_list):
#     print(str(index+1))

# part 4 --->>> using a while loop to ask the user if they want to delete names
while True:
    cont = input('Would you like to delete names? y to continue or n to quit')
    if cont == 'y':  # the key to input if the user wants to continue
        guest_del = input(' enter a name that you want to delete: ')
        guest_list.remove(guest_name)
    else:  # press anything other than 'y' to quit the loop
        print('thanks for using the program')
        break  # lets the program stop the loop

# part 3: print all names. Use enumerate() to print a numbered list.
print('After adding all the names, your list is: ')

# part 5
for index, name in enumerate(guest_list, 1):  # uses the enumerate() function to print a list
    print(index, name)  # print numbered list beginning with 1
print()  # line feed
