# The if-elif-else Chain
#### this is used to test more than two possible situations
### python only executes only one block of a if-elif-else chain.
### it runs eh conditional test in orderuntil one passes
### when the test passes , the code is executed
# example) 
### admission for anyone under age 4 is free
### admission for anyone between the ages of 4 and 18 is 25$
### admission for anyone age 18 or older is $40
age = 12

if age < 4:
    print("Your admission cost is $0.")

elif age < 18:
    print("Your admission cost is $25.")

else:
    print("Your admission cost is $40.")
#example 2
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price= 40

print(f"Your admission cost is ${price}.") 
#example 3
# using multiple elif blocks
### adding a senior discount
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"your admission cost is ${price}.")

#example 4
# omitting the else block
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 20

print(f"Your admission cost is ${price}.")