import json
from product import Product
from inventory import Inventory


def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            inventory.add_product(product)

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

    return inventory


def save_inventory(inventory):
    data = []

    for product in inventory.get_products():
        data.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


def display_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    inventory = load_inventory()

    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    while True:
        display_menu()

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            print("Add New Product")

            product_id = input("Product ID: ")
            product_name = input("Product Name: ")

            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))

                if price < 0 or stock < 0:
                    print("Price and stock cannot be negative.")
                    continue

            except ValueError:
                print("Invalid price or stock quantity.")
                continue

            product = Product(
                product_id,
                product_name,
                price,
                stock
            )

            inventory.add_product(product)

        elif option == "3":
            print("Update Stock")

            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                print("Product Found:")
                print("Name:", product.get_name())
                print("Current Stock:", product.get_stock())

                try:
                    quantity = int(input("New Stock Quantity: "))
                    product.update_stock(quantity)

                except ValueError:
                    print("Invalid stock quantity.")

        elif option == "4":
            print("Search Product")

            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                print("Product Found")
                print("------------------------------------------------")
                product.display_information()
                print("------------------------------------------------")

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please select 1 to 6.")


if __name__ == "__main__":
    main()