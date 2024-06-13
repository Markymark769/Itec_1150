# Define variables
state = input('What is the state you want to be a senator in?')
age = int(input('What is your age?'))
us_citizen = input('Are you a citizen of the US for at least 9 years? (yes/no)')
current_state = input('What is the state that you currently live in?')

# Validation (you can add more validation as needed)

# Print statements
if age >= 30:
    print('You meet the requirement of being at least 30 years old.')
else:
    print('You do not meet the requirement of being at least 30 years old.')

if us_citizen.lower() == 'yes':
    print('You meet the requirements of being a US citizen for at least 9 years.')
else:
    print('Ineligible, you are not a US citizen for at least 9 years.')

if current_state == state:
    print('You meet the requirement of living in the state you would like to represent.')
else:
    print('You do not meet the requirement of living in the state you would like to represent.')
