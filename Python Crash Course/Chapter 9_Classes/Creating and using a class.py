# Classes
#### object oriented programming is one of the most effective approaches to writing software.
####Classes- represents real world things and situations, and objects are created based on classes.
#### when you write a class youdefine the general behavior that a whole category of objects can have.
#### making an object from a class is called instantiation, and you work with instances of a class.

#### knowing the logic behind classes will train you to think logically so you can write programs
#### that effectively address almost any problem you encounter.


# Creating and using a class

# Creating the Dog class
### created from the dog class will sore a name and an age, and we'll give each dog the ability
### to sit() and roll_over():

class Dog:
    """A simple attempt to model aa dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Stimulate a dog sitting in reponse to a command."""
        print(f"{self.name} is not sitting")

    def roll_over(self):
        """Stimulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# The _init_() method - a function that's part of a class is a method.
#### everything learned about functions also applies to methods.
#### the _init_() method runs automatically whenever we create a new instance based
#### on the dog class.

#### We define the _init_() method to have three parameters: self, name, and age. 
# ## The self parameter is required in the method definition, and it must come first before
#### the other parameters. It must be included in the definition because when Python calls 
#### this method later, the method call will automatically pass the self arguement. 


#### The line self.name = name takes the value associated with the parameter name and assigns it
#### to the variable name, which is then attatched to the instance being created. The same process
#### happens with self.age = age.
#### Variables that are accessible through instances like this are called attributes.
#### for noe sit() and roll_over() do not do much, but in a game this could code for the dog rolling
#### over and sitting down.

# Making an instance from a Class
#### thinnk of a class as a set of instructions fro how to make an instance.
class Dog:
    """A simple attempt to model aa dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Stimulate a dog sitting in reponse to a command."""
        print(f"{self.name} is not sitting")

    def roll_over(self):
        """Stimulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Accessing Attributes
#### To access the attributes of an instance, you use dot notations

# Calling methods
#### after we create an instance from the class Dog, we can use dot notation to call any method define
#### in Dog. Let's make our dog sit and roll over:
class Dog:
    """A simple attempt to model aa dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Stimulate a dog sitting in reponse to a command."""
        print(f"{self.name} is not sitting")

    def roll_over(self):
        """Stimulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

#### When attributes and methods have been given appropreatly descriptive names like name, age, sit(), and 
#### roll_over(), we can easily infer what a block of code, even once we've never seen before, is 
#### supposed to do.

# creating Multiple Instances
#### You can create as amny instances from a class you need. Let's create a 2nd dog to your_dog:
class Dog:
    """A simple attempt to model aa dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Stimulate a dog sitting in reponse to a command."""
        print(f"{self.name} is not sitting")

    def roll_over(self):
        """Stimulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lacy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
your_dog.sit()