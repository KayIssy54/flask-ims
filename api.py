from flask import Blueprint, request, jsonify
from services import (
    get_inventory,
    get_item,
    add_item,
    update_item,
    delete_item,
    fetch_product_from_api
)

inventory_bp = Blueprint("inventory", __name__)

# GET all inventory
@inventory_bp.route("/inventory", methods=["GET"])
def inventory():
    return jsonify(get_inventory())


# GET one item
@inventory_bp.route("/inventory/<int:item_id>", methods=["GET"])
def one_item(item_id):
    item = get_item(item_id)

    if item:
        return jsonify(item)

    return jsonify({"error": "Item not found"}), 404


# POST item
@inventory_bp.route("/inventory", methods=["POST"])
def create_item():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing data"}), 400

    item = add_item(data)

    return jsonify(item), 201


# PATCH item
@inventory_bp.route("/inventory/<int:item_id>", methods=["PATCH"])
def patch_item(item_id):

    data = request.get_json()

    updated = update_item(item_id, data)

    if updated:
        return jsonify(updated)

    return jsonify({"error": "Item not found"}), 404


# DELETE item
@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):

    deleted = delete_item(item_id)

    if deleted:
        return jsonify({"message": "Deleted successfully"})

    return jsonify({"error": "Item not found"}), 404


# Fetch from OpenFoodFacts
@inventory_bp.route("/product/<barcode>", methods=["GET"])
def get_product(barcode):

    product = fetch_product_from_api(barcode)

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404




