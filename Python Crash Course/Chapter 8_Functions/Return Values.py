#Return Values
### return values - a function does not always have to display its output directly. Instead, it can
### process some data and then retuen a value or a set of values.
### return values allow you to move much of your program's grunt work into functions, which can simplify
### the body of your program.
# Returning a Simple Value
###### Example 1 ######
def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name}{last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# Making an Arguement Optional
### it makes sense to make an arguement optional so that people using the function can shoose to provide
### information only if they want to. you can use the default values to make an arguement optional.
###### Example 2 ######
def get_formatted_name(first_name, middle_name ,last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('johnny' , 'lee' , 'hooker')
print(musician)

# Returning a Dictionary
###### Example 3 ######
def build_person(first_name, last_name):
    """"Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

###### Example 4 ######
def build_person(first_name, last_name, age=None):
    """"Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Using a Function with a While Loop
### using the get_formatted_name() function with a while loop to greet users
### more formally.
###### Example 5 ######
#def get_formatted_name(first_name, last_name):
#    """Return a full name, neatly formatted."""
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()

# this is an infinite loop!
###### Example 6 ######
#while True:
    #print("\nPlease tell me your name:")
    #f_name = input("First name: ")
    #l_name = input("Last name: ")

    #formatted_name = get_formatted_name(f_name, l_name)
    #print(f"\nHello, {formatted_name}!")

####### Example 7 #######
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
