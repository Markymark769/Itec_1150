"""
Mark Porraz
Clara's class lecture on APIs or JSON
3/27/2024

In all this it is really how we save time in automate things in documents
"""

import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'  # note, when you launch this in a web browser, you can
# see the associated code that it is pulling the data from.
# https://api.coindesk.com/  -->>> means name of other computer
# v1/bpi/currentprice.json  --->>> what data do we want?

response = requests.get(url).json()
print(response)  # response is a dictionary with other dictionaries

# note that the names are made up, and they do not have to match with the keys
# bpi = response['bpi']
# print(bpi)
#
# exchange_rate = bpi['rate_float']
#
# usd_data = bpi['USD']
# print(usd_data)
#
# usd_exchange_rate = usd_data['rate_float']
# print(usd_exchange_rate)
#
# usd_exchange_rate = respo  print(usd_exchange_rate)
