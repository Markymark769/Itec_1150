"""Start with a working copy of avg_rainfall.py program from the last lab (provided in D2L resources if necessary).
• Re-design the program to use all of our new standard features, plus the old ones:
• Interactive functions called main(), inputs(), processing(), and outputs(), plus the separate get_pos_int() validation function
• Exception handling & restart in main()

exception handling
try:
    # insert code here
except Exception as err:
    print(err)    """

def inputs():
    years = 'a'
    rainfall_grand_total = 0
    year_rainfall_total = 0

    print("I'm going to ask you for monthly rainfall amounts over the number of years that you specify.")

    while not (years.isnumeric()):
        years = input("Enter the number of years that you would like to average (whole numbers only: ")
    years = int(years)

    for year in range(years):
        for month in range(12):
            thisMonth = 'a'
            while not(thisMonth.isnumeric()):
                thisMonth = input(f'Enter rainfall in cm for year {year + 1}, month {month + 1}: ')
            year_rainfall_total += int(thisMonth)
        year_rainfall_average = year_rainfall_total/12
        print(f'The total rainfall for year {year+1} was {year_rainfall_total} cm.')
        print(f'The average monthly rainfall for year {year + 1} was {year_rainfall_average} cm.')
    rainfall_grand_total += year_rainfall_total
    processing(years, rainfall_grand_total)
    return

def processing(years, rainfall_grand_total):
    rainfall_grand_average = rainfall_grand_total/(years*12)
    outputs(years, rainfall_grand_average, rainfall_grand_total)
    return

def outputs(years, rainfall_grand_average, rainfall_grand_total):
    print(f'The total rainfall for the {years} years was {rainfall_grand_total} cm.')
    print(f'The average monthly rainfall for the {years} years was {rainfall_grand_average} cm.')
    print(f'The average annual rainfall for the {years} was {rainfall_grand_total/years} cm.')
    return


def main():
    runAgain = 'Y'
    while runAgain == ('Y' or 'y'):
        inputs()
        runAgain = input("Enter Y to run the program again: ")
    return

main()
