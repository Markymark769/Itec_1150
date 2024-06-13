# Testing Multiple Conditions
### the if-elif-else chain is only appropriate to use when you only need
### one test to pass. As soon as the criteria is met, it skips the rest
### of the tests. 

#example 1
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

### The test for the mushrooms is the first test to pass, so it is added 
### to the pizza. However, the values extra cheese and pepperoni are never
### checked. This is due Python not running anything beyond the first test
### to pass.
# example 2
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#Using if Statements with Lists
#Checking for special items
### This is simiilar to the bmw example in checking for special characters,
### and if it is needed to be printed differently. 
# example 3
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# example 4
### If -checks to see if the person requested green peppers, the message
### is displayed informing them why they can't have green peppers. 
### else: ensures all the other toppings will be added to the pizza
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding{requested_topping}.")

print("\nFinished making your pizza!")

# Checking That a List Is Not Empty
### Letting users provide the information that is stored on the list below.
### We need to check if the list is empty before running a loop. 
# example 5
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Using Multiple Lists
### 
### The following example defines two lists. The First list is of avilable toppings. 
### The second is the list of toppings the user has requested.
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")