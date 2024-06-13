"""1) text_validator.py – until now, we have not validated text
input. But some text inputs should follow a pattern. Write a
short program that defines and calls a text validation
function. Its purpose is to validate a full name or a book
title (pick one).
In your function definition, ask the user for input, then
use .split() on the string entered, to turn it into a list of
words. That way, you can use a loop to check each word,
and correct capitalization and spacing. Then, you will add
each corrected word back to a new string, and return.
Hint: Inside the loop, use conditional logic to determine the
right fix for each word. Parts of names should stay in lower
case, like van, der, de or di. In book titles, prepositions and
articles are lower case, UNLESS they are the first word.
Tricky!? Slides 15 & 17 of the lesson PPT may help"""

def main():
    choice = ""
    valid_choices = ["N", "n", "T", "t"]
    while not (choice in valid_choices):
        choice = input("Do you want to validate a name (enter N) or a title (enter T)? ")

    if choice == "N" or choice == "n":
        name_input = get_input("Welcome to the name validation program", "full name")
        split_name_list = name_input.split(" ")
        print(split_name_list)
        corrected_name = validate_name(split_name_list)
        print_results("full name", corrected_name)
    elif choice == "T" or choice == "t":
        title_input = get_input("Welcome to the title validation program", "title")
        split_title_list = title_input.split()
        corrected_title = validate_title(split_title_list)
        print_results("title", corrected_title)


def get_input(input_string, input_type):
    print(input_string)
    user_input = ""
    while len(user_input) < 1:
        user_input = input("Please enter a " + input_type + " for validation and correction: ")
    return user_input


def validate_name(split_name_list):
    name_article_list = ["van", "de", "der", "di"]
    name_string = ""
    for word in split_name_list:
        name = word
        if name not in name_article_list:
            name = name.capitalize()
        name_string += name + " "
    return name_string


def validate_title(split_title_list):
    title_string = ""
    prepositions = ["of","in","at","into","to","off","under","upon","over","with","within","by","down","from","over","near"]
    # there are more but this is a good list to begin with
    articles = ["a", "an", "the"]
    uppercase = []
    for word in split_title_list:
        if not(word in prepositions or word in articles):
                uppercase.append(word.capitalize())
        else:
            uppercase.append(word)
    print (uppercase[0])
    uppercase[0] = uppercase[0].capitalize()
    title_string = " ".join(uppercase)
    return title_string


def print_results(type, corrected_string):
    print("The corrected " + type + " is: " + corrected_string)


main()