"""Mark Porraz, 1/29/2023
This program calculates math functions.
The results are printed below."""

### Define Variables
# cut off 7.89 to 7





# round 54.345395 to 54.345
value = 54.345

print('The value is: ', value)
print(' The value rounded to 0 decimal places: ', round(value, 1))
print(' The value rounded to 1 decimal places: ', round(value, 2))
print(' The value rounded to 2 decimal places: ', round(value, 3))
print(' The value rounded to 3 decimal places: ', round(value, 4))

###
# calculate the square root of 2
import math
number = int(input("enter a number to calculate the square root:"))
sqrt = math.sqrt(number)
print("square root:", sqrt)

###
# calculate the sin of 7 = 0.6569865987187891
import math
number = int(input("enter a number to calculate the sin:"))
sin = math.sin(number)
print("sin:" , sin)

# display the value of pi = 3.141592653589793

import math
print(math.pi)

# display pi rounded to 3 decimal places to 3 places = 3.142

import math
print(round(math.pi,3))


