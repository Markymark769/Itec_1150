"""
Mark Porraz
2/12/2024
greetings_function.py

Question 1: Greetings Function! (4 points)

Start with the greeting program, the first program with functions we used in Python Tutor.
It's from this video. This time, the computer is very happy to meet you.  Modify the greeting
function to return the user's name in uppercase, with !!!! after it.  The greeting function
should convert the name to uppercase.

So, if the user's name is Miriam, the greeting function will return 'HELLO MIRIAM!!!!'
"""

def greeting(name):
    message = f'Hello {name}!'
    return message

def main():
    username = 'Zoe'
    hello_message = greeting(username)
    print(hello_message)


main()


