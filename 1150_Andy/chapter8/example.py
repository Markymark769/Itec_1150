import bs4
import requests
from pprint import pprint

my_url = r'https://automatetheboringstuff.com/index.html'

my_response = requests.get(my_url)

my_soup = bs4.BeautifulSoup(my_response.text, 'html.parser')

for element in my_soup.select('li a'):
    pprint( element.getText() )