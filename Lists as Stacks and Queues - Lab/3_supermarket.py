from collections import deque

people_on_the_queue = deque()

while True:
    name = input()
    if name == "End":
        break

    elif name == "Paid":
        while people_on_the_queue:
            print(people_on_the_queue.popleft())

    else:
        people_on_the_queue.append(name)

print(f"{len(people_on_the_queue)} people remaining.")


# from collections import deque

# people_on_the_queue = deque()

# while True:
#     name = input()
#     if name == "End":
#         break

#     elif name == "Paid":
#         while people_on_the_queue:
#             print(people_on_the_queue.popleft())

#     else:
#         people_on_the_queue.append(name)

# print(f"{len(people_on_the_queue)} people remaining.")



# from _collections import deque

# names_deque = deque()
# COMMAND_END = 'End'
# COMMAND_PAID = 'Paid'

# while True:
#     command = input()

#     if command == COMMAND_END:
#         print(f'{len(names_deque)} people remaining.')
#         break

#     elif command == COMMAND_PAID:
#         while names_deque:
#             print(names_deque.popleft())

#     else:
#         names_deque.append(command)
      
