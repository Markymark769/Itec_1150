"""
Mark Porraz, 4/30/2023
"""
# ! python3
# removeCsvHeader.py - Removes the header from all CSV files int the current
# working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)
# using the directory os.makedirs
# creating a new directory called 'headerRemoved'

# Loop through every file in the current working directory.
# Loop through every file using the list directory
# current working directory by using the dot notation
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'): # scanning for csv file
        continue        # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row)
    csvRows = []  # empty list
    csvFileObj = open(csvFilename)  # opening a specific file
    readerObj = csv.reader(csvFileObj)  # using a reader to read that specific file obj
    for row in readerObj:
        if readerObj.line_num == 1:  # since we skipped the first row, basically overwriting those files.
            continue
        csvRows.append(row)  # adding that file to the list
    csvFileObj.close()  # need to close that file

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',  # we are going to open the file
                      newline='')  # with the header removed, going to write over it on a new line as empty
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)  # using the write row, passing write row as an arguement.
    csvFileObj.close()

