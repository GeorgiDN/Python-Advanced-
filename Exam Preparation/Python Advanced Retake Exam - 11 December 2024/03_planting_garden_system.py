def plant_garden(available_space, *allowed_plant_types, **requested_plant_types):
    allowed_space_per_plant = {p: space for p, space in allowed_plant_types}
    sorted_requests = sorted(requested_plant_types.items())

    planted_plants = {}
    all_planted = True

    for plant_type, quantity in sorted_requests:
        if plant_type in allowed_space_per_plant:
            space_per_plant = allowed_space_per_plant[plant_type]
            required_space = space_per_plant * quantity

            if required_space <= available_space:
                planted_plants[plant_type] = quantity
                available_space -= required_space
            else:
                all_planted = False
                max_plants = int(available_space // space_per_plant)
                if max_plants > 0:
                    planted_plants[plant_type] = max_plants
                    available_space -= max_plants * space_per_plant

    result = []

    if all_planted:
        result.append(f'All plants were planted! Available garden space: {available_space:.1f} sq meters.')
    else:
        result.append('Not enough space to plant all requested plants!')

    result.append('Planted plants:')
    for plant_type, quantity in planted_plants.items():
        result.append(f'{plant_type}: {quantity}')

    return '\n'.join(result)


#####################################################################################################################
# def plant_garden(available_space, *allowed_plant_types, **requested_plant_types):
#     planted_data = {}
#     sorted_requested_plant_types = dict(sorted(requested_plant_types.items(), key=lambda x: x[0]))
#     all_planted = True
#
#     for required_plant_type, required_quantity in sorted_requested_plant_types.items():
#         for plant, space_required in allowed_plant_types:
#             if required_plant_type == plant and plant not in planted_data:
#                 total = required_quantity * space_required
#                 if available_space >= total:
#                     planted_data[plant] = required_quantity
#                     available_space -= total
#                 else:
#                     all_planted = False
#                     max_plants = available_space // space_required
#                     if max_plants > 0:
#                         planted_data[plant] = int(max_plants)
#                         available_space -= max_plants * space_required
#
#     result = []
#     sorted_planted_data = dict(sorted(planted_data.items(), key=lambda x: x[0]))
#
#     if all_planted:
#         result.append(f"All plants were planted! Available garden space: {available_space:.1f} sq meters.")
#     else:
#         result.append(f"Not enough space to plant all requested plants!")
#
#     result.append("Planted plants:")
#
#     for plant, pieces in sorted_planted_data.items():
#         result.append(f"{plant}: {pieces}")
#
#     return "\n".join(result)


# print(plant_garden(
#     50.0,
#     ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0),
#     rose=10, tulip=20)
# )
#
# print(plant_garden(
#     20.0,
#     ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0),
#     rose=10, tulip=20, sunflower=5)
# )

# print(plant_garden(
#     2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2),
#     rose=4, tulip=15, sunflower=3, daisy=4)
# )
