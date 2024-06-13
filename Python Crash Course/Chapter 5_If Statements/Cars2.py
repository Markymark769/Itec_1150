### IF statements - examining a set of conditions and deciding which action to take based on those 
### conditions. The IF statement allows you to examine the current state of a program and respond 
### appropriately to the state. A conditional test. 
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.title())
    else:
        print(car.title())
### IF statements at heart can be determined by true and false statements, which is a conditional test.
### true or false is generated in terminal if it meets the conditions of the test. 
### equal (=) means set the value, double equal (==) asks a question:"is the value of the car equal to 'bmw'?"
car = 'bmw'
print(car=='bmw')
#true
car = 'audi'
print(car=='bmw')
#false
### testing the eqaulity is case sensitive
car = 'Audi'
print(car== 'audi')
#false
### when case does not matter and just the value is needed, convert the variable's value to lowercase before comparision
### use .lower()==
car = 'Audi'
print(car.lower()== 'audi')
# Checking for Inequality
### using the (!=) method to determine whether two values are not equal. 
### the ! represents not, this is common in other programming lanuages.

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")
### if the values did not match we would print false and would not run the code.
### because the values match the print fuction is executed. 