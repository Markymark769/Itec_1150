# Organizing a List
## Sorting a List Permanently with the sort() Method ----------------------
###### note) the sort() method sorts alphabetically
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
###### sorting in reverse alphabetical order with the argument
###### .sort(reverse=True) method
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
# Sorting a List Temporarily with the sorted() Function
cars = ['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# Printing a List in Reverse Order
#### use the reverse() method
#### changes the order of a list permanently
#### however the order can be changed back by applying the reverse() a second time.
cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)
# Finding the Length of a List
#### using the len() function method
#### note) use print() to create an output<<<
cars = ['bmw','audi','toyota','subaru']
print(len(cars))