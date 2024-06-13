# https://comicvine.gamespot.com/api/documentation#toc-0-2

"""
Mark Porraz
National Park info from API
National Park Guide

1) Make a request from that list at random
2) Pick 5 parks from that list at random
3) make a Word document
4) for each of the random parks, make another API request for that park, write data
from the response to the Word document
5) (next week) get images
6) save the Word document


"""
# the goal is to make a complete working document based off this API
# the first thing we want to do with an API is look at what want to return
# then look to see if the information we have is accurate
# when looking at the API, the first website only gives us the name of the park, we neeed more info
# the other links have more info such as activities, contact info and descriptions

import requests
import random #
import docx
# part 1
park_list_url = 'https://national-parks-1150.azurewebsites.net/api/list'
response_list_of_all_parks = requests.get(park_list_url).json()
# print(park_list_response)

# step 2
list_of_random_parks_chosen = random.sample(response_list_of_all_parks,5)  # list, number of things which is park list url
print(list_of_random_parks_chosen)  # it is always a great idea to print to problem-solve

# step 3
park_word_document = docx.Document()

# step 4
for one_park in list_of_random_parks_chosen:
    print(one_park)
    park_code = one_park['park_code']
    print(park_code)

    url_for_one_park_details =


# step 5

# step 6

# TODO: review the getting started video to know how to do this
# TODO: