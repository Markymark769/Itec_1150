from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break

    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

### This program imports get_formatted_name() from the file name_function.py. The
## user can enter a series of first and last, and see the formatted full names
## that are generated. 

### after testing the program we see that the names are correct, but now we want to modify 
### get_formatted_name() for middle names. however, we do not want to break the format.


# Unit Tests and Test Cases 
### The module unitest is a standard for testing your code.
### Unit test - verifies that one specific aspect of a funcitons behavior is correct.

### Test Case- is a collection of unit tests that together prove that a function behaves 
### the way that it is supposed to.

### Full Coverage - includes a full range  of unit tests covering all the possible ways you
### can use a function. 

###### It is a good practice to impliment tests in code

#Passing a syntax
### The syntax for setting up a text case takes some getting used to, but once you've set up
### the testcase its common sense to add more unit tests for the functions. To writea test case
### for a function import the function you want to test. Then create a class that inherits from
### unitest.TestCase, and write a series of methods to test different aspects of your functions
### behavior.
