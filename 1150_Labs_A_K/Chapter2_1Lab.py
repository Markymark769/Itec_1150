"""Complete the grade.py program from the lesson slide 15, which has beginning validation:
• Make improvements mentioned in the lesson: 1) Handle all grade levels, down to 0 . 2) Give better feedback for all
grade levels.
• Finalize comments ( doc string at the top and # short comments thru-out)
• Run several times to show ALL the possible options.
(example output shows only one outcome).
• Also complete the apollo.py program, started in the lesson PPT. Validation not required.
• Improvements: 1) add an elif block to give custom feedback if the user's answer is close - within one year of the
correct answer. 2) improve the user feedback text, so they find out the right answer.
• Always: add 2 types of comments, and customize/ improve the program through a testing process.
"""
score = input('Enter quiz score as a whole number from 0-100: ')
if not(score.isnumeric):
    print('Try again, using only a whole number: ')
else:
    score = int(score)
    if score>=90:
        print('Grade: A     Great work!')
    elif score>=80:
        print('Grade: B     Excellent effort!')
    elif score >= 70:
        print('Grade: C     Keep working hard!')
    elif score >=65:
        print('Grade: D     What resources might help?')
    else:
        print('You are currently failing the class.  Have you turned in all your assignments?')
