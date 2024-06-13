# The _init_() method for a child class
#### inheritance - when one class inherits from another, it takes on the attributes that
#### were defined in the parent _init_() method and make them available in the child class. 

#example 1
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
############# new code added below ##################
#### child code is define and super() method added
#### note, the parent class MUST be first
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def _init_(self,make,model,year):
        """Internalize attributes of the parent class."""
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla' , 'model s' , '2019')
print(my_tesla.get_descriptive_name())

# Defining attributes and methods for the Child class
#### you can add new attributes and methods necessary to differentiate the child class 
### from the parent class.

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
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Overriding Methods from the parent class
#### You can overwrite any method in a parent class by defining a method in the
###child class with teh same name as the method you want to override in the parent
###class. Python will disregard the parent class method and only pay attention to 
###the method you define in the child class. for example electric cars do not need
###gas and you may want to override that. 
################### example #################################
#class ElectricCar(Car):
#    """Represent aspects of a car, specific to electric vehicles."""
#    
#    def __init__(self, make, model, year):
#        """
#        Initialize attributes of the parent class.
#        Then initialize attributes specific to an electric car.
#        """
#        super().__init__(make, model, year)
#        self.battery_size = 75

#    def describe_battery(self):
#        """Print a statement describing the battery size."""
#        print(f"This car has a {self.battery_size}-kWh battery.")

#def fill_gas_tank(self):
#    """Electric cars don't have gas tanks."""
#    print("This car doesn't need a gas tank!")
#############################################################

# Inheritance as attributes
#### Real world applications require more detail to a class. The list of attributes, methods,
###and files becoming lengthy. part one can be broken apart on a seperate list. In other words
###it can be broken down into classes that work together.
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

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attirbutes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This can has a {self.battery_size}- kWh battery.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Modeling Real World Objects
####