"""Mark Porraz, 2/19/2023, zero divide
homework, chapter 3, Functions
This program describes a function structure

"""

# a math error happens due to division by zero

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0)) ## cannot divide by Zero
print(spam(1))