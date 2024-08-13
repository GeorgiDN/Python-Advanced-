def accommodate(*args, **kwargs):
    groups = list(args)
    rooms = {}
    accommodated_guest = {}

    for key, value in kwargs.items():
        key = int(key.split("_")[1])
        rooms[key] = value

    sorted_rooms = sorted(rooms.items(), key=lambda x: (x[1], x[0]))
    not_accomodated = []

    for guests in groups:
        for room in sorted_rooms:
            room_number, capacity = room[0], room[1]
            if guests <= capacity:
                if room_number not in accommodated_guest:
                    accommodated_guest[room_number] = guests
                    break
        else:
            not_accomodated.append(guests)

    empty_rooms = len(kwargs) - len(accommodated_guest)
    total_number_of_unaccommodated_guests = sum(not_accomodated)

    result = []
    if accommodated_guest:
        result.append(f"A total of {len(accommodated_guest)} accommodations were completed!")
        sorted_accomnodated_persons = dict(sorted(accommodated_guest.items(), key=lambda g: g[0]))
        for r, g in sorted_accomnodated_persons.items():
            result.append(f"<Room {r} accommodates {g} guests>")
    else:
        result.append("No accommodations were completed!")

    if not_accomodated:
        result.append(f"Guests with no accommodation: {total_number_of_unaccommodated_guests}")

    if empty_rooms > 0:
        result.append(f"Empty rooms: {empty_rooms}")

    return "\n".join(result)

# print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
# print(accommodate(10, 9, 8, room_307=6, room_802=5))
# print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
