def shop_from_grocery_list(*args):
    budget = int(args[0])
    grocery_list = args[1]
    products_info = args[2:]
    all_products_purchased = True

    purchased_products = {}

    for data in products_info:
        product, price = data[0], float(data[1])
        if product in purchased_products or product not in grocery_list:
            continue
        if budget < price:
            break
        else:
            purchased_products[product] = price
            budget -= price

    missing_products = [product for product in grocery_list if product not in purchased_products]
    if missing_products:
        all_products_purchased = False

    result = ""
    if all_products_purchased:
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result += f"You did not buy all the products. Missing products: {', '.join(missing_products)}."

    return result


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
#
#
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
