"""Mark Porraz, 4/2/2023, isPhoneNumber.py"""

def isPhoneNumber(text):
    # the code follows a series of checks, if failed it returns false
    if len(text) != 12:   # checks that the string is exactly 12 characters
        return False # if no the case you will return false
    for i in range(0,3):
        if not text[i].isdecimal():  # checks area code, if the letters are numeric
            return False
    # the rest of the function checks that the string
    if text[3] != '-':  # the number must have the first hyphen after the area code
        return False
    for i in range(4,7): # checking for the second three digit block
        if not text[i].isdecimal():  # checks if three or more characters are numeric
            return False
    if text[7] != '-':  # checks the second hyphen in the phone number
        return False # if that is not the case, it is false
    for i in range(8,12):
        if not text[i].isdecimal():  # has four more numbers
            return False
    return True  # If all the program passes all the checks, returns true.


# if you want to find a number with a larger string.


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):  # finding the range in the length of the message is a valid phone number
    # you have to loop through this message to find a valid number
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
