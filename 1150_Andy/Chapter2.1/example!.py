"""
MArk Porraz

"""
# Integer- whole number  - int()
# Float - decimal - Float()
# string - a string of letters - str()
# print() - prints a string of letters
# if and else is boolean logic meaning it is true or false.
# (and, or, and not)

money = 55
print('money',money,'money')  # option one, to separate the print statements
print(f'money is {money}')  # option two use an f string with {}

name = 'Mary'
password = 'swordfish'

if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

name = input('what is your name?')  # asking the user for input and setting = to a variable
if name == 'Alice':  # 1st argument is only wanting Alice
    print('Hi, Alice.')
else:  # If the person is not alice
    print('Hello, stranger.')  # it will print hello stranger



name = input('what is your name?')
age = int(input('how old are you?'))  # python wants to print only a string of letters, we have to be specific and add int()
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')