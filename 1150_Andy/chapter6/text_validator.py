"""
Mark Porraz, 4/19/2023, text_validator
This program defines and calls a text validation function.
Its purpose is to validate a full name or a book title (only one).
This function asks the user for input then uses the .split() method.
"""

# TODO: slide 15 and 17 will help.
print('Welcome to the name validation program.')

def block():
    while True:
        sentence = str(input('Please enter a full name for validation & correction: \n'))
        if sentence.isnumeric():
            print('Invalid input. Please enter a full name consisting of letters only.')
            continue
        if sentence != str:  # wrong: if sentence <0 :
            print('ERROR, a name cannot be a negative number')
            continue

        else:
            break

    full_name = sentence.title()
    print(full_name)

block()



