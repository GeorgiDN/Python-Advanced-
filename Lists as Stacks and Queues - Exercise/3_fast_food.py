from _collections import deque

food_quantity = int(input())
orders = list(map(int, input().split(' ')))
orders_deque = deque(orders)
biggest_order = max(orders_deque)

# while len(orders_deque) > 1:
for _ in range(len(orders_deque)):
    if food_quantity <= 0:
        break
    current_order = orders_deque[0]

    if current_order <= food_quantity:
        food_quantity -= current_order
        orders_deque.popleft()
    else:
        pass


print(biggest_order)

if len(orders_deque) > 0:
    remaining_orders = " ".join(map(str, orders_deque))
    print(f"Orders left: {remaining_orders}")

else:
    print("Orders complete")
  
