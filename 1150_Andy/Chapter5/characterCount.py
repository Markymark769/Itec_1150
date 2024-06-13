""" Mark Porraz, 2/28/2023, Character Count
Homework file for chapter 5

This program demonstrates that the setdefault() method is a nice shortcut to ensure that a key exists.
"""

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) # The program loops over each character in the message variable’s string,
                                   #counting how often each character appears
    count[character] = count[character] + 1 # The setdefault() method ensures that the key is in the count dictionary
    # (with a default value of 0) so the program does not throw a KeyError error when
    # count[character] = count[character] + 1 is executed

print(count)