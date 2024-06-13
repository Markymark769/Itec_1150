#num= int(input('Enter a number:'))
#print(num)
#if num > 25:
#    print('num > 25 ')
#else:
#    print('False.')

####  when comparing two values it is either true or false

print("Welcome!\nNow that you have learned about",

"input\nand output, you may be wondering,\"What\nis",

"next?\"")

#my_number = float(input("Enter a number:"))
#my_number = input("Enter a number:")
#float_num = my_number
#my_number = float(input "Enter a number:")
#my_number = input(float("Enter a number:"))

### Lecture Example 1
temp = 67
if temp > 0:
    print(f'The temperature {temp}F is greater than 0.')

### Lecture Example 2
temp = float(input('Enter the temperature: '))
if temp > 0:
    print(f'The temperature {temp}F is greater than 0.')
print('That\'s all folks!')

### Lecture Example 3
temp = float(input('Enter the temperature: '))
if temp > 0:
    print(f'The temperature {temp}F is greater than 0 – thankfully!')
else:
    print(f'The temperature {temp}F is less than 0 - brrr!')
print('That\'s all folks!')

### Lecture Example 4
temp = float(input('Enter the temperature: '))
if temp > 0:
    print(f'The temperature {temp}F is greater than 0 – thankfully!')
elif temp == 0:
    print('The temperature is exactly 0!')
else:
    print(f'The temperature {temp}F is less than 0 - brrr!')
print('That\'s all folks!')

### Lecture Example 5
#Making Decisions
college = input('Please enter your college: ')
if college == 'Minneapolis College':
    print('Good choice!')

### Lecture Example 6
college = input('Please enter your college: ')
if college != 'Minneapolis College' :
    print('You should go to Minneapolis College!') # any difference will return True

### Lecture Example 7
year = int(input('What year did Apollo 11 land on the moon? '))
if year != 1969:
	print(f'Sorry, {year} is the wrong answer.')
else:
	print(f'Correct! {year} is right!')

### Lecture Example 8
year = int(input('What year did Apollo 11 land on the moon? '))
if year == 1969:
	print(f'Correct! {year} is right!')
else:
	print(f'Sorry, {year} is the wrong answer.')

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
