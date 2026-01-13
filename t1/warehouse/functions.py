def create_product(name, quantity, price):
    return {
        "name": name,
        "quantity": int(quantity),
        "price": int(price)
    }

def add_product(warehouse, name, quantity, price):
    try:
        q = int(quantity)
        p = int(price)
    except ValueError:
        raise ValueError("Quantity and price must be integers.")
    if q <= 0 or p <= 0:
        raise ValueError("Quantity and price must be positive integers.")
    for product in warehouse:
        if product["name"] == name:
            product["quantity"] += q
            product["price"] = p
            return

    new_product = create_product(name, q, p)
    warehouse.append(new_product)

def remove_product(warehouse, name):
    """
    Removes a product from the warehouse based on its name.

    Args:
        warehouse (list): The list of current products.
        name (str): The name of the product to remove.

    Raises:
        ValueError: If the product with the given name does not exist.
    """
    for i, product in enumerate(warehouse):
        if product["name"] == name:
            del warehouse[i]
            return
    raise ValueError("Product does not exist.")


def get_all_products_sorted(warehouse):
    return sorted(warehouse, key=lambda x: x["name"], reverse=True)

def calculate_total(warehouse):
    total = 0
    for product in warehouse:
        total += product["price"] * product["quantity"]
    return total