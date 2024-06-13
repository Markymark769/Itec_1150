# """ Mark Porraz, 4/11/2023, sandwich.py.
# This program asks the user for their sandwich preferences.
# This program uses pyinputplus for validation, displays the prices for each
# of these option, displays all choices made, plus a total cost at the very end.
#
# You can set dictionary to match each ingredient choice and its price.
# It's much easier to bring the price value for calculating or displaying
# output with dictionary than define prices for each item separately
#
# """
#
# def inputs():
#     sandwich_number = pyip.inputInt(prompt="Enter the number of sandwiches you want: ")
#     bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'])
#     protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'])
#     cheese_choice = pyip.inputYesNo('Would you like cheese? Yes or No?')
#     if cheese_choice == 'yes':
#     cheese = pyip.inputMenu(['Cheese', 'Swiss', 'Mozzarella'])
#     cheese_cost = price_list[cheese]
#     else:
#     cheese = 'no cheese'
#     cheese_cost = 0
#     condiments = pyip.inputMenu(['Mayo', 'Mustard', 'Lettuce', 'Tomato'])
#     condiments_cost = sum(price_list[c] for c in condiments)
#     return sandwich_number, bread, protein, cheese, condiments
#
# def processing(price_list, bread, protein, cheese, condiments, sandwich_number):
#     bread_cost = price_list[bread]
#     protein_cost = price_list[protein]
#     condiments_cost = sum(price_list[c] for c in condiments)
#     subtotal = bread_cost + protein_cost + cheese_cost + condiments_cost
#     total = subtotal * sandwich_number
#     return bread_cost, protein_cost, cheese_cost, condiments_cost, subtotal, total
#
# def outputs(bread, protein, cheese, condiments, sandwich_number, bread_cost, protein_cost, cheese_cost, condiments_cost, total):
#     print(f'Info on {sandwich_number} sandwiches needed')
#     print(f'{"Ingredients ":<10}{"Price":>10}')
#     print(f'{bread:<10} ${bread_cost:>8.2f}')
#     print(f'{protein:<10} ${protein_cost:>8.2f}')
#     if cheese != 'no cheese':
#     print(f'{cheese:<10} ${cheese_cost:>8.2f}')
#     for c in condiments:
#     print(f'{c:<10} ${price_list[c]:>8.2f}')
#     print(f'{"Total":<10} ${total:>8.2f}')
#
# main()
#
