from src.data_loader import (
    load_products,
    load_users,
    save_products,
    save_users
)

from src.recommender import RecommendationEngine

from src.report_generator import generate_report

from src.csv_export import export_recommendations

from src.models import Product, User


products = load_products()
users = load_users()

engine = RecommendationEngine(
    products,
    users
)

USER_ID = 101


while True:

    print("\n")
    print("=" * 50)
    print("E-COMMERCE RECOMMENDATION ENGINE")
    print("=" * 50)

    print("1. View Products")
    print("2. Top Recommendations")
    print("3. Similar Products")
    print("4. Category Recommendations")
    print("5. Generate Report")
    print("6. Search Product")
    print("7. Add Product")
    print("8. Delete Product")
    print("9. View Users")
    print("10. Add User")
    print("11. Export CSV")
    print("12. Analytics Dashboard")
    print("13. Exit")

    choice = input("\nEnter Choice: ")

    # ----------------------------------
    # View Products
    # ----------------------------------

    if choice == "1":

        print("\nProducts\n")

        for product in products.values():
            print(product)

    # ----------------------------------
    # Top Recommendations
    # ----------------------------------

    elif choice == "2":

        recommendations = (
            engine.recommend_products(
                USER_ID
            )
        )

        print("\nTop Recommendations\n")

        for score, product in recommendations:

            print(
                f"{product.name}"
                f" | Score={score}"
            )

    # ----------------------------------
    # Similar Products
    # ----------------------------------

    elif choice == "3":

        try:

            pid = int(
                input(
                    "Enter Product ID: "
                )
            )

            similar = (
                engine.similar_products(
                    pid
                )
            )

            if similar is None:

                print(
                    "\nInvalid Product ID!"
                )

            else:

                print(
                    "\nSimilar Products\n"
                )

                for product in similar:

                    print(product.name)

        except ValueError:

            print(
                "\nPlease enter a valid number."
            )

    # ----------------------------------
    # Category Recommendations
    # ----------------------------------

    elif choice == "4":

        category = input(
            "Enter Category: "
        )

        products_list = (
            engine.category_recommendations(
                category
            )
        )

        if not products_list:

            print(
                "\nNo products found."
            )

        else:

            print(
                f"\nTop {category} Products\n"
            )

            for product in products_list:

                print(
                    product.name,
                    "| Rating:",
                    product.rating
                )

    # ----------------------------------
    # Generate Report
    # ----------------------------------

    elif choice == "5":

        recommendations = (
            engine.recommend_products(
                USER_ID
            )
        )

        report_path = (
            generate_report(
                recommendations
            )
        )

        print(
            f"\nReport Saved: "
            f"{report_path}"
        )

    # ----------------------------------
    # Search Product
    # ----------------------------------

    elif choice == "6":

        keyword = input(
            "Enter product name: "
        )

        results = (
            engine.search_product(
                keyword
            )
        )

        if not results:

            print(
                "\nNo products found."
            )

        else:

            print(
                "\nSearch Results\n"
            )

            for product in results:

                print(product)

    # ----------------------------------
    # Add Product
    # ----------------------------------

    elif choice == "7":

        try:

            pid = int(
                input("ID: ")
            )

            if pid in engine.products:

                print(
                    "\nProduct ID already exists!"
                )

                continue

            name = input(
                "Name: "
            )

            category = input(
                "Category: "
            )

            rating = float(
                input(
                    "Rating: "
                )
            )

            price = float(
                input(
                    "Price: "
                )
            )

            new_product = Product(
                pid,
                name,
                category,
                rating,
                price
            )

            engine.add_product(
                new_product
            )

            save_products(
                engine.products
            )

            print(
                "\nProduct Added Successfully!"
            )

        except ValueError:

            print(
                "\nInvalid Input."
            )

    # ----------------------------------
    # Delete Product
    # ----------------------------------

    elif choice == "8":

        try:

            pid = int(
                input(
                    "Product ID: "
                )
            )

            status = (
                engine.delete_product(
                    pid
                )
            )

            if status:

                save_products(
                    engine.products
                )

                print(
                    "\nProduct Deleted Successfully!"
                )

            else:

                print(
                    "\nProduct Not Found!"
                )

        except ValueError:

            print(
                "\nInvalid Product ID."
            )

    # ----------------------------------
    # View Users
    # ----------------------------------

    elif choice == "9":

        print("\nUsers\n")

        for user in engine.view_users():

            print(
                user.user_id,
                "|",
                user.name
            )

    # ----------------------------------
    # Add User
    # ----------------------------------

    elif choice == "10":

        try:

            uid = int(
                input(
                    "User ID: "
                )
            )

            if uid in engine.users:

                print(
                    "\nUser ID already exists!"
                )

                continue

            name = input(
                "Name: "
            )

            new_user = User(
                uid,
                name,
                [],
                [],
                [],
                {}
            )

            engine.add_user(
                new_user
            )

            save_users(
                engine.users
            )

            print(
                "\nUser Added Successfully!"
            )

        except ValueError:

            print(
                "\nInvalid User ID."
            )

    # ----------------------------------
    # Export CSV
    # ----------------------------------

    elif choice == "11":

        recommendations = (
            engine.recommend_products(
                USER_ID
            )
        )

        path = (
            export_recommendations(
                recommendations
            )
        )

        print(
            f"\nCSV Exported Successfully:"
            f"\n{path}"
        )

    # ----------------------------------
    # Analytics Dashboard
    # ----------------------------------

    elif choice == "12":

        analytics = (
            engine.analytics_dashboard()
        )

        print("\n")
        print("=" * 40)
        print("ANALYTICS DASHBOARD")
        print("=" * 40)

        print(
            f"Total Products: "
            f"{analytics['total_products']}"
        )

        print(
            f"Total Users: "
            f"{analytics['total_users']}"
        )

        print(
            f"Average Rating: "
            f"{analytics['avg_rating']}"
        )

        highest = analytics[
            "highest_rated"
        ]

        print(
            "\nHighest Rated Product:"
        )

        print(
            f"{highest.name}"
            f" ({highest.rating})"
        )

        print(
            "\nProducts Per Category:"
        )

        for category, count in analytics[
            "category_count"
        ].items():

            print(
                f"{category}: {count}"
            )

    # ----------------------------------
    # Exit
    # ----------------------------------

    elif choice == "13":

        print(
            "\nThank You!"
        )

        break

    # ----------------------------------
    # Invalid Choice
    # ----------------------------------

    else:

        print(
            "\nInvalid Choice. Try Again."
        )