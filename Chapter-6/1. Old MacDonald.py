def verse(animal, animal_noise):
    return ('''
    Old MacDonald had a farm, Ee-igh, Eeigh, Oh!
    And on that farm he had a {0}, Ee-igh, Eeigh, Oh!
    With a {1}, {1} here and a {1}, {1} there.
    Here a {1}, there a {1}, everywhere a {1}, {1}.
    Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!'''.format(animal, animal_noise))
def oldMacDonald():
    animals = (input('Enter 5 animals name and their noise, everything separated by comma:\n')).split(',')
    for i in range(0, len(animals), 2):
        animal = animals[i]
        noise = animals[i+1]
        print(verse(animal, noise))
oldMacDonald()
