class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_id()) is not None:
            print("Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully!")

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product

        return None

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")

        if len(self.__products) == 0:
            print("Inventory is empty.")

        for product in self.__products:
            product.display_information()

        print("------------------------------------------------")

    def get_products(self):
        return self.__products


from product import Product

inventory = Inventory()

inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
inventory.add_product(Product("P002", "Mouse", 25.50, 40))

inventory.display_all()