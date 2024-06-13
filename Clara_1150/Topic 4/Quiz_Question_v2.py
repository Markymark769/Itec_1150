"""
Mark Porraz
2/6/2024
Quiz Question v2

Question #4
This program should do the same as Question 3, but make these changes:

Only let the user have 3 attempts to get the answer correct
Count how many attempts it took the user to get the answer right (Hint: you may need another variable,
or you can use the counter in a for loop)
If the user gets the right answer before they run out of attempts, print a message saying how many
attempts the user needed
If the user runs out of attempts, end the loop and print a message with the correct answer. (Hint: one way to solve
this is to look in the textbook which discusses a way to end a loop)

You can solve this problem with a for loop or a while loop.  We saw an example that used a for loop with an if
statement inside it in the lectures, you can write if statements inside while loops too.
"""

# example 1 # note, this is almost there. But this does not end at 3 wrong attempts
# attempt = 0
# while attempt < 3:
#     quiz_question = input('What is the capital of Wisconsin ?')
#     if quiz_question.lower() != "madison":
#         print(print(f'Sorry, {quiz_question} is not the capital of Wisconsin.  Try again.'))
#     elif attempt == 3:
#         print(f"Sorry, you have used up all of your attempts. The correct answer is Madison")
#     else:
#         print('Correct! madison is the right answer')
#         break
#
#
# # example 2
# for attempt in range(3):
#     quiz_question = input('What is the capital of Wisconsin? ')
#     if quiz_question != "madison":
#         print(f'Sorry, {quiz_question} is not the capital of Wisconsin.  Try again.')
#     else:
#         print('Correct! Madison is the right answer.')
#         break
# else:
#     print("Sorry, you've used all your attempts. The correct answer is Madison.")
#
#
# # example 3
# attempts = 3
# for attempt in range(attempts):
#     quiz_question = input('What is the capital of Wisconsin? ')
#     if quiz_question != "madison":
#         print(f'Sorry, {quiz_question} is not the capital of Wisconsin.  Try again.')
#     else:
#         print('Correct! Madison is the right answer.')
# else:
#     print("Sorry, you've used all your attempts. The correct answer is Madison.")
#
# example 4
attempt = 0
max_attempts = 3

while attempt < max_attempts:
    quiz_question = input('What is the capital of Wisconsin? ')
    if quiz_question.lower() != "madison":
        print(f'Sorry, {quiz_question} is not the capital of Wisconsin. Try again.')
    else:
        print('Correct! Madison is the right answer.')
        break
    attempt += 1

if attempt == max_attempts:
    print(f"Sorry, you have used up all of your attempts. The correct answer is Madison.")

