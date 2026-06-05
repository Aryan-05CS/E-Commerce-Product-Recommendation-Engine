import streamlit as st

from src.data_loader import (
    load_products,
    load_users
)

from src.recommender import (
    RecommendationEngine
)

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="E-Commerce Recommendation Engine",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------------
# Load Data
# -----------------------------------

products = load_products()
users = load_users()

engine = RecommendationEngine(
    products,
    users
)

# -----------------------------------
# Header
# -----------------------------------

st.title(
    "🛒 E-Commerce Product Recommendation Engine"
)

st.markdown(
    """
    DSA-Based Recommendation System
    using Hash Maps, Heaps,
    Sorting and Recommendation Logic
    """
)

# -----------------------------------
# Sidebar
# -----------------------------------

menu = st.sidebar.selectbox(

    "Navigation",

    [
        "Home",
        "Products",
        "Search Product",
        "Recommendations",
        "Similar Products",
        "Users",
        "Analytics Dashboard"
    ]
)

# -----------------------------------
# Home
# -----------------------------------

if menu == "Home":

    st.header("Welcome")

    st.write(
        """
        This project demonstrates:

        ✅ Product Recommendation System

        ✅ Hash Map Based Storage

        ✅ Priority Queue Ranking

        ✅ Product Search

        ✅ User Management

        ✅ Analytics Dashboard

        ✅ Persistent JSON Storage
        """
    )

# -----------------------------------
# Products
# -----------------------------------

elif menu == "Products":

    st.header("📦 Product Catalog")

    for product in products.values():

        with st.container():

            st.write(
                f"**ID:** {product.product_id}"
            )

            st.write(
                f"**Name:** {product.name}"
            )

            st.write(
                f"**Category:** {product.category}"
            )

            st.write(
                f"**Rating:** ⭐ {product.rating}"
            )

            st.write(
                f"**Price:** ₹{product.price}"
            )

            st.divider()

# -----------------------------------
# Search Product
# -----------------------------------

elif menu == "Search Product":

    st.header("🔍 Product Search")

    keyword = st.text_input(
        "Enter Product Name"
    )

    if keyword:

        results = (
            engine.search_product(
                keyword
            )
        )

        if results:

            st.success(
                f"{len(results)} product(s) found"
            )

            for product in results:

                st.write(
                    f"{product.product_id} | "
                    f"{product.name} | "
                    f"{product.category} | "
                    f"⭐ {product.rating}"
                )

        else:

            st.error(
                "No Products Found"
            )

# -----------------------------------
# Recommendations
# -----------------------------------

elif menu == "Recommendations":

    st.header(
        "⭐ Recommended Products"
    )

    user_ids = list(
        users.keys()
    )

    selected_user = st.selectbox(
        "Select User ID",
        user_ids
    )

    if st.button(
        "Generate Recommendations"
    ):

        recommendations = (
            engine.recommend_products(
                selected_user
            )
        )

        for score, product in recommendations:

            st.success(
                f"{product.name}"
            )

            st.write(
                f"Category: "
                f"{product.category}"
            )

            st.write(
                f"Rating: "
                f"{product.rating}"
            )

            st.write(
                f"Recommendation Score: "
                f"{score}"
            )

            st.divider()

# -----------------------------------
# Similar Products
# -----------------------------------

elif menu == "Similar Products":

    st.header(
        "🔄 Similar Products"
    )

    product_ids = list(
        products.keys()
    )

    selected_product = st.selectbox(
        "Select Product ID",
        product_ids
    )

    if st.button(
        "Find Similar Products"
    ):

        result = (
            engine.similar_products(
                selected_product
            )
        )

        if result:

            for product in result:

                st.write(
                    f"{product.name}"
                )

        else:

            st.error(
                "No Similar Products Found"
            )

# -----------------------------------
# Users
# -----------------------------------

elif menu == "Users":

    st.header(
        "👥 Users"
    )

    for user in users.values():

        st.write(
            f"User ID: "
            f"{user.user_id}"
        )

        st.write(
            f"Name: "
            f"{user.name}"
        )

        st.divider()

# -----------------------------------
# Analytics Dashboard
# -----------------------------------

elif menu == "Analytics Dashboard":

    st.header(
        "📊 Analytics Dashboard"
    )

    analytics = (
        engine.analytics_dashboard()
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Products",
            analytics[
                "total_products"
            ]
        )

    with col2:

        st.metric(
            "Total Users",
            analytics[
                "total_users"
            ]
        )

    with col3:

        st.metric(
            "Average Rating",
            analytics[
                "avg_rating"
            ]
        )

    st.subheader(
        "Highest Rated Product"
    )

    highest = analytics[
        "highest_rated"
    ]

    st.success(
        f"{highest.name} "
        f"({highest.rating} ⭐)"
    )

    st.subheader(
        "Products Per Category"
    )

    for category, count in analytics[
        "category_count"
    ].items():

        st.write(
            f"{category}: {count}"
        )