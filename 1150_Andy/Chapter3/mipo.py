"""Mark Porraz, 2/19/2023, MIPO
This program is a skeleton of what most programs should look like. It
has four parts: main, input, processing, and output.
"""

print('This program calculates the volume of a box')


def main():  # main is the function# what is happening inside it will run the loop
    try:
        length, width, height = inputs()
        volume = processing(length, width, height)
        outputs(volume)
        restart = input('continue? Enter Y or N: ')
        if restart == 'y':
            print('OK, let\'s calculate the volume of another box.')
            main()
        else:
            print('Thank you for using the program.')
    except Exception as err:
        print(err)


def inputs():
    print('What is the length of the box? ')
    length = get_pos_int()
    print('What is the width?')
    width = get_pos_int()
    print('what is the height?')
    height = get_pos_int()
    return length, width, height


def get_pos_int():
    pos_int = input('Please enter a whole number: ')
    if pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a while number greater than 0: ')
    else:
        pos_int = int(pos_int)
    return pos_int


def processing(length, width, height):
    volume = length * width * height
    return volume
    # calculate_volume()


def outputs(volume):
    print(f'The volume of the box is: {volume} cubic units.')


main()  # call main
# lets the program run in loops

# code in progress
# try:
#     print("This program calculates the volume of a box")
#     length, width, height = inputs()
#     volume = processing(length,width,height)
#     outputs(volume)
#     again = input("continue? y or no ")
#     while again != ('y', 'Y', 'n', 'N'):
#         again = input("continue? Enter Y or N")
#     else:
#         if again == "y" or again == "Y":
#             main()
#         else: print("Thanks for using the program")
# except Exception as err:
#     print()


# correct code
# try:
#     length, width, height = inputs()
#     volume = processing(length, width, height)
#     outputs(volume)
#     restart = input('continue? Enter Y or N: ')
#     if restart == 'y':
#         print('OK, let\'s calculate the volume of another box.')
#         main()
#     else:
#         print('Thank you for using the program.')
# except Exception as err:
#     print(err)
