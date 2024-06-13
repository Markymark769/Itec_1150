"""
Mark Porraz
Clara's class for lab 10

using spreadsheets to accomplish data
"""
import requests
import docx
# the import gets data from a library that makes is possible to run the API
#

url = 'https://country-list-1150.azurewebsites.net/api/country'

country_response = requests.get(url).json()
print(country_response)

country_document = docx.Document()

for country_dictionary in country_response:
    country_name = country_dictionary['name']
    print(country_name)
    country_document.add_paragraph(country_name)

country_document.save('countries_and_capitals.docx')


