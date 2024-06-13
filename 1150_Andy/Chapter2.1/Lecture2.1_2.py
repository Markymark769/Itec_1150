### Lecture Example 9
score = int(input('Enter quiz score: '))
if score >= 90:
	print('Grade: A')
elif score >= 80:
	print('Grade: B')
elif score >= 70:
	print('Grade: C')

### Lecture Example 10
score = input('Enter quiz score – whole number 0-100: ')
# validation block
if score.isnumeric() is False:
	print('Try the program again; it only takes whole numbers.')
else:
    score = int(score)
    if score >= 90:
        print('Grade: A')
    elif score >= 80:
        print('Grade: B')
    elif score >= 70:
        print('Grade: C')
    else:
        print('Your grade is currently undefined.')
