class Inventory:
    
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_id()) is not None:
            raise ValueError("Product ID already exists.")
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()
            print("  Fulfilment:", product.get_fulfilment_info())
        print("------------------------------------------------")

    def get_products(self):
        return tuple(self.__products)
