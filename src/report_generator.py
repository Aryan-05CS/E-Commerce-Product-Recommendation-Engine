import os

def generate_report(recommendations):

    os.makedirs("outputs", exist_ok=True)

    path = "outputs/recommendation_report.txt"

    with open(path, "w", encoding="utf-8") as file:

        file.write("E-COMMERCE RECOMMENDATION REPORT\n")
        file.write("=" * 50 + "\n\n")

        for score, product in recommendations:

            file.write(f"Product: {product.name}\n")
            file.write(f"Category: {product.category}\n")
            file.write(f"Rating: {product.rating}\n")
            file.write(f"Score: {score}\n")
            file.write("-" * 40 + "\n")

    return path