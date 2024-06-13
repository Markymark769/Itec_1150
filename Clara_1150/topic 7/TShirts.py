"""
Mark Porraz
T-shirt problem
4/1/2024

"""
monday = int(input('how many t-shirts did you sell for monday?'))
tuesday = int(input('how many t-shirts did you sell for tuesday ?'))
wednesday = int(input('how many t-shirts did you sell for wednesday?'))
thursday = int(input('how many t-shirts did you sell for thursday?'))
friday = int(input('how many t-shirts did you sell for friday ?'))
saturday = int(input('how many t-shirts did you sell for saturday ?'))
sunday = int(input('how many t-shirts did you sell for sunday ?'))

hours_worked = {
    'Monday': monday,
    'Tuesday': tuesday,
    'Wednesday': wednesday,
    'Thursday': thursday,
    'Friday': friday,
    'Saturday': saturday,
    'Sunday': sunday
}

# Table heading
#  https://github.com/claraj/ProgrammingLogic1150Examples/blob/main/8_strings/padding_tables.py
total_sales = monday + tuesday + wednesday + thursday + friday + saturday + sunday
average_sales_day = total_sales / 7
# print(f'{"Day":<15}{"t-shirts sold":<15}')
print('{:<15}{:<15}{:<10}{:<20,.2f}'.format('Total Sales:', total_sales, 'average per day ', average_sales_day))

# Table data from dictionary
for day, hours in hours_worked.items():
    # print(f'{day:<15}{hours:<15}')
    print('{:<10}{:<6}{:<6}{:<10}'.format(day, 'sold:', hours, 'T-Shirts'))
