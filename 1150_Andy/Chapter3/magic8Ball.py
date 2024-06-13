"""Mark Porraz, 2/19/2023, magic 8 ball
homework, chapter 3, Functions
This program describes a function structure
"""

import random # imports a random functon model

def getAnswer(answerNumber): # the get answer funciton is defined
    if answerNumber == 1: #the R parameter is stored in a parameter named getAnswer()
        return 'It is certain'
    elif answerNumber == 2: # depending on the value that is called, it will bring it down to print
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'reply hazy, try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outloook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9) # since it defined not called, it skips here.
# has an arguement from one to nine. # it is then stored in r
fortune = getAnswer(r)
print(fortune) # recieves the return to the random corresponding number