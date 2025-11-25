#animal["code":Z01 , "name":Alex, "type":herbivore, "species":zebra]


def create_animal_fun(code, name, type, species) :
    """
    Creates an animal object represented as a dictionary.
    """
    return{
        'code': code,
        'name': name,
        'type': type,
        'species': species
    }
def get_already_created_animals():
    """
    Returns the initial hard-coded list of animals
    """
    return[
        create_animal_fun("Z01", "Alex", "Herbivore", "zebra"),
        create_animal_fun("Z02", "Ion", "Herbivore", "elephant"),
        create_animal_fun("Z03", "Andrei", "Carnivore", "wolf"),
        create_animal_fun("Z04", "Maria", "Herbivore", "cow"),
        create_animal_fun("Z05", "Bob", "Carnivore", "lion")
    ]
#1

def add_animal_fun(animals, code, name, type, species):

    animals.append(create_animal_fun(code, name, type, species))

#2
def find_index_by_code(animals, code):

    for i, a in enumerate(animals):
        if a['code'] == code:
            return i
    return -1



def change_animal_type_fun(animals, code, type):

    i=find_index_by_code(animals, code)
    animals[i]['type'] = type
    return animals

#3
def check_existence_type_fun(animals, type, species):
    for i, a in enumerate(animals):
        if a['type'] == type and a['species'] == species:
            return 1
    return -1

def check_type_fun(animals, type, index):
    if animals[index]['type'] == type:
        return 1
    return -1

def change_type_fun(animals, type, species):
    for i, a in enumerate(animals):
        if a['species'] == species:
            a['type'] = type
    return animals

#4

def Sort_animals(animals):
    animall=animals.copy()
    animall.sort(key=lambda a: a['name'], reverse=False)
    return animall