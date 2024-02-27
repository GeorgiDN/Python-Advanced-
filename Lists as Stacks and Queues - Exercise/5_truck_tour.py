from collections import deque

pumps_count = int(input())
pumps_data = deque()

for _ in range(pumps_count):
    pumps = [int(el) for el in input().split(" ")]
    pumps_data.append(pumps)

for pump in range(pumps_count):
    tank = 0
    circle_is_completed = True
    for p in range(pumps_count):
        tank += pumps_data[p][0] - pumps_data[p][1]
        if tank < 0:
            circle_is_completed = False
            pumps_data.append(pumps_data.popleft())
            break

    if circle_is_completed:
        print(f"{pump}")
        break
