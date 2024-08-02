import requests
# from openpyxl import Workbook
# import docx
# grab World Bank data
url = 'http://api.worldbank.org/v2/country?format=json&per_page=400'
world_bank_data = requests.get(url).json()
# use World Bank data to extract countries and their capitals
country_info = world_bank_data[1]
countries = {}
for data in country_info:
    country = data['name']
    capital = data['capitalCity']
    if capital:
        countries[country] = capital
    print(country_info)
