"""Mark Porraz, 2/19/2023, global statement
homework, chapter 3, Functions
This program describes a function structure
"""


# a global statement is used when a global variable is needed
# within a function, or needs to be modified.

# eggs refers to the global variable, so
# don’t create a local variable with this name.

def spam():  # function spam
    global eggs  # global variable is declared
    eggs = 'spam'  #

eggs = 'global'
spam()
print(eggs)