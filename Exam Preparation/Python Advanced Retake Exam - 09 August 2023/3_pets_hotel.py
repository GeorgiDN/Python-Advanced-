def accommodate_new_pets(*args):
    hotel_capacity, weight_limit, *rest = args
    pets_accommodated = {}
    all_pets_accommodated = True

    for info in rest:
        pet_type = info[0]
        pet_weight = info[1]

        if hotel_capacity > 0:
            if pet_weight <= weight_limit:
                if pet_type not in pets_accommodated:
                    pets_accommodated[pet_type] = 1
                else:
                    pets_accommodated[pet_type] += 1
                hotel_capacity -= 1
        else:
            all_pets_accommodated = False
            break

    sorted_pets_accommodated = dict(sorted(pets_accommodated.items(), key=lambda x: x[0]))
    final_accommodated = ''

    if all_pets_accommodated:
        final_accommodated += f'All pets are accommodated! Available capacity: {hotel_capacity}.\n'

    elif not all_pets_accommodated:
        final_accommodated += "You did not manage to accommodate all pets!\n"

    final_accommodated += "Accommodated pets:\n"

    for k, v in sorted_pets_accommodated.items():
        final_accommodated += f"{k}: {v}\n"

    return final_accommodated


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
