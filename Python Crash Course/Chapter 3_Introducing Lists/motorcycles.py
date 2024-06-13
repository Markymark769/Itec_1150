#Changing, Adding, and Removing Elements
### modifying elements on a list----------------
##### note)Lets say we have a list and the first item on the list is Honda, we would like to add another item on the list, such as Ducati
##### note) use the [0] method
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
##Adding Elements to a List by using the .append() method ---------------
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
#### new example of append method
### used for when you are usure of the data you want to store
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
# Inserting Elements to a List -----------------------
### adding using the insert() method
### note) at the zero item we are going to insert ducati
motorcycles = ['honda','yamaha','suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
# Removing an Item Using the del Statement -------------------
######## note) the following example removes honda
######## note) this can be done only if you know the location of the item you want to remove. 
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
######## note) the following example removes yamaha
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)
# REmoving an Item using the pop() Method ---------------------
#### note)removing the last item in a list but still using the value from an item you have removed
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
##### using the pop() method to to print statements about the last motorcycle bought
motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
# Popping Items from any Position in a List
### using the pop() method to remove
##### 
motorcycles = ['honda','yamaha','suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
###### recap on when to use the pop() method or the del statement
#### pop()- if you want to use an item as you remove it
#### del statement - when you wnat to delete an item from a list and not use that item in any way
#Removing an Item by Value -----------------------------------
##### using the remove() method
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
####### using the remove() method in variables and sentences 
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
###### The remove() method deletes only the first occurance of the value you specify. 
###### If there is a possibility the value appears more than once in the list, youll need to use
###### a loop to make sure all occurances of the value are removed. 

