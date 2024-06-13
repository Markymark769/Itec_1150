"""
Mark Porraz
cat.py
This program gets and downloads images from a website
"""

import requests

kitten_picture_urls = ['https://placekitten.com/600/400',
                       'https://placekitten.com/600/401',
                       'https://placekitten.com/320/240']

# note since we have more than one picture we need a loop to run through them all pics,
# otherwise we get an error
# if no loop or only response you will receive raise for invalid schema

for index, url in enumerate(kitten_picture_urls):  # using enumerate will give a number as well as the string
    response = requests.get(url)

    # with open('kitten.jpeg','wb') as file:
    #     for chunk in response.iter_content():
    #         file.write(chunk)
    filename = f'kitten_{index}.jpeg'  # the index is placed there to add a unique name to find the file
    with open(filename, 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)



