import random
import requests
# import docx

# makes a call the api, note: it is hard to find the working api
pokemon_list_url = 'https://pokeapi.co/api/v2/pokemon?limit=1000'
response_list_of_Pokemon_stats = requests.get(pokemon_list_url).json()

# Extract the list of Pokémon from the API response
list_of_pokemon = response_list_of_Pokemon_stats['results']  # this pulls out the key of results from the dictionary
# to get the value

# Get a sample of how many random Pokémon, in this case it is 10
list_of_random_pokemon = random.sample(list_of_pokemon, 20)
print(list_of_random_pokemon)

# # step 3
# pokemon_word_document = docx.Document()
#
# # step 4
# for one_pokemon in list_of_random_pokemon:
#     print(one_pokemon)
#     park_code = one_pokemon['park_code']
#     print(park_code)
