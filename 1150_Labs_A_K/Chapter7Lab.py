# fullname_regex.py – Ask the user to enter the source text to search, such as the name_source variable here:
# name_source = input('Enter full name in this format – first middle last').
# Then, you can adapt the first two code lines from lesson slide 13, to search this new source.
#        bat_regex = re.compile(r'Bat(wo)+man') # establish pattern with one or more wo's
#        source_bat2 = bat_regex.search('Where does Batwoman live') # source to search in
# Edit the code to match the new situation and change the regex pattern
#   to identify text that could be a full name.
# Hints: Initially write your regex pattern to check if the user enters three words separated by a space. Then, strive
# to make the regex adaptable if the person's full name has more than or less than 3 words. Then, think about allowing
# (not requiring) common characters like a period, hyphen or '. Slides 11-13 should be helpful.
#        phone_regex = re.compile(r'.?(\d\d\d)?-?(\d\d\d-\d\d\d\d)') # pattern with optional characters and group
#        '?' for optional
#        Match zero or more occurrences of the preceding group by using the star character
#        bat_regex = re.compile(r'Bat(wo)*man') # establish pattern with zero or more wo's
# For printing, end with a conditional block that provides an appropriate message if there is a match or not.

import re

def main():
    print("This program will determine if text entered could possibly be a name.")
    name_string = inputs()
    name_match = processing(name_string)
    outputs(name_match, name_string)

def inputs():
    name_string = ""
    while name_string == "":
        name_string = input("Enter the full name, first middle last: ")
    return name_string

def processing(name_string):
    name_match = re.search(r"(^[a-zA-Z'-]+(\s+[a-zA-Z'-]+)*$)", name_string)
    # tested at regexr.com

    # print(name_match)
    return name_match


def outputs(name_match, name_string):
    if name_match:
        print("Here is the name: ", name_string)
    else:
        print("This doesn't look like a name.")


main()