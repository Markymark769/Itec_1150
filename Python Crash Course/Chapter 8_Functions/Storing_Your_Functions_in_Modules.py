# Storing Your Functions in Modules
### one advantage of functions is the way they seperate blocks from code from your
### main program. An import statement tells python to that module into your main program
### file.
### storing your functions in a seperate file allows you to hide the details of your programs
### code and focus on it's higher level of logic.

# Importing an Entire Module
### A Module is a file ending in .py that containsthe code you want to imprt into your program.
### making a module containing the function make_pizza().
                            ###### example 1######
                            # pizza.py + making_pizzaz.py

#### I f you use this kind of import statement to import an entire model named module_name.py, each
#### function in the module is available through the following syntax.
                            #### module_name.function_name()

# Importing Specific Functions
### you can also import a specific function
                            ### from module_name import function_name
### you can seperate rating each function's name with a comma:
                            ### from module_name import function_0, function_1, function_2
### The making_pizzas.py example would look like this if we want to import just the function
### we are going to use.
                            ### from pizza import make_pizza 
                            ### make_pizza(16, 'pepperoni')
                            ### make_pizza(12,'mushrooms','green peppers','extra cheese')
### because we've explicitly imported the function make_pizza() in the import statement, we
### can call it by name when we use the function. 

# Using as to Give a Function an Alias
### Consider giving an alias for the name of a function for many reasons: too long, file 
### might already exist, and etc.
### examples) make_pizza() for mp()
                            ##### example 2 ##### 
# from pizza import make_pizza as mp
#
#mp(16,'pepperoni')
#mp(12,'mushrooms','green peppers','extra cheese')

# Using as to Give a Module an Alias
### import pizza as p 
###
### p.make_pizza(16, 'pepperoni')
### p.make_pizza(12, 'mushrooms','green peppers','extra cheese')

# Importing All Funcitons in a Module
### from pizza import*
### make_pizza(16, 'pepperoni')
### make_pizza(12, 'mushrooms','green peppers','extra cheese')
### The askrisk in the import statement tells python to copy every function from
### the module pizza into this program file. you can call each function without
### using the dot notation.
### best use for this is when working with larger modules