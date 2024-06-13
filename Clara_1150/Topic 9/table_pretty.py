import requests
from pprint import pprint

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url).json()

pprint(response)   # pprint, extra p = pretty print