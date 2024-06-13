"""Mark Porraz, 2/19/2023, other local scopes
homework, chapter 3, Functions
This program describes a function structure.
Local Scopes Cannot Use Variables in Other Local Scopes
"""

def spam(): # spam function is called the other local functions below are created
    eggs = 99 ## local vairbale is set to 99
    bacon()
    print(eggs)

def bacon(): # bacon fuction is called the other local functions are created
    ham = 101
    eggs = 0 # local variable is set to 0

spam()

# Local variables in one function are completely seperate
# from the local vairables in another function.