"""Mark Porraz, 2/19/2023, local global
homework, chapter 3, Functions
This program describes a function structure.
Local and Global Variables with the Same Name
"""
# there are three local variables names eggs which gets confusing to decipher

def spam(): # spam as a funtion
    eggs = 'spam local'
    print(eggs)    # prints 'spam local'

def bacon(): # bacon as a function
    eggs = 'bacon local'
    print(eggs)    # prints 'bacon local'
    spam()
    print(eggs)    # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)        # prints 'global'

# variable eggs exists in local scope when spam() is called
# variable eggs exists in local scope when bacon() is called
# variable eggs exists in the gloabal scope