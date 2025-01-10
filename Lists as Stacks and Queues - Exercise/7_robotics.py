from collections import deque
from datetime import datetime, timedelta

robots_input = input().split(';')
robots_data = {}
busy_robots = {}

for robot_info in robots_input:
    robot_info = robot_info.split('-')
    robot, time_needed = robot_info[0], int(robot_info[1])
    robots_data[robot] = time_needed
    busy_robots[robot] = 0

time = input()
start_time = datetime.strptime(time, '%H:%M:%S')
current_time = start_time
products = deque()


while True:
    product = input()
    if product == 'End':
        break

    products.append(product)

while products:
    curr_product = products.popleft()
    current_time = current_time + timedelta(seconds=1)

    for robot_name in busy_robots.copy():
        busy_robots[robot_name] = max(busy_robots[robot_name] - 1, 0)

    available_robot = None
    for robot_name, busy_time in busy_robots.copy().items():
        if busy_time == 0:
            available_robot = robot_name
            break

    if available_robot:
        print(f'{available_robot} - {curr_product} [{current_time.strftime("%H:%M:%S")}]')
        busy_robots[available_robot] = robots_data[available_robot]

    else:
        products.append(curr_product)



# from collections import deque
# from datetime import datetime, timedelta
# 
# robots_input = input().split(';')
# robots_data = {}
# 
# for robot_info in robots_input:
#     robot_name, time_needed = robot_info.split('-')
#     robots_data[robot_name] = [int(time_needed), 0]
# 
# time = input()
# start_time = datetime.strptime(time, '%H:%M:%S')
# current_time = start_time
# 
# products = deque()
# 
# while True:
#     product = input()
#     if product == 'End':
#         break
#     products.append(product)
# 
# while products:
#     curr_product = products.popleft()
#     current_time += timedelta(seconds=1)
# 
#     for robot_name in robots_data:
#         robots_data[robot_name][1] = max(robots_data[robot_name][1] - 1, 0)
# 
#     available_robot = None
#     for robot_name, (process_time, busy_time) in robots_data.items():
#         if busy_time == 0:
#             available_robot = robot_name
#             break
# 
#     if available_robot:
#         print(f'{available_robot} - {curr_product} [{current_time.strftime("%H:%M:%S")}]')
#         robots_data[available_robot][1] = robots_data[available_robot][0]
#     else:
#         products.append(curr_product)



# from collections import deque
# from datetime import datetime, timedelta
#
# robots_data = {}
#
# for r in input().split(";"):
#     name, time_needed = r.split("-")
#     robots_data[name] = [int(time_needed), 0]
#
# factory_time = datetime.strptime(input(), "%H:%M:%S")
# products = deque()
#
# while True:
#     product = input()
#
#     if product == "End":
#         break
#
#     products.append(product)
#
# while products:
#     factory_time += timedelta(seconds=1)
#     product = products.popleft()
#
#     available_robots = []
#
#     for name, value in robots_data.items():
#         robots_data[name][1] = max(robots_data[name][1] - 1, 0)
#         busy_time = value[1]
#
#         if busy_time == 0:
#             available_robots.append([name, value])
#
#     if not available_robots:
#         products.append(product)
#         continue
#
#     robot_name, data = available_robots[0]
#     robots_data[robot_name][1] = data[0]
#
#     print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")



# from collections import deque


# def time_in_seconds(time):
#     hours, minutes, seconds = list(map(int, time.split(":")))
#     return hours * 3600 + minutes * 60 + seconds


# def formatted_time(seconds):
#     hours = seconds // 3600 % 24
#     minutes = (seconds % 3600) // 60
#     seconds = (seconds % 3600) % 60
#     return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# robots_info = input().split(";")
# robots = []

# for item in robots_info:
#     name, process_time = item.split("-")
#     robots.append([name, int(process_time), int(process_time), "free"])

# time = input()
# time_in_seconds = time_in_seconds(time)
# products_queue = deque()
# while True:
#     product = input()
#     if product == "End":
#         break
#     products_queue.append(product)

# while products_queue:
#     time_in_seconds += 1
#     current_product = products_queue.popleft()
#     for robot in robots:
#         robot_name = robot[0]
#         status = robot[3]
#         if status == "free":
#             robot[3] = "busy"
#             print(f"{robot_name} - {current_product} [{formatted_time(time_in_seconds)}]")
#             break
#     else:
#         products_queue.append(current_product)
#     for robot in robots:
#         if robot[3] == "busy":
#             robot[2] -= 1
#         if robot[2] <= 0:
#             robot[3] = "free"
#             robot[2] = robot[1]




# from collections import deque
#
#
# def time_to_seconds(time):
#     hours, minutes, seconds = list(map(int, time.split(":")))
#     return hours * 60 * 60 + minutes * 60 + seconds
#
#
# def formatted_time(seconds):
#     hours = seconds // (60 * 60) % 24
#     minutes = (seconds % (60 * 60)) // 60
#     seconds = (seconds % (60 * 60)) % 60
#     return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#
#
# robots_info = input().split(";")
# robots = []
#
# for item in robots_info:
#     name, process_time = item.split("-")
#     robots.append([name, int(process_time), int(process_time), "free"])
#
# time = input()
# time_in_seconds = time_to_seconds(time)
# products_queue = deque()
# while True:
#     product = input()
#     if product == "End":
#         break
#     products_queue.append(product)
#
# while products_queue:
#     time_in_seconds += 1
#     current_product = products_queue.popleft()
#     for robot in robots:
#         robot_name = robot[0]
#         status = robot[3]
#         if status == "free":
#             robot[3] = "busy"
#             print(f"{robot_name} - {current_product} [{formatted_time(time_in_seconds)}]")
#             break
#     else:
#         products_queue.append(current_product)
#     for robot in robots:
#         if robot[3] == "busy":
#             robot[2] -= 1
#         if robot[2] <= 0:
#             robot[3] = "free"
#             robot[2] = robot[1]




# 83/100
# from collections import deque
# from datetime import datetime, timedelta
#
# robots_input = input().split(';')
# robots_data = {}
# busy_robots = {}
#
# for robot_info in robots_input:
#     robot_info = robot_info.split('-')
#     robot, time_needed = robot_info[0], int(robot_info[1])
#     robots_data[robot] = time_needed
#     busy_robots[robot] = 0
#
# time = input()
# start_time = datetime.strptime(time, '%H:%M:%S')
# current_time = start_time
# products = deque()
# available_robots = deque()
#
# while True:
#     product = input()
#     if product == 'End':
#         break
#
#     products.append(product)
#
# while products:
#     curr_product = products.popleft()
#     current_time = current_time + timedelta(seconds=1)
#
#     for robot_name in busy_robots.copy():
#         busy_robots[robot_name] = max(busy_robots[robot_name] - 1, 0)
#         if robot_name not in available_robots and busy_robots[robot_name] == 0:
#             available_robots.append(robot_name)
#
#     if available_robots:
#         available_robot = available_robots.popleft()
#         print(f'{available_robot} - {curr_product} [{current_time.strftime("%H:%M:%S")}]')
#         busy_robots[available_robot] = robots_data[available_robot]
#
#     else:
#         products.append(curr_product)
