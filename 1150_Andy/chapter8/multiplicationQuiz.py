"""
Mark Porraz, 4/9/2023, idiot.py
"""


import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # in the for loop, the program will pick two single-digit numbers to multiply


    # Pick two numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    # pyip.inputStr() function handles most features in program
    #The argument we pass for allowRegexes is a list with the regex string
    # '^%s$', where %s is replaced with the correct answer.

    #The argument we pass for blocklistRegexes is a list with ('.*', 'Incorrect!').

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*','Incorrect!')], timeout= 8, limit=3)
        #, pyip.inputStr() raises a TimeoutException exception
        # If the user answers incorrectly more than 3 times,
        # it raises a RetryLimitException exception.
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')

    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1

    time.sleep(1) # Brief pause to let user see the result
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))