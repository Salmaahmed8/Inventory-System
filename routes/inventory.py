from flask import Blueprint, request, jsonify
from models.product import Product
from services.inventory import InventoryService

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/", methods=["GET"])
def get_products():
    """
    Fetch all products in the inventory.
    """
    products = InventoryService.get_all_products()
    return jsonify([product.to_dict() for product in products]), 200

@inventory_bp.route("/", methods=["POST"])
def add_product():
    """
    Add a new product to the inventory.
    """
    data = request.get_json()
    product = Product.from_dict(data)
    InventoryService.add_product(product)
    return jsonify({"message": "Product added successfully"}), 201

@inventory_bp.route("/<name>", methods=["PUT"])
def update_product(name):
    """
    Update a product in the inventory.
    """
    data = request.get_json()
    InventoryService.update_product(name, data["price"], data["quantity"])
    return jsonify({"message": "Product updated successfully"}), 200

@inventory_bp.route("/<name>", methods=["DELETE"])
def delete_product(name):
    """
    Delete a product from the inventory.
    """
    InventoryService.delete_product(name)
    return jsonify({"message": "Product deleted successfully"}), 200
