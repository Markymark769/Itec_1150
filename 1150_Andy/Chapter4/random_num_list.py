"""Mark Porraz, 2/19/2023, Random Number list
this program adds up digits in a range that is counted.

welcome to our random number game.
how many integers should the computer pick for your list?

correction: You can only enter a number 1 or higher:

here is your list of integers
here is your list - printed w/shortcut method:
here is your list - printed via a loop, with total:

would you like to continue? Enter Y or N:



"""
import random  # this imports the randomized function

print('Welcome to our random number game.') #Tells the user what to do
def main(): # main is the function # tells us what is happening inside loop
    try: # beginning of the block
        list_of_num = input_prompt()  # output variables into small and large
        list_of_num.sort()
        total_of_num, min_num, max_num = processing(list_of_num)
        output(list_of_num,total_of_num, min_num, max_num)
        restart = input('would you like to continue? Enter Y or N: ')
        if restart == 'y':
            print('Ok, let\s count some more numbers.')
            main()
        else:
            print('Thank you for using the program.')
    except Exception as err:
        print(err)


def input_prompt():  # this is the inputs that the user sees
    print('Let\'s get ready to count some numbers!')
    # this is where the list of numbers come from
    array_num = get_pos_int()
    num_list = []
    for crap in range(array_num):
        crap = random.randint(0, 20)  # generates a random number between 0 and 20 like a polyhedron
        num_list.append(crap)
    return num_list # returns small and large numbers to

def get_pos_int(): # A function check for errors
    pos_int = input('How many numbers would you like the computer to generate for your list? ')
    while pos_int.isnumeric() is False or int(pos_int) == 0: # If the input is not int greater than zero or
        # isn't numeric, the user is given a second chance to correct issue.
        pos_int = input('Please enter a number greater than 0: ')
    pos_int = int(pos_int) # declares the string as a positive integer
    return pos_int # this returns a positive variable.

def processing(list_nums): # defines the processing function, and utilizes
    total_of_num = 0
    for something in range(len(list_nums)):
        total_of_num += something # += is a shortcut for  total_of_num = total_of_num + something
    min_num = list_nums[0] # calling the first in the list
    max_num = list_nums[-1] # calling the last in the list
    return total_of_num, min_num, max_num # returns the calculated total in the list

def output(list_nums, total_of_num, min_num, max_num):

    print('Here is your list of numbers. It is placed in a sorted format')
    print(list_nums) # this prints a sorted list
    print('Here is your list placed in a more elegant posh like format')
    print(*list_nums, sep=', ') # this is a shortcut that places the list without commas

    print('Here is a closer statistical look at your list')
    print(f'The smallest number in your list is {min_num}.') # smallest number that is sorted in the range
    print(f'The largest number in your list is {max_num}') # largest number that is sorted in the range

    print('The total of all your numbers added up.')  # total added up
    for crap in range(len(list_nums) -1):
        print(list_nums[crap], end= ' + ')
    print(f'{list_nums[-1]} ={ total_of_num}')
        # prints the last number of the list
        # which is eqaul to the total amount of numbers

main()