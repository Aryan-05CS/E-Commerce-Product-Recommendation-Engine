class Product:

    def __init__(
        self,
        product_id,
        name,
        category,
        rating,
        price
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.rating = rating
        self.price = price

    def __str__(self):
        return (
            f"{self.product_id} | "
            f"{self.name} | "
            f"{self.category} | "
            f"Rating: {self.rating}"
        )


class User:

    def __init__(
        self,
        user_id,
        name,
        purchase_history,
        search_history,
        cart_items,
        ratings
    ):
        self.user_id = user_id
        self.name = name
        self.purchase_history = purchase_history
        self.search_history = search_history
        self.cart_items = cart_items
        self.ratings = ratings