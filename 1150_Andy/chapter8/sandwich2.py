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
    try:
        sandwich_amount, bread, protein, cheese, condiments = inputs() # main input we are trying to get
        total = processing(sandwich_amount) # what is there to process?? no formulas
        outputs(sandwich_amount, bread, protein, cheese, condiments,total)
        restart = input('Continue? Enter y or n: ')
        if restart == 'y':
            print('OK, let\'s process more sandwiches.')
            main()
        else:
            print('Thanks for using the program.')

    except Exception as err:
        print(err)

def inputs():
    sandwich_amount = pyip.inputInt("Enter the number of sandwiches you want: ")
    bread_list = {'Wheat': '1.50', 'White': '1.50', 'Sourdough': '1.50'} # ingredient is key # value is price
    protein_list = {'Chicken': '2.00', 'Turkey': '2.00', 'Ham': '2.00', 'Tofu': '3.00'}
    cheese_list = {'Cheese': '1.50', 'Swiss': '2.00', 'Mozzarella': '1.50'}
    condiments_list = {'Mayo': '0.25', 'Mustard': '0.25', 'Lettuce': '0.25', 'Tomato': '0.25'}


    for index in range(sandwich_amount):  # need to specify a key??????
        bread = pyip.inputMenu('what kind of bread would you like? ')
        protein = pyip.inputMenu('What kind of protein would you like? ')
        cheese = pyip.inputYesNo('Would you like cheese? Yes or No?')
        if input() == 'yes':
            pyip.inputMenu('what kind of cheese would you like?')
        else:
            continue
        condiments = pyip.inputMenu('what kind of condiments would you like? ')


    return sandwich_amount, bread_list, protein_list, cheese_list, condiments_list

def get_pos_int():
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a whole number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int
def processing(sandwiches): # what even goes here?!! no formulas given
    for key in sandwiches.keys():
        value = sandwiches.get(key)
        choice = input("Select your item: ")
    # if choice in sandwiches:
    return choice,value

    # total = sum(sandwiches)
    # return total
#TODO: use formula sum(list(d.values))
def outputs(sandwich_amount, bread, protein, cheese, condiments, total):
    print(f'Info on {sandwich_amount} sandwiches needed')  # diplays the number of books needed by user
    print(f'{"Ingredients ":<10}{"Price":>10}')  # formats the book name and price in 10 characters
    for index in range(len(sandwich_amount)):  # calls for the index of the book price in the list
        print(f'{bread.keys[index]:<10} ${bread.values[index]:>8.2f}')  # formats book names and prices
        print(f'{protein.keys[index]:<10} ${protein.values[index]:>8.2f}')
        print(f'{cheese.keys[index]:<10} ${cheese.values[index]:>8.2f}')
        print(f'{condiments.keys[index]:<10} ${condiments.values[index]:>8.2f}')
        # in a list with 10 characters.
    print(f'{"Total":<10} ${total:>8.2f}')
    #print(f'{"Average":<10} ${average:>8.2f}')
main()

# bread = {'Wheat': '1.50', 'White': '1.50', 'Sourdough': '1.50'}
# protein = {'Chicken': '2.00', 'Turkey': '2.00', 'Ham': '2.00', 'Tofu': '3.00'}
# cheese = {'Cheese': '1.50', 'Swiss': '2.00', 'Mozzarella': '1.50'}
# condiments = {'Mayo': '0.25', 'Mustard': '0.25', 'Lettuce': '0.25', 'Tomato':'0.25'}
#
# for index in range(sandwiches):
#     bread = pyip.inputMenu(prompt= 'what kind of bread would you like? ')
#     protein = pyip.inputMenu(prompt= 'What kind of protien would you like? ')
#     cheese = pyip.inputYesNo(prompt= 'Would you like cheese? Yes or No?')
#         if input() = yes:
#             cheese = pyip.inputMenu('what kind of cheese would you like?')
#         else:
#             continue
#     condiments = pyip.inputMenu(prompt= 'what kind of condiments would you like? ')

# bread_cost = (['1.50', '1.50', '1.50'])
# if bread_cost == 'wheat':
#     protein_cost = (['2.00', '2.00', '2.00', '3.00'])
# cheese = cheese_cost
# if cheese == 'yes':
#     cheese_cost = (['1.50', '2.00', '1.50'])
# condiments_cost = (['0.25', '0.25', '0.25', '0.25'])
