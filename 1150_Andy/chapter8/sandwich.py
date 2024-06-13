""" Mark Porraz, 4/11/2023, sandwich.py.
This program asks the user for their sandwich preferences.
This program uses pyinputplus for validation, displays the prices for each
of these option, displays all choices made, plus a total cost at the very end.

You can set dictionary to match each ingredient choice and its price.
It's much easier to bring the price value for calculating or displaying
output with dictionary than define prices for each item separately

"""

import pyinputplus as pyip


def main():
    print('Welcome to the best average sandwich shop!')

    price_list = {'wheat': '1.50', 'white': '1.50', 'sourdough': '1.50',
                  # both the keys and values are placed in dict
                  'chicken': '2.00', 'turkey': '2.00', 'ham': '2.00', 'tofu': '3.00',
                  'cheese': '1.50', 'swiss': '2.00', 'mozzarella': '1.50',
                  'mayo': '0.25', 'mustard': '0.25', 'lettuce': '0.25', 'tomato': '0.25'}
    # the ingredient is the key and the cost is the value of this dictionary.

    sandwich_number, bread, protein, cheese, condiments = inputs()
    # the input for the number of sandwiches and ingredients.
    bread_cost, protein_cost, cheese_cost, condiments_cost, subtotal, total \
        = processing(price_list, bread, protein, cheese, condiments, sandwich_number)

    outputs(bread, protein, cheese, condiments, sandwich_number, bread_cost, protein_cost,
            cheese_cost, condiments_cost, total)
    restart = input('Continue? Enter y or n: ')
    if restart == 'y':
        print('OK, let\'s process more books.')
        main()
    else:
        print('Thanks for using the program.')


def inputs():  # create list [] to pull out the key value from dictionary
    sandwich_number = pyip.inputInt(prompt="Enter the number of sandwiches you want: ")
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])  # input choice of bread type desired
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])  # input choice of protein type desired
    cheese = pyip.inputYesNo('Would you like cheese? Please enter: Yes or No ')  # yes or no choice
    if cheese == 'yes':
        cheese = pyip.inputMenu(['cheese', 'swiss', 'mozzarella'])  # input choice of cheese type desired
    else:
        cheese = 'no cheese'
    condiments = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])  # input choice of condiment type desired
    return sandwich_number, bread, protein, cheese, condiments


def processing(price_list, bread, protein, cheese, condiments, sandwich_number):
    # find the price of bread choice from dictionary & define
    # create value price list
    bread_cost = float(price_list[bread])  # specifies access to the value of bread
    protein_cost = float(price_list[protein])  # specifies access to the value of protein
    cheese_cost = float(price_list[cheese]) if cheese != 'no cheese' else 0
    # specifies access to the value of cheese# if no cheese, cost is zero
    condiments_cost = float(price_list[condiments])  # specifies access to the value of protein
    choice_total = 0
    subtotal = bread_cost + protein_cost + cheese_cost + condiments_cost + choice_total
    total = subtotal * sandwich_number  # gathers the subtotal obtained * number of sandwiches for overall total
    return bread_cost, protein_cost, cheese_cost, condiments_cost, subtotal, total


def outputs(bread, protein, cheese, condiments, sandwich_number, bread_cost, protein_cost, cheese_cost,
            condiments_cost, total):
    print(f'Info on {sandwich_number} sandwiches needed')  # diplays the number of sandwiches needed by user
    print(f'{"Ingredients ":<15}{"Ingredients Chosen " :<15}{"":<8}{"Price":<15}')  # formats the ingredients,
    # #ingredients chosen, and  the price in 15 characters. There is a space of 8 characters
    # to better format the table.

    for index in range(sandwich_number):  # calls for the index of the key and value for sandwiches in dictionary
        print(f'{"bread":<15}{bread:<16}{"":<10} ${bread_cost:<8.2f}')  # formats ingredients, and  the price
        print(f'{"protein":<15}{protein:<16}{"":<10} ${protein_cost:<8.2f}')  # along with ingredients chosen.
        print(f'{"cheese":<15}{cheese:<16} {"":<10}${cheese_cost:<8.2f}')
        print(f'{"condiments":<15}{condiments:<16}{"":<10} ${condiments_cost:<8.2f}')
    print(f'{"Total":<10} ${total:>8.2f}')


main()
