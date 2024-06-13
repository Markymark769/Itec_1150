import random
print('Welcome to our random number game! Let\'s count some numbers')
def main(): # main is the function # tells us what is happening inside loop
    try:
        num_list = inputs() # output variables into small and large
        list_of_nums.sort()
        total_nums, min_num, max_num = processing(list_of_nums)
        outputs(list_of_nums, total_nums, min_num, max_num)
        restart = input('would you like to continue? Enter Y or N: ')
        if restart == 'y':
            print('OK, let\'s make another list!')
            main()
        else:
            print('Thanks for using our program!')
    except Exception as err:  # The except block
        print(err)


def inputs():
    print('Alright! Let\'s begin.')
    num_of_nums = get_pos_int()
    num_list = []
    for thing in range(num_of_nums):
        thing = random.randint(0, 20)
        num_list.append(thing)
    return num_list


def get_pos_int():
    pos_int = input('How many numbers do you want the computer to pick for your list?: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Please enter a whole number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


def processing(num_list):
    total = 0
    for stuffs in range(len(num_list)):
        total += num_list[stuffs]
    min_num = num_list[0]
    max_num = num_list[-1]
    return total, min_num, max_num


def outputs(list_nums, total_nums, min_num, max_num):
    print('Ok, here\'s your list of numbers! We sorted them for your convenience. You\'re welcome.')
    print(list_nums)
    print('Here\'s your list again, this time printed with a fancy lil\' shortcut method so there\'s no ugly brackets!')
    print(*list_nums, sep=', ')
    print('We\'ve got some stats for you about your list too!')
    print(f'The smallest number in your list is {min_num}.')
    print(f'The largest number in your list is {max_num}.')
    print('AND, here\'s all your numbers added up!')
    for stuffs in range(len(list_nums) - 1):
        print(list_nums[stuffs], end=' + ')
    print(f'{list_nums[-1]} = {total_nums}')
main()
