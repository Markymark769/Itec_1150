# Passing an Arbitrary Number of Arguements
### sometimes you won't know ahead of time how many arguements a function needs to accept.
### Python allows a function to collect an arbitrary number of arguements from the calling
### statement.

                            ### example 1 ####
### this can be used to get a person toppings when you dont know the number of toppings a 
### person will wnant.
### the asterisk *topping cells python to make an empty tuple called topppings and pack what
### ever values it recieves into this tuple.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

### we can replace the print() call with a loop that runs through the list of toppings and
### describes the pizza being ordered:
                            #### Example 2 #####
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# Mixing positional and Arbitrary Arguements
### If you want a function to accept several different kinds of arguements, the
### parameter that accepts an arbitrary number of arguements must be placed last 
### in the function definition. Python matches positional and keyword arguements
### first and then collects any remaining arguements in the final parameter.
                            #### Example 3 #####

def make_pizza(size,*toppings):
    """"Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}- inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')

# Preventing a Function from modifying a List
### Sometimes you'll want to accept an arbitrary number of arguements, but you won't 
### know ahead of time what kind of information will be passed to the function. 
### You can write fucntions that accept as many key-value pairs as the calling 
### statement provides.
                            #### Example 4 #####

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',
                           location= 'princeton',
                           field= 'physics')
print(user_profile)
