"""Mark Porraz. 2/5/2023, This program enters a score then interpret
into a grade, A through F. Uses Boolean expressions. No number over 100
or negative numbers.
"""

# asks the user for input
score = input('Enter quiz score – whole number 0-100: ')


# validation block
# if score.isnumeric() is False:  # function displays only numbers. no letters, fractions or decimals.
# 	print('Try the program again; it only takes whole numbers.')
#
# # print statements
# else:
score = int(score)  # score as an integer
if score > 100:
    print('Sorry this quiz only goes up to 100 percent. Please Try again.')
elif score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
elif score >= 0:
    print('Grade: F')
else:
    print('Your grade is currently undefined.')


