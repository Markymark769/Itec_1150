"""
Mark Porraz
2/14/2024

Question 2: Quiz question function (6 points)

Write a quiz function that takes two arguments - one quiz question and the question's correct answer.

In your quiz function, you will print the question, and ask the user for the answer. If the user gets the answer correct, print a success message. Else, print a message with the correct answer.   Your function does not need to return anything.

Create a main function. From your main function, call your quiz function twice. So your program will ask the user one question, verify the answer, ask the user another question, verify that answer. Here's some suggestions for questions and their answers,

Q: Which planet is closest to the sun?  A: Mercury
Q: Who painted the Mona Lisa? A: Leonardo da Vinci
"""

def main():
    question1 = int(input('what is the airspeed velocity of an unladen swallow (in miles per second)? '))
    question2 = int(input('What year did Apollo 11 land on the moon? '))

    correct_answer = correct_answer_check(question1,question2)

    if correct_answer:
        print('your answer is correct')
    else:
        print('you are answer is not correct')

def correct_answer_check(question1,question2):
    if question1 == 20:
        print('you must like Monty Python ')
    else:
        print('maybe, you should watch Monty Python')
    if question2 == :


