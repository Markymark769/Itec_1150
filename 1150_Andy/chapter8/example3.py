import pyinputplus as pyip

myPassword = pyip.inputPassword('Please enter secret password', mask='@')

print('My secret password is', myPassword)


myTime = pyip.inputTime("Enter a valid time")
print('My Date is:', myTime)
