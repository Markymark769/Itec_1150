"""
Name: Mark Porraz
Date: 7/1/2024
Program: quiz question function.py

Write a function that takes two arguments: a quiz question and the correct answer.

- In your function, you will print the question, and ask the user for an answer.
- If the user gets the answer correct, print a success message. Otherwise, print a
message saying they got it wrong and show the correct answer. Your function doesn't need to return anything.

- In your main program code, all your function with two example quiz questions. Here's some suggestions,
    - Q: What year did Apollo 11 land on the moon? A: 1969
    - Q: Who painted the Mona Lisa? A: Leonardo da Vinci

"""
#
# def main():
#     question1 = int(input('What year did Apollo 11 land on the moon?'))
#     question2 = str(input('Who painted the Mona Lisa?'))
#
#     correct_answer = correct_answer_check(question1, question2)
#     if correct_answer:
#         print('your answer is correct')
#     else:
#         print('your answer is not correct.')
#
# def correct_answer_check(question1,question2):
#     if question1 == 1969:
#         print('Yes, you know what year we went to the moon.')
#     else:
#         print('you must not know what year we went to the moon')
#     if question2.lower() == 'Leonardo da Vinci':
#         print('yes, you know who painted the mona lisa')
#     # else:
#         print('you must not know who painted the mona lisa.')

# Version 2
def quiz(question, answer):
    if input(f'{question} ') == answer:
        print('Correct!')
    else:
        print(f'Incorrect. The answer is {answer}')


quiz("When did we land on the moon?", "1969")
quiz("Who painted the Mona Lisa?", "Leonardo da Vinci")