import requests

BASE_URL = "http://127.0.0.1:5000"


def menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. View All Inventory")
    print("2. View Single Item")
    print("3. Add Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Find Product from OpenFoodFacts")
    print("7. Exit")


def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        items = response.json()

        if not items:
            print("Inventory is empty.")
            return

        for item in items:
            print(item)
    else:
        print("Error retrieving inventory")


def view_single_item():
    item_id = input("Enter Item ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        print(response.json())
    else:
        print("Item not found")


def add_item():
    name = input("Product Name: ")
    barcode = input("Barcode: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    data = {
        "name": name,
        "barcode": barcode,
        "price": price,
        "stock": stock
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=data
    )

    if response.status_code == 201:
        print("Item added successfully")
        print(response.json())
    else:
        print("Failed to add item")


def update_item():
    item_id = input("Enter Item ID: ")

    print("Leave blank if no change")

    name = input("New Name: ")
    barcode = input("New Barcode: ")
    price = input("New Price: ")
    stock = input("New Stock: ")

    data = {}

    if name:
        data["name"] = name

    if barcode:
        data["barcode"] = barcode

    if price:
        data["price"] = float(price)

    if stock:
        data["stock"] = int(stock)

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    if response.status_code == 200:
        print("Item updated successfully")
        print(response.json())
    else:
        print("Item not found")


def delete_item():
    item_id = input("Enter Item ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    if response.status_code == 200:
        print("Item deleted successfully")
    else:
        print("Item not found")


def find_product():
    barcode = input("Enter Product Barcode: ")

    response = requests.get(f"{BASE_URL}/product/{barcode}")

    if response.status_code != 200:
        print("Product not found")
        return

    product = response.json()

    print("\n--- Product Details ---")
    print(f"Name: {product.get('product_name')}")
    print(f"Brand: {product.get('brands')}")
    print(f"Ingredients: {product.get('ingredients')}")
    print(f"Quantity: {product.get('quantity')}")
    print(f"Categories: {product.get('categories')}")

    choice = input("\nAdd this product to inventory? (Y/N): ").lower()

    if choice == "y":

        try:
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))
        except ValueError:
            print("Invalid price or stock.")
            return

        data = {
            "name": product.get("product_name"),
            "barcode": barcode,
            "price": price,
            "stock": stock
        }

        save_response = requests.post(
            f"{BASE_URL}/inventory",
            json=data
        )

        if save_response.status_code == 201:
            print("\nProduct successfully added to inventory!")
        else:
            print("\nFailed to add product.")

    else:
        print("Product not saved.")
   


def main():

    while True:

        menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_single_item()

        elif choice == "3":
            add_item()

        elif choice == "4":
            update_item()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            find_product()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()