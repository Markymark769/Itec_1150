"""
Mark Porraz, 4/23/2023, mapit

"""
# ! python 3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip  # we need more than one command, so we can provide it to the mapit module
# below we are checking the command line arguments that we provide
if len(sys.argv) > 1:  # the number of arguments should be larger than 1. (import webbrowser, sys, pyperclip)
    # we are using the name of the program mapit.py
    # Get address from command line.
    address = ' Empire State Building'.join(sys.argv[1:])  # we are going to get all the number of arguments except for the 1st one
    # those arguments will return as a list
    # using the join command that will join them together as a string
    # each part of the address will be separated by a white space
else:
    # Get address from clipboard
    address = pyperclip.paste()  # if we do not provide an address, then we are going to go to the address provided in
    # the pyperclip module

webbrowser.open('https://www.google.com/maps/search/' + address)  # default address <<<--- replaced place with search
# we are passing the address and then appending the address next to it


# part 1
# in command line paste
# mapIt.py Empire State Building
# 870 Valencia St, San Francisco, CA 94110

# part 2
# write in notepad in the same folder the following:
# @py.exe D:\PycharmProjects\chapter12\mapit.py %*
# @pause


