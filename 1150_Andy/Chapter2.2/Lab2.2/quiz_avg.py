"""Mark Porraz, 2/12/2023, Quiz Averages
This program calculates, displays the total, and average
the quiz score for each student in a group."""

#How many students are in the group
#How many quizzes do they take?
#Quiz info for student #1:
#enter score for quiz #:>?

total_points = 0.00
while True:         # Loop to check number of students input is an integer
    try:
        s_num = int(input('How many students are in the group? '))
    except ValueError:
        print('Would you kindly enter the number already?')
    else:
        break
while True:         #Loop for number of quizzes
    try:
        quiz_num = int(input('How many quizzes did they take? '))
    except ValueError:          #makes sure input number is an integer
        print('Please enter the number of quizzes in a whole, positive number?')
    else:
        break


for s in range(s_num): # loops through the groups
    print(f'Quiz info for Student #{s+1}')

    for s in range(quiz_num): #loops through all the quizes
        quiz_score = float(input(f'Enter the score for Quiz # {s +1}: '))
        total_points = total_points + quiz_score
        average = total_points / quiz_num

    print(f'\tTotal quiz points for  = {total_points :<.2f}')
    print(f'The average score for the student {average :<.2f}')


