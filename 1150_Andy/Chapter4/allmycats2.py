"""Mark Porraz, 2/22/2023, All My Cats 2
This program demonstrates an imporvement on writing code
from the previous program allmycats1
"""

catNames = [] # cat name is equal to an empty list that the user creates
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ## uses the function str(len()) to return only letters
      ' (Or enter nothing to stop.):')
    name = input()

    if name == '':  # processing for mistakes
        break
    catNames = catNames + [name]  # list concatenation

print('The cat names are:') #the output screen.
for name in catNames:
    print('  ' + name)

### The code is now more flexable in processing the data
# more benificial than it would be with several repetitive variables.