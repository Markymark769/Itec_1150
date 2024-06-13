"""
Mark Porraz
Chapter 13: Excel files
Python console code
"""

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# type(wb)
# # expected output: <class 'openpyxl.workbook.workbook.Workbook'>

# wb.sheetnames
# # expected output: ['Sheet1', 'Sheet2', 'Sheet3']

# sheet = wb['Sheet3']
# sheet
# expected output:<Worksheet "Sheet3">
# note that 'Sheet' needs to be capitalized, or it will not know what to reference

# sheet = wb['Sheet1']
# sheet['A1']
# # expected output <Cell 'Sheet.A1'>

# C = sheet['B1']
# C.value
# expected output: 'Apples'

# type(sheet)
# # expected output: <class 'openpyxl.worksheet.worksheet.Worksheet'>

# sheet.title
# expected output: 'Sheet3'

# anotherSheet = wb.active
# anotherSheet
# expected output: <Worksheet "Sheet1">

# c = sheet['B1']
# c.value
# # expected output: 'Apples'


# using a for loop. to loop through the Excel worksheet.
# for i in range(1, 8, 2): # here we are using a for loop to loop through the Excel worksheet
# above we are printing out every other cell
# we are printing cells 1-8, we are going in steps of 2
#     print(i, sheet.cell(row=i, column=2).value)
# expected output:
    # 1
    # Apples
    # 3
    # Pears
    # 5
    # Apples
    # 7
    # Strawberries

# we are returning the size of our spreadsheet
# sheet.max_row
# sheet.max_column


# in Excel, we are noting each column by rows, we need to notate that letters
# therefore we need to have certain syntax to receive this info
# from openpyxl.utils import get_column_letter, column_index_from_string
# get_column_letter(3)
# expected output: 'C'

# here we are able to slice worksheet objects to get all cell objects in a row column
# or an area inside the spreadsheet
# tuple(sheet['A1':'C3'])
# ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))

# when using a for loop we can get a look at individual values from the area
# for rowOfCellObjects in sheet['A1':'C3']:  # here we are looping over all the cell values
#     for cellObj in rowOfCellObjects:  # we are looping over all the individual cells in there
#         print(cellObj.coordinate, cellObj.value)  # printing the coordinate and value
#     print('---END OF ROW ---')  # printing the statement at the end of each row
# expected output below:

# A1 2015-04-05 13:34:02
# B1 Apples
# C1 73
# ---END OF ROW ---
# A2 2015-04-05 03:41:23
# B2 Cherries
# C2 85
# ---END OF ROW ---
# A3 2015-04-06 12:46:51
# B3 Pears
# C3 14
# ---END OF ROW ---


