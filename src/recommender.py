import heapq
from collections import Counter


class RecommendationEngine:

    def __init__(self, products, users):

        self.products = products
        self.users = users

    # ----------------------------------
    # Recommendation Score Calculation
    # ----------------------------------

    def calculate_score(
        self,
        user,
        product
    ):

        score = 0

        category_count = Counter(
            user.search_history
        )

        score += (
            category_count.get(
                product.category,
                0
            ) * 3
        )

        if (
            product.product_id
            in user.cart_items
        ):
            score += 10

        score += product.rating * 2

        purchased_categories = []

        for pid in user.purchase_history:

            if pid in self.products:

                purchased_categories.append(
                    self.products[pid].category
                )

        if (
            product.category
            in purchased_categories
        ):
            score += 5

        return round(score, 2)

    # ----------------------------------
    # Top Recommendations
    # ----------------------------------

    def recommend_products(
        self,
        user_id,
        top_n=5
    ):

        if user_id not in self.users:
            return []

        user = self.users[user_id]

        purchased = set(
            user.purchase_history
        )

        heap = []

        for pid, product in self.products.items():

            if pid in purchased:
                continue

            score = self.calculate_score(
                user,
                product
            )

            heapq.heappush(
                heap,
                (
                    score,
                    product
                )
            )

        return heapq.nlargest(
            top_n,
            heap,
            key=lambda x: x[0]
        )

    # ----------------------------------
    # Similar Products
    # ----------------------------------

    def similar_products(
        self,
        product_id
    ):

        if (
            product_id
            not in self.products
        ):
            return None

        target = self.products[
            product_id
        ]

        result = []

        for pid, product in self.products.items():

            if (
                pid != product_id
                and product.category
                == target.category
            ):

                result.append(
                    product
                )

        return result

    # ----------------------------------
    # Category Recommendations
    # ----------------------------------

    def category_recommendations(
        self,
        category
    ):

        result = []

        for product in self.products.values():

            if (
                product.category.lower()
                ==
                category.lower()
            ):

                result.append(
                    product
                )

        result.sort(
            key=lambda x: x.rating,
            reverse=True
        )

        return result

    # ----------------------------------
    # Product Search
    # ----------------------------------

    def search_product(
        self,
        keyword
    ):

        keyword = keyword.lower()

        results = []

        for product in self.products.values():

            if (
                keyword
                in product.name.lower()
            ):

                results.append(
                    product
                )

        return results

    # ----------------------------------
    # Add Product
    # ----------------------------------

    def add_product(
        self,
        product
    ):

        self.products[
            product.product_id
        ] = product

    # ----------------------------------
    # Delete Product
    # ----------------------------------

    def delete_product(
        self,
        product_id
    ):

        if (
            product_id
            in self.products
        ):

            del self.products[
                product_id
            ]

            return True

        return False

    # ----------------------------------
    # View Users
    # ----------------------------------

    def view_users(self):

        return (
            self.users.values()
        )

    # ----------------------------------
    # Add User
    # ----------------------------------

    def add_user(
        self,
        user
    ):

        self.users[
            user.user_id
        ] = user

    # ----------------------------------
    # Analytics Dashboard
    # ----------------------------------

    def analytics_dashboard(self):

        total_products = len(
            self.products
        )

        total_users = len(
            self.users
        )

        highest_rated = max(
            self.products.values(),
            key=lambda product:
            product.rating
        )

        average_rating = round(
            sum(
                product.rating
                for product
                in self.products.values()
            ) / total_products,
            2
        )

        category_count = {}

        for product in self.products.values():

            category = product.category

            category_count[
                category
            ] = (
                category_count.get(
                    category,
                    0
                ) + 1
            )

        return {

            "total_products":
            total_products,

            "total_users":
            total_users,

            "highest_rated":
            highest_rated,

            "avg_rating":
            average_rating,

            "category_count":
            category_count
        }