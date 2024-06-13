import re
name_source = input('Enter full name in this format – first middle last: ')
name_regex = re.compile(r'[A-Za-z]+(?:[-,\'][A-Za-z]+)?')
matches = name_regex.findall(name_source)

# [A-Za-z] - matches all instances of capital and lowercase letters
# ?: - non-capturing groups, this groups multiple tokens together without creating a capture group
# + - matching one or more preceding token or rule
# [-,\'] - matches hyphens and apostrophes.
# [A-Za-z] - matches all instances of capital and lowercase letters
# + - matching one or more preceding token or rule
# ? - match between 0 and 1 of the token before

if name_regex.match(name_source):
    print('This is a valid string')
    print('Here is the name:', name_source.title())

else:
    print('This does not look like a match')

# import re
#
# # Sample input string
# input_string = "John-Doe O'Connor Smith"
#
# # Regular expression pattern to match first name, middle name, and last name
# name_part = r"[A-Za-z]+(?:[-'][A-Za-z]+)?"
# pattern = re.compile(rf"^{name_part}(?:\s{name_part})?(?:\s{name_part})?$")
#
# # Check if the input string matches the pattern
# if pattern.match(input_string):
#     print("Input string is a valid full name.")
# else:
#     print("Input string is not a valid full name.")