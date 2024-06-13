"""
Mark Porraz
"""


import requests  # alt+enter or hover over error to import
from pprint import pprint  # optional use pprint to print the response


def get_random_activity():
    url = 'https://www.boredapi.com/api/activity'
    # get response and convert json response to python dictionary
    response = requests.get(url).json()
    # pprint(response)  # make sure you import pprint at the top of the file
    # extract the activity text
    activity = response['activity']  # spelling must match dictionary keys
    return activity


def main():
    # Can you use a while loop to ask the user if they
    # would like another suggestion?
    # make another request if they do
    # end program if not
    while True:  # how many times does this repeat? infinity times
        activity = get_random_activity()
        print(f'Your suggested activity is: {activity}')
        another_activity = input('Another suggestion? Enter "Y" for another, anything else to quit')
        if another_activity.lower() != 'y':  # end loop if not Y or y for yes
            break

    print('Thanks for using the program, hope you found something fun to do!')


main()
