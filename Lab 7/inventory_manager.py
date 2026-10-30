import json
from pathlib import Path

from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

DATA_FILE = Path(__file__).with_name("inventory.json")


def product_from_dict(item):
    common = (item["id"], item["name"], item["price"], item["stock"])
    product_type = item.get("type", "physical")
    if product_type == "physical":
        # Legacy Lab 6 records did not have a weight; 0 is a migration default.
        return PhysicalProduct(*common, item.get("weight", 0.0))
    if product_type == "digital":
        return DigitalProduct(*common, item["download_size"])
    raise ValueError(f"Unknown product type: {product_type}")


def load_inventory(path=DATA_FILE):
    inventory = Inventory()
    try:
        with open(path, "r", encoding="utf-8") as file:
            records = json.load(file)
        if not isinstance(records, list):
            raise ValueError("Inventory JSON must contain a list.")
        for record in records:
            inventory.add_product(product_from_dict(record))
        print(f"Loaded {len(inventory.get_products())} product(s) from {path}.")
    except FileNotFoundError:
        print("Inventory file not found; starting with an empty inventory.")
    return inventory


def save_inventory(inventory, path=DATA_FILE):
    data = [product.to_dict() for product in inventory.get_products()]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully.")


def read_nonnegative_float(prompt):
    value = float(input(prompt))
    if value < 0:
        raise ValueError("Value cannot be negative.")
    return value


def read_nonnegative_int(prompt):
    raw = input(prompt)
    value = int(raw)
    if value < 0:
        raise ValueError("Value cannot be negative.")
    return value


def add_product_from_input(inventory):
    print("1. Physical product")
    print("2. Digital product")
    kind = input("Choose product type (1/2): ").strip()
    if kind not in ("1", "2"):
        print("Invalid product type.")
        return
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return
    price = read_nonnegative_float("Price: ")
    stock = read_nonnegative_int("Stock Quantity: ")
    if kind == "1":
        weight = read_nonnegative_float("Weight (kg): ")
        product = PhysicalProduct(product_id, name, price, stock, weight)
    else:
        download_size = read_nonnegative_float("Download size (MB): ")
        product = DigitalProduct(product_id, name, price, stock, download_size)
    inventory.add_product(product)
    print("Product added successfully!")


def update_stock_from_input(inventory):
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product:", product.get_name(), "| Current stock:", product.get_stock())
    quantity = read_nonnegative_int("New Stock Quantity: ")
    product.update_stock(quantity)
    print("Stock updated successfully!")


def search_product_from_input(inventory):
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())
    if isinstance(product, PhysicalProduct):
        print(f"Shipping cost: ${product.calculate_shipping_cost():.2f}")


def main():
    try:
        inventory = load_inventory()
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print("Could not load inventory:", exc)
        return
    while True:
        print("\n----------- INVENTORY MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        option = input("Enter option: ").strip()
        try:
            if option == "1":
                inventory.display_all()
            elif option == "2":
                add_product_from_input(inventory)
            elif option == "3":
                update_stock_from_input(inventory)
            elif option == "4":
                search_product_from_input(inventory)
            elif option == "5":
                save_inventory(inventory)
            elif option == "6":
                save_inventory(inventory)
                print("Program terminated.")
                break
            else:
                print("Invalid option. Please choose 1 to 6.")
        except (ValueError, TypeError) as exc:
            print("Invalid input:", exc)
        except OSError as exc:
            print("File error:", exc)


if __name__ == "__main__":
    main()
