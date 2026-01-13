import functions

def start_app():
    warehouse = []

    while True:
        command_line = input(">>> ")
        parts = command_line.split()

        if not parts:
            continue

        command = parts[0]

        if command == "add":
            if len(parts) != 4:
                print("Error: Invalid number of arguments. Usage: add <name> <quantity> <price>")
            else:
                try:
                    functions.add_product(warehouse, parts[1], parts[2], parts[3])
                    print("Product added.")
                except ValueError as e:
                    print(f"Error: {e}")

        elif command == "remove":
            if len(parts) != 2:
                print("Error: Invalid number of arguments. Usage: remove <name>")
            else:
                try:
                    functions.remove_product(warehouse, parts[1])
                    print("Product removed.")
                except ValueError as e:
                    print(f"Error: {e}")

        elif command == "list":
            if len(parts) < 2:
                print("Error: Invalid command. Use 'list all' or 'list total'")
            elif parts[1] == "all":
                sorted_list = functions.get_all_products_sorted(warehouse)
                for p in sorted_list:
                    print(f"{p['name']} (Qty: {p['quantity']}, Price: {p['price']})")
            elif parts[1] == "total":
                total_value = functions.calculate_total(warehouse)
                print(f"Total value: {total_value}")
            else:
                print("Error: Invalid list command.")

        elif command == "exit":
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    start_app()