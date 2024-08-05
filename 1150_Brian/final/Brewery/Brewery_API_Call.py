"""
Mark Porraz
8/6/2024
Brewery_API.py

Here is where I make calls for brewers and try to sort them locally

Here is the grand website where data is pulled from:
https://www.openbrewerydb.org/documentation#by_dist
"""

import requests
import random

# step 1 make API call
url = 'https://api.openbrewerydb.org/v1/breweries'
response_list_of_all_breweries = requests.get(url).json()
# print(brewery_list_url)

# step 2
list_of_random_breweries_chosen = random.sample(response_list_of_all_breweries, 20)
print(list_of_random_breweries_chosen)


# step 4
for one_brewery in list_of_random_breweries_chosen:
    print(one_brewery)
    brewery_id = one_brewery['id']

    url_for_one_brewery_details = 'https://api.openbrewerydb.org/v1/breweries' + brewery_id
    print(url_for_one_brewery_details)