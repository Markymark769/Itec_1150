"""
Brian's example
"""

from urllib import request
import json
import os
from datetime import datetime
import shelve


def main():
    cached = False
    directory = 'ExchangeRates'
    # if the directory doesn't exist ...
    if not os.path.exists(directory):
        # ... try to create it
        try:
            os.makedirs(directory)
        except IOError:
            print(f'IOError: Unable to create the directory "{directory}"')

    # if it's there, let's go into it
    os.chdir(directory)
    # now is a datetime object that represents the current date/time
    now = datetime.now()
    # strftime formats dates into strings.
    # More info here: https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior
    # %Y = year, %m = month %d = day
    now_string = now.strftime('%Y-%m-%d')  # the ISO 8601 standard
    # see https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates
    # setup a filename in the format ConversionRates_2024-07-12.db
    filename = f'ConversionRates_{now_string}'
    # do we have a cache file for today?
    shelf = shelve.open(filename)
    # get the exchange rate data from the shelf
    exchange_rates = shelf.get('exchange_rates')
    # if there is a cache file, tell the user
    if exchange_rates:
        print(f'Using cached data from the file {filename}')
        cached = True
    else:
        print('Fetching exchange rate data from the web ...', end='')
        # get the exchange rate data
        exchange_rates = get_exchange_rates()
        print(' DONE')
    if not cached:
        # tell the user we're now going to cache the data
        print(f'Caching rates data to the file {filename}:...', end='')
        shelf['exchange_rates'] = exchange_rates
        print(' DONE')
    shelf.close()  # Remember to close your shelf

    user_currency = input('What currency (three letter code) would you like to convert to (or ENTER to quit)? ')
    while user_currency:
        if user_currency.upper() in exchange_rates['conversion_rates']:
            dollars = float(input('How many dollars to convert? '))
            conversion = exchange_rates['conversion_rates'][user_currency.upper()]
            print(f'As of {exchange_rates["time_last_update_utc"]}, ${dollars:,.2f} is about {conversion * dollars:,.2f} {user_currency.upper()}')
        else:
            print(f'{user_currency.upper()} is not a currency I can convert. I know about:\n')
            count = 0
            for currency in exchange_rates['conversion_rates']:
                count += 1
                print(f'{currency}, ', end=f'')
                if count % 13 == 0:
                    print()

        user_currency = input('\nWhat currency (three letter code) would you like to convert to (or ENTER to quit)? ')


# You do not need to modify any code below here.

def get_exchange_rates():
    """ Connect to the exchangerate-api.com server and request the latest exchange rates,
    relative to US Dollars.  Return the response as a dictionary. """
    api_key = 'ad5754e743f5135340643429'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

    try:  # Attempt to connect to the exchangeratesapi server
        response = request.urlopen(url).read()   # and get the server's response
        data = json.loads(response)   # convert the response to a Python dictionary
        return data # return the dictionary
    except:  # this code runs if there's any error fetching data.
        # It returns some example data, that has the same structure as real data, to use instead
        # So it's no problem if you don't have an internet connection or there exchangeratesapi server is down.
        print('There was an error fetching real data. Perhaps you are offline? Returning example data.')
        return example_exchange_rates()


