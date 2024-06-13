"""Mark Porraz, 2/19/2023, Average rainfall fun
"""

def main():
    n_years_grand = inputs_grand()  # this is where you would need to pass a parameter. would not need to pass a string.
    # this function says, go to inputs_grand and pull out the n_years_grand
    yearly_rainfall_grand_total = 0
    for year in range(1, n_years_grand + 1):
        added_rain = inputs_year()  # note) changed the yearly rainfall name to added rain
        yearly_rainfall_avg = process_year(added_rain)
        output_year(year, added_rain, yearly_rainfall_avg)
        yearly_rainfall_grand_total = yearly_rainfall_grand_total + added_rain  # (place into processing)
    yearly_rainfall_avg_grand = process_grand(n_years_grand, yearly_rainfall_grand_total)
    output_grand(yearly_rainfall_grand_total, yearly_rainfall_avg_grand)

def get_pos_int_monthly_rainfall(monthly_rainfall): # we are recieving the monthly rainfall from the input function and
    # performing a check to make sure it is a positive int
    pos_int = monthly_rainfall # need to define pos_int. pos_inst = monthly_rainfall
    while pos_int.isnumeric() is False:
        pos_int = input('Please enter a whole number: ')
    pos_int = int(pos_int)
    return pos_int

def get_pos_int_num_years(): # a checks for the number of years validaiton
    pos_int = input('Please enter a whole number only: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Please enter a whole number greater than zero: ')
    pos_int = int(pos_int)
    return pos_int

def inputs_grand(): #inputs for each year user needs
    print('How many years are in your rainfall sample? ')
    n_years_grand = get_pos_int_num_years()
    return n_years_grand # returns to the main() function

def inputs_year(): # add loop for only 12 months## 1-13
    added_rain = 0  # this is going to be a running total where it keeps adding up every time it loops through each month.
    # So added rain = added rain + inches per month.
    #when adding the running total, this would mean adding to the 0 that has been set.
    for month in range(1, 13):  # the loops is to prevent from hard coding each month by hand.
        # (1,13) because always stops before you get to the final number
        monthly_rainfall = input(f'Enter rain for month #{month}: ') # needed a new variable to store the monthly rain
        # the month variable is going to be a number# 1-12
        # Enter rain for month #1
        monthly_rainfall = get_pos_int_monthly_rainfall(monthly_rainfall)# send the monthly rainfall to pass as an arguement
        # sending the monthly rainfall to the get_pos_int function
        added_rain = monthly_rainfall + added_rain # create a running total # this means you are going to keep adding
        #to the monthly total
    return added_rain  # returns to main()# returning the total rainfall for that year
# gives us the added rain
#created added rain and monthly rainfall all in this function, no need to reference it in line 5 on ()

def process_year(added_rain):
    yearly_rainfall_avg = added_rain/12 # this is the total divided by months
    return yearly_rainfall_avg


def output_year(year, added_rain, yearly_rainfall_avg): #displays the total for each individual year
    print(f'Total rain for year #{year}= {added_rain}')
    print(f'Year # {year} Monthly average rainfall = {yearly_rainfall_avg}')
    # this is going to be the year number everytime it loops

def process_grand(n_years_grand, yearly_rainfall_grand_total): #gets the average rainfall for all years together
    yearly_rainfall_avg_grand = yearly_rainfall_grand_total/n_years_grand
    return yearly_rainfall_avg_grand

def output_grand(yearly_rainfall_grand_total, yearly_rainfall_avg_grand):

# output grand displays the ovrall rainfall for all years togehter.
    print(f'Total rain, all years = {yearly_rainfall_grand_total}')
    print(f'Average monthly rain, all years = {yearly_rainfall_avg_grand}')
    print('Thank you for using the program.')
# most of this function comes from the output that is on the powerpoint slide.
main()

# the goal is to start with the main() ###use as a road map to continue the rest of function.