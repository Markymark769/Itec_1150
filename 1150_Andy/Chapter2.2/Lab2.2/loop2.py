"""Mark Porraz, 2/12/2023, Loop 2

this program uses a loop and range function to print numbers counted
the list of number are added together from small to large
the total number is displayed in a print statement. """

print('Welcome to our counting program.')
print('It also adds up the digits that you count!')

# total_cost = 0
foo = input('Please enter a small number, 0 or higher: ')
while not(foo.isnumeric()):
    foo = input('That wasn\'t a positive number. Try again: ')
small = int(foo)

while True:     #check numbers are integers
    try:        # function similar to the if, else, elif statements##### Try and Except
        small = int(input('Please enter a small number, 0 or higher: '))
    except ValueError: #### # function similar to the if, else, elif statements
        print('Please enter a whole number.')
    else:
        break


while True:     ## loop that checks for integers
    try:
        large = int(input('Now, enter a larger number that you want to count up to: '))
    except ValueError:
        print('Please enter a while number.')
    else:
        break

print('your range small to large is: ') ## prints the range
total = 0
for i in range(small,large +1):
    total = total + i ## addds the range of numbers listed
    print(i)
print(f'The total of all the numbers you counted is : {total}')

