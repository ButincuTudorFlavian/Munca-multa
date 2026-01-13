#manufactrer, model, price
from function import *

def  print_options():
    print("\n===MENU===")
    print("1. Add a phone")
    print("2. View all phone by manufacturer")
    print("3. Add to price")
    print("4. Add percent to all phones (-50 -> 100)")
    print("5. Display items")
    print("Q. Exit")
def print_list(phone_list):
    for i, a in enumerate(phone_list):
        print(f"Manufacturer: {a['manufacturer']} | Model: {a['model']} | : {a['price']}")

#1
def add_phone_ui(phone_list,manufacturer, model, price):
    add_phone_fun(phone_list, manufacturer, model, price)

#2
def display_phone_manufacturer(phone_list, manufacturer):
    for i, a in enumerate(phone_list):
        if a['manufacturer'] == manufacturer:
            print(f"Manufacturer: {a['manufacturer']} | Model: {a['model']} | : {a['price']}")

#3
def not_exist_manufacturer_ui(phone_list, manufacturer):
    for i, a in enumerate(phone_list):
        if a['manufacturer'] == manufacturer:
            return False
    return True

def not_exist_model_ui(phone_list, model):
    for i, a in enumerate(phone_list):
        if a['model'] == model:
            return False
    return True

def add_price_manufacturer_model_ui(phone_list, manufacturer, model, price):
    add_price_manufacturer_model_fun(phone_list, manufacturer, model, price)

#4

def modify_percent_ui(phone_list, precent):
    modify_percent_fun(phone_list, precent)

def main():
    phone_list=create_5_phone_models()
    while True:
        print_options()
        choice = input("Enter your choice>")
        if choice == "1":
            try:
                manufacturer=input("Enter manufacturer>")
                if manufacturer == "" or len(manufacturer) < 3 :
                    raise ValueError("invalid manufacturer")
                model=input("Enter model>")
                if model == "" or len(model) < 3:
                    raise ValueError("invalid manufacturer")

                price=input("Enter price>")
                if not price.isdigit():
                    raise ValueError("invalid price. Not a number")
                if price == "":
                    raise ValueError("invalid price. Nothing here")

                price=int(price)
                if price<100:
                    raise ValueError("invalid price. To small")

                add_phone_ui(phone_list, manufacturer, model, price)

            except ValueError as message:
                print(f"Invalid input: {message}")

        elif choice == "2":
            try:
                manufacturer=input("Enter manufacturer>")
                if manufacturer == "" or len(manufacturer) < 3:
                    raise ValueError("invalid manufacturer")

                display_phone_manufacturer(phone_list, manufacturer)

            except ValueError as message:
                print(f"Invalid input: {message}")

        elif choice == "3":
            try:
                manufacturer=input("Enter manufacturer>")
                if manufacturer == "" or len(manufacturer) < 3 or not_exist_manufacturer_ui(phone_list, manufacturer):
                    raise ValueError("invalid manufacturer")


                model=input("Enter model>")
                if model == "" or len(model) < 3 or not_exist_model_ui(phone_list, model):
                    raise ValueError("invalid manufacturer")


                price=input("Enter the adding price>")
                if not price.isdigit():
                    raise ValueError("invalid price. Not a number")
                if price == "":
                    raise ValueError("invalid price. Nothing here")

                price=int(price)
                add_price_manufacturer_model_ui(phone_list, manufacturer, model, price)

            except ValueError as message:
                print(f"Invalid input: {message}")

        elif choice == "4":
            try:
                precent = input("Enter the precent>")
                if not precent.isdigit():
                    raise ValueError("invalid precent. Not a number")
                if precent == "":
                    raise ValueError("invalid precent. Nothing here")

                precent = int(precent)
                if not -49<precent<101:
                    raise ValueError("invalid precent. Not between -50 and 100")

                modify_percent_ui(phone_list, precent)

            except ValueError as message:
                print(f"Invalid input: {message}")
        elif choice == "5":
            print_list(phone_list)
        elif choice == "Q":
            break




if __name__ == "__main__":
    main()