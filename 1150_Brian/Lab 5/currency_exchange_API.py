"""
Mark Porraz
Clara's class
Currency Exchange
this program writes a currency exchange using a dictionary

(example) convert 100 Euros to Canadian dollars, 100 * 1.3351 = 133.51 Canadian dollars.
"""

rates = {
    'AUD': 1.5311,
    'BGN': 1.9558,
    'BRL': 4.9682,
    'CAD': 1.3351,
    'CHF': 0.9863,
    'CNY': 7.0894,
    'CZK': 24.422,
    'DKK': 7.4419,
    'EUR': 1,
    'GBP': 0.87478,
    'HKD': 7.7493,
    'HRK': 7.5353,
    'HUF': 401.15,
    'IDR': 15491.81,
    'ILS': 3.5065,
    'INR': 81.02,
    'ISK': 145.5,
    'JPY': 145.19,
    'KRW': 1397.7,
    'MXN': 19.2611,
    'MYR': 4.6872,
    'NOK': 10.2019,
    'NZD': 1.6769,
    'PHP': 57.672,
    'PLN': 4.6825,
    'RON': 4.8893,
    'RUB': 86.7666,
    'SEK': 10.8538,
    'SGD': 1.3891,
    'THB': 36.906,
    'TRY': 18.3845,
    'USD': 0.9872,
    'ZAR': 17.7983
}

# step 3 - reading value using a variable that contains the key, that the use
currency_name = input('Entering the currency code to exchange: ')


how_many_euros = float(input('How many Euros to convert? '))

# example - how to get the value for 'CAD' ? - the exchange rate
# cad_exchange_rate = rates[''CAD'] # sometimes we know actual data
exchange_rate = rates[currency_name]  # sometimes the data is in a variable
print(exchange_rate)

exchanged_currency_amount = how_many_euros * exchange_rate
print(f'The total of the currency exchanged is: {exchanged_currency_amount} ')  # TODO print a nice neat message
# TODO: If the user enters a currency code that is not in the dictionary,
#  print a message telling them that the conversion can't be done.

# step 2 - reading value using a variable that contains the key
# cad_currency_name = 'CAD'
# example- how to get the value for 'CAD' ? - the exchange rate
# cad_exchange_rate = rate['CAD']  # sometimes we know actual
# print(cad_exchange_rate)

# Step 1 : reading the value by the key, using a string
# chf_exchange_rate = rate['CHF']
# print(chf_exchange_rate)
