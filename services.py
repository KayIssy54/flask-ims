import json
import os
import requests

DATA_FILE = "inventory.json"


# Read inventory
def read_inventory():

    if not os.path.exists(DATA_FILE):

        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    with open(DATA_FILE, "r") as f:
        return json.load(f)


# Save inventory
def save_inventory(data):

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# Get all
def get_inventory():

    return read_inventory()


# Get one
def get_item(item_id):

    inventory = read_inventory()

    for item in inventory:

        if item["id"] == item_id:
            return item

    return None


# Add item
def add_item(data):

    inventory = read_inventory()

    if inventory:
        new_id = inventory[-1]["id"] + 1
    else:
        new_id = 1

    new_item = {
        "id": new_id,
        "name": data.get("name"),
        "barcode": data.get("barcode"),
        "price": data.get("price"),
        "stock": data.get("stock")
    }

    inventory.append(new_item)

    save_inventory(inventory)

    return new_item


# Update item
def update_item(item_id, data):

    inventory = read_inventory()

    for item in inventory:

        if item["id"] == item_id:

            item["name"] = data.get("name", item["name"])
            item["barcode"] = data.get("barcode", item["barcode"])
            item["price"] = data.get("price", item["price"])
            item["stock"] = data.get("stock", item["stock"])

            save_inventory(inventory)

            return item

    return None


# Delete item
def delete_item(item_id):

    inventory = read_inventory()

    for item in inventory:

        if item["id"] == item_id:

            inventory.remove(item)

            save_inventory(inventory)

            return True

    return False


# OpenFoodFacts API
def fetch_product_from_api(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    headers = {
        "User-Agent": "InventoryManagementSystem/1.0 (Student Flask Project)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("HTTP Status:", response.status_code)
        print(response.text)
        return None

    data = response.json()

    if data.get("status") == 1:
        product = data["product"]

        return {
            "product_name": product.get("product_name"),
            "brands": product.get("brands"),
            "ingredients": product.get("ingredients_text"),
            "quantity": product.get("quantity"),
            "categories": product.get("categories"),
        }

    return None