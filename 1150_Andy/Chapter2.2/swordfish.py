"""Mark Porraz, 2/12/2023
Homework 2_2, swordfish."""

# This program runs a loop is name and password are not correct
## adding the continue and break statements

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe': ## note spaces matter
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')