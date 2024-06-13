"""
Question 3: While Loops - Quiz Question (5 points)

Modify the quiz question program from the last topic to use a while loop instead of an
if statement (Quiz question program that asked What's the capital of Wisconsin?)
so the user can keep trying answers until they get the answer right.
Make sure you print a message that asks the user to try again if they get the answer wrong,
and print a message that says "correct!" when they get the answer right.
The user is allowed as many attempts as they need to get the right answer.

Example output from the same program if the user is correct, it will do this,
"""

# while True:
#     quiz_question = input('What is the capital of Wisconsin ?')
#     if quiz_question != "madison":
#         print(f'Sorry, {quiz_question} is not the capital of Wisconsin.  Try again.')
#     else:
#         print('Correct! madison is the right answer')
#         break

# while True:
#     books = int(input('What is the capital of Wisconsin ?'))
#     if books != books.isnumeric():
#         print(f'Sorry, try a whole number')
#     else:
#         print('Correct! madison is the right answer')
#         break

while True:
    answer = input('What is the capital of Wisconsin? ')
    if not answer.isnumeric():
        print('Sorry, try entering a whole number')
    else:
        print('Correct! That is the right answer')
        break

