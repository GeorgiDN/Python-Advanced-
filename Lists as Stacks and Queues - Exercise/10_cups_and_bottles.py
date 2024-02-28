from collections import deque

cups = deque(map(int, input().split(" ")))
bottles = list(map(int, input().split(" ")))
wasted_liters_of_water = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()
    if bottle >= cup:
        bottle -= cup
        wasted_liters_of_water += bottle
    else:
        cup -= bottle
        cups.insert(0, cup)

if bottles:
    print(f"Bottles: {' '.join(map(str, bottles))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")
print(f"Wasted litters of water: {wasted_liters_of_water}")




# from collections import deque

# cups = deque(list(map(int, input().split())))
# bottles = list(map(int, input().split()))
# wasted_water = 0

# while True:
#     if not cups or not bottles:
#         break
#     cup = cups[0]
#     bottle = bottles.pop()
#     if cup - bottle <= 0:
#         cups.popleft()
#         wasted_water += abs(cup - bottle)
#     else:
#         cups[0] -= bottle

# if cups:
#     cups_list = [str(i) for i in cups]
#     print(f"Cups: {' '.join(cups_list)}")
# else:
#     bottles_list = [str(i) for i in bottles]
#     print(f"Bottles: {' '.join(bottles_list)}")
# print(f"Wasted litters of water: {wasted_water}")
