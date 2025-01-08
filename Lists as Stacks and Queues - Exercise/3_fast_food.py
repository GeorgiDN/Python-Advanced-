from collections import deque

food = int(input())
orders = deque(map(int, input().split()))
max_order = max(orders)

while orders:
    order = orders.popleft()
    if order <= food:
        food -= order
    else:
        orders.appendleft(order)
        break

print(max_order)
print('Orders complete') if not orders else print(f'Orders left: {" ".join(map(str, orders))}')



# from collections import deque

# total_sum = int(input())
# orders = deque(map(int, input().split(" ")))
# print(max(orders))

# for _ in range(len(orders)):
#     current_order = orders.popleft()
#     if current_order <= total_sum:
#         total_sum -= current_order
#     else:
#         orders.insert(0, current_order)

# if orders:
#     print(f"Orders left: {' '.join(map(str, orders))}")
# else:
#     print("Orders complete")

