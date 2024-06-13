# guest list
# ex 1
# note) look at the todo list program to finish this first program

# part 1 - empty list
# as the program runs, we'll add data to the list
guest_list = []  # plural word - s at the end to indicate there are multiple guests

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
# we don't know how many guessts there are - how many names will the user enter?
# so we can't a for loop, but we can use a while loop

while True:  # set up the loop, and then return and review the condition.
    guest_name = input('Enter your guest name: ')  # variable to store name of one guest

    # before we add the name to the list, need to check if user is done with names,
    # The user presses enter ehrn they are done, their input 'guest_name' us an empty string
    # so check

    # if guest_name == '':  # is the length 0? is it equal to empty string?
    #     break
    # check for duplicates before adding name
    # use if and else since we need to make a choice between two tasks
    # - EITHER print message OR add guest
    if guest_name in guest_list:  # this is true if the name is already in the list
        print(' you have already addded' + guest_name)
        continue

    guest_list.append(guest_name)
    # more_names will be y if they want to enter more names
    # more_names will be n if they want to stop

    more_names = input('Any more names? Y for more names, N to stop')
    if more_names == 'N':  # if they want to stop, user will have entered "N"
        break
    # if this is not true, then the loop will repeat. if er don't stop the loop, it keeps going
    print(guest_list)  # I like to print data as I am working on a program
        # it helps me keep track of the data as I am working on a program
        # The way I expect, or that variable have the expected values
        # the TODO: list program in the videos has a lot in common with this lab
        #TODO: and the loop when user is done
print('The final list is')  # part 3
for number, guest_name in enumerate(guest_list):  # this is what is called a tuple  which means take these two things and
    # seperate those two in a list format
    # print(number)
    # print(guest_name)
    print(f'{number +1}: {guest_name}')  # add 1 to the number so the numbers start at 1, not 0.

#print(guest_list)
# part 4