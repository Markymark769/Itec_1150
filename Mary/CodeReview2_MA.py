# Miguel Azpiroz-Blas

# Prompts user to enter name
customer_name = input("Please enter your name: ")

# Assign prices
sandwich_price = 8
platter_price = 12

# Ask user for order and set price
meal_choice = input("Do you want a sandwich meal or platter meal? (sandwich/platter): ")
if meal_choice.lower() == "sandwich":  #
    meal_price = sandwich_price
elif meal_choice.lower() == "platter":
    meal_price = platter_price
else:
    print("Invalid choice. Defaulting to sandwich meal.")
    meal_choice = "sandwich"
    meal_price = sandwich_price

# Ask user for amount of meals
num_meals = int(input("How many meals do you want? "))

# Determine price
total_cost = meal_price * num_meals

# Ask customer for sauce
extra_sauce = input("Do you want extra sauce? (yes/no): ")
if extra_sauce.lower() == "yes":
    total_cost += 0.50 * num_meals

# Calculate price before sauce
original_total = meal_price * num_meals
sauce_added = extra_sauce.lower() == "yes"

# Display order summary
print("\nOrder Summary")
print("Customer Name: " + customer_name)
print("Meal Type: " + meal_choice + " meal")
print("Number of Meals: " + str(num_meals))
print("Extra Sauce: " + ("Yes" if sauce_added else "No"))
print("Original Total: $" + "{:.2f}".format(original_total))
print("Final Total: $" + "{:.2f}".format(total_cost))
