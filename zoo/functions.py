def create_animal(code, name, type1, species):
    return {
        "code": code.strip(),
        "name": name.strip(),
        "type": type1.strip(),
        "species": species.strip()
    }
def add_animal(animal_list, code, name, type1, species):
    """
    Adds a new animal to the collection based on the given attributes.

        animal_list (list): The list of existing animals.
        code (str): The unique identifier for the animal.
        name (str): The name of the animal.
        type1 (str): The type of the animal (e.g., Herbivore).
        species (str): The species of the animal (e.g., Zebra).

    Raises:
        ValueError: If any of the fields are empty or if the code already exists in the list.
    """
    if not code or not name or not type1 or not species:
        raise ValueError("All fields are required")
    for animal in animal_list:
        if animal["code"] == code:
            raise ValueError("Code already exists")
    new_animal = create_animal(code, name, type1, species)
    animal_list.append(new_animal)

def modify_animal(animal_list, code, new_type):
    if not new_type:
        raise ValueError("New type cannot be empty")
    for animal in animal_list:
        if animal["code"] == code:
            animal["type"] = new_type
            return
    raise ValueError(f"Animal with code {code} not found")

def modify_species(animal_list, target_species, new_type):
    if not new_type:
        raise ValueError("New type cannot be empty")
    count = 0
    for animal in animal_list:
        if animal["species"] == target_species:
            animal["type"] = new_type
            count += 1
    if count == 0:
        raise ValueError(f"No animals found with species {target_species}")
    return count

def list_animal_ascending_by_type(animal_list, target_type):
    result_list = []
    for animal in animal_list:
        if animal['type'] == target_type:
            result_list.append(animal)
    def get_sort_key(animal):
        return animal['name']
    result_list.sort(key=get_sort_key)
    return result_list