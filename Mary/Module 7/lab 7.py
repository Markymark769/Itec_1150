"""
Module 7
MArys Class
Mark Porraz
"""

# step 1
food_stands = {
    "Pronto Pups": "Corn dogs",
    "Big Fat Bacon": "Bacon on a Stick "}


# Printing the food stands
print("Food stands at the fair: ")
for stand, food in food_stands.items():
    print(stand + ":" + food)

# Adding a food item
food_stands["FResh French Fries"] = "Fries"

# Removing a food stand
del food_stands["Big Fat Bacon"]

# Display the dictionary
print("\nAfter adding Fries stand, updating Pronto Pups a ")
print(food_stands)

# Step 2: Now lets use tuples
attractions = [
    ("Giant Slide", "East of the Grandstand"),
    ("Skyride", "Near Dan Patch Avenue")
]

# Prining Attracctions
print("Fair Attractions: ")
for attraction in attractions:
    print(attraction[0] + "is located" + attraction[1])

# Adding a New attraction
new_attraction = ("Haunted House", "Near the Midway")
attractions.append(new_attraction)

# Step 3: Finally, lets use sets for unique fair activites
print("\nAfter adding an attraction: ")
for attraction in attractions:
    print(attraction[0] + "is located" + attraction[1])

# Trying to add a duplicate activity

# Removing an activity

# Optional Challange
# Lets create a daily planner using all three
