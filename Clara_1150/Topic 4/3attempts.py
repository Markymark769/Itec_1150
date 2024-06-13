# attempt = 0  # Initialize attempt counter outside the loop
#
# while attempt < 3:  # Limit to three attempts
#     quiz_question = input('What is the capital of Wisconsin? ')
#     if quiz_question.lower() != "madison":
#         attempt += 1  # Increment attempt counter
#         print(f'Sorry, {quiz_question} is not the capital of Wisconsin. Try again.')
#     else:
#         print('Correct! Madison is the right answer.')
#         break  # Exit the loop if the correct answer is given
#
# if attempt == 3:
#     print("Sorry, you've used all your attempts. The correct answer is Madison.")


for attempt in range(3):
    quiz_question = input('What is the capital of Wisconsin? ')
    if quiz_question.lower() != "madison":
        print(f'Sorry, {quiz_question} is not the capital of Wisconsin.  Try again.')
    else:
        print('Correct! Madison is the right answer.')
        break
else:
    print("Sorry, you've used all your attempts. The correct answer is Madison.")

for attempt in range(3):
    quiz_question = input('What is the capital of Wisconsin? ')
    if quiz_question.lower() != "madison":
        print(f'Sorry, {quiz_question} is not the capital of Wisconsin. Try again.')
    else:
        print('Correct! Madison is the right answer.')
        break
else:
    print("Sorry, you've used all your attempts. The correct answer is Madison.")

