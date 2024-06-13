# A Simple Disctionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#Working with Dictionaries
### A dictionary is a collection of key value pairs. Each key is connected
### to a value, and you can use the key to access the value associated with
### that key. A keys value can be a number, string, a list, or even another
### dictionary.
### a key value pair is a set of values associated with each other. When you
### provide a key, in return comes the value associated with the key. 
### every key is connected by a (:)
### individual key value pairs seperated by (,)
### 
# Accessing Values in a Dictionary
### to get the value associated with a key, give the name of the dictionary
### and then place the key inside a set of square brackets.
### example 2 ###
alien_0 = {'color': 'green'}
print(alien_0['color'])

### example 3 ###
alien_0 = {'color':'green', 'points': 5 }

new_points= alien_0['points']
print(f"You just earned {new_points} points!")

# Adding New Key-Value Pairs
### adding x and y coordinates to the alien

### example 4 ###
### we add a new key value pair to the dictionary:'x_position' 
### and value 0. we do the same for the 'y_position'
### when print is modified we see two additional pair values.
###
alien_0 = {'color':'green', 'points': 5 }
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
### we define a dictionary with an empty set of braces and then add each
### key value pair on its own line. 
### example 5 ###
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary
### to modify a value in a dictionary, give the name of the dictionary
### with the key in square brackets and then the new value you want associated
### with the key.
### example 6 ###
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}.")

### tracking the position of an alien that can move different speeds.
### example 7 ###
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

####move alien to the right
####determimne how far to move the alien based on it's current speed. 
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this alien is fast as hell
    x_increment = 3
# the new posotion is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing Key Value Pairs
alien_0 = {'color': 'green','points' : 5 }
print(alien_0)

del alien_0['points']
print(alien_0)
