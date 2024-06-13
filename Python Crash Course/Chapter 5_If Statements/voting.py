# If Statements
# Simple if Statements 
### The simplest kind of if statements has one test and one action
###
#if conditional_test
#    do something
### you can put any conditional test in the first line, then any action in the indented block following the test
#### true -- the code is executed following the if statement
#### false -- the code is ignored following the if statement
age = 19
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet?")
### indentation plays the same role as it did for loops
### many lines of code cand be added after the if statement
# If-else Statements
### take one action when a conditional test passes and a different action in all other cases.
### allows you to define any action  that is executed when the conditional test fails.
age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet?")
else:
    print("sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")