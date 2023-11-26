commands_number = int(input())

parking = []
for i in range(commands_number):
    info = input().split(", ")
    command = info[0]
    number = info[1]

    if command == 'IN':
        if number not in parking:
            parking.append(number)
    elif command == 'OUT':
        if number in parking:
            parking.remove(number)

if parking:
    for curr_num in parking:
        print(''.join(curr_num))

elif not parking:
    print('Parking Lot is Empty')
  
