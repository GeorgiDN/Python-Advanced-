def grocery_store(**kwargs):
    sorted_products = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    return '\n'.join([f"{product}: {qty}" for product, qty in sorted_products.items()])


######################################################################################################################################################
# def grocery_store(**kwargs):
#     return '\n'.join([f"{product}: {qty}" for product, qty in dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))).items()])


######################################################################################################################################################
# def grocery_store(**kwargs):
#     products = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

#     result = "\n".join([f"{product}: {qty}" for product, qty in products.items()])
#     return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
