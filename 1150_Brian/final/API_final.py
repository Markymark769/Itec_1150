"""
Mark Porraz
Brian's class
8/1/2024

using an API in your final

code from Stack Overflow
https://stackoverflow.com/questions/920645/when-to-use-while-or-for-in-python

"""

# import statements, if needed
import random
import requests

# makes a call the api, note: it is hard to find the working api
pokemon_list_url = 'https://pokeapi.co/api/v2/pokemon?limit=1000'
response_list_of_Pokemon_stats = requests.get(pokemon_list_url).json()

# Extract the list of Pokémon from the API response
list_of_pokemon = response_list_of_Pokemon_stats['results']  # this pulls out the key of results from the dictionary
# to get the value

# Get a sample of how many random Pokémon, in this case it is 10
list_of_random_pokemon = random.sample(list_of_pokemon, 10)
print(list_of_random_pokemon)


