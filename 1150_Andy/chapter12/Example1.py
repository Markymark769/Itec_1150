# import requests
#
# my_url = r'https://automatetheboringstuff.com/no_page_named_this.html'
#
# my_response = requests.get(my_url)
#
# print(my_response.status_code)

# import requests
#
# my_url = r'https://automatetheboringstuff.com/index.html'
#
# my_response = requests.get(my_url)
#
# my_html_body = my_response.text
#
# print( my_html_body )

# import bs4
# import requests
#
# my_url = r'https://automatetheboringstuff.com/index.html'
#
# my_response = requests.get(my_url)
#
# print( my_response.text )
#
# my_soup = bs4.BeautifulSoup(my_response.text, 'html.parser')
#
# print( my_soup.select('title') )
# print( my_soup.select('title')[0] )
# print( my_soup.select('title')[0].getText() )

# import bs4
# import requests
# from pprint import pprint
#
# my_url = r'https://automatetheboringstuff.com/index.html'
#
# my_response = requests.get(my_url)
#
# my_soup = bs4.BeautifulSoup(my_response.text, 'html.parser')
#
# for element in my_soup.select('li a'):
#     pprint( element.getText() )

import re
import requests

my_url = r'https://automatetheboringstuff.com/index.html'

my_response = requests.get(my_url)

my_html_body = my_response.text

my_html_body_lines = my_html_body.splitlines()

my_regex = re.compile(r'>Chapter')
for line in my_html_body_lines:
    if my_regex.search(line):
        print( line )