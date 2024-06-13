"""Mark Porraz, 2/19/2023, same name local global
homework, chapter 3, Functions
This program describes a function structure
The global statement
"""

def spam(): # spam as a function
    global eggs
    eggs = 'spam' # this is the global

def bacon(): # bacon as a function
    eggs = 'bacon' # this is a local

def ham(): # ham as a function
    print(eggs) # this is the global

eggs = 42 # this is the global, no global or assignment statement
spam()
print(eggs)

# 4 rules to tell whether a variable is in a local scope or global scope:
# If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
# If there is a global statement for that variable in a function, it is a global variable.
# Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
# But if the variable is not used in an assignment statement, it is a global variable