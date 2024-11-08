def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}

    for emperor_data in args:
        emperor = emperor_data[0]
        is_successful = emperor_data[1]
        if is_successful:
            successful_emperors[emperor] = kwargs[emperor]
        else:
            unsuccessful_emperors[emperor] = kwargs[emperor]

    sorted_successful_emperors = dict(sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0])))
    sorted_unsuccessful_emperors = dict(sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0])))

    num_of_all_emperors = len(successful_emperors) + len(unsuccessful_emperors)
    result = [f"Total number of emperors: {num_of_all_emperors}"]

    if successful_emperors:
        result.append("Successful emperors:")
        for emperor, years in sorted_successful_emperors.items():
            result.append(f"****{emperor}: {years}")

    if unsuccessful_emperors:
        result.append("Unsuccessful emperors:")
        for emperor, years in sorted_unsuccessful_emperors.items():
            result.append(f"****{emperor}: {years}")

    return "\n".join(result)


# print(list_roman_emperors(("Augustus", True),
#                           ("Nero", False),
#                           Augustus=40,
#                           Nero=14, ))

# print(list_roman_emperors(("Augustus", True),
#                           ("Trajan", True),
#                           ("Nero", False),
#                           ("Caligula", False),
#                           ("Pertinax", False),
#                           ("Vespasian", True),
#                           Augustus=40, Trajan=19,
#                           Nero=14, Caligula=4,
#                           Pertinax=4,
#                           Vespasian=19, ))
