def shopping_cart(*args):
    products_limit = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    result = []
    if args[0] == 'Stop':
        result.append('No products in the cart!')
        return ''.join(result)

    bought_products = {'Dessert': [], 'Pizza': [], 'Soup': []}

    for data in args:
        if data == 'Stop':
            break
        meal, product = data[0], data[1]
        if len(bought_products[meal]) < products_limit[meal] and product not in bought_products[meal]:
            bought_products[meal].append(product)

    sorted_products = dict(sorted(bought_products.items(), key=lambda x: (-len(x[1]), x[0])))

    for meal, products in sorted_products.items():
        result.append(f'{meal}:')
        products.sort()
        for product in products:
            result.append(f' - {product}')

    return '\n'.join(result)


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))


# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
