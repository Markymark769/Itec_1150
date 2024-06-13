# We want user input like -12.34 to be recognized as a number! Write a program using regex that can identify
# input of numerals that may or may not have a minus sign (–) in the first position, and may or may not have
# one decimal (.). It's the long-awaited float validation!

import re
run_again = True
print("This code validates float-format numbers.")
while run_again:
    number = input("Enter the number would you like to validate: ")
    float_match = re.search(r"(^-?\d+(\.\d+)?$)", number)
    # -? allows for optional negative
    # \d matches one or more digits - can have digits before the decimal point
    # (\.\d+)? optional decimal point and additional digits

    if float_match:
        print(number, " is a floating point number.")
    else:
        print(number, " is not a floating point number")

    again = input("Enter 'Y' to run again.")
    if again != "Y" and again !="y":
        run_again = False

