def get_capitals():
    capitals = {country: city for country, city in zip(input().split(", "), input().split(", "))}
    return capitals


def print_result():
    return [print(f"{country} -> {city}") for country, city in get_capitals().items()]


print_result()


# One row
# print("\n".join([f"{country} -> {capital}" for country, capital in zip(input().split(", "), input().split(", "))]))
