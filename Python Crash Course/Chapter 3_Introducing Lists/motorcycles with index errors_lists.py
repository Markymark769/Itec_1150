#Avoiding Index Errors When Working with Lists

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles[2])

######## do not use########
#motorcycles = ['honda','yamaha','suzuki']
#print(motorcycles[3])
#           Index Error Below
#Traceback (most recent call last):
#File "c:\Users\marky\OneDrive\Documents\coding project folder\Python Coding\motorcycles with index errors_lists.py", line 4, in <module>
#   print(motorcycles[3])
#IndexError: list index out of range
#
#no item in index three exists, instead it should be print(motorcycles[2])
######### index error means that python cannot find an item you requested

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles[-1])
## the only time when this will have an error is when you request the last item from an empty list
#motorcycles = []
#print(motorcycles[-1])
#            Index Error Below
#Traceback (most recent call last):
#  File "c:\Users\marky\OneDrive\Documents\coding project folder\Python Coding\motorcycles with index errors_lists.py", line 22, in <module>
#    print(motorcycles[-1])
#IndexError: list index out of range
