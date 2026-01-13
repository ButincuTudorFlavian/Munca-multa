from t1.functions import *
def test_count_codes():
    assert count_codes(1023, "3041") == 1
    assert count_codes(1023, "1023") == 4
    assert count_codes(1023, "7895") == 0
    assert count_codes(1023, "1024") == 3
    assert count_codes(7965, "7956") == 2

def test_count_runners():
    assert count_runners(1234, "4321") == 4
    assert count_runners(12234, "5678") == 0
    assert count_runners(1234, "7832") == 1


def test_valid_guess():
    assert valid_guess("q") == False
    assert valid_guess("qq") == False
    assert valid_guess("0002") == False
    assert valid_guess("3333") == False
    assert valid_guess("12345") == False
    assert valid_guess("1234") == True


if __name__ == "__main__":
    test_count_codes()
    test_count_runners()
    test_valid_guess()
    print("All tests passed")




