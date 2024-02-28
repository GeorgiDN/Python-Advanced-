from collections import deque


def time_to_seconds(time):
    hours, minutes, seconds = list(map(int, time.split(":")))
    return hours * 60 * 60 + minutes * 60 + seconds


def formatted_time(seconds):
    hours = seconds // (60 * 60) % 24
    minutes = (seconds % (60 * 60)) // 60
    seconds = (seconds % (60 * 60)) % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots_info = input().split(";")
robots = []

for item in robots_info:
    name, process_time = item.split("-")
    robots.append([name, int(process_time), int(process_time), "free"])

time = input()
time_in_seconds = time_to_seconds(time)
products_queue = deque()
while True:
    product = input()
    if product == "End":
        break
    products_queue.append(product)

while products_queue:
    time_in_seconds += 1
    current_product = products_queue.popleft()
    for robot in robots:
        robot_name = robot[0]
        status = robot[3]
        if status == "free":
            robot[3] = "busy"
            print(f"{robot_name} - {current_product} [{formatted_time(time_in_seconds)}]")
            break
    else:
        products_queue.append(current_product)
    for robot in robots:
        if robot[3] == "busy":
            robot[2] -= 1
        if robot[2] <= 0:
            robot[3] = "free"
            robot[2] = robot[1]



# from collections import deque
# from datetime import datetime, timedelta

# data = input().split(";")
# time = datetime.strptime(input(), "%H:%M:%S")
# robots = []
# available_robots = deque()
# products = deque()

# for element in data:
#     robot_data = element.split("-")
#     robot = {}
#     robot["name"] = robot_data[0]
#     robot["speed"] = int(robot_data[1])
#     robot["available"] = time
#     robots.append(robot)
#     available_robots.append(robot)

# while True:
#     product = input()
#     if product == "End":
#         break
#     products.append(product)

# time += timedelta(seconds=1)

# while products:
#     current_product = products.popleft()
#     if available_robots:
#         current_robot = available_robots.popleft()
#         current_robot["available"] = time+timedelta(seconds=current_robot["speed"])
#         print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
#     else:
#         for rob in robots:
#             if time >= rob["available"]:
#                 available_robots.append(rob)
#         if not available_robots:
#             products.append(current_product)
#         else:
#             current_robot = available_robots.popleft()
#             current_robot["available"] = time+timedelta(seconds=current_robot["speed"])
#             print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
#     time += timedelta(seconds=1)
