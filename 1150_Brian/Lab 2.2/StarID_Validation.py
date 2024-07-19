"""
Name: Mark Porraz
Date: 7/1/2024
Program: Star ID validation

Write a program to calculate the average number of students taking Programming Logic the past four semesters.


Write a program that uses a for loop to ask the user for number of students in each of the last four semesters.
Your for loop should contain an input() statement to ask the user for a number of students that semester.

Add up all of the user answers, and divide by 4 to calculate the average.
Print the average number of students registered for Programming Logic over the last four semesters.
For test data, total number of students registered in
Programming Logic class for the last 4 semesters was 92, 84, 73, and 90.

"""

# for
#     print('Enter the number of students in each of the last four semesters. ')
#     semester1 = input('input the ')
# for


semesters = 4
total = 0
for semester in range(semesters):
    students = int(input('How many students in semester ' + str(semester+1) + '? '))
    total = total + students
average = total / semesters
print('There were an average of ' + str(average) + ' students in 1150 each semester.')

