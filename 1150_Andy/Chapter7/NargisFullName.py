import re

while True:
    name_source = input('Enter full name in this format – first middle last')
    if name_source:
        first_name = name_source.group(1)
        middle_name = name_source.group(2)
        last_name = name_source.group(3)
        # return f"First Name: {first_name}, Middle Name: {middle_name}, Last Name: {last_name}"
        re.verbose()
        print(f"First Name:{first_name}, Middle Name: {middle_name}, Last Name: {last_name}")
        # return print(r'\n'.join(match))
    else:
        print("Invalid name format! 😕")



    # name_source = re.match(pattern, name_source)
    #
    # pattern = r'^(\w+)\s?(\w+)?\s?(\w+)?$'
    # name_source = re.match(pattern, name_source)
    # if match:
    #     first_name = match.group(1)
    #     middle_name = match.group(2)
    #     last_name = match.group(3)
    #     # return f"First Name: {first_name}, Middle Name: {middle_name}, Last Name: {last_name}"
    #     return f"First Name:{first_name}, Middle Name: {middle_name}, Last Name: {last_name}"
    #     # return print(r'\n'.join(match))
    # else:
    #     return "Invalid name format! 😕"


# Usage example
# name = "Nargis Farooq Khan"
# result = extract_name(name)
# print(result)