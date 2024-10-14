# Module 4 Lab
# Student name: ____IRA TOLES____________________
# Instructor name: Dr. Mary Lebens
# Step 2: Setting up our spaceship


# import random

fuel = 100
planets_visited = 0
alien_encounters = 0

# this isnt working side_quests = 1
# i tried adding something under line 10 and its not working


print('Welcome aboard the Python Explorer!')
print('Intial fuel: ')
print(fuel)
print('Mission: Visit 5 planets and meet 3 friendly aliens.')

# Step 3: Using a while loop for space travel

while fuel > 0 and planets_visited < 5:
    print("\nCurent fuel: ")
    print(fuel)
    print("Planets_visited: ")
    print(planets_visited)

    fuel -= 20
    planets_visited += 1


    print("Visiting planet ")
    print(planets_visited)

print("\nMission status:")
if planets_visited == 5:
    print("Success! You've visited all 5 planets. ")

else:
    print("Mission failed. You did not visit all of the planets before running out of fuel. ")

# Step 4: Using a for loop to meet aliens


friendly_aliens = ['Zorg', 'Blip', 'Glorp', 'Xena', 'Qwark']
planets_names = ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Endor', 'Hoth', 'dathomir']

print('\nTime to meet some aliens! ')
for alien in friendly_aliens:
    if alien_encounters >= 3:
        break

    print("You've met " + alien + "!")
    alien_encounters += 1

print()

print("\nYou've encountered ")
print(alien_encounters)
print("friendly aliens.")

# You met 3 friends

























