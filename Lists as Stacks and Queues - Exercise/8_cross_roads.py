from collections import deque

green_light_time = int(input())
free_window = int(input())
cars_on_crossroad = deque()

passed_cars = 0
crash_happened = False

while True:
    info = input()
    if info == "END" or crash_happened:
        break

    if info == "green":
        current_green_time = green_light_time
        current_free_window = free_window

        while cars_on_crossroad and not crash_happened and current_green_time > 0:
            current_car = cars_on_crossroad.popleft()
            for char in current_car:
                if current_green_time > 0:
                    current_green_time -= 1
                else:
                    if current_free_window > 0:
                        current_free_window -= 1
                    else:
                        crash_happened = True
                        print("A crash happened!")
                        print(f"{current_car} was hit at {char}.")
                        break
            if not crash_happened:
                passed_cars += 1
    else:
        car = info
        cars_on_crossroad.append(car)

if not crash_happened:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")




# from collections import deque

# green_light = int(input())
# free_window = int(input())
# time_to_enter = green_light
# passed_time = 0

# cars = deque()
# passed_cars = 0
# crash = False

# while True:
#     command = input()
#     if command == "END":
#         print("Everyone is safe.")
#         print(f"{passed_cars} total cars passed the crossroads.")
#         break
#     elif command == "green":
#         while cars:
#             if time_to_enter <= 0:
#                 break
#             current_car = cars.popleft()
#             car_size = len(current_car)
#             available_time = time_to_enter + free_window
#             if car_size <= available_time:
#                 passed_cars += 1
#                 time_to_enter -= len(current_car)
#             else:
#                 crash = True
#                 print("A crash happened!")
#                 print(f"{current_car} was hit at {current_car[available_time]}.")
#                 break
#         time_to_enter = green_light
#     else:
#         cars.append(command)
#     if crash:
#         break
        
