"""
Name:
Date:
Assignment: lecture slides


"""

# slide 5
# A list of strings
# villains = ['Voldemort', 'Darth Vader', 'Sauron']
#
# # A list of int numbers
# students_per_semester = [97, 122, 89, 103]
# # A list of float numbers
# rainfall_in_mm = [1.9, 7.6, 3.5, 12.2]
#
# # A list with a mixture of data types
# strange_data = ['Voldemort', 100, 3.5]
#
# # A list of lists
# profile_data = [['a', 'b', 'c'], [1, 2, 3], [1.1, 2.2, 3.3]]

#
""" Changing a list item """

quiz_scores = [8, 4, 10, 9, 7]
# What if the student re-took the second quiz?
# Let's say they aced the quiz and scored a 10

# Update the quiz_scores list
quiz_scores[1] = 10
print(quiz_scores)  # prints [8, 10, 10, 9, 7]

# Lists and Loops
# It can be easier to read lists if they
# are written on more than one line
colleges = ['Minneapolis College',
            'Metro State',
            'Saint Paul College',
            'North Hennepin Community College',
            'Century College']

for college in colleges:
    print(college)

# slide 15
credits_per_class = [3, 2, 2, 4]

total = 0

for credits in credits_per_class:
    total = total + credits

print(f'The total number of credits is {total}.')

if total >= 12:
    print('You are a full time student.')
elif total >= 6:
    print('You are a half time student.')
else:
    print('You are less than half time.')

# slide 22
todo_list = []  # Make an empty list

while True:
    task = input('Enter your task or press <ENTER> to stop: ')
    if task:  # An empty string is False
        todo_list.append(task)  # Add task to end of todo_list
    else:
        break

print('Thank you, your tasks are: ')

for task in todo_list:  # For every task in the todo_list,
    print(task)  # print the task.

# import random
#
# movies = ['Star Wars', 'Tron', 'Jarhead', 'The Martian']
# random.shuffle(movies)
#
# for index, movie in enumerate(movies):
#     print(f'{index + 1}: {movie}')

