"""Mark Porraz, 3/18/2023,mclip.py"""
#! python 3
# bulletPointAdderr.py - adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()
# TODO: Separate lines and add stars.
# the to do comment is a reminder that you should complete this program
#eventually.
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] #add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)

