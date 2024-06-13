my_college = 'Minneapolis'
print(my_college)
for letter in my_college:
    print(letter)
print('Acronym = ' + my_college[0] + 'C')  # the [] refers to the number od the letter in minneapolis
print()

print('Here is the 12 times table: ')
for number in range(13):
    print(f'\t{number :>2d} times 12 is {number *12:>3d}')  # \t makes a tab  # the f in f-string stands for format
print('That\'s all folks!')


