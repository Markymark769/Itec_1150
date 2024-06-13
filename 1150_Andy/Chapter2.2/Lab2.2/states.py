print('Quiz program!')
# number of loops
question = input(str('What is the capital of Wisconsin?'))

total = 0
attempts = 1
while attempts < 3:  # true or false
    attempts = attempts + 1
    if question == 'Madison' or question == 'madison':
       print(f'Correct. You got the answer in {total} attempt(s).')

    else:
        print('Sorry that is not right. Please try again.')
        question = input(str('What is the capital of Wisconsin?'))
        # if question != 'madison' or question != 'Madison':
        #  print('Sorry that is not right. Please try again.')
        # question = input(str('What is the capital of Wisconsin?')
        # for i in range(question, answer, attempts=3):
        #     total = total + i  # adds the range of numbers listed
        #     print(i)
if attempts <= 3:
    print("sorry you ran out of tries")
