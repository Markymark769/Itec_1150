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
    # create an empty dictionary, one that we want to fill from our shelve file
  #  my_data = {}
    cached = False  # by default, we haven't used cached data yet
    directory = 'test_shelve'
    # if the directory doesn't exist ...
    if not os.path.exists(directory):
        # ... try to create it
        try:
            os.makedirs(directory)
        except IOError:
            print(f'IOError: Unable to create the directory "{directory}"')

    # if it's there, let's go into it
    os.chdir(directory)
    # .now() is a datetime object that represents the current date/time
    now = datetime.now()
    # strftime formats dates into strings.
    # More info here: https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior
    # %Y = year, %m = month %d = day
    now_string = now.strftime('%Y-%m-%d')  # the ISO 8601 standard
    # see https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates
    # setup a filename in the format test_2024-07-12.db
    filename = f'test_{now_string}'
    # do we have a cache file for today?
    shelf = shelve.open(filename)
    # get the data from the shelf
    my_data = shelf.get('my_data')  # we specifically want the my_data variable from the shelve
    # if there is a cache file, tell the user
    if my_data:  # dictionaries with data are True
        print(f'Using cached data from the file {filename}')
        cached = True  # since we DID use cached data, update our variable
    else:  # dictionaries without data are False
        print('Initializing my_data ...', end='')
        # set the my_data variable to default / initial values
        my_data = {1: 'shelve is a great library', 'data': [42, 17, 64], 'coupling': 0.0072993}
        print(' DONE')

    # print what we have
    print_dict(my_data)
    # do something with my_data
    description = input('Enter today\'s new description: ')
    my_data[1] = description
    # print what we have now
    print_dict(my_data)

    # If we didn't get my_data from our daily shelve cache it could be that there
    # was no cache OR it was the very first time that we're running the program.
    # Regardless, if there is no cache file for today, it's time to create one
    if not cached:
        # tell the user we're now going to cache the data
        print(f'Caching my_data to the shelve called {filename}:...', end='')
        shelf['my_data'] = exchange_rates
        print(' DONE')
    shelf.close()  # Remember to close your shelf


def print_dict(the_dict):
    for key, value in the_dict.items():
        print(f'{key}: {value}')


main()  # Remember to call main() otherwise your program won't run