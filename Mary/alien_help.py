# Module 4 Lab
# Student name:Mark
# Instructor name: Dr. Mary Lebens

# import random library
import random  # This references an external library of code to make my code work. To call this code we would use
# random.(whatever i need done).

# create variable
fuel = 100
planets_visited = 0
alien_encounters = 0

# Welcome the user
print("Welcome aboard the Python Explorer!")
print("Initial fuel: ")
print(fuel)
print("Mission: Visit 5 planets and meet 3 friendly aliens.")

while fuel > 0 and planets_visited < 5:
    print("\nCurrent fuel: ")
    print(fuel)
    print("Planets visited: ")
    print(planets_visited)

    fuel -= 20
    planets_visited += 1

    print("Visiting planet ")
    print(planets_visited)

print("\nMission status:")
if planets_visited == 5:
    print("Success! You've visited all 5 planets.")
else:
    print("Mission failed. You did not visit all of the planets before running out of fuel.")

friendly_aliens = ["Zorg", "Blip", "Glorp", "Xena", "Qwark"]

print("\nTime to meet some aliens!")

for alien in friendly_aliens:
    if alien_encounters >= 3:
        break

    print("You've met " + alien + "!")
    alien_encounters += 1

print("\nYou've encountered: ")
print(alien_encounters)
print("friendly aliens.")

random.randint()  # here I am using the import for random

# what is the difference between a while loop and a for loop?
# a for loop is used when there is a definite start and an end like a range of numbers
# a while loop while continue on for a certain amount and we may not know when the loop will stop,
# often a while loop ends with a break

