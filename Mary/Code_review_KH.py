# BarbQue Assignment
# Kieran Hanson
# Last Updated 9/12

# Start with the customer name input
customer_name = input("Please enter your name:")
# Time to add the meal prices
sandwich_price = 8
platter_price = 12
# Time to ask for a meal choice and let them know the price
meal_choice = input("Do you want a sandwich meal or platter meal? (sandwich/platter): ")
# Add the if/elif/else statements
if meal_choice.lower() == "sandwich":
    meal_price = sandwich_price
elif meal_choice.lower() == "platter":
    meal_price = platter_price
else:
    print("Invalid choice. Defaulting to sandwich meal.")
    meal_choice = "sandwich"
    meal_price = sandwich_price

# I did not have lines 19 and 20 indented, which caused my code to consistently print out the sandwich meal.
# I was very frustrated because I thought the code was right but when I figured out why, I had no choice but to laugh
# I probably spent around 30 minutes trying to figure out why it was defaulting to sandwich.

#Time to ask for the number of meals the customer wants

num_meals = int(input("How many meals do you want? "))
# Line above converts the input to an integer using the int()
# Calculate the total cost of the meal, we do this by multiplying the meal price by number of meals.
total_cost = meal_price * num_meals
# Ask them if they want to get lost in the sauce
extra_sauce = input("Do you want extra sauce? (yes/no): ")
if extra_sauce.lower() == "yes":
    total_cost += 0.50 * num_meals
# It costs to get lost in the sauce (.50 cents)
original_total = meal_price * num_meals
sauce_added = extra_sauce.lower() == "yes"
# The lower lines will print out everything the user submitted into the prompts.
print("\nOrder Summary:")
print("Customer Name:" + customer_name)
print("Meal Type:" + meal_choice + " meal")
print("Number of Meals:" + str(num_meals))
print("Extra Sauce:" + ("Yes" if sauce_added else "No"))
print("Original Total: $" + "{:.2f}".format(original_total))
print("Final Total: $" + "{:.2f}".format(total_cost))

# I am very excited to continue this coding journey. Thank you!!

