#### You can use classes to represent many real world situations. once you write a class,
#### youll spend most of your time working with instances created from that class.

#### first modify the attributes of an instance directly or write methods that update 
#### attributes in specific ways.

# The Car Class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to define a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4' , 2019)
print(my_new_car.get_descriptive_name())   

# Setting a DEfault VAlue for an Attribute
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to define a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4' , 2019)
print(my_new_car.get_descriptive_name()) 
my_new_car.read_odometer()  

# Modifying attribute Values
### You can change an attribute's value in three ways: you can change the value 
### directly through the instance, set the value through a method, or increment the value.
### (add a certain amount to it) through a method.

# Modifying Attribute Values
### The easiest way to modify the value of an attribute is to access the attribute
### directly thorugh an instance, set the value through a method, or incement the value.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to define a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """set the odometer reading to the given value."""
        self.odometer_reading = milage

my_new_car = Car('audi', 'a4' , 2019)
print(my_new_car.get_descriptive_name()) 

my_new_car.update_odometer(23)
my_new_car.read_odometer()  

# Incrementing an attribute's value through a method

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to define a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """set the odometer reading to the given value."""
        self.odometer_reading = milage
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru' , 'outback' , 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()