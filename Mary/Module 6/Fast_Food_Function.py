"""
Mark Porraz
Prof. Lebens class
10/2/2024

this function adds ingredients to burgers
we are creating custom burgers by adding ingredients

Define a function to add ingredients to burgers
"""

# # Example 1: simple
# def add_ingredient(ingredient): # accepts pieces of input, called parameters
#     # Adds an ingredient to the virtual burger
#     print("Adding" + ingredient +" to your burger!")
#
#
# # how to call a function and make it do a task
# # everytime you call this, it will pass a different message
# add_ingredient("cheese")
# add_ingredient("lettuce")
# add_ingredient("bacon")


# Example 2: in depth
# step 1: Define a function to add ingredients to burgers
def add_ingredient(ingredient):  # accepts pieces of input, called parameters
    # Adds an ingredient to the virtual burger
    print("Adding " + ingredient + " to your burger!")


# how to call a function and make it do a task
# everytime you call this, it will pass a different message
add_ingredient("cheese")
add_ingredient("lettuce")
add_ingredient("bacon")


# step 2: calculate the price of the combo meal
def calculate_combo_price(burger_price, fries_price, drink_price):
    # calculates the total cost of a combo meal
    # assumes 8.5% tax
    subtotal = burger_price + fries_price + drink_price
    tax = 0.085 * subtotal
    total_cost = subtotal + tax
    print("Total combo price: $" + str(total_cost))


# call the function
burger_cost = 4.99
fries_cost = 2.49
drink_cost = 1.29
calculate_combo_price(burger_cost, fries_cost, drink_cost)


def order_decision():
    # Asks the user if the want to supersize their combo
    supersize = input("Would you like to supersize your combo?")
    # use a conditional statement (if statement)
    # to make a decision about their input
    if supersize.lower() == 'yes':
        print("GReat choice! Go big or go home")
    else:
        print("remember, life is short-go for the large fries!")


order_decision()
# base case in recusive function
# as long as there is another item, the function will continue to call things
# in other words, it keeps calling itself when the base case is true
# in this case it keeps calling itself until the base case is true
# the base case is that there are no more menu items in the list


def order_food(menu):
    if not menu:
        print("Your order is complete. Enjoy your meal!")
        return
    else:  # if the menu list is not empty, prompt the user to order
        print(" would you like to order a " + menu[0])  # remember that the menu is a list
        input()
        order_food(menu[1:])  # the function calls itself
        # it passes the menu list starting at the next item


# create a list of menus items and call the order_food function
menu_items = ["burger", "fries", "soda"]
order_food(menu_items)

#  f-strings do not work in trinket
