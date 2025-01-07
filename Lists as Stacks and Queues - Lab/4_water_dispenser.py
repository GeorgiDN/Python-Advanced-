from collections import deque


people_on_queue, water = deque(), int(input())

while True:
    command = input()
    if command == 'End':
        break

    elif command == 'Start':
        continue

    elif command.isdigit():
        liters = int(command)
        person = people_on_queue.popleft()
        if water >= liters:
            water -= liters
            print(f'{person} got water')
        else:
            print(f'{person} must wait')

    elif command.startswith('refill'):
        command = command.split(' ')
        curr_liters = int(command[1])
        water += curr_liters

    else:
        name = command
        people_on_queue.append(name)

print(f'{water} liters left')


# from collections import deque

# liters_in_dispenser = int(input())
# people_in_the_queue = deque()

# start = False
# while True:
#     command = input()
#     if command == "End":
#         break

#     if command == "Start":
#         start = True
#         continue

#     if not start:
#         name = command
#         people_in_the_queue.append(name)

#     else:
#         if command.startswith("ref"):
#             data = command.split()
#             liters = int(data[1])
#             liters_in_dispenser += liters

#         else:
#             wanted_water = int(command)
#             if wanted_water <= liters_in_dispenser:
#                 print(f"{people_in_the_queue.popleft()} got water")
#                 liters_in_dispenser -= wanted_water
#             else:
#                 print(f"{people_in_the_queue.popleft()} must wait")

# print(f"{liters_in_dispenser} liters left")




# from _collections import deque

# def add_names_in_deque():
#     people_data = deque()
#     while True:
#         name = input()

#         if name == COMMAND_START:
#             break
#         people_data.append(name)

#     return people_data


# COMMAND_END = 'End'
# COMMAND_START = 'Start'
# COMMAND_REFILL = 'refill '
# water_amount = int(input())
# people_deque = add_names_in_deque()

# while True:
#     command = input()

#     if command == COMMAND_END:
#         print(f'{water_amount} liters left')
#         break

#     elif command.startswith(COMMAND_REFILL):
#         refill_command_data = command.split(' ')
#         refill_water_amount = int(refill_command_data[1])
#         water_amount += refill_water_amount

#     else:
#         person = people_deque.popleft()
#         current_litres = int(command)

#         if current_litres <= water_amount:
#             print(f'{person} got water')
#             water_amount -= current_litres
#         else:
#             print(f'{person} must wait')
