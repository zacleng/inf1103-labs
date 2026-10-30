from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
   

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f"  Type: Physical | Weight: {self.__weight:g} kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        # Example lab rule: S$3 base fee + S$2 per kilogram.
        return round(3.00 + 2.00 * self.__weight, 2)

    def to_dict(self):
        data = super().to_dict()
        data.update({"type": "physical", "weight": self.__weight})
        return data
