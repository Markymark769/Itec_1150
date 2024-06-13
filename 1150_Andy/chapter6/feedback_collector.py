"""
Mark P., 4/19/2023, feedback_collector
This program asks the user to enter multiple phrases in a single prompt.
Each phrase is separated by an " ! ".
Validation will not allow blank prompts, have at least one "!",
and space.
"""

print('Welcome to the feedback generator')


def main():
    phrase = inputs()
    phrase_list, correct_phrase = processing(phrase)
    outputs(phrase_list, correct_phrase)


def inputs():
    print('Please enter multiple feedback phrases, each ending in a \'!\' ')  # asks the user for intput
    #  & advises of separation of the phrase by a " ! "
    phrase = input('Enter as many as you like. you don\'t have to capitalize: \n')
    if '!' not in phrase or ' ' not in phrase:
        phrase = str(input("Invalid input. Please enter at least one phrase ending with an exclamation point: "))
    return phrase  # returns to main

# def wrong_phrase(phrase):
#     while '!' not in phrase or ' ' not in phrase:
#         phrase = str(input("Invalid input. Please enter at least one phrase ending with an exclamation point: "))
#     return phrase


def processing(phrase):
    # Ex. from coffee = coffee.strip():
    phrase = phrase.strip()  # takes phrases and separates it into strips
    phrase_list = phrase.split('!')  # each split is called by a " ! "
    correct_phrase = []  # each phrase is collected in an empty list
    for words in range(len(phrase_list)):
        correct_phrase.append(phrase_list[words].strip())
        # takes the phrases entered and separates them.
    return phrase_list, correct_phrase  # returns to main


def outputs(phrase_list, correct_phrase):
    print('Here are your feedback phrases:')
    for words in range(len(phrase_list)):  # recalls the phrase list entered
        print(correct_phrase[words])  # prints the range in the corrected phrase list
    print('Thanks for helping us build our feedback library.')


main()
