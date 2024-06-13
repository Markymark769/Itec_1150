"""Mark Porraz, 1/29/2023
This program calculates the area and displays the answer within a sentence
based on measurement units.
The results are printed in the column."""

### Define Variables
print('Welcome to the Rectangle Area Calculator!')
unit = str(input('What is your measurement unit (in.,ft., cm.,etc).? '))
len_rect = float(input(f'What is the length of the rectangle in {unit}?'))
width_rect = float(input(f'What is the width of the rectangle in {unit}?'))

### Calculate the area using the formula
area = len_rect * width_rect

### Display in table
print(f'The area of your rectangle is {area:,.2f} square {unit}.')


print('ask a question')