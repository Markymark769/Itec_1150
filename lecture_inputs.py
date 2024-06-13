"""
Author: Mark Porraz
Date: 9/5/2023
Description: working code for lecture of chapter 1 pt 2
"""

num1 = 2
num2 = 3


# print("The first number is: " + str(num1))
print("The first number is: {}".format(num1))  # the {} is a placeholder. The old way of formatting a string

print("The first number is: {} and the second number is {}".format(num1, num2))

# This is the new way -- f-strings.
print(f"The first number is: {num1} and the second number is: {num2} ")  # the most superior way

# an even better way
print(f"The first number is: {num1} and the second number is: {num2}, their sum is {num1 + num2} ")

# Alignment with f-strings

word1 = "Dog"
word2 = "Land"

word3 = "Spotted Alligator"
word4 = "very wet areas"

# Ugly
print(f"{word1} {word2}")
print(f"{word3} {word4}")

# better
print(f"{word1:<25} {word2}")
print(f"{word3:<25} {word4}")

# < left justify
# > right justify
# ^ center justify
print(f"{word1:.<25} {word2}")
print(f"{word3:.<25} {word4}")



