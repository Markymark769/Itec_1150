"""
Mark Porraz
favorite_foods.py

Brian's class


"""

from openpyxl import Workbook

favorite_foods = ['Pizza', 'Chocolate Cake', 'Broccoli']
favorite_colors = ['Blue','Purple','Green','Orange']

workbook = Workbook()

# Get the active sheet. Workbooks
worksheet = workbook.active
worksheet.title = 'Favorite Things'

for index, food in enumerate(favorite_foods):
    worksheet.cell(index + 1, 1, food)

workbook.save('favorites.xlsx')
