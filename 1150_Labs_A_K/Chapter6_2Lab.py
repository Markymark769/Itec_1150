# 2. feedback_collector.py - use all of the mipo_ex program features for this program.
# It collects phrases that will be used in an online learning system, when students get answers right.
# Inputs: ask the user to enter multiple feedback phrases into a single input prompt. Each phrase must end in an
# exclamation point. No capitals required. Validate that the input is not blank, and has at least 1 exclamation point +
# space. Fix common errors, like taking out extra spaces. Return the corrected input string.
# Processing: take in the input string, and send it to a function that splits the phrases into a list, based on the !
# character. Create an empty list, to hold corrected phrases. Use the first list with a loop, to work on each phrase.
# Apply methods like .strip() and .title(), and add back the ! to each phrase. Append each corrected phrase to the
# corrected list & return
# Outputs() – take in the corrected phrase list and use loop printing to display each phrase as shown.

def main():
    try_again = "Y"
    updated_feedback_list = []
    while try_again == "Y" or try_again == "y":
        if len(updated_feedback_list) != 0:
            old_feedback = updated_feedback_list
        else:
            old_feedback = []
        phrases = inputs()
        updated_feedback_list = processing(phrases)

        for feedback in old_feedback:
            updated_feedback_list.append(feedback)
        outputs(updated_feedback_list)
        try_again = input("Enter 'Y' to add more phrases: ")

    print("Thanks, the program is ending.")


def inputs():
    phrases = ""
    valid = False
    print("Welcome to the feedback collector!")
    print("Please enter feedback phrases, each ending in !, on the following line.")

    while not valid:
        while phrases == "":
            phrases = input("Feedback: ")
        if "!" in phrases and " " in phrases:
            valid = True
            phrases.strip() # remove whitespace at beginning and end of string
            return phrases
        else:
            phrases = ""
            print("Please enter a valid phrase, ending in '!'")

def processing(phrases):
    feedback_list = phrases.split("!")
    updated_feedback_list = []
    for phrase in feedback_list:
        phrase.strip()

        updated_phrase_list = phrase.split() # remove excess spaces in the phrase
        updated_phrase = " ".join(updated_phrase_list)
        updated_phrase = updated_phrase + "!"

        updated_phrase = updated_phrase.title()
        if len(updated_phrase) >1:
            updated_feedback_list.append(updated_phrase)

    return updated_feedback_list

def outputs(updated_feedback_list):
    print("Here are your feedback phrases:")
    count = 1
    for phrase in updated_feedback_list:
        print(count, ": ", phrase)
        count = count + 1
    print ("Thanks for adding to the feedback library!")


main()