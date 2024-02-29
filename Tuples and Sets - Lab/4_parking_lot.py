number_of_commands = int(input())
parking_lot = []

for _ in range(number_of_commands):
    command, current_number = input().split(", ")
    if command == "IN":
        parking_lot.append(current_number)
    elif command == "OUT":
        if parking_lot:
            parking_lot.remove(current_number)

if parking_lot:
    print('\n'.join([num for num in set(parking_lot)]))

else:
    print("Parking Lot is Empty")




# number_of_commands = int(input())
# parking_lot = []
#
# for _ in range(number_of_commands):
#     command, current_number = input().split(", ")
#     if command == "IN":
#         if current_number not in parking_lot:
#             parking_lot.append(current_number)
#     elif command == "OUT":
#         if parking_lot and current_number in parking_lot:
#             parking_lot.remove(current_number)
#
# if parking_lot:
#     print('\n'.join([num for num in parking_lot]))
#
# else:
#     print("Parking Lot is Empty")






# commands_number = int(input())

# parking = []
# for i in range(commands_number):
#     info = input().split(", ")
#     command = info[0]
#     number = info[1]

#     if command == 'IN':
#         if number not in parking:
#             parking.append(number)
#     elif command == 'OUT':
#         if number in parking:
#             parking.remove(number)

# if parking:
#     for curr_num in parking:
#         print(''.join(curr_num))

# elif not parking:
#     print('Parking Lot is Empty')
  
