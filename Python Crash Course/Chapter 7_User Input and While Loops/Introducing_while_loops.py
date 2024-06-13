# The While Loop in Action
### The for loop takes a collection of items and executes a block of code
### for each item in the collection. In contrast, the while loop runs as 
### long as or while, a certain condition is true. 
### example 1 ###
from email import message


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit
### example 2 ###

### we can make the program run longer as the user wants by putting
### most of the program in a while loop. we'll define the quit value
### and then keep the program as long as the user has not entered the
### quit value.

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program."

#message = ""
#while message != 'quit':
#    message = input(prompt)
    
#    if message != 'quit':
#        print(message)
# Using a Flag
### The variable, flag, acts as a signal to the program. we set programs
### to run while the flag is set to True and stop running when any of
### several events sets the value of the flag to false.

### Overall the while statement needs to check only one condition: whether
### of not the flag is true.

### example 3 ###

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program."

#active = True
#while active:
#    message = input(prompt)

#    if message == 'quit':
#        active = False
#    else:
#        print(message)
# Using break to Exit a Loop
### to exit a while loop immediately without running any remaining code in
### loop, regardless of the results of any conditional test, use the break statement.
### The break statement directs the flow of your program; you can use it to control
### which lines of code are executed and which are not, so the the program only 
### executes the code that is needed

#### example 4 ####
#prompt = "\nPlease enter the name of the city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.)"

#while True:
#    city = input(prompt)

#    if city == 'quit':
#        break
#    else:
#        print(f"I'd love to go to {city.title()}!")

# Using Continue in a Loop
### instead of breaking out of the code, you can use the continue statement to return to the
### beginning of the loop based on the result of the conditional test. 
##### example 5 ######
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding Infinite Loops
#### example 6 ####
x = 1
while x <= 5:
    print(x)
    x +=1
#### example 7 ####
### This loop run forever!
#x = 1
#while x < 5:
#    print(x)
### every programmer accidentally writes an infinite while loop  
###