# sandwich.py – follow the instructions below. You may adjust the food items to include your personal favorites.
# • It uses all of our standard mipo_ex features.
# • The menu should have numbered or letter options.
# Sandwich Maker: Write a program that asks users for their sandwich preferences. The program should use
# PyInputPlus to ensure that they enter valid input, such as:
# • Using inputMenu() for a bread type: wheat, white, or sourdough.
# • Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# • Using inputYesNo() to ask if they want cheese.
# • If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# • Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# • Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
# Come up with prices for each of these options, and have your program display all the
# choices and their prices plus a total cost at the very end.

import pyinputplus as pyip

def main():
    menu() # print the menu
    bread, filling, cheese, mayo, mustard, lettuce, tomato, quantity = inputs()
    sandwich_price, total_price = processing(bread, filling, cheese, mayo, mustard, lettuce, tomato, quantity)
    outputs(bread, filling, cheese, mayo, mustard, lettuce, tomato, quantity, sandwich_price, total_price)

def getprice(food_string):
    prices = {
        'wheat': 2.00,
        'white': 2.00,
        'sourdough': 3.00,
        'chicken': 3.00,
        'turkey': 3.00,
        'roasted veg': 3.50,
        'tofu': 2.50,
        'cheddar': 1.50,
        'Swiss': 1.50,
        'mozzarella': 1.50,
        'none': 0
        }
    return prices[food_string]

def format_price(input_food):
    price = getprice(input_food)
    return format(price, ".2f")

def menu():
    # print the menu with prices
    print()
    print("Welcome to pySandwich!")
    print()
    print("Menu")
    print()
    print("Bread options")
    print("Whole wheat: $", format_price('wheat'), "  White: $", format_price('white'), "  Sourdough: $", format_price('sourdough'))
    print()
    print("Filling options")
    print("Chicken: $", format_price('chicken'), "  Turkey: $", format_price('turkey'), "  Roasted veg: $", format_price('roasted veg'), "  Tofu: $", getprice('tofu'))
    print()
    print("Cheese options")
    print("Cheddar: $", format_price('cheddar'), "  Swiss: $", format_price('Swiss'), "  Mozzarella: $", format_price('mozzarella'))
    print()
    print("Condiment options: mayonnaise, mustard, lettuce, and tomato $0.50 each")
    print()

def inputs():

    bread = pyip.inputMenu(prompt="What bread would you like?\n ", choices=['wheat','white','sourdough'],default=0,numbered=True)
    filling = pyip.inputMenu(prompt="What filling would you like?\n", choices=['chicken','turkey','roasted veg','tofu'],default=0, numbered=True)
    option = pyip.inputYesNo(prompt="Would you like cheese?  Enter yes or no.", limit=2)
    if option.upper() == "YES":
        cheese = pyip.inputMenu(prompt="What cheese would you like?\n", choices=['cheddar','Swiss','mozzarella'],default=0,numbered=True)
    else:
        cheese = 'none'
    mayo = pyip.inputYesNo(prompt="Would you like mayonnaise?  Enter yes or no: ")
    mustard = pyip.inputYesNo(prompt="Would you like mustard?  Enter yes or no: ")
    lettuce = pyip.inputYesNo(prompt="Would you like lettuce?  Enter yes or no: ")
    tomato = pyip.inputYesNo(prompt="Would you like tomato?  Enter yes or no: ")
    quantity = pyip.inputInt(prompt="How many of this sandwich would you like? ", min=1)

    return bread, filling, cheese, mayo, mustard, lettuce, tomato, quantity


def processing(bread, filling, cheese, mayo, mustard, lettuce, tomato, quantity):
    sandwich_price = 0.0
    sandwich_price += getprice(bread)
    sandwich_price += getprice(filling)
    sandwich_price += getprice(cheese)
    if mayo.upper() == "YES":
        sandwich_price += 0.50
    if mustard.upper() == "YES":
        sandwich_price += 0.50
    if lettuce.upper() == "YES":
        sandwich_price += 0.50
    if tomato.upper() == "YES":
        sandwich_price += 0.50
    total_price = sandwich_price * quantity
    return sandwich_price, total_price


def outputs(bread, filling, cheese, mayo, mustard, lettuce, tomato, quantity, sandwich_price, total_price):
    print()
    print("Thank you for your order!")
    print("You requested ", quantity," of this sandwich: ")
    print(bread)
    print(filling)
    if cheese != "none":
        print(cheese)
    print("with these condiments: ")
    if mayo.upper() == "YES":
        print("mayo")
    if mustard.upper() == "YES":
        print("mustard")
    if lettuce.upper() == "YES":
        print("lettuce")
    if tomato.upper() == "YES":
        print("tomato")
    print()
    print("The cost per sandwich is $", format(sandwich_price, ".2f")," and your total cost is $", format(total_price, ".2f"))


main()