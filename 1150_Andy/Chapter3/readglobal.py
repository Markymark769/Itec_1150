"""Mark Porraz, 2/19/2023, global statement
homework, chapter 3, Functions
This program describes a function structure
Global Variables Can Be Read from a Local Scope
"""

def spam(): # spam function
    print(eggs)
eggs = 42
spam()
print(eggs)

# There is no parameter named eggs or assigns eggs a value
# in the spam() function.
# Python considers eggs as referencing the global variable and
# this is why only 42 is printed.