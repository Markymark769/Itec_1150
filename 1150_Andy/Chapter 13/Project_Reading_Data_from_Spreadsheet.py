"""
Mark Porraz
5/8/2024
Project: Reading Data from a Spreadsheet
readCensusExcel.py

description: this program reads data from a spreadsheet. this data is from the census data
of the United States.

We have 4 columns: Census track, State, County, and population. based off this, we want to get the population
based off of those separate counties.

Note: this is a very extensive list
https://www.youtube.com/watch?v=yOVwmtH2ii0&list=PLiEts138s9P0aG6soKBoMsmJrwIOPXoXR&index=14
"""

import openpyxl, pprint
print('Opening workbook ...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows ...')

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    # Make sure the key for this state exists.
    countyData.setdefault(state, {})

    # make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents on census tract, so increment by one.
    countyData[state][county]['tracts'] += 1

    # Increase the county (pop)ulation by the (pop)ulation in this census tract
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results ...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData =' + pprint.pformat(countyData))
resultFile.close()
print('Done')






