# Author: Robert Ashmore
# Date: 09/30/2024

# Importing random module
import random
#
# Setting dad joke variables
jk_one = "What has five toes and isn't your foot?\n My foot!"
jk_two = "What do you call a werewolf with a youtube channel?\n A lycan subscribe!"
jk_three = "What is a necromancer's favorite exercise?\n Dead lifts!"
jk_four = "How do you know if a mummy is sick?\n When he can't stop coffin!"
jk_five = "Why do cows have hooves instead of feet?\n Because they lactose!"
jk_six = " Why don't oysters donate to charity?\n Because they're shellfish!"
jk_seven = "Why are spirits so bad at communicating?\n Because they ghost you!"
jk_eight = "Where does a general keep his armies?\n Up his sleevies!"
jk_nine = "Why is coffee always getting into trouble?\n Because it is not tea!"
jk_ten = "Why don't scientists trust atoms anymore?\n Because they make up everything!"
#
# Setting dad joke list
dad_jokes = [jk_one, jk_two, jk_three, jk_four, jk_five, jk_six, jk_seven, jk_eight, jk_nine, jk_ten]
#
# Greeting user
print("Welcome to the dad joke generator!")
# Displaying to user total amount of dad jokes
quantity_jokes = len(dad_jokes)
print("We have " + (str(quantity_jokes) + " dad jokes in our collection! "))
#
# Informing user dad jokes are being printed
print("Generating dad jokes...\n")
print("Here are some dad jokes for you!\n")
# Printing Dad jokes using a for loop that repeats 4 times
for i in range(4):
    print(random.choice(dad_jokes))
#
# Thanking the user
print("Thank you for using the dad joke generator! Have a great day!")