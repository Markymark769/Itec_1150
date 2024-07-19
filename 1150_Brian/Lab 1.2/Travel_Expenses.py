"""
Mark Porraz
6/13/2024
Travel_Expenses.py
- This program calculates the amount of money spent on bus fare last month
- Ask the user for the number of times they rode the bus last month
- Ask the user for the cost of one bus ride
- Multiply these numbers to calculate the total cost of riding the bus.
- Print the number of rides, the cost of one bus ride, and the total cost for the user.
"""

# Input #####
rode_bus = int(input('how many times did you ride the bus last month ? '))
bus_cost = float(input('what was the cost of one bus ride ? '))
# we must

# Formula #####
total_bus_ride_cost = rode_bus * bus_cost

# Output ####
# print(f'You rode the bus {rode_bus} times last month. One bus ride costs $ {bus_cost}, '
#      f'so your total cost was $ {total_bus_ride_cost}.')

print(f'You rode the bus' +rode_bus + 'times last month. One bus ride costs $ '+{bus_cost} + ',
      'so your total cost was $ {total_bus_ride_cost}.')