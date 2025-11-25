from functions import *

#animal["code":Z01 , "name":Alex, "type":herbivore, "species":zebra]
#1
def add_animal_ui(animals, code, name, type, species):
    add_animal_fun(animals, code, name, type, species)

#2
def change_animal_type_ui(animals, code, type):
    change_animal_type_fun(animals, code, type)

#3

def check_existence_type_ui(animals, type, species):
    return check_existence_type_fun(animals, type, species)

def change_type_ui(animals, type, species):
    change_type_fun(animals, type, species)

#4

def print_animals_by_type_sorted_ui(animals, type):
    animals_sorted = Sort_animals(animals)
    for i, a in enumerate(animals_sorted):
        if a['type'] == type:
            print(f"Code: {a['code']}, Name: {a['name']}, Type: {a['type']}, Species: {a['species']}")


def print_meniu():
    print("\n ===ZOO MENIU===")
    print("1. Add a new animal")
    print("2. Change an animal type")
    print("3. Change species type")
    print("4. Print animal by type")
    print("Q. Quit")

def print_animal(animals):
    for i in animals:
        print(f"Code: {i['code']}, Name: {i['name']}, Type: {i['type']}, Species: {i['species']}")

def main():
    animals=get_already_created_animals()
    while True:

        print_animal(animals)
        print_meniu()
        choice=input("\nChoose an option: ")

        if choice=="1":
            try:
                code=input("Enter the code of the animal: ")
                if code == "":
                    raise ValueError  ("not a valid code")

                name=input("Enter the name of the animal: ")
                if name == "":
                    raise ValueError  ("not a valid name")

                type=input("Enter the type of the animal: ")
                if type == "":
                    raise ValueError  ("not a valid type")

                species=input("Enter the species of the animal: ")
                if species == "":
                    raise ValueError  ("not a valid species")

                add_animal_ui(animals, code, name, type, species)
            except ValueError as message:
                print(f"Invalid input: {message}")

        if choice=="2":
            try:
                code=input("Enter the code of the animal: ")
                if code == "":
                    raise ValueError  ("not a valid code")

                if find_index_by_code(animals, code)==-1:
                    raise ValueError ("there is no animal with that code")

                type=input("Enter the new type: ")
                if type == "":
                    raise ValueError  ("not a valid type")

                change_animal_type_ui(animals, code, type)


            except ValueError as message:
                print(f"Invalid input: {message}")

        if choice=="3":
            try:
                species=input("Enter the species of the animal: ")
                if species == "":
                    raise ValueError  ("not a valid species")

                type=input("Enter the new type: ")
                if type == "":
                    raise ValueError ("not a valid type")
                if check_existence_type_ui(animals, type, species) == 1:
                    raise ValueError ("there is no modification")

                change_type_ui(animals, type, species)

            except ValueError as message:
                print(f"Invalid input: {message}")

        if choice=="4":
            try:
                type=input("Enter the type of the animal: ")

                if type == "":
                    raise ValueError ("not a valid type")

                print_animals_by_type_sorted_ui(animals, type)
                print ("\n")

            except ValueError as message:
                print(f"Invalid input: {message}")

        elif choice=="Q":
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()

