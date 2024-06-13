# Importing a single
#### in creating a module called car creates and issue due to a file already named car.
#### therfore, the issue can be resolved by storing the car class in a moduleand 
#### replacing the file we were previously usuing. 


"""A class that can be used to represent a car."""
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


# Storing Multiple Classes in a Module
# Importing Multiple Classes from a Module
# Importing an entire module
# Impoting all classes from a module
# Importing a Module into a Module
# Using Aliases
# Finding Your Own Workflow
