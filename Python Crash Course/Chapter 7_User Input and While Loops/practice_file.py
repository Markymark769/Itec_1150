message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")

user_name = 'Mark'
print('Hello {}, it\'s nice to meet you!'.format (user_name)) # Python 3.x
print(f'Hello {user_name}, it\'s nice to meet you!') # Python 3.4+ shortcut

number_of_cds = 45
number_of_lps = 23
number_of_albums = number_of_cds + number_of_lps
print('With', str(number_of_cds), 'CDs and', str(number_of_lps), 'LPs, the number of albums you have is', str(number_of_albums)+ '.')

number_of_cds = int(input('How many CDs do you have? '))
number_of_lps = int(input('How many LPs do you have? '))
number_of_albums = number_of_cds + number_of_lps
print('With', str(number_of_cds), 'CDs and', str(number_of_lps), 'LPs, the number of albums you have is', str(number_of_albums)+ '.')

temp = float(input('Enter the patient\'s temperature: '))
pay = float(input('Enter the employee\'s hourly pay: '))
print('Your temp is', str(temp), 'degrees and your pay is $', str(pay))

cups = int(input('How many cups of coffee sold? '))
price = float(input('Price of coffee? '))
coffee_sales = cups * price
print(f'Total sales = ${coffee_sales:,.2f}')
print(f'Gross sales today, for {cups} cups of coffee: ')
print('{:<20}{:>3}{:>8,.2f}'.format('Price per cup', '$', price))
print('{:<20}{:>3}{:>8,.2f}'.format('Total sales', '$', coffee_sales))

message= input('How many miles did you drive?')
print(message)

message= input('How many gallons of gas did you use?')
print(message)

message= input('How much was your gas per gallon?')
print(message)