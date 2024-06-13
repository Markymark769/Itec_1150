##### two approaches are below, however the last one is more concise.
##### however both approaches are correct.
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)
##### writing the code more concisely, omit the temp variable square
##### and append each new value directly to the list.
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(value**2)

print(squares)
# Simple Statistics with a List of Numbers
##### minimum, maximum, and sum
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
# List Comprehensions
##### allows you to generate the same list of code under one line
squares = [value**2 for value in range(1,11)]
print(squares)