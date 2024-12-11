import json
from models.product import Product

class InventoryService:
    """
    Service for managing inventory operations: add, update, delete, and fetch products.
    """
    DATA_FILE = "data/inventory.json"

    @staticmethod
    def load_inventory():
        """
        Load inventory from the JSON file.
        """
        try:
            with open(InventoryService.DATA_FILE, "r") as file:
                return [Product.from_dict(item) for item in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_inventory(inventory):
        """
        Save the inventory to the JSON file.
        """
        with open(InventoryService.DATA_FILE, "w") as file:
            json.dump([product.to_dict() for product in inventory], file)

    @staticmethod
    def add_product(product: Product):
        """
        Add a product to the inventory.
        """
        inventory = InventoryService.load_inventory()
        inventory.append(product)
        InventoryService.save_inventory(inventory)

    @staticmethod
    def update_product(name: str, price: float, quantity: int):
        """
        Update a product's details in the inventory.
        """
        inventory = InventoryService.load_inventory()
        for product in inventory:
            if product.name == name:
                product.price = price
                product.quantity = quantity
                break
        InventoryService.save_inventory(inventory)

    @staticmethod
    def delete_product(name: str):
        """
        Remove a product from the inventory by its name.
        """
        inventory = InventoryService.load_inventory()
        inventory = [product for product in inventory if product.name != name]
        InventoryService.save_inventory(inventory)

    @staticmethod
    def get_all_products():
        """
        Fetch all products from the inventory.
        """
        return InventoryService.load_inventory()
