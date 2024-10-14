import random  #
print("Welcome to the Magical number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print("But beware, the number might change its mind!")
secret_number = random.randint(1, 100)
while True:
    number_guess = input('Please guess a number:')
    for guess_count in range(1, 6):  # guesses before the number changes
        if number_guess == secret_number:  # if guess is correct, statement that checks for the correct answer
            print('you have guessed the correct answer')
        else:
            print('you have not guessed the correct answer')

