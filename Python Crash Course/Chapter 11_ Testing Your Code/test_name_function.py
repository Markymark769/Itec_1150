#Passing a syntax
### The syntax for setting up a text case takes some getting used to, but once you've set up
### the testcase its common sense to add more unit tests for the functions. To writea test case
### for a function import the function you want to test. Then create a class that inherits from
### unitest.TestCase, and write a series of methods to test different aspects of your functions
### behavior.

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '_main_':
    unittest.main()