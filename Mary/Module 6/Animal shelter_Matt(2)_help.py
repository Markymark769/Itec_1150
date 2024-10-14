shelter = {}
# define a function animals to the system


def add_animal(name,species):  # adds an animal to the shelter
    shelter[name] = species
    print("Adding " + name + " to the shelter")


# animal information
add_animal("Sammy", "Dog")
add_animal("Rover", "Dog")
add_animal("Smedly", "Cat")
add_animal("Smo", "Cat")
add_animal("Yeller", "Dog")
add_animal("Goby", "Cat")
add_animal("Shadow", "Cat")
add_animal("Rocky", "Cat")
add_animal("Tank", "Dog")
add_animal("Monk", "Dog")


def adopt_animal(name):
    if name in shelter:
        del shelter[name]  # Takes the animal's name off of the list
        return name + " has been adopted!"  # celebrating the aniamls new forever home
    else:
        return name + "Is not in the shelter"  # informs us that the animal is not in the shelter


def get_animal_count():

    # gives us the total number of animals in the shelter
    return len(shelter)
    # checks how many animals are in the shelter


print("Total number of animals in shelter: " + str(get_animal_count()))
# display a message that a specific animal was adopted
print("Adopt an animal: " + adopt_animal("Sammy"))