def example_exchange_rates():
    """ In case the exchangeratesapi.io is not available, the program will use this example data.
     This data has the same structure as real data, so your program doesn't need to worry if real data
     or example data is used. """

    example_data = {
        'result': 'success',
        'documentation': 'https://www.exchangerate-api.com/docs',
        'terms_of_use': 'https://www.exchangerate-api.com/terms',
        'time_last_update_unix': 1720396801,
        'time_last_update_utc': 'Mon, 08 Jul 2024 00:00:01 +0000',
        'time_next_update_unix': 1720483201,
        'time_next_update_utc': 'Tue, 09 Jul 2024 00:00:01 +0000',
        'base_code': 'USD',
        'conversion_rates': {
            'USD': 1,          'AED': 3.6725,     'AFN': 71.0583,    'ALL': 92.6905,
            'AMD': 388.1535,   'ANG': 1.79,       'AOA': 872.8072,   'ARS': 918.25,
            'AUD': 1.4827,     'AWG': 1.79,       'AZN': 1.7004,     'BAM': 1.8066,
            'BBD': 2.0,        'BDT': 117.5095,   'BGN': 1.8066,     'BHD': 0.376,
            'BIF': 2873.1942,  'BMD': 1.0,        'BND': 1.3491,     'BOB': 6.9066,
            'BRL': 5.4694,     'BSD': 1.0,        'BTN': 83.5263,    'BWP': 13.617,
            'BYN': 3.2718,     'BZD': 2.0,        'CAD': 1.3631,     'CDF': 2834.578,
            'CHF': 0.8957,     'CLP': 936.6707,   'CNY': 7.2943,     'COP': 4094.533,
            'CRC': 527.935,    'CUP': 24.0,       'CVE': 101.8525,   'CZK': 23.2459,
            'DJF': 177.721,    'DKK': 6.891,      'DOP': 59.0519,    'DZD': 134.4226,
            'EGP': 47.9555,    'ERN': 15.0,       'ETB': 57.884,     'EUR': 0.9237,
            'FJD': 2.2323,     'FKP': 0.7815,     'FOK': 6.8912,     'GBP': 0.7815,
            'GEL': 2.7968,     'GGP': 0.7815,     'GHS': 15.4624,    'GIP': 0.7815,
            'GMD': 65.2826,    'GNF': 8597.2548,  'GTQ': 7.7609,     'GYD': 209.4051,
            'HKD': 7.8129,     'HNL': 24.7424,    'HRK': 6.9597,     'HTG': 131.9614,
            'HUF': 362.2588,   'IDR': 16278.6441, 'ILS': 3.6902,     'IMP': 0.7815,
            'INR': 83.5164,    'IQD': 1311.0944,  'IRR': 42079.6654, 'ISK': 137.9201,
            'JEP': 0.7815,     'JMD': 156.5276,   'JOD': 0.709,      'JPY': 160.7947,
            'KES': 128.2425,   'KGS': 86.4968,    'KHR': 4132.0327,  'KID': 1.4829,
            'KMF': 454.4337,   'KRW': 1377.2648,  'KWD': 0.3062,     'KYD': 0.8333,
            'KZT': 478.4111,   'LAK': 22109.5734, 'LBP': 89500.0,    'LKR': 304.3346,
            'LRD': 194.2186,   'LSL': 18.1616,    'LYD': 4.8776,     'MAD': 9.8898,
            'MDL': 17.8358,    'MGA': 4476.9615,  'MKD': 56.9192,    'MMK': 2099.4143,
            'MNT': 3363.3219,  'MOP': 8.0474,     'MRU': 39.7771,    'MUR': 46.8389,
            'MVR': 15.4103,    'MWK': 1743.3076,  'MXN': 18.1096,    'MYR': 4.7089,
            'MZN': 63.9404,    'NAD': 18.1616,    'NGN': 1525.2995,  'NIO': 36.7784,
            'NOK': 10.5611,    'NPR': 133.642,    'NZD': 1.6286,     'OMR': 0.3845,
            'PAB': 1.0,        'PEN': 3.795,      'PGK': 3.8501,     'PHP': 58.5393,
            'PKR': 278.4703,   'PLN': 3.9544,     'PYG': 7527.6162,  'QAR': 3.64,
            'RON': 4.5976,     'RSD': 108.1343,   'RUB': 88.0599,    'RWF': 1322.1064,
            'SAR': 3.75,       'SBD': 8.5186,     'SCR': 13.7441,    'SDG': 532.9759,
            'SEK': 10.4962,    'SGD': 1.349,      'SHP': 0.7815,     'SLE': 22.6679,
            'SLL': 22667.9196, 'SOS': 572.149,    'SRD': 30.6557,    'SSP': 2001.8756,
            'STN': 22.6308,    'SYP': 12989.2363, 'SZL': 18.1616,    'THB': 36.5235,
            'TJS': 10.7527,    'TMT': 3.501,      'TND': 3.1253,     'TOP': 2.3293,
            'TRY': 32.6941,    'TTD': 6.7597,     'TVD': 1.4829,     'TWD': 32.4208,
            'TZS': 2637.6108,  'UAH': 40.5603,    'UGX': 3695.763,   'UYU': 40.2528,
            'UZS': 12578.1541, 'VES': 36.5123,    'VND': 25464.899,  'VUV': 119.419,
            'WST': 2.7349,     'XAF': 605.9116,   'XCD': 2.7,        'XDR': 0.7555,
            'XOF': 605.9116,   'XPF': 110.2277,   'YER': 250.2883,   'ZAR': 18.1488,
            'ZMW': 24.3701, 'ZWL': 13.6946}
    }

    return example_data


main()  # Remember to call main() otherwise your program won't run

# in this program, that assignment is generally asking you to place your program that was worked on from
# chapter 5 and place it into your program for chapter 9.


