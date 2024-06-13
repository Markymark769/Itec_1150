"""
Mark Porraz, 5/11/2023, csv_reader

This program uses my own csv file with least 6 rows and
3 columns of data. This program references a csv file called
lab16 to display the different type of alcohol in a table.
The prettytable function is used to display as a pretty table.
"""
# unused code
# import csv
# lab16File = open('lab16.csv.txt')
# lab16Reader = csv.reader(lab16File)
# lab16Data = list(lab16Reader)
# print(lab16Data, '\n')

import csv
from prettytable import PrettyTable

lab16File = open('lab16.csv.txt')  # open lab16File as a txt + csv file
lab16Reader = csv.reader(lab16File)  # read the lab16File using the reader() method
lab16Data = list(lab16Reader)  # display an empty list if no arguments given

table = PrettyTable()  # uses the pretty table function to display as pretty table
table.field_names = lab16Data[0]  # sets the names of the fields in the table
# lab16Data is the header name for the table
for row in lab16Data[1:]:  # loops over the rows in the second row using the table.add_row(row) method
    table.add_row(row)

print(table)  # print the table, in pretty fashion
