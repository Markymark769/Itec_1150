"""
Mark Porraz
10/31/2023
Regular Expressions
This is pattern matching - this is finding needles in haystacks
you would find things like phone numbers, social security numbers, or other data

It usually has an exchange or an extension

we can find digits, strings, or NONE objects

resource:
https://pythex.org/
http://www.pyregex.com/
https://www.pythoncheatsheet.org/cheatsheet/regular-expressions
"""
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')  # note the \d\d\d is the pattern that
# you want to look for and match
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
'(415)'
mo.group(2)
'555-4242'

# we can put formats infront of strings.
# we can put an "r" in front so you do not have to double escape characters

print(re.search("\d{3}-\d{3}-\d{4}","Do not call 612-555-1212, no one will pick up."))

# the plus sign says repeat it one or more times
print(re.search("\d{3}-\d{3}-\d{4}","Do not call 612-555-1212, Call 800-223-4567."))
print(re.findall("\d{3}-\d{3}-\d{4}","Do not call 612-555-1212, Call 800-223-4567."))
# findall is a great tool to get the pieces that you need out of there.

