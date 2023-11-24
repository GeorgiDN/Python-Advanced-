from collections import deque

green_light = int(input())
free_window = int(input())
time_to_enter = green_light
passed_time = 0

cars = deque()
passed_cars = 0
crash = False

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{passed_cars} total cars passed the crossroads.")
        break
    elif command == "green":
        while cars:
            if time_to_enter <= 0:
                break
            current_car = cars.popleft()
            car_size = len(current_car)
            available_time = time_to_enter + free_window
            if car_size <= available_time:
                passed_cars += 1
                time_to_enter -= len(current_car)
            else:
                crash = True
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[available_time]}.")
                break
        time_to_enter = green_light
    else:
        cars.append(command)
    if crash:
        break
