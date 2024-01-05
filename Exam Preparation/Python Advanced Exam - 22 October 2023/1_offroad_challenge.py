from collections import deque
initial_fuel = list(map(int, input().split(' ')))
consumption = deque(map(int, input().split(" ")))
fuel_needed = deque(map(int, input().split(" ")))
fail = False

altitude = 0
lst_altitudes = []

while initial_fuel and consumption:
    curr_fuel = initial_fuel.pop()
    curr_consumption = consumption.popleft()
    fuel_altitude = fuel_needed.popleft()
    result = curr_fuel - curr_consumption

    if result < fuel_altitude:
        print(f"John did not reach: Altitude {altitude + 1}")
        fail = True
        break
    altitude += 1
    lst_altitudes.append(f"Altitude {altitude}")
    print(f"John has reached: Altitude {altitude}")

if fail:
    print("John failed to reach the top.")
    if lst_altitudes:
        print("Reached altitudes: " + ', '.join(lst_altitudes))
    else:
        print("John didn't reach any altitude.")
elif not fail:
    print("John has reached all the altitudes and managed to reach the top!")
