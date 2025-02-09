def cookbook(*args):
    recipies = {}
    all_ingredients = {}

    for cook in args:
        cuisine, food, ingredients = cook[1], cook[0], cook[2]

        if cuisine not in recipies:
            recipies[cuisine] = []
        recipies[cuisine].append(food)
        all_ingredients[food] = ingredients

    result = []

    sorted_recipes = dict(sorted(recipies.items(), key=lambda x: (-len(x[1]), x[0])))

    for cuisine, foods in sorted_recipes.items():
        result.append(f'{cuisine} cuisine contains {len(foods)} recipes:')
        foods.sort()
        for food in foods:
            result.append(f'  * {food} -> Ingredients: {", ".join(all_ingredients[food])}')

    return '\n'.join(result)


############################################################################################################################################################
# def cookbook(*args):
#     ingredients_book = {}

#     for elements in args:
#         cuisine = elements[1]
#         recipe_name = elements[0]
#         ingredients = elements[2]

#         if cuisine not in ingredients_book:
#             ingredients_book[cuisine] = {}

#         if recipe_name not in ingredients_book[cuisine]:
#             ingredients_book[cuisine][recipe_name] = ingredients

#     result = ''
#     sorted_ingredients_book = dict(sorted(ingredients_book.items(), key=lambda x: (-len(x[1]), (x[0]))))

#     for cuisine, recipies in sorted_ingredients_book.items():
#         recipies = dict(sorted(recipies.items()))
#         result += f"{cuisine} cuisine contains {len(recipies)} recipes:\n"
#         for recipie, ingredients in recipies.items():
#             result += f"  * {recipie} -> Ingredients: {', '.join(ingredients)}\n"

#     return result


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

