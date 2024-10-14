# Module 5 Coding Challenge
# Kieran Hanson
# Last Updated 9/26


# Start with Import Random

import random

# Create a dad joke list
dad_jokes = ["Of all the inventions of the last 100 years, the dry erase board has to be the most remarkable. ",
             "Where do pirates get their hooks? Second hand stores. ",
             "I hate my job—all I do is crush cans all day. It’s soda pressing. ",
             "How do cows stay up to date? They read the Moo-spaper.",
             "I just found out I’m colorblind. The news came out of the purple!",
             "How does cereal pay its bills? With Chex.", "I don't trust stairs. They're always up to something.",
             "Never date a tennis player. Love means nothing to them.",
             "I used to hate facial hair, but then it grew on me.",
             "What’s an astronaut’s favorite part of the computer? The Space Bar.",
             "Why was 2019 afraid of 2020? Because they had a fight and 2021.",
             "Ever since we started quarantining, I've only been telling inside jokes.",
             "Why did the Invisible Man turn down a job offer? He couldn’t see himself doing it.",
             "What do you call a sad cup of coffee? Depresso.",
             "What happens when frogs park illegally? They get toad."]

# Print welcome message
print("Welcome to the Dad Joke Generator!")
# Ask if they want to hear some dad jokes, create that yes_no variable
yes_no = input("Would you Like to hear some dad jokes?")
# Time for the if else statement, use .lower() to make sure it still goes through if they type in lowercase!
if yes_no.lower() == "yes":
    print("Okay perfect!")
# Else statement prints message and end the code with an exit()
# if they typed yes, it will continue down the line of code!
else:
    print("That's okay, not everyone has a good sense of humor!")
    exit()

# Use the print function start with quotes, add len(dad_jokes) this will tell the user the number of dad jokes in the list
# Add the comma's to make a space between we have, the number, and Dad Jokes!
print("We have", len(dad_jokes), "Dad Jokes!")

# Time for the for loop
# set the range to 4
# rj (random joke) is the variable name for the random.choice
# In random.choice() set variable dad_jokes in the quotes
# Print (rj) calls the loop to print four random jokes out of the list we made
for i in range(4):
    rj = random.choice(dad_jokes)
    print(rj)

# Create another user input variable, very original use of y_n
y_n = input("Would you like some more jokes? ")
# Use a while loop(with a .lower() incase they use lowercase) to print another random joke if they said yes
while y_n.lower() == "yes":
    rj = random.choice(dad_jokes)
    print(rj)
# To not get stuck in an infinite while loop, ask them for y_n again! Pesky infinite loops had me stuck for a few minutes lol
    y_n = input("Would you like some more jokes? ")
# Else end with a thank-you statement!
# else:
print("Thanks for enjoying the dad jokes!")
# And scene

