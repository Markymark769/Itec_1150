"""Mark Porraz, 2/19/2023, try except zero divide
homework, chapter 3, Functions
This program describes a function structure
Try and except statements
"""

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: # math error coded for
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0)) # division math error
print(spam(1))