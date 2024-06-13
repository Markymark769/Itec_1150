"""Mark Porraz, 2/22/2023, My Pets
This program demonstrates the bad way to write code"""

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

