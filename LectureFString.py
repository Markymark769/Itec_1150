"""
Author: Mark Porraz
Date: 9/5/2023
DEscription: working code for lecture of chapter 1 pt 2

Know the difference between string, character, or number
use int of float to do actual math with the inputs
"""
# Example 1: goal, to take a program and have it add something
num1 = input()
num2 = input()
sum = int(num1) + int(num2)
print(sum)

# does this program work? is the program a good program?
# It works, and the program is doing with it intends to do
# the program above does not help the user understand what the program is doing

# Example 2: improve the program
print("Enter 2 integers, and the program will print the sum.")
num1 = input()
num2 = input()
sum = int(num1) + int(num2)
print(sum)

# Example 3: putting strings to where the user knows what is going where
print("Enter 2 integers, and the program will print the sum.")
num1 = input("Enter the first integer: ")
num2 = input("Enter the second integer: ")
sum = int(num1) + int(num2)
print(sum)

# Example 4:
print("Enter 2 integers, and the program will print the sum.")
num1 = input("Enter the first integer: ")
num2 = input("Enter the second integer: ")
sum = int(num1) + int(num2)
print("The sum of the two numbers is: ", + sum) ### why is this an error without comma
## or print("The sum of the two numbers is: " + str(sum))

