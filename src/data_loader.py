import json

from src.models import Product
from src.models import User


# ----------------------------
# Load Products
# ----------------------------

def load_products():

    with open(
        "data/products.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    products = {}

    for item in data:

        products[item["id"]] = Product(
            item["id"],
            item["name"],
            item["category"],
            item["rating"],
            item["price"]
        )

    return products


# ----------------------------
# Load Users
# ----------------------------

def load_users():

    with open(
        "data/users.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    users = {}

    for item in data:

        users[item["id"]] = User(
            item["id"],
            item["name"],
            item["purchase_history"],
            item["search_history"],
            item["cart_items"],
            item["ratings"]
        )

    return users


# ----------------------------
# Save Products
# ----------------------------

def save_products(products):

    data = []

    for product in products.values():

        data.append(
            {
                "id": product.product_id,
                "name": product.name,
                "category": product.category,
                "rating": product.rating,
                "price": product.price
            }
        )

    with open(
        "data/products.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


# ----------------------------
# Save Users
# ----------------------------

def save_users(users):

    data = []

    for user in users.values():

        data.append(
            {
                "id": user.user_id,
                "name": user.name,
                "purchase_history": user.purchase_history,
                "search_history": user.search_history,
                "cart_items": user.cart_items,
                "ratings": user.ratings
            }
        )

    with open(
        "data/users.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )