"""
Mark Porraz
Dr. Lebens
Module 5
"""

import random
# Step 1: create a new list of goldfish
goldfish = ['Bubbles','Finley','Goldie','Splash','Nemo']

#Create a new fish variable and populating it with
print("Welcome to the Goldfish Playdate Planner!")
print("Our goldfish friends are:" + " , " .join(goldfish))

# step2: create a new fish variable and populating input ffrom the user
new_fish = input(" Enter the name of the new Goldfish: ")
goldfish.append(new_fish)

# display the list again
print("Updated goldfish list:"+"," .join(goldfish))

# step 3: remove a goldfish from the list
fish_to_remove = input("Enter the name of the fish you want to remove: ")

# Use an if statement to iterate over the elements in the list and remove
# the goldfish if they are in the list
if fish_to_remove in goldfish:
    goldfish.remove(fish_to_remove)
else:
    print("sorry," + fish_to_remove + "is not in the list.")

# shoe the updated list
print("Current goldfish list" + "," .join(goldfish))

# Output that we are creating pairs for play-dates
print("\nlet's create some play-date pairs")
random.shuffle(goldfish)

# Use a for loop to traverse the elements in the list
for i in range(0,len(goldfish), 2):
    if i + 1 < len(goldfish):
        print(goldfish[i] + "will have a play-date with" + goldfish[i+1])
    else:
        print(goldfish[i]+" will have a solo play-date session")


