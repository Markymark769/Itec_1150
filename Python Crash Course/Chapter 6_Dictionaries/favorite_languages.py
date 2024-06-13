### example 1
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil' : 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# Using get() to Acsess Values
### example 2 ### error produced
#alien_0 = {'color': 'green','speed': 'slow'}
#print(alien_0['points'])

#Traceback (most recent call last):
#  File "c:\Users\Allysha O'Donnell\Documents\Coding 22-23\chapter 6_ Dictionaries\favorite_languages.py", line 14, in <module>
#    print(alien_0['points'])

alien_0 = {'color': 'green','speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping Through a Dictionary
### looping can be taken place between dictionary's key value pairs, through its keys, or its values.
# Looping Through All Key-Value Pairs
### example 3 ###
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# Looping Through a Dictionary's Keys in a Particular Order
### example 4 ###
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
# Looping Through All Values in a Dictionary
### example 5 ###
### using the values() method to return to a value without any keys.
### the for statement pulls each value from a dictionary and assigns
### it to the variable language.
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
### example 6 ###
### a set is a collection in which each item must be unique:
### a set is used when there is a large number of respondants
### and the result would be a very repetitive list.
favorite_languages = {
    ########################### deleted to make less repetitive.
}

print(" The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
### when you wrap  set() around a list that contains duplicate items, the 
### unique items in the list are identifed and builds a set from said items.