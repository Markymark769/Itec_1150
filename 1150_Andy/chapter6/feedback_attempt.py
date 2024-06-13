"""
Mark Porraz, 4/19/2023, feedback_collector

"""

print('Welcome to the feedback generator')
def main():
    phrase = inputs()
    phrase_list, correct_phrase = processing(phrase)
    outputs(phrase_list, correct_phrase)


def inputs():
    print('Please enter multiple feedback phrases, each ending in a !\' ')
    phrase = input('Enter as many as you like. you don\'t have to capitalize: \n')
    return phrase


def processing(phrase):
    # example) coffee = coffee.strip():
    #
    phrase = phrase.strip()  # takes phrases and seperates it into strips
    phrase_list = phrase.split('!')  # each split is called by a  " ! "
    correct_phrase = []  # each phrase is collected in an empty list

    for words in range(len(phrase)):
        correct_phrase.append(phrase_list[words].strip())  # appends or adds to the list of phrases
        # takes the phrases entered and seperates them.
        break
    return phrase_list, correct_phrase  # returns the to main


def outputs(phrase_list, correct_phrase):
    print('Here are your feedback phrases:')
    for words in range(len(phrase_list)):
        print(correct_phrase)
    print('Thanks for helping us build our feedback library.')


main()
# output attempt 1
# def outputs(phrase_list, correct_phrase):
#     print('Here are your feedback phrases:')
#     for words in range(len(phrase_list)):
#         print(correct_phrase.append(phrase_list[words]))
#     print('Thanks for helping us build our feedback library.')

#TODO: figure out why only the first sentence prints
#TODO: figure out why sometimes it prints 3 or 4
#TODO: figure out more validation
