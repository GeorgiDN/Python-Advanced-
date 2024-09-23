from collections import deque

caffeine_milligrams = list(map(int, (input().split(","))))
energy_drinks = deque(map(int, (input().split(","))))
max_caffeine_per_night, total_caffeine = 300, 0

while energy_drinks and caffeine_milligrams:
    caffeine = caffeine_milligrams.pop()
    drink = energy_drinks.popleft()

    if total_caffeine + (caffeine * drink) <= max_caffeine_per_night:
        total_caffeine += (caffeine * drink)
    else:
        energy_drinks.append(drink)
        total_caffeine = max(0, total_caffeine - 30)

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
