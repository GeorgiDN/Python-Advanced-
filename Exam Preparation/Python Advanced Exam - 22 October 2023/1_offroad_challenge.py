# https://judge.softuni.org/Contests/Practice/Index/4193#0
from collections import deque
fuels = list(map(int, input().split(' ')))
consumptions = deque(map(int, input().split(" ")))
fuel_needed = deque(map(int, input().split(" ")))
fail = False

altitude = 0
altitudes_list = []

while fuels and consumptions:
    fuel = fuels.pop()
    consumption = consumptions.popleft()
    fuel_altitude = fuel_needed.popleft()
    result = fuel - consumption

    if result < fuel_altitude:
        print(f"John did not reach: Altitude {altitude + 1}")
        fail = True
        break
    altitude += 1
    altitudes_list.append(f"Altitude {altitude}")
    print(f"John has reached: Altitude {altitude}")

if fail:
    print("John failed to reach the top.")
    print("Reached altitudes: " + ', '.join(altitudes_list)) if altitudes_list \
        else print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")
