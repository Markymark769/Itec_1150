
def feedback_collector():  # Define the feedback_collector function
    # Ask the user to enter multiple feedback phrases
    user_input = str(input("Enter multiple feedback phrases, each ending with an exclamation point: "))

    # Validate that the input is not blank and has at least 1 exclamation point + space
    # while len(user_input) == 0 or user_input !=str: #'! ' not in user_input:
    #     user_input = input("Invalid input. Please enter at least one phrase ending with an exclamation point: ")
    while '!' not in user_input or ' ' not in user_input:
        user_input = str(input("Invalid input. Please enter at least one phrase ending with an exclamation point: "))

    # Split the phrases into a list based on the '!' character
    phrases_list = user_input.split('!')

    # Create an empty list to hold corrected phrases
    corrected_list = []

    # Loop through each phrase in the phrases_list
    for phrase in phrases_list:
        # Remove extra spaces using .strip() and capitalize the phrase using .title()
        corrected_phrase = phrase.strip().title()

        # Add back the '!' to each corrected phrase
        corrected_phrase += '!'

        # Append the corrected phrase to the corrected_list
        corrected_list.append(corrected_phrase)

    # Return the corrected input string
    return corrected_list


# Call the feedback_collector function and store the returned list
corrected_phrases = feedback_collector()

# Display each corrected phrase using a loop
for phrase in corrected_phrases:
    print(phrase)
