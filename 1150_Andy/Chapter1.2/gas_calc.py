"""Mark Porraz, 1/29/2023
This program calculates the MPG and Total cost.
The results are printed in the column."""

### Define Variables
miles_driven = float(input('How many miles did you drive? '))
gallons_used = float(input('How many gallons of gas did you use? '))
price_per_gas = float(input('How much was your gas per gallon? '))


### Calculate MPG and Trip Cost
mpg = miles_driven / gallons_used  ## formula
trip_cost = gallons_used * price_per_gas ##formula


### Display in table
print('Here are some fun facts about your trip!')

print('{:<12}{:>5}{:>12,.2f}'.format('MPG','',mpg))
print('{:<12}{:>5}{:>12,.2f}'.format('Trip Cost','$',trip_cost))