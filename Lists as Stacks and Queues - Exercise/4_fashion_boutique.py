from _collections import deque

clothes = deque(int(el) for el in input().split(" "))
capacity = int(input())
total_sum = capacity
num_racks = 1

while clothes:
    curr_sum_clothes = clothes[-1]

    if curr_sum_clothes <= total_sum:
        clothes.pop()
        total_sum -= curr_sum_clothes
    else:
        num_racks += 1
        total_sum = capacity

print(num_racks)
