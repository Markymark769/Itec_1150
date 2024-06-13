"""Gas Calculator PDP & program.
• Create a file called PDP-gas-calc.docx. Use Program Development Plan
template from D2L , Materials, Content, Resources, Grading_PDPtemplate.
• The PDP will cover a program called gas_calc.py, which asks the user 1) the number
of miles they drove on a trip, 2) the number of gallons of gas they used, and 3) the
price of gas per gallon. The program uses their input to figure out and display the
cost of the trip & the miles per gallon (MPG) for the trip. See output format below."""

"""Program Development Plan
Problem definition: Write a program that will calculate the cost of a roadtrip and miles per gallon given inputs 
for total miles, gallons of gas, cost of gas. 
Variables, Calculations, and Functions:
    gallons = gallons of gas used
    miles = miles traveled
    gas_cost = cost per gallon of gas
    total_cost = gallons * gas_cost
    mpg = miles/gallons
Algorithm:
    Get user inputs, convert to numeric
    Run calculations
    Provide output
Coding, Testing
"""
miles = float(input('I will calculate the cost of your trip.  How many miles did you travel? '))
gallons = float(input('How many gallons of gas did you use? '))
gas_cost = float(input('What was the average price per gallon of gas? '))

total_cost = gallons * gas_cost
mpg = miles/gallons

print(f'You traveled {miles:.0f} miles and used {gallons:.0f} gallons of gas at ${gas_cost:.2f} per gallon.')
print(f'Your total cost was ${total_cost:.2f} and your average gas mileage was {mpg:.1f} MPG.')
