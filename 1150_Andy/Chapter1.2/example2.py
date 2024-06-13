"""
Mark Porraz
Tutoring
9/6/2023
"""

### Define Variables ## ask questions # user inputs
item_price = float(input('What is the total price of your purchase order?'))

### Calculate Sales Tax, County Tax, and Total Cost
#### formula
state_tax = item_price * 0.05

### printed answer
print('{:<12}{:>5}{:>12,.2f}'.format('State Tax','$',state_tax))
print('{:<12}{:>5}{:>12,.2f}'.format('Total','$',state_tax + item_price))
