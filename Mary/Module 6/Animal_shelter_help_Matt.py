# shelter = {}


# define a funtion animals to the system
def add_animal(name,species):
    # adds an animal to the shelter
    print("Adding" + name + " to the shelter")


# animal information
add_animal(" Sammy", "Dog")
add_animal(" Rover", "Dog")
add_animal(" Smedly", "Cat")
add_animal(" Smo", "Cat")
add_animal(" Yeller", "Dog")
add_animal(" Goby", "Cat")
add_animal(" Shadow", "Cat")
add_animal(" Rocky", "Cat")
add_animal(" Tank", "Dog")
add_animal(" Monk", "Dog")


def adopt_animal(name):
    if name in shelter:
        del shelter[name]  # Takes the animal's name off of the list
        return name + " has been adopted!"  # celebrating the animals new forever home
    else:
        return name + "Is not in the shelter"  # informs us that the animal is not in the shelter


# def get_animal_count(species, name):
#     if name in species:
#         length_of_name = len(species[name])
#         return length_of_name
#     else:
#         return name
def get_animal_count(species):
    # Return the count of animals of the given species
    if species in shelter:
        return len(shelter[species])  # Number of animals in the species list
    else:
        return 0  # Return 0 if species not found in shelter


# print("Total number of animals in the shelter are:" + str(get_animal_count(len(name)))
# Display total number of animals for a given species
print(f"Total number of animals in the shelter are:" + str(get_animal_count()))

# print(f"Total number of cats in the shelter are: {get_animal_count('Cat')}")
