def grocery_store(**kwargs):
    result = {}

    for key, value in kwargs.items():
        result[key] = value

    receipt = dict(sorted(result.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    result_str = "\n".join([f"{k}: {v}" for k, v in receipt.items()])

    return result_str

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
