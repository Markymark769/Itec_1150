"""
Here we are learning if else statements
Boolean logic

"""

# first create variable for taco ingredients
tortilla = True  # False  # note that true or false will give different results

# assigning a value of true to the variable tortilla
meat = "beef"  # indicates to the compiler that the data is going to be a string
cheese = False  # means that the customer wants cheese on their taco
salsa = "spicy"  #
guacamole = False
# a single = means a single operator

# Display a welcome message to the user
print('Welcome to Python\'s taco stand.')

# check if there is a tortilla
if tortilla:
    print('Great! We have a tortilla to start our taco.')
else:
    print('Oh no! We\'re out of tortillas. We cannot make a taco')

# Display meat option
if meat == "chicken":  # two equal signs mean a comparison operator, this means that you are comparing the value to
    # chicken
    print("Adding some delicious chicken to your taco")
elif meat == "beef":
    print("Beef it is, adding some juicy beef to your taco.")
elif meat == "pork":
    print("Pork fan, eh? Adding tasty pork to your taco.")
else:
    print("Looks like we are going vegetarian today.")  # this condition else exist if they choose any meat

# checking for the cheese and the type of salsa
if cheese:
    print("time for some cheese !")
    if salsa == "spicy":
        print("Adding extra cheese to balance out the spice for the taco.")
    else:
        print("Adding a normal amount of cheese.")
else:
    print("No cheese on this taco.")

# ingredients = tortilla + meat + cheese + salsa + guacamole
# ingredients = tortilla(int) + meat(int) + cheese(int) + salsa(int) + guacamole(int)
ingredients = 0
# check for at least 3 ingredients
if ingredients <= 3:
    # there are 3 ingredients
    print('you have at least 3 ingredients')
else:
    print('you do not have 3 ingredients')


