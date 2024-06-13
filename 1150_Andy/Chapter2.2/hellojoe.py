"""Mark Porraz, 2/12/2023
Homework 2_2, hello joe."""
# this program asks for name and password.
# adds continue and break.
# restarts program to prompt if wrong data input.

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. what is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':  #wrong password restarts the prompt.
        break
print('Access granted.')