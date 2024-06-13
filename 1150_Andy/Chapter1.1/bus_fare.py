"""
Mark Porraz
This program calculate the bus fare given
"""

# Define variables
reg_bus_fare = 1.75
rush_hour_bus_fare = 3.00
rode_bus = 7
rode_rush_bus = 12

# calculate the average grade of the 3 scores
# total = (1.75* 7) + (3.00*12)
total_bus_spending = (reg_bus_fare*rode_bus) + (rush_hour_bus_fare*rode_rush_bus)

# Display the average

print(f'Your total bus spending this month was ${total_bus_spending}.')
