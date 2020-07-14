animals = ("pig", "bear", "cow", "giraffe", "rhino", "octopus", "jellyfish", "lamb", "goat", "dinosaur")

animals.index("rhino")

missing_animal = "giraffe"

if missing_animal in animals:
    print(f'{missing_animal} was found! :)')
else:
    print(f'{missing_animal} was not found! :(')

(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth) = animals
print(first, second, third, fourth, fifth)
print(sixth, seventh, eighth, ninth, tenth)

animal_list = list(animals)
animal_list.extend(["flounder", "seagull", "anteater"])
print(animal_list)
animals = tuple(animal_list)
print(animals)