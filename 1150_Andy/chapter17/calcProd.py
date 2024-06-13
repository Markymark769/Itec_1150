"""
Mark Porraz, 5/4/2023, calcPro.py
"""

import time
# defining function calcProd, calculating product of 1st 1000 nums
# this is the function we want to check and see how long it takes
# calculate the product of the first 100,000 numbers.
def calcProd():
    product = 1
    for i in range(1, 1000):  # finding letter i in range 1-100000
        # 100000 is too big for device to process, set it down to 1000 ########
        product = product * i  # taking that product and multiplying it by that number
    return product  # we are returning that number.


# below we set up variables to see how long the function takes.
startTime = time.time()  # we get the timestamp from the time.time() variable
prod = calcProd()  # getting variable calcProd from above, setting equal to new return variable
endTime = time.time()  # calling time.time() to be our endTime
print('The result is %s digits long.' % (len(str(prod))))  # the len of strings in prod
print('Took %s seconds to calculate.' % (endTime - startTime))  # formula of endTime - startTime

