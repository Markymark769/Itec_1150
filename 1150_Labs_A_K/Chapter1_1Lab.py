"""albums.py : Adapt the code from the lesson slide 14 – number of albums.
Currently, when you run the code, it just displays the number 68 in the console/
interpreter. In your program, make sure the output explains what's going on, as
shown in this sample output:
• bus_fare.py: create a new program to calculate spending on bus fares for the
month. In this program, regular bus fares are $1.75. Rush hour bus fares are $3.
This month, you rode the bus 7 times during regular hours, and 12 times during
rush hours. What did you spend on bus fares this month? Sample output:

Note: Use PDP steps to think through variables, calculations & printing. Use
variable names in your print statements. Do NOT just hard code numbers in
print statements.
"""
number_of_cds = 45
number_of_lps = 23
number_of_albums = number_of_lps + number_of_cds
print(f'You have {number_of_cds} CDs and {number_of_lps} LPs for a total of {number_of_albums} albums.')

bus_fare = 1.75
rush_bus_fare = 3
bus_rides = 7
rush_bus_rides = 12
total_bus_spending = bus_fare*bus_rides + rush_bus_fare*rush_bus_rides
print(f'Your total bus spending this month was ${total_bus_spending}.')