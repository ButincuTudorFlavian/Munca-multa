from t1.zoo import test, functions


def print_menu():
    print("1. Add an animal")
    print("2. Modify type of a specific animal")
    print("3. Modify type for a whole species")
    print("4. Show animals by type (Sorted by Name)")
    print("Exit")

def print_list(animal_list):
    if not animal_list:
        print("No animals found.")
    else:
        print(f"{'CODE':<10} {'NAME':<15} {'TYPE':<15} {'SPECIES':<15}")
        print("-" * 55)
        for a in animal_list:
            print(f"{a['code']:<10} {a['name']:<15} {a['type']:<15} {a['species']:<15}")

def start_app():
    zoo = [
        functions.create_animal("Z01", "Alex", "Carnivore", "Lion"),
        functions.create_animal("Z02", "Marty", "Herbivore", "Zebra"),
        functions.create_animal("Z03", "Gloria", "Herbivore", "Hippo"),
        functions.create_animal("Z04", "Melman", "Herbivore", "Giraffe"),
        functions.create_animal("Z05", "Skipper", "Carnivore", "Penguin")
    ]

    test.run_tests()

    while True:
        print_menu()
        option = input("Choose an option: ")

        if option == '1':
            c = input("Code: ")
            n = input("Name: ")
            t = input("Type: ")
            s = input("Species: ")
            try:
                functions.add_animal(zoo, c, n, t, s)
                print("Animal added successfully.")
            except ValueError as e:
                print(e)

        elif option == '2':
            c = input("Enter Code of animal to modify: ")
            t = input("Enter new Type: ")
            try:
                functions.modify_animal(zoo, c, t)
                print("Update successful.")
            except ValueError as e:
                print(e)

        elif option == '3':
            s = input("Enter Species to re-classify: ")
            t = input("Enter new Type for all of them: ")
            try:
                count = functions.modify_species(zoo, s, t)
                print(f"Updated {count} animals.")
            except ValueError as e:
                print(e)

        elif option == '4':
            t = input("Enter Type to search for: ")
            result = functions.list_animal_ascending_by_type(zoo, t)
            print_list(result)

        elif option == 'Exit':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    start_app()