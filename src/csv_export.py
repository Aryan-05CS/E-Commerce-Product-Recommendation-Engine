import csv


def export_recommendations(
    recommendations
):

    with open(
        "outputs/recommendations.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(
            file
        )

        writer.writerow(
            [
                "Product",
                "Category",
                "Rating",
                "Score"
            ]
        )

        for score, product in recommendations:

            writer.writerow(
                [
                    product.name,
                    product.category,
                    product.rating,
                    score
                ]
            )

    return (
        "outputs/"
        "recommendations.csv"
    )