"""For this lab, and every lab: comment your code. If you use/adapt code from the internet, you must add a comment with the source of the code.
Reading: Chapter 4, Lists https://automatetheboringstuff.com/2e/chapter4/
Code: In this lab you will write one program, but it has several parts.  Write everything in one file.

Guest List Program
This program is for creating and managing a guest list for an event or party. 
Part 1: Create an empty list. 
Part 2: Use a while loop to ask the user for the names of guests. They will enter the names, one by one.
Add each name to the list. When the user is done, they should press enter to stop adding names.
Your program should reject duplicate names.  Don't add a name to the list if
that name is already in the list.
Part 3: Print all of the names. Use enumerate() to print a numbered list.
"""
import random  # will need to select random guests


def getnames(guestlist):  # function to take input of names
    # input: empty list  return: guest list populated from inputs
    notinlist = True

    name = input("Please enter guest name (enter to end): ")
    while not (name == ""):  # run until user hits enter to end name entry
        for index, savedname in enumerate(guestlist):
            # print(index, guestlist[index]) for debugging
            if savedname == name:
                notinlist = False  # name matches one already saved
        if notinlist:
            guestlist.append(name)  # add each name to the end of the list
        else:
            print("You already added ", name, " to the guest list.")
        notinlist = True
        name = input("Please enter guest name (enter to end): ")
    # appending and then asking for next name avoids having an empty value added to the list
    return guestlist


def deletenames(guestlist):  # function will run if user wants to delete any names
    # input: guest list  return: modified guest list
    """Part 4: Ask the user if they would like to delete any names. Use a while loop
    so the user can delete as many names as needed. You can either use remove to
    delete by name, or pop to delete by index. You can decide what the user should
    do to end this loop.  For part 9 -- validate name or index"""
    index = 0
    response = "Y"
    # print (index<len(guestlist)) # for debugging
    # print(response!="") # for debugging
    while index < len(guestlist) and response != "":

        # print(guestlist[index]) # print each name during loop iterations for debugging
        response = input("Hit enter to stop deleting, Y to delete "+guestlist[index]+", N to keep: ") # ask to delete
        if response == "Y" or response == "y":
            print("deleting "+(guestlist[index]))
            guestlist.pop(index)
            index = index-1  # length of list decreases if name is deleted
        index += 1  # increment loop counter (after a name deletion, the counter will be the same)
    return guestlist


def give_prizes(guestlist):  # define how many prizes and who wins them
    # input: guest list    return: winners, a list
    """Part 6: At the event, the user want to give out prizes to random guests.  Ask
    the user how many prizes there should be.   Use random to select that many
    names from the guest list. Each guest should win at most, one prize. So,
    don't allow a guest to win more than one prize. """
    numguests = len(guestlist)
    print(numguests, " guests")
    prizecount = -1  # starting value to run loop
    while prizecount < 0 or prizecount > numguests:  # validates number for part 9
        print("The maximum number of prizes is "+str(len(guestlist)))
        prizecount = int(input("How many prizes should there be ? "))
    winners = []  # empty list for prize winners
    index = 0
    while index < prizecount and numguests > 0: # doesn't run if 0 prizes or if 0 guests
        newwinner = random.choice(guestlist)
        while newwinner in winners:
            newwinner = random.choice(guestlist) # if new name already in list, get another name
        winners.append(newwinner)
        index += 1 # loop runs from index=0 to index=prizecount-1, which is prizecount times
        # index is incremented each time a winner is appended


    # print("There are " + str(numguests) + " guests: ")
    # printlist(guestlist)
    # if numguests > 0: # using printlist function instead of printing from here
    #    print("The following guests will receive prizes: ")
    #    print(winners)
    print(2*'\n')
    # reference for printing multiple empty lines https://www.pythonpool.com/python-print-blank-line/
    return winners


def printlist(inputlist):  # prints an enumerated list
    # input: any list    return: nothing
    """Part 5: Print all of the names, again using enumerate() to print a numbered
list.   Can you write and call a function instead of re-writing part 3?"""
#    print("print function call") # for debugging
#    print (list(enumerate(inputlist,1))) #different format of print
    print()  # line feed
    for index, name in enumerate(inputlist,1):
        print(index, name)  # print numbered list beginning with 1
    print()  # line feed
    # reference for enumerate: https://pythonbasics.org/enumerate/
    # reference for enumerate: https://www.programiz.com/python-programming/methods/built-in/enumerate
    # enumerate creates a tuple that is (index, list_item) - index begins at 0 unless chosen otherwise


def main():
    print("Follow the prompts to enter and edit a guest list and select guests for prizes.")
    guestlist = []  # create empty list
    getnames(guestlist)  # get names
    printlist(guestlist)
    if (input("Enter Y to delete any guests from the list: ").upper()) == "Y":
        deletenames(guestlist)
    printlist(guestlist)
    winners = give_prizes(guestlist)
    # reference on function return https://realpython.com/python-return-statement/
    print("There are "+str(len(guestlist))+" guests: ")
    printlist(guestlist)  # print enumerated list of guests
    if len(winners) > 1:
        print("Prizes will be given to: ")
        printlist(winners)
    elif len(winners) == 1:
        print("A prize will be given to: ")
        printlist(winners)
    else:
        print("No prizes are planned.")


"""Part 7: Print 
    The total number of guests
    All the guests as a numbered list  (use the function described in part 5)
    The names of the guest(s) who will be given a prize"""
"""
Part 8: Comment your code
Part 9: Extra credit, +3 points: add validation to your program so it doesn't
crash if the user enters invalid data. Places to add validation:

    Check for valid names if removing by name;  or check for valid indexes if
    popping names by index
    End part 4's while loop if the user has removed all of the names from the
    guest list. 
    Check the number of guests that will be given a prize is equal or less
    than the total number of guests 
"""
main()
