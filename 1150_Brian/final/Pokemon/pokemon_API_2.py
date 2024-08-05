import requests
import random
import docx

# step 1 make the API call
pokemon_list_url = 'https://pokeapi.co/api/v2/pokemon?limit=1000'
response_list_of_all_Pokemon_stats = requests.get(pokemon_list_url).json()

# Extract the list of Pokémon from the API response
list_of_pokemon_chosen = response_list_of_all_Pokemon_stats['results']  # this pulls out the key of results from
# the dictionary to get the value

pokemon_dict ={}

list_of_random_pokemon_chosen = random.sample(list_of_pokemon_chosen, 20)
print(list_of_random_pokemon_chosen)

# step 3: create the Word document
pokemon_word_document = docx.Document()

# step 4: create a loop among the chosen Pokémon and get the details for the Word Document
for one_pokemon in list_of_random_pokemon_chosen:
    if pokemon_dict:
        name = one_pokemon['name']
        indiv_poke_url = one_pokemon['url']
    print(list_of_pokemon_chosen)
        