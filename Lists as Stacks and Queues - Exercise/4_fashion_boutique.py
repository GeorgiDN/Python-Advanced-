clothes_list = list(map(int, input().split()))
capacity = int(input())
racks, total_sum = 1, 0

while clothes_list:
    item = clothes_list.pop()
    if total_sum + item <= capacity:
        total_sum += item
    else:
        racks += 1
        total_sum = 0
        clothes_list.append(item)

print(racks)



# from collections import deque


# clothes = deque(map(int, input().split(" ")))
# max_capacity = int(input())
# number_of_racks = 1

# total_sum_clothes = 0
# while clothes:
#     number_of_clothes = clothes.popleft()
#     total_sum_clothes += number_of_clothes
#     if total_sum_clothes > max_capacity:
#         clothes.insert(0, number_of_clothes)
#         number_of_racks += 1
#         total_sum_clothes = 0

# print(number_of_racks)



# from _collections import deque

# clothes = deque(int(el) for el in input().split(" "))
# capacity = int(input())
# total_sum = capacity
# num_racks = 1

# while clothes:
#     curr_sum_clothes = clothes[-1]

#     if curr_sum_clothes <= total_sum:
#         clothes.pop()
#         total_sum -= curr_sum_clothes
#     else:
#         num_racks += 1
#         total_sum = capacity

# print(num_racks)
