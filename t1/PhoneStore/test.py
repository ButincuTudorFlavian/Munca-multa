# test.py
import pytest
from function import *


def test_create():
    phone = create("Samsung", "S20", 4000)
    assert phone["manufacturer"] == "Samsung"
    assert phone["model"] == "S20"
    assert phone["price"] == 4000


def test_create_5_phone_models():
    phones = create_5_phone_models()
    assert len(phones) == 5
    # check some entries
    assert phones[0]["manufacturer"] == "Samsung"
    assert phones[0]["model"] == "Note 9"
    assert phones[0]["price"] == 3000


def test_add_phone_fun():
    phones = []
    add_phone_fun(phones, "Nokia", "3310", 200)
    assert len(phones) == 1
    assert phones[0]["manufacturer"] == "Nokia"
    assert phones[0]["model"] == "3310"
    assert phones[0]["price"] == 200


def test_add_price_manufacturer_model_fun():
    phones = create_5_phone_models()

    add_price_manufacturer_model_fun(phones, "Samsung", "Note 9", 500)


    note9 = next(p for p in phones if p["manufacturer"] == "Samsung" and p["model"] == "Note 9")
    assert note9["price"] == 3000 + 500


    iphone_x = next(p for p in phones if p["model"] == "IPhone X")
    assert iphone_x["price"] == 5000


def test_calculate_percent():
    # 10% din 200 = 20
    assert calculate_percent(10, 200) == 20
    # 25% din 1000 = 250
    assert calculate_percent(25, 1000) == 250


def test_modify_percent_fun():
    phones = create_5_phone_models()
    # mărim toate prețurile cu 10%
    modify_percent_fun(phones, 10)

    # 3000 + 10% = 3300
    note9 = next(p for p in phones if p["manufacturer"] == "Samsung" and p["model"] == "Note 9")
    assert note9["price"] == 3300

    # 5000 + 10% = 5500
    iphone_x = next(p for p in phones if p["model"] == "IPhone X")
    assert iphone_x["price"] == 5500