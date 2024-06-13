"""

python and email. py - finds phone numbers and email addresses

"""
import re
email = 'abcdef@gmail.com'
phone = '612-777-1234'
both = 'abcdef@gmail.com 612-456-5678'
phone2 = '612-123-1234 612-456-5678'

# patterns
phoneRegex = re.compile('''(
                (\d{3}|\(\d{3}\))? ) # area code
                (\S|-|\.)? # seporator
                (\d{3})  # first 3 digits
                (\s|-|\.) # separator
                (\d{4})  #last 4 digits
                (\s*(ext|x|ext.)\s*(\d{2,5})  # extension
                )''', re.VERBOSE)
# create email
emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+  # username
            @ # @ symbol
            [a-zA-Z0-9.-]+ # domain name
            (\.[a-zA-Z]{2,4}){1,2} # dot-something
            )''', re.VERBOSE)
# find matches in clipboard text
# text = str(pyperclip.paste())
# text = email
# text = phoneA
text = both
# text = phone 2

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses')
# abcdef@gmail.com 612-777-1234



