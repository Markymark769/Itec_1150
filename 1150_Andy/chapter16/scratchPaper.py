import csv
from prettytable import PrettyTable

lab16File = open('lab16.csv.txt')
lab16Reader = csv.reader(lab16File)
lab16Data = list(lab16Reader)

table = PrettyTable()
table.field_names = lab16Data[0]
for row in lab16Data[1:]:
    table.add_row(row)

print(table)

