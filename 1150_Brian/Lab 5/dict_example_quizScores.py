"""
Mark Porraz
7/17/2024
quiz scores w/ dictionaries
"""

# Each student took 3 quizzes
quiz_scores = {
'Ahmed': [10, 9, 5],
'Bella': [9, 10, 10],
'Cody':[6, 7, 9]
}

# Loop
for student, list_of_scores in quiz_scores.items():
    input(f'{student}\'s scores are: {list_of_scores}')

# Get one list
cody_scores = quiz_scores['Cody']
# cody_scores is a list so we can do all the list operations

for i, score in enumerate(cody_scores):
    print(f'On quiz {i+1} Cody scored {score}.')

cody_max = max(cody_scores)
print(f'Cody\'s best score is {cody_max}.')
