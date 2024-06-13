
while True:
    sentence = input('Please enter a full name for validation & correction: \n')
    if sentence.isnumeric():
        print('Invalid input. Please enter a full name consisting of letters only.')
        continue
    # if sentence < 0:
    #     print('ERROR, a name cannot be a negative number')
    #     continue
    else:
        break

full_name = sentence.title()
print(full_name)

# while True:
#    try:
#        sentence = input('Please enter a full name for validation & correction: \n')
#    except isnumeric():
#        print('Invalid input. Please enter a full name consisting of letters only.')
#        continue
#    else:
#        break
#
# if sentence = str():
#     full_name = sentence.title()
#     print(full_name)
# else:


# sentence = input(str('Please enter a full name for validation & correction: \n'))
# if sentence != str:
#     print('Try again, and enter a full name: ')
# else:
#     continue:
#
# full_name = sentence.title()
# print(full_name)
