"""Mark Porraz, 2/19/2023, abcd call stack
homework, chapter 3, Functions
This program describes a function structure
"""

def a():
    print('a() starts')
    b() # no parameters
    d() # no parameters
    print('a() returns')

def b():
    print('b() starts')
    c() # no parameters
    print('b() returns')

def c(): # doesn't call anything
    print('c() starts')
    print('c() returns') # goes back to def b

def d():
    print('d() starts')
    print('d() returns')

a() # when this function is called, it called def b() which calls def c()
    #