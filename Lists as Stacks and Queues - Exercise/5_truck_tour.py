from collections import deque

pumps_quantity = int(input())
pumps_info = deque()

for _ in range(pumps_quantity):
    pumps = [int(el) for el in input().split(" ")]
    pumps_info.append(pumps)

for pump in range(pumps_quantity):
    tank = 0
    is_ok_condition = True
    for p in range(pumps_quantity):
        tank += pumps_info[p][0] - pumps_info[p][1]
        if tank < 0:
            is_ok_condition = False
            pumps_info.append(pumps_info.popleft())
            break

    if is_ok_condition:
        print(f"{pump}")
        break
