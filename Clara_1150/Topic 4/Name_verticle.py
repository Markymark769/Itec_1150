"""

Question 2: For loops - shout your name vertically (5 points)

Write a program that asks the user for their name.

Use a loop to print one letter of their name per line.
Convert each letter to uppercase inside the loop.
In other words, don't convert the whole name to uppercase.

Your program should print any name vertically.
So, store the user's name in a variable, and use that variable in your loop.
Test your program with different example names.

After the loop, print a message with the user's name in the original case they entered it.
For example, if the user's name is "Miriam" and they type in "Miriam", the output from the program will look like this,
"""

# name = 'mark'
#
# for letter in name:
#     print(letter)


name = input('what is your name?')
for letter in name:
    print(letter)

name = input('what is your name?')
upper_text = name.upper()
for letter in upper_text:
    print(letter)
