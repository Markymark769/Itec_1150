"""Mark Porraz, 2/19/2023, Same name error
homework, chapter 3, Functions
This program describes a function structure

"""

def spam(): # spam as a function
    print(eggs) # ERROR! # thinks there is an assignment for eggs in spam
                # because print(eggs) is executed before assigned and no local variable
    eggs = 'spam local'

eggs = 'global'
spam()

# This error happens when you try to use a local variable in a function before you assign a value
# to it, as in the following program,