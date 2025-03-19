def accommodate(*args, **kwargs):
    rooms = {room.split('_')[1]: num for room, num in kwargs.items()}
    sorted_rooms = dict(sorted(rooms.items(), key=lambda r: (r[1], r[0])))
    accommodated_guests = {}
    guest_with_no_accomodation = sum(args)

    for guests in args:
        for room, capacity in sorted_rooms.items():
            if capacity >= guests and room not in accommodated_guests:
                accommodated_guests[room] = guests
                guest_with_no_accomodation -= guests
                break

    accommodations = len(accommodated_guests)
    empty_rooms = len(sorted_rooms) - len(accommodated_guests)
    result = []

    if accommodations > 0:
        result.append(f'A total of {accommodations} accommodations were completed!')
        sorted_accommodated_guests = dict(sorted(accommodated_guests.items(), key=lambda n: n[0]))
        for room_number, guests_number in sorted_accommodated_guests.items():
            result.append(f'<Room {room_number} accommodates {guests_number} guests>')

    else:
        result.append(f'No accommodations were completed!')

    if guest_with_no_accomodation > 0:
        result.append(f'Guests with no accommodation: {guest_with_no_accomodation}')

    if empty_rooms > 0:
        result.append(f'Empty rooms: {empty_rooms}')

    return '\n'.join(result)



#################################################################################

# def accommodate(*args, **kwargs):
#     rooms = {}
#     for key, value in kwargs.items():
#         key = int(key.split('_')[1])
#         rooms[key] = value
# 
#     sorted_rooms = dict(sorted(rooms.items(), key=lambda r: (r[1], r[0])))
# 
#     accommodated = {}
# 
#     for guests in args:
#         for room_number, capacity in sorted_rooms.items():
#             if room_number not in accommodated and guests <= capacity:
#                 accommodated[room_number] = guests
#                 break
# 
#     all_accommodated = len(args) == len(accommodated)
# 
#     result = []
# 
#     if accommodated:
#         sorted_accommodated = dict(sorted(accommodated.items(), key=lambda r: r[0]))
#         result.append(f"A total of {len(accommodated)} accommodations were completed!")
# 
#         for room, num_guests in sorted_accommodated.items():
#             result.append(f"<Room {room} accommodates {num_guests} guests>")
# 
#     else:
#         result.append("No accommodations were completed!")
# 
#     if not all_accommodated:
#         guest_with_no_accommodation = sum(args) - sum(accommodated.values())
#         result.append(f"Guests with no accommodation: {guest_with_no_accommodation}")
# 
#     empty_rooms = len(kwargs) - len(accommodated)
#     if empty_rooms:
#         result.append(f"Empty rooms: {empty_rooms}")
# 
#     return "\n".join(result)



#################################################################################
# def accommodate(*args, **kwargs):
#     groups = list(args)
#     rooms = {}
#     accommodated_guest = {}
#
#     for key, value in kwargs.items():
#         key = int(key.split("_")[1])
#         rooms[key] = value
#
#     sorted_rooms = sorted(rooms.items(), key=lambda x: (x[1], x[0]))
#     not_accomodated = []
#
#     for guests in groups:
#         for room in sorted_rooms:
#             room_number, capacity = room[0], room[1]
#             if guests <= capacity:
#                 if room_number not in accommodated_guest:
#                     accommodated_guest[room_number] = guests
#                     break
#         else:
#             not_accomodated.append(guests)
#
#     empty_rooms = len(kwargs) - len(accommodated_guest)
#     total_number_of_unaccommodated_guests = sum(not_accomodated)
#
#     result = []
#     if accommodated_guest:
#         result.append(f"A total of {len(accommodated_guest)} accommodations were completed!")
#         sorted_accomnodated_persons = dict(sorted(accommodated_guest.items(), key=lambda g: g[0]))
#         for r, g in sorted_accomnodated_persons.items():
#             result.append(f"<Room {r} accommodates {g} guests>")
#     else:
#         result.append("No accommodations were completed!")
#
#     if not_accomodated:
#         result.append(f"Guests with no accommodation: {total_number_of_unaccommodated_guests}")
#
#     if empty_rooms > 0:
#         result.append(f"Empty rooms: {empty_rooms}")
#
#     return "\n".join(result)



#################################################################################
# def accommodate(*args, **kwargs):
#     guests = list(args)
#     rooms = list(kwargs.items())
#
#     rooms.sort(key=lambda x: (x[1], int(x[0].split('_')[1])))
#
#     accommodations = []
#     unaccommodated_guests = 0
#     for group in guests:
#         accommodated = False
#         for i, (room, capacity) in enumerate(rooms):
#             if group <= capacity:
#                 accommodations.append((int(room.split('_')[1]), group))
#                 rooms.pop(i)
#                 accommodated = True
#                 break
#         if not accommodated:
#             unaccommodated_guests += group
#
#     if accommodations:
#         accommodations.sort()
#         result = [f"A total of {len(accommodations)} accommodations were completed!"]
#         for room_number, guests in accommodations:
#             result.append(f"<Room {room_number} accommodates {guests} guests>")
#         result = "\n".join(result)
#     else:
#         result = "No accommodations were completed!"
#
#     if unaccommodated_guests > 0:
#         result += f"\nGuests with no accommodation: {unaccommodated_guests}"
#
#     if rooms:
#         result += f"\nEmpty rooms: {len(rooms)}"
#
#     return result
# #
#
