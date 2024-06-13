"""Mark Porraz. 2/5/2023, This program asks the user what year Apollo
11 landed on the moon. Gives feedback if user is close within one year of
correct answer.
"""

# asks the user for input.

year = int(input('What year did Apollo 11 land on the moon? '))

# validation block.
if year == 1969:
	print(f'Correct! {year} is right!')
# print statements.
elif 1969 < year:
	print(f'Sorry, {year} is the wrong answer.')
elif 1970 == year:
	print('sorry, that is the wrong answer')
	print('you are a year above the correct answer')
elif 1969 > year:
	print(f'Sorry, {year} is the wrong answer.')
elif 1968 == year:
	print('sorry, that is the wrong answer')
	print('sorry, you are under by a year')
