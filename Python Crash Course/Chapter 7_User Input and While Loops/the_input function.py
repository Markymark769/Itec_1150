# How the input() fuction works
### The input() function pauses your program and waits for the user to enter some text.
### Once Python recieves the user's input, it assigns that input to a variable to make 
### it convenient for you to work with.

### The input() function takes one arguement: the prompt, or instructions, that we want 
### to display to the user.

### example 1 ###

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Writing Clear Prompts

### example 2 ###

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

### example 3 ### 

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to Accept Numerical Input

### example 4 ###

age = input("how old are you? ")
print(age)

### example 5 ###

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The Modulo Operator

### example 6 ###

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")