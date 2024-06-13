# Numerical Comparisions 
### seeing if numbers are equal
age = 18
print(age == 18)
### seeing if two numbers are not equal
### conditional test. the correct answer is 17, not 42. instead the prompt is printed. 
answer = 17
if answer != 42:
    print("this is not the correct answer. Please try again!")
age = 19
print(age<21)
print(age <= 21)
print(age > 21)
print(age >= 21)
# Checking Multiple Conditions
### sometimes you may need two conditions to be true to take action.
### using and to check multiple condiditons.
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# Using OR to check Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)