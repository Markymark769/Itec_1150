#Passing a List
### when you pass a list to a function, the function gets direct access to the
### of the list.
### passing a list to a function, by: names, numbers, or more complex objects, 
### such as dictionaries.
###### Example 1 ######
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
### every user sees a personalized greeting, and you can call the function any
### time you want to greet a specific set of users.


#Modifying a List in a Function
### when you pass a list to a function, the function can modify the list. Any
### changes made to the list inside the function's body are permanent, allowing
### you to work efficiently even when you're dealing with large amounts of data. 

###### Example 2 ######
# Start with some designs that need to be printed.

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

# Stimulate printing each design, until none are left.
# Move each design to completed_model after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()

    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

###### Example 3 ######
def print_models(unprinted_designs, completed_models):
    """
    Stimulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Preventing a Function from a Modifying a List
### sometimes you would want to prevent a function from being modified
### you can send a copy of a list to a function like this:
# function_name(list_name[:])
# print_models(unprinted_designs[:], completed_models) 