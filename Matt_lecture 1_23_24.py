"""
inputs and variables
"""
# inputs
username = input('Enter your name: ')
print("Hello",username,"!")

# inputs
toe_count = input('Enter the number of toes you have: ')
print("you have", toe_count, "toes.")

# does not work
# print("If you lost one, you would have", toe_count - 1 ,"toes")
# you have to convert to a number. Use 'int()' if you know it is a non-decimal
# number, 'float()' if it is a decimal number

print(int(toe_count))
print("If you lost one, you'd",int(toe_count),"toes.")

print(int(toe_count))
# print(int(myName))
print("If you lost one, you would have", int(toe_count) - 1 ,"toes")

toe_count =int(toe_count)
print("If you lost one, you would have", toe_count - 1 ,"toes")

# a conversion to change a string to an integer
# when you use variables you have  make sure you do the math on the numbers correctly
##################
# formatting
#######################
# Resources:
#
# make a ruler

# myruler = '-----+-----1-----+-----2'

# let's decorate some food!
userFood = input('Enter a food:  ')

# Basic
print("="*40)
print(f"{userFood}")  # an f string, which means it is a formatted string
print("="*40)

# if you do not have an f string, he {} part, i do not get the variable value
print("{userFood}")
print("userFood")

# Let's center the text
print("="*40)
print(f"{userFood:^40}")
print("="*40)

# wider ...
print("="*80)
print(f"{userFood:^80}")
print("="*80)

# Push to the left or the Right side -- called 'justification'
print("="*40)
print(f"{userFood:>40}")

print("="*40)
print(f"{userFood:<40}")
print(f"{userFood:^40}")
print(f"{userFood:>40}")

# you can line things up nicely
print("="*40)
print(f"You chose: {userFood:>29}")

# what if you have a bill?
item1 = 'steak'
cost1 = 29
item2 = 'caviar'
cost2 = 112

print("="*40)
print(f"{item1:<35}{cost1:>4}")
print(f"{item2:<35}{cost2:>4}")

# we can use formatting to round digits
myNum = 2.0/3
print(f"Raw number: {myNum}")
print(f"Rounded to 3 decimal places: {myNum:.3f}")

# we can use formats to add commas
myNum = 1000000
print(f"I wouldn't do it if you paid me $ {myNum:,d}!")

# you can reserve spaces for numbers
print(f"I wouldn't do it if you paid me $ {myNum:,d}!")

