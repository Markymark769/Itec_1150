# Passing Arguements
#### a function call may need multiple arguements. You can pass arguements to your
#### functions in a number of ways. Positional arguements need to be the same order
#### the parameters were written: keyword arguements, where each arguement consists
#### of a variable name and a value; and lists and dictionaries of values. 

# Positional Arguements

#### Python must match each arguement in the function call with a parameter in the 
#### function definition. The simplist way to do this is based on the order of the 
#### arguements provided. Values matched up this way are called positional arguements.
from pydoc import describe

##### example 1 ####

def describe_pet(animal_type, pet_name):
    """"Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

# Multiple Function Calls

##### example 2 #####
def describe_pet(animal_type, pet_name):
    """"Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')

# Order Matters in Positional Arguements

##### example 3 #####
def describe_pet(animal_type, pet_name):
    """"Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry','hamster')

# Keyword Arguements
### keyword arguement - a name-value pair that you pass to a function. 
### You directly associate the name and the value within the arguement, so when you
### pass the arguement to the function, there is no confusion. Keyword arguements free from
### you having to worry about correctly ordering your arguements in the function call, and
### they clarify the role of each value in the function call.

### rewriting the keyword arguement

##### example 4 #####
def describe_pet(animal_type, pet_name):
    """"Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type= 'hamster', pet_name= 'harry')
#### two ways to end up at the same output
###describe_pet(animal_type= 'hamster', pet_name= 'harry') 
###describe_pet(pet_name='harry', animal_type= 'hamster')

# Default Values

### Default Values -If an arguement for a parameter is provided in the function call, 
### Python uses the arguement value. If not, it uses the parameter's default value. 
### so when you define a default value for a parameter, you can exclude the corresponding
### arguement you'd ususally write in the fucntion call. using default values can simplify
### your function calls and clarify the ways in which your functions are typically used.
##### example 5 ######
def describe_pet(pet_name, animal_type ='dog'):
    """"Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My{animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# Equivalent Fucntion Calls
### Because positional arguements, keyword arguements, and default values can all be used 
### together, often youll have several equivalent ways to call a function. 
### definition for desccribe_pet()
### def describe_pet(pet_name, animal_type= 'dog'):

#### example 6 ####
# a dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# a hamster named Harry
describe_pet('harry','hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding Arguement Errors
### unmatched arguements occur when you provide fewer or more arguements than a function
### needs to do its work.
### the error below reports missing two arguements and reports the names of missing 
### arguements. 