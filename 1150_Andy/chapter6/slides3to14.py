"""
Mark Porraz, 4/19/2023,
slide 3to14
"""

## slide 3
# print('This is Alice\'s cat')
# print('\nAlice says, "What\'s her coat type?"')
# print('\nShe\'s called a \t\t tabby cat.')
# print('\nWhat does Alice have? \nA tabby cat!')
# print('\nAlice\'s pet is of the feline\\cat family.')

## slide 4
# print('''
# Dear Alice,
#
# 	Just wanted to say, "Hello" and let you know how it's going with cat sitting. Your cat has been naughty/nice. She caught a mouse!
#
# Happy travels,
# Mo
# ''')

## slide 6
# phone = 'Android'
# print(phone[5])  # prints  the letter i
# print(len(phone))  # prints 7
# for i in 'Android':
# 	print(i.upper(), end = " ") # try w/ and without end = " "

## slide 7
# phone = 'Android'
# length = len(phone)  # returns 7
# last_letter = phone[length]  # causes index error
# print(last_letter)
#
# # shorthand to access the last letter in a string variable
# print(phone[len(phone)-1])

## slide 8
# name = input('Enter a name: ')
# if 'e' in name:
# 	print('This name has the letter e.')
# else:
# 	print('There\'s no letter e in this name.')

## slide 9

# email = input('Enter your email address: ')
# if '.edu' in email:
# 	print('This is a school email.')
## slide 10
    ## example 1
# whisper = 'speak up!'
# shout = whisper.upper() # places things in uppercase
# print(shout)
# print(shout.isupper()) # this is an T/F arguement

    ## example 2
# shout = 'TONE IT DOWN!'
# whisper = shout.lower() # places text in lowercase
# print(whisper)
# print(whisper.islower()) # this is a T/F arguement.

## slide 12
# string1 = 'abcdef'
# string2 = 'abc123'
# string3 = '123456'	  # Strings are NOT numbers unless converted
# string4 = '123.456'  # Even if they look like numbers!
# string5 = '\t   \n'
# string6 = 'Hello World'
# print('Is string1 alpha? ', string1.isalpha())
# print('Is string2 alpha? ', string2.isalpha())
# print('Is string2 alnum? ', string2.isalnum())
# print('Is string1 alnum? ', string1.isalnum())
# print('Is string3 a number? ', string3.isnumeric())
# print('Is string4 a number? ', string4.isnumeric()) # Why not?
# print('Is string4 convertible? ', float(string4))
# print('Is string5 spacey? ', string5.isspace())
# print('Is string6 title? ', string6.istitle())

## slide 13
# spelling_mistakes = 'I am going too school too learn programming.'
# correct = spelling_mistakes.replace('too', 'to')
# print(correct)
# sentence = 'My ca=t pres==ses= the equals= key= when I ty=pe.'
# new_sentence = sentence.replace('=', '')
# print(new_sentence)

## slide 14
# stuff = input('Type in a sentence with 3 spaces at the beginning and at the end')
# print('1 '+stuff+'!')
# print('2 '+stuff.strip()+'!')
# print('3 '+stuff.rstrip()+'!')
# print('4 '+stuff.lstrip()+'!')

