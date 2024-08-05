"""
Mark Porraz
8/6/2024
Pokemon_API_Word.py

Here is where I make a call to pull 20 randomly selected Pokémon and place them in a Word document

Here is the grand website where data is pulled from:
https://www.openbrewerydb.org/documentation#by_dist
"""

import random
import requests
import docx

# step 1 make the API call
pokemon_list_url = 'https://pokeapi.co/api/v2/pokemon?limit=1000'
response_list_of_all_Pokemon_stats = requests.get(pokemon_list_url).json()

# Extract the list of Pokémon from the API response
list_of_pokemon_chosen = response_list_of_all_Pokemon_stats['results']  # this pulls out the key of results from
# the dictionary to get the value

# step 2
# Get a sample of how many random Pokémon, in this case it is 20
list_of_random_pokemon_chosen = random.sample(list_of_pokemon_chosen, 20)
print(list_of_random_pokemon_chosen)

# step 3: create the Word document
pokemon_word_document = docx.Document()

# step 4: create a loop among the chosen Pokémon and get the details for the Word Document
for one_pokemon in list_of_random_pokemon_chosen:
    # print(one_pokemon)
    results = one_pokemon['results']
    # print(results)
    url_for_one_pokemon_details = f'https://pokeapi.co/api/v2/pokemon?limit=1000/{one_pokemon}'
    print(url_for_one_pokemon_details)
    one_pokemon_details_response = requests.get(url_for_one_pokemon_details)
    print(one_pokemon_details_response)
