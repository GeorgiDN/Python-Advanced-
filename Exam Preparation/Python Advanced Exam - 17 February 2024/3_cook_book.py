def cookbook(*args):
    ingredients_book = {}

    for elements in args:
        cuisine = elements[1]
        recipe_name = elements[0]
        ingredients = elements[2]

        if cuisine not in ingredients_book:
            ingredients_book[cuisine] = {}

        if recipe_name not in ingredients_book[cuisine]:
            ingredients_book[cuisine][recipe_name] = ingredients

    result = ''
    sorted1_ingredients_book = dict(sorted(ingredients_book.items(), key=lambda x: (-len(x[1]), (x[0]))))

    for kitchen, data in sorted1_ingredients_book.items():
        data = dict(sorted(data.items()))
        result += f"{kitchen} cuisine contains {len(data)} recipes:\n"
        for recipie, current_ingredients in data.items():
            result += f"  * {recipie} -> Ingredients: {', '.join(current_ingredients)}\n"

    return result


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))



# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))



# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
#     ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
#     ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
#     ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
#     ))
