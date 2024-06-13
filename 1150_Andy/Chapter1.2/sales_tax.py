"""
Mark Porraz, 1/29/2023
This program calculates the price of a purchase order. It calculates
item price, the state tax, county tax, and total cost.
The results are printed in the column.
"""

### Define Variables
item_price = float(input('What is the total price of your purchase order?'))


### Calculate Sales Tax, County Tax, and Total Cost
state_tax = item_price * 0.05
county_tax = item_price * 0.025
total_cost = item_price + state_tax + county_tax

### Display in table
print('Custom Delivery Sales Report')
print('{:<12}{:>5}{:>12,.2f}'.format('Item Price','$',item_price))
print('{:<12}{:>5}{:>12,.2f}'.format('State Tax','$',state_tax))
print('{:<12}{:>5}{:>12,.2f}'.format('County Tax','$',county_tax))
print('{:<12}{:>5}{:>12,.2f}'.format('Total Cost','$',total_cost))
