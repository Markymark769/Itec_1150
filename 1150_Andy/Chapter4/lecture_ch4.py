"""
lists
"""

# element:         0       1            2           3           4
grocery_list = ["milk", "eggs", "peanut butter", "mayo", "tater tots"]
#

# print one entry
print(grocery_list[0])
print(grocery_list[3])
# slices
# first two enteries
print(grocery_list[0:2])
print(grocery_list[1:4])
print(grocery_list[1:5])
print(grocery_list[1:6])  # you can go anywhere past; it will go to the highest one listed

# Third entry to the end
print(len(grocery_list))  # this lists the whole list established by the grocery list


print(grocery_list[2:len(grocery_list)])  # you can get element 2 from the end # I want 2-5
# this gets you peanut butter through tater tots
# make python figure out the end value not you
# another clean way ... the cleanest way
print(grocery_list[2:])

# Everything
print(grocery_list)
print(grocery_list[:])
print(grocery_list[0:len(grocery_list)])


# element
grocery_list = ["milk", "eggs", "peanut butter", "mayo", "tater tots"]

# back up two from the eend
print(grocery_list[-2])  # you back up two to mayo
print(grocery_list[-4])  # to get eggs
print(grocery_list[-1])  # tater tots
print(grocery_list[3 - 1]) # starts from mayo then goes to peanut butter
print(grocery_list[5-1])

# adding or appending to a list
print(grocery_list)
grocery_list.append("ice cream")
print(grocery_list)

grocery_list += ["potatoes"]  # this is called extend
print(grocery_list)

grocery_list.insert(1,"pickles")  # this means that I want to put pickles in position 1
print(grocery_list)

# Print all enteries:
for i in range(len(grocery_list)):  # whatever the legth of the grocery list is make another list that same length
    print(f"At grocery_list position {i} is {grocery_list}")

for i in range(len(grocery_list)): # note we usually use an index + 1 because it would start you at 0
    print(f"At grocery_list position {i} is {grocery_list[i]}")

# another trick: print has a "sep" parameter, that helps you use a seperator
# between things you print:
print("a", "b","c", sep=",")  # this means that it is a seperator
print("a", "b","c" )


print(grocery_list, sep= ",")

# a splat operator, it is called splatting = *
# put individual operators to print
print(*grocery_list, sep=", ")
print(["x" , "y", "z"], sep= ", ")
print(*["x" , "y", "z"], sep= ", ")

# some functions expect a list to operate on:
# This does not work to add up a bunch of numbers
# sum(1,2,3) # This does not work to add up a bunch of numbers
# sum([1,2,3])
#
# try:
#     sum(1,2,3)
# except Exception as ex:
#     print(f"Error: {ex}")

# But this does:
nums = [1,2,3]
sum(nums)
