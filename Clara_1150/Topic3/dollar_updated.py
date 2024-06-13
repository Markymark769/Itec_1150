"""
Mark Porraz
1/24/2024

Do you have a dollar?

Write a program that asks the user how many cents (penny coins) they have.

If they have less than 100 cents, print the message 'you have less than a dollar'.
Or, the user could have exactly 100 cents, so print the message 'you have exactly one dollar'
Or, they could have more than 100 cents, so print the message 'you have more than one dollar'
(Bonus question, +3 points: extend your program to check if the user has an exact number of dollars in cents
(penny coins), for example 100 or 300 or 700 pennies. Print a message if so. Hint: look up the modulo % operator.
It's covered in Chapter 1 of the textbook.)
"""

number_of_cents = int(input('How many cents do you have?'))

if number_of_cents < 100:
    print("You have less than a dollar.")

