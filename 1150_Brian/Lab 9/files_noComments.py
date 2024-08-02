"""
MArk Porraz
Brian's class
ITEC 1150
Lab 9 Files


code from Stack Overflow
https://stackoverflow.com/questions/920645/when-to-use-while-or-for-in-python
"""

"""
Brian Huilman
ITEC 1150
Shelve and Date

This program is an example of how to use the shelve module as well as how to create
a filename based on today's date, read a stored variable from that shelve file, and
write a variable back to the shelve file.
"""

import os
from datetime import datetime
import shelve


def main():

    my_data = {}
    cached = False
    directory = 'test_shelve'
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except IOError:
            print(f'IOError: Unable to create the directory "{directory}"')
    os.chdir(directory)
    now = datetime.now()
    now_string = now.strftime('%Y-%m-%d')
    filename = f'test_{now_string}'
    shelf = shelve.open(filename)
    my_data = shelf.get('my_data')
    if my_data:
        print(f'Using cached data from the file {filename}')
        cached = True

    else:
        print('Initializing my_data ...', end='')
        my_data = {1: 'shelve is a great library', 'data': [42, 17, 64], 'coupling': 0.0072993}
        print(' DONE')
    print_dict(my_data)
    description = input('Enter today\'s new description: ')
    my_data[1] = description
    print_dict(my_data)


    if not cached:
        print(f'Caching my_data to the shelve called {filename}:...', end='')
        shelf['my_data'] = exchange_rates
        print(' DONE')
    shelf.close()


def print_dict(the_dict):
    for key, value in the_dict.items():
        print(f'{key}: {value}')


main()