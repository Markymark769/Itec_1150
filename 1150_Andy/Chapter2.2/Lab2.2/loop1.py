"""Mark Porraz, 2/12/2023, Loop 1
This program helps understand how to perform various range functions.
"""

print('These are the numbers from 0 through 5.') #lists numbers in a range from 1 to 5
for i in range(0, 6):
 print(i)

print('These are the numbers from 1 through 20.') # lists numbers in a range from 1 to 20
for i in range(0, 21):
 print(i)

print('These are even numbers from 0 through 24.') # lists even numbers in a range from 0 to 24
for i in range(0, 25, 2): # third number is the step
 print(i)

print('These are the odd numbers from 37 through 53.') # lists odd numbers in range from 37 to 53
for i in range(37, 54): # adding plus 1
 if(i % 2 != 0): ## formula for printing odd
  print(i)

# print('This counts by tens from 10 through 60.') ## range by 10's
# for i in range(10, 70, 10):
#  print(i)
#
# print('This counts down from 30 to 20 by ones') ## range counting down by one from 30 to 20
# for i in range( 30, 19, -1):
#  print(i)