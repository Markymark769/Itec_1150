"""
name:
date
professor
assignment

"""


name = input('what is your name')  # this a string, only prints string of letters
age = int(input('how old are:'))  # we have to be specific and tell pycharm we need integers not strings

if name == 'Alice': # if name is set to the vainble alice
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')

# if state is equal to current state, you are eligible

