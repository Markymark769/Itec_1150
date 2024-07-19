"""
Connar
currency exchange rate.py

"""
from urllib import request
import json
import time
import pprint

key = '95f3608fbcf460e3ae7ad6a5'


def exchange_currency(init_currency, target_currency, amount):
    rate = json.loads(request.urlopen(f'https://v6.exchangerate-api.com/v6/{key}/pair/{init_currency}/{target_currency}').read())['conversion_rate']
    return (float(amount)*float(rate))

# print(exchange_currency('USD', 'EUR', 12))


def main():
    print('WELCOME TO CURRENCY EXCHANGE BOT')
    time.sleep(1)
    print('VERY GOOD VERY NICE EXCHANGE!')
    time.sleep(1)
    print('PRINTING LIST OF SUPPORTED CURRENCY COUNTRY CODES...')
    time.sleep(1)
    pprint.pprint(json.loads(request.urlopen(f'https://v6.exchangerate-api.com/v6/{key}/latest/usd').read())['conversion_rates'].keys())
    time.sleep(1)
    init_currency = input('ENTER COUNTRY CODE OF CURRENCY YOU WANT TO EXCHANGE\n').upper()
    target_currency = input('ENTER COUNTRY CODE OF TARGET CURRENCY\n').upper()
    amount = input('ENTER AMOUNT CURRENCY\n')
    print('EXCHANGING...')
    time.sleep(1)
    print(f'${exchange_currency(init_currency, target_currency, amount)} {target_currency}')


main()
