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


# print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
# print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
