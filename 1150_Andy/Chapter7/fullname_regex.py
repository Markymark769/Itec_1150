# # """
# # Mark Porraz, 5/2/2023, fullname_regex.py
# # this program 'Enter full name in this format – first middle last'
# # it validates to only accept names.
# # """
# #
# # import re  # import regex
# #
# # while True:
# #     name_source = input('Please enter your full name in this format - first middle last: ')
# #     if re.search(r'[^A-Za-z\s]+ [-,\'] ', name_source):  # if the name does not match criteria,
# #
# #         # print the following validation.
# #         # ^ match the beginning of each string of the search
# #         # [A-Za-z] - the character class a-z, both capital and not capital
# #         # \s - any character Not in \s
# #         print('That doesnt look like a full name. Please enter a full name consisting of letters only.')
# #         # validation prompt
# #     else:
# #         break  # break and print the following name printed.
# # print('Here is the name:', name_source.title())  # prints name_source in title case.
# #
# #
# import re
#
# # Regular expression pattern to match potential full names with hyphens
# name_source = input('Enter full name in this format – first middle last: ')
#
# # Regular expression to match names with first, middle, and last names
# name_regex = re.compile(r'[A-Z][a-z]+[-,\']?[A-Z][a-z]+[-,\']?[A-Z][a-z][-,\']+')
#
# # Find all matches in the input
# matches = name_regex.findall(name_source)
#
# # Display the matches found
# if matches:
#     print("Here are the names found:")
#     for matches in matches:
#         print(name_regex)
# else:
#     print("This doesn't look like a name.")

import re

while True:
    # Ask the user to enter the source text
    source_text = input('Enter the source text to search: ')

    # Regular expression pattern to match potential full names with hyphens
    name_regex = re.compile(r'[A-Z][a-z]+(?:-[A-Z][a-z]+)?(?:\s[A-Z][a-z]+(?:-[A-Z][a-z]+)?){1,2}')

    # Find all matches in the input
    matches = name_regex.findall(source_text)

    # Display the matches found
    if matches:
        print("Here are the names found:")
        for match in matches:
            print(match)
    else:
        print("No names found in the source text.")
        break
