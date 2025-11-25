import pytest
from functions import *


# 1. TEST add_animal_fun


def test_add_animal_fun_adds_correctly():
    animals = []
    add_animal_fun(animals, "X01", "Test", "Herbivore", "zebra")

    assert len(animals) == 1
    assert animals[0]["code"] == "X01"
    assert animals[0]["name"] == "Test"



# 2. TEST find_index_by_code


def test_find_index_by_code_found():
    animals = get_already_created_animals()
    index = find_index_by_code(animals, "Z01")
    assert index == 0


def test_find_index_by_code_not_found():
    animals = get_already_created_animals()
    index = find_index_by_code(animals, "ZZZ")
    assert index == -1



# 3. TEST change_animal_type_fun


def test_change_animal_type_fun_changes_type():
    animals = get_already_created_animals()
    change_animal_type_fun(animals, "Z01", "Carnivore")

    assert animals[0]["type"] == "Carnivore"



# 4. TEST check_existence_type_fun

def test_check_existence_type_fun_exists():
    animals = get_already_created_animals()
    result = check_existence_type_fun(animals, "Herbivore", "zebra")

    assert result == 1


def test_check_existence_type_fun_not_exists():
    animals = get_already_created_animals()
    result = check_existence_type_fun(animals, "Carnivore", "zebra")

    assert result == -1



# 5. TEST change_type_fun


def test_change_type_fun_all_species():
    animals = get_already_created_animals()

    change_type_fun(animals, "NewType", "zebra")

    # toate zebrele trebuie sa fie NewType
    for a in animals:
        if a["species"] == "zebra":
            assert a["type"] == "NewType"



# 6. TEST Sort_animals


def test_sort_animals_sorts_by_name():
    animals = [
        create_animal_fun("1", "Charlie", "Herbivore", "cow"),
        create_animal_fun("2", "Alice", "Carnivore", "lion"),
        create_animal_fun("3", "Bob", "Herbivore", "penguin"),
    ]

    sorted_animals = Sort_animals(animals)

    names = [a["name"] for a in sorted_animals]

    assert names == ["Alice", "Bob", "Charlie"]