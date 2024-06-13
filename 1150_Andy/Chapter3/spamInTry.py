"""Mark Porraz, 2/19/2023, spamin try
homework, chapter 3, Functions
This program describes a function structure

"""

def spam(divideBy):  # spam as function
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

#(spam(1)) is never executed is because once
# execution jumps to code in the except clause, does not return to the try clause
# continues moving down the program