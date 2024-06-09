def accommodate_new_pets(*args):
    accommodated_pets = {}
    available_capacity_of_hotel = int(args[0])
    max_weight = float(args[1])
    not_all_acomodated = False
    result = ''

    for pet, weight in args[2:]:
        if available_capacity_of_hotel == 0:
            not_all_acomodated = True
            break
        if weight <= max_weight:
            if pet not in accommodated_pets:
                accommodated_pets[pet] = 0
            accommodated_pets[pet] += 1
            available_capacity_of_hotel -= 1

    if not_all_acomodated:
        result += 'You did not manage to accommodate all pets!\n'
    else:
        result += f'All pets are accommodated! Available capacity: {available_capacity_of_hotel}.\n'

    result += 'Accommodated pets:\n'

    sorted_pets = sorted(accommodated_pets.items())

    for pet_, count in sorted_pets:
        result += f'{pet_}: {count}\n'

    return result.strip()


# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))



# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))


# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))




##############################################################################################################
# from unittest import TestCase, main
#
#
# class Test(TestCase):
#     def test_accommodate_pets(self):
#         result = accommodate_new_pets(
#             10,
#             10.0,
#             ("cat", 5.8),
#             ("dog", 10.5),
#             ("parrot", 0.8),
#             ("cat", 3.1),
#         )
#
#         self.assertEqual(
#             result.strip(),
#             """All pets are accommodated! Available capacity: 7.
# Accommodated pets:
# cat: 2
# parrot: 1""")
#
#
# if __name__ == '__main__':
#     main()
#





# def accommodate_new_pets(*args):
#     hotel_capacity, weight_limit, *rest = args
#     pets_accommodated = {}
#     all_pets_accommodated = True
#
#     for info in rest:
#         pet_type = info[0]
#         pet_weight = info[1]
#
#         if hotel_capacity > 0:
#             if pet_weight <= weight_limit:
#                 if pet_type not in pets_accommodated:
#                     pets_accommodated[pet_type] = 1
#                 else:
#                     pets_accommodated[pet_type] += 1
#                 hotel_capacity -= 1
#         else:
#             all_pets_accommodated = False
#             break
#
#     sorted_pets_accommodated = dict(sorted(pets_accommodated.items(), key=lambda x: x[0]))
#     final_accommodated = ''
#
#     if all_pets_accommodated:
#         final_accommodated += f'All pets are accommodated! Available capacity: {hotel_capacity}.\n'
#
#     elif not all_pets_accommodated:
#         final_accommodated += "You did not manage to accommodate all pets!\n"
#
#     final_accommodated += "Accommodated pets:\n"
#
#     for k, v in sorted_pets_accommodated.items():
#         final_accommodated += f"{k}: {v}\n"
#
#     return final_accommodated
#
#
# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))
