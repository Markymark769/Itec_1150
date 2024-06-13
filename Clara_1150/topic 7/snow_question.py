"""
Clara's class 3/20/2024
How a zoom poll works for expecting snow
"""

survey_title = 'Survey Question - Minnesota weather'

question = 'Do you like snow?'

yes_response_text = 'Yes!'
no_response_text = 'No'
dont_care_response_text = 'Don\'t care'

yes_votes = 7
no_votes = 7
dont_care_votes = 2

list_of_choices = ['yes','no','dont care']

for choice in list_of_choices:
    print(choice)

# how can we store choice text and number of voters?
# answer: you can either use a list or a dictionary
# square brackets means list
# curly braces a dictionary

# here are our keys and values

results_list = [
    {
        'response_text': 'Yes!',
        'votes': 7,
        'percentage': 44
    },
{
        'response_text': 'No',
        'votes': 7,
        'percentage': 44
    },
{
        'response_text': 'Don\'t',
        'votes': 2,
        'percentage': 13
    },
]

for one_result_dictionary in results_list:
    response_text = one_result_dictionary
    votes = one_result_dictionary['votes']
    print(f'{response_text} recieved {votes} votes')
