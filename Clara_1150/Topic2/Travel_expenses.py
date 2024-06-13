"""
Mark Porraz
Travel_expenses.py
1/16/2024

This program calculates the amount of money spent on bus fares last month
"""
# define variables
bus_rode = int(input('How many times did you ride the bus last month?'))  # we use the int data type to turn strings
# into integers. There are integer- int(), string- str(), float - float()
bus_fare = float(input('What was the cost of one bus ride?'))

# why do we have two different data types for variables??
# other languages like javascript have a type called number which is used for all numbers, floats, and ints
# Most other languages have separate types for float and int
# why?
# 1. it takes less space in memory as the program runs to store int variables
# 2. float variables are less precise than int. ex) if you add 3.0 + 3.0 = 5.99999999, sometimes you might see this

# formulas
total_bus_spending = bus_rode * bus_fare

# print statement
# print(f'You rode the bus {bus_rode} times last month. One bus ride costs ${bus_fare}.' f' Your total cost was ${total_bus_spending}')

print('The total cost is' + str(total_bus_spending))
