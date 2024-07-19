"""
name: Mark Porraz
date: 7/1/2024
project: quiz question version 2

This program should do the same as Problem 1 above, but make these changes:

- Only let the user have 3 attempts to get the answer correct
- Count how many attempts it took the user to get the answer right
- If the user gets the right answer before they run out of attempts,
print a message saying how many attempts the user needed
- If the user runs out of attempts, end the loop and print a message
with the correct answer.


- You can use a for loop or a while loop for this problem.

"""

print("Quiz program!")
attempt = 0  # Initialize attempt counter outside the loop
while attempt < 3:  # Limit to three attempts
    quiz_question = input('What is the capital of Wisconsin? ')
    if quiz_question.lower() != "madison":
        attempt += 1  # Increment attempt counter
        print(f'Sorry, {quiz_question} is not the capital of Wisconsin. Try again.')
    else:
        print('Correct! Madison is the right answer.')
        break  # Exit the loop if the correct answer is given

if attempt == 3:
    print("Sorry, you've used all your attempts. The correct answer is Madison.")
