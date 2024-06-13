""" Mark Porraz, 2/28/2023, birthdays
Homework file for chapter 5
"""
# creates a dictionary and store it at birthdays
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}  # this is a dictonary, it is specified by
# curly brackets

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
# You can see if the entered name exists as a key in the dictionary with the in keyword
    if name in birthdays: # You access the value using square brackets,
        # in this example it is name associated with [name]
        print(birthdays[name] + ' is the birthday of ' + name)  # If the name is in the dictionary,
        # you access the associated value using square brackets
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday # If the name cannot be accessed from the list above, you can add it to the list.
        print('Birthday database updated.')
# all the data you enter in this program is forgotten when the program terminates
# e.g. in textbook eva is forgotten along with her birthday of december 5.
