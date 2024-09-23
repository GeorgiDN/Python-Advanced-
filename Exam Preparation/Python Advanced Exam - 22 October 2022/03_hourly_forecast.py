def forecast(*args):
    forecast_data = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for data in args:
        city, weather = data[0], data[1]
        forecast_data[weather].append(city)

    result = ""
    for curr_weather, towns in forecast_data.items():
        towns.sort()
        result += "".join(map(str, [f"{town} - {curr_weather}\n" for town in towns]))

    return result.strip()


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))



# def forecast(*args):
#     forecast_data = {"Sunny": [], "Cloudy": [], "Rainy": []}
#
#     for data in args:
#         city, weather = data[0], data[1]
#         forecast_data[weather].append(city)
#
#     result = []
#     for curr_weather, towns in forecast_data.items():
#         towns.sort()
#         for town in towns:
#             result.append(f"{town} - {curr_weather}")
#
#     return "\n".join(result)



