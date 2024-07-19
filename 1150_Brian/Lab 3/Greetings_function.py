"""
Name: Mark Porraz
Date: 7/1/2024
Program: grettings.py

lAB 3: Question 1
This time, the computer is very happy to meet you.
Modify the code to ask for the users name and then return the greeting
all in UPPERCASE, with !!!! after it. So, if the user's name is Miriam,
the greeting function will return: HELLO MIRIAM

"""


def greeting(name):
    message = f'Hello {name}!'
    return message


def main():
    username = input('Please enter your name:  ')  # note the change
    hello_message = greeting(username)
    print(hello_message.upper())  # note the change from the original example


main()
