# Using a while Loop with Lists and Dictionaries
### 
# Moving Items from One List to Another
# start with users that need to be verified, and an empty list
# to hold confirmed users.

#### example 1 ####
from http.client import responses
from timeit import repeat
from unicodedata import name
from urllib import response


unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user : {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Removing All Instances of Specific VAlues from a List
#### example 2 ####
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a Dictionary with User Input
responses = {}
#### set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and response
    name = input("\nWhat is your name?")
    responses = input("which mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("would you like to let another person respond? (yes/ no)" )
    if repeat == 'no':
        polling_active = False

# polling is complete. Show the results.
print("\n---Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")