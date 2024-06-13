#Testing a Fucntion
#### the function get_formatted_name() combines the first and last name with a space in
#### between to complete a full name,  and then capitalizes and returnd the full name.

#### to check that get_formatted_name() works, make a program that uses this function.
#### Another program should be open names.py to have a full first and last name. 
####

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title() 