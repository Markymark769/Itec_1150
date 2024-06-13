# Function - 

# needed when need to perform a task multiple times throughout
# your program, you dont need to type all the code for the same task 
# again and again; you just call the fucntion dedicated to handling the
# task, and the call tells Python to run the code  inside the function.

# Modules - storing functions in seperate files to help organize our
# main program files.

# Defining a Function
# a simple function called greet_user() that prints a greeting. 
###########################
#def  greet_user():
#    """"Display a simple greeting."""
#    print("Hello!")

#greet_user()
############################
# Passing Information to a Fucntion
def  greet_user(username):
    """"Display a simple greeting."""
    print(f"Hello,{username.title()}!")

greet_user('Ally Monster')

#Arguements and Parameters
# the variable username in the definition of greet_user() is an example of a parameter, a piece of information
# the function needs to do the job. The value 'jesse' is the arguement. An arguement is a piece of information
# that is passed from a function call to a function. 

# Jesse was passed to the function greet_user(), and the value was assigned to the parameter username.