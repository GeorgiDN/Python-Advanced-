number_of_guests = int(input())
vip_guests = []
regular_guests = []

for _ in range(number_of_guests):
    reservation_code = input()
    if reservation_code[0].isdigit():
        if reservation_code not in vip_guests:
            vip_guests.append(reservation_code)
    else:
        if reservation_code not in regular_guests:
            regular_guests.append(reservation_code)

while True:
    reservation_code = input()
    if reservation_code == "END":
        break

    if reservation_code in vip_guests:
        vip_guests.remove(reservation_code)

    elif reservation_code in regular_guests:
        regular_guests.remove(reservation_code)

number_guest_not_coming = len(vip_guests) + len(regular_guests)
print(number_guest_not_coming)

if vip_guests:
    vip_guests = sorted(vip_guests)
    print('\n'.join([guest for guest in vip_guests]))
if regular_guests:
    regular_guests = sorted(regular_guests)
    print('\n'.join([guest for guest in regular_guests]))




# number = int(input())

# vip = []
# regular = []

# for i in range(number):
#     reservation = input()

#     if reservation[0].isdigit():
#         if reservation not in vip:
#             vip.append(reservation)
#     else:
#         if reservation not in regular:
#             regular.append(reservation)

# while True:
#     command = input()
#     if command == "END":
#         break

#     guest = command

#     if guest in vip:
#         vip.remove(guest)
#     elif guest in regular:
#         regular.remove(guest)

# total = len(vip) + len(regular)
# vip = sorted(vip)
# regular = sorted(regular)

# print(total)

# if vip:
#     for v in vip:
#         print(''.join(v))
# if regular:
#     for r in regular:
#         print(''.join(r))
      
