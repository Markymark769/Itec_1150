# #set variables
# PO_amount = 753.00
# State_tax = 37.65
# County_tax = 18.82
# #set formulas
# total_cost = (PO_amount+State_tax+County_tax)
# #print statements
# print(f'Your total cost is {total_cost:,.2f}')


# float - numbers that deal with decimals
# string - string of letters
# integer - whole number
# print - sting of letters # we have to trick pycharm to put int() or float or variables
# input - sting of letters  # we have to trick pycharm to put int() or float

# set variables
PO_amount = float(input('what was the PO amount'))
State_tax = float(input('what is the state tax'))
County_tax = float(input('what is the county tax'))
# set formulas
total_cost = (PO_amount+State_tax+County_tax)
# print statements
print(f'Your total cost is {total_cost:,.2f}')
