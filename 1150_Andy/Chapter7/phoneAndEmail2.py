"""Mark Porraz, 4/2/2023, phone and email.py"""

#! python 3
# This program finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?  #seperator
    (\d{3})  # first three digits
    (\s|-|\.)  # seperator
    (\d{4})  #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
    )''', re.VERBOSE)
# TODO: Create email regex.
# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.

