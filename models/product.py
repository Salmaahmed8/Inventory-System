class Product:
    """
    Represents a product in the inventory with attributes: name, price, and quantity.
    """
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        """
        Convert the product object to a dictionary for JSON serialization.
        """
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

    @staticmethod
    def from_dict(data: dict):
        """
        Create a product object from a dictionary.
        """
        return Product(data["name"], data["price"], data["quantity"])
