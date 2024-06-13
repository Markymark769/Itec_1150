"""
Mark Porraz
API request program - random cat fact
4/3/2024
"""

import requests

data = requests.get('https://catfact.ninja/fact').json()
# you are making a variable called data
# that data is getting a request from the website https://catfact.ninja/fact
    # what server to connect to: https://catfact
    # what data do you want:.ninja/fact
# we are then converting our JSAON response into a python dictionary
print(data)

fact = data['fact']  # we can create dictionary and access the value by the key
# in this case the key is 'fact', we are going to get the value based off that fact we pulled out
print('A cat fact is: ' + fact)


