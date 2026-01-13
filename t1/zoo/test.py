from t1.zoo import functions


def run_tests():
    test_list = []
    try:
        functions.add_animal(test_list, "Z01", "Alex", "Carnivore", "Lion")
        assert len(test_list) == 1
        assert test_list[0]['name'] == "Alex"
    except Exception as e:
        print(f"Test 1 Failed: {e}")

    try:
        functions.add_animal(test_list, "Z01", "Marty", "Herbivore", "Zebra")
        print("Test 2 Failed")
    except ValueError as e:
        assert "exists" in str(e)

    try:
        functions.add_animal(test_list, "Z02", "", "Herbivore", "Zebra")
        print("Test 3 Failed")
    except ValueError as e:
        assert "required" in str(e)

    print("All tests passed.\n")