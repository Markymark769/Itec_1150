# Nesting
# A List of Dictionaries 
### example 1 ###
alien_0 = {'color': 'green','points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red','points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
### example 2 ###
### using range() to create a fleet of 30 aliens
### make an empty list for the alien
aliens = []
### make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green','points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

### show alien
for alien in aliens[:5]:
    print(alien)
print("...")

### show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

### example 3 ###
### similar to the example above, except using a for loop and
### if statement to change the color of aliens.

### make an empty list for storing aliens.
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green','points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

# A List in a Dictionary
### example 4 ###
### store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
    }
### summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

### example 5 ###
favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A Dictionary in a Dictionary
### example 6 ###
user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstien',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

for username, user_info in user.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
