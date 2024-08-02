print('Welcome to our counting program.')
print('It also adds up the digits that you count!')

while not s_number.isnumeric():
    print('Please enter a small number')
    s_number = input('Please enter a whole number only')

for small_digit in range(s_number):
    small_final = float(input(f'Please enter a whole number only #{small_digit + 1}:'))

large_end = int(input('Now, enter a larger number that you want to count up to:'))
large_start = 5.0
for large_digit in range(large_end):
    large_final = float(input(f'Enter a whole number greater than your start number #{large_start + 1}:'))

for count_digit in range(small_final, large_final):
    print(count_digit)

count_total = 0
for sub_total in range(small_final, large_final):
    print(sub_total)
    total += sub_total # longhand version total = total + number
print(f'The grand total of all the numbers is: {total:,d}.')