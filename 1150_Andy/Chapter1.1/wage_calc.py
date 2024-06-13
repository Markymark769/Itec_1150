"""
Mark Porraz
"""


# Define variables
hours_worked = 40
rate_of_pay = 15.34
overtime_worked = 10


# calculate the average grade of the 3 scores
wage_pay = rate_of_pay * hours_worked
overtime_pay = rate_of_pay * 1.5 * 10
gross_pay = wage_pay + overtime_pay

# Display the average
print(f'Your gross pay is $', gross_pay)
