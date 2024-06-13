"""Complete the textbook.py program by making sure you have:
• Int validation in a while loop to ensure that a number > 0 is entered
• All other standard features 
• Plus - improve the user-facing messages"""

books_needed = -1
while books_needed < 0:
    books_needed = int(input('How many textbooks do you need to buy? '))
total_cost = 0.0
for book in range(books_needed):
    price = float(input(f'Enter price iin whole dollars for book #{book+1}: '))
    total_cost = total_cost + price
    print(f'\tRunning subtotal: ${total_cost:<.2f}.')
print(f'Grand total: ${total_cost:<.2f}.')

print()
print()

# loops: write a loop that prints numbers counting down from 30 to 20
start = 30
end = 20
current = start
while current >= end:
    print(current)
    current = current -1

print()
print()
# loops: write a loop that prints 10, 20, 30, 40, 50, 60

start = 10
end = 60
step = 10
for i in range(start, end+step, step):
    print(i)

print()
print()

"""avg_rainfall.py: Write a program that collects rainfall data and calculates the average rainfall for a user-defined 
number of years.
• Ask the user for the number of years in their study - use a small number to test, like 2, because you have to 
collect 12 months of data for each year!
• The outer loop will run once for each year (hint: use range function).
• The inner loop will run once for each of 12 months, and ask the user for a rainfall amount for that month. 
The inner loop will accumulate a total for each year.
• The outer loop will finish by calculating average monthly rainfall for that year.
• At the end of each year, display the total for the year and the average.
• Challenge: add a feature to show the total and average rainfall for the entire study period (multi-year figures).
"""

print("I'm going to ask you for monthly rainfall amounts over the number of years that you specify.")
years = 'a'
rainfall_grand_total = 0
# print(years.isnumeric())
while not(years.isnumeric()):
    years = input("Enter the number of years that you would like to average (whole numbers only: ")
years = int(years)
for year in range(years):
    rainfall_total = 0
    for month in range(12):
        rainfall_total += int(input(f'Enter rainfall in cm for year {year+1}, month {month + 1}: '))
    print(f'The total rainfall for year {year+1} was {rainfall_total} cm.')
    print(f'The average rainfall for year {year+1} was {rainfall_total/12} cm.')
    rainfall_grand_total += rainfall_total
print(f'The total rainfall for all years was {rainfall_grand_total} cm.')
print(f'The average monthly rainfall for all years was {rainfall_grand_total/(12*years)} cm.')
print(f'The average yearly rainfall for all years was {rainfall_grand_total/years} cm.')