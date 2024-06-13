"""Mark Porraz, 1/29/2023
This program calculates the total number of cups of
each drink sold, and how much each drink costs.
The results are printed in the column."""

# Define Variables
num_coffee = int(input('How many cups of coffee were sold ? '))
price_coffee = float(input('At what price were the cups of coffee sold?'))
num_tea = int(input('How many cups of tea were sold ? '))
price_tea = float(input('At what price were the cups of tea sold ? '))
num_capp = int(input('How many cups of cappuccino were sold ? '))
price_capp = float(input('At what price were the cups of cappuccino sold ? '))

# total sales = sum * sales
coffee_sales = num_coffee * price_coffee
tea_sales = num_tea * price_tea
capp_sales = num_capp * price_capp

# Grand Total
total_cups = num_coffee + num_tea + num_capp
total_sales = coffee_sales + tea_sales + capp_sales

# Display in a column
print('Drink Sales for the Reported Period.')
print('{:<14}{:<14}{:<4}{:<12}{:<4}{:<12}'.format('Drink Type', 'Cups Sold', '', 'Price', '', 'Total'))
print('{:<14}{:^14}{:^4}{:^12}{:^4}{:^12}'.format('Coffee', num_coffee, '$', price_coffee, '$', coffee_sales))
print('{:<14}{:^14}{:^4}{:^12}{:^4}{:^12}'.format('Tea', num_tea, '$', price_tea, '$', tea_sales))
print('{:<14}{:^14}{:^4}{:^12}{:^4}{:^12}'.format('Cappuccino', num_capp, '$', price_capp, '$', capp_sales))
print('{:<14}{:^14}{:^4}{:^12}{:^4}{:^12}'.format('Total', total_cups, '', '', '$', total_sales))
