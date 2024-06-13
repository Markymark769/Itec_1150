""" Mark Porraz, 2/28/2023, Pretty Character Count
Homework file for chapter 5

This program demonstrates that the setdefault() method is a nice shortcut to ensure that a key exists.
"""

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count ={}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count.values())
