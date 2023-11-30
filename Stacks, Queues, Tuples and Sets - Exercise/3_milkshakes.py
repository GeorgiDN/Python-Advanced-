from collections import deque

chocolate = list(map(int, input().split(", ")))
milk_cups = deque(map(int, input().split(", ")))
prepared_milkshakes = 0

while True:
    if len(chocolate) == 0 or len(milk_cups) == 0 or prepared_milkshakes == 5:
        break
    current_chocolate = chocolate.pop()
    current_milk = milk_cups.popleft()
    if current_chocolate <= 0 and current_milk <= 0:
        continue
    if current_chocolate <= 0:
        milk_cups.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolate.append(current_chocolate)
        continue
    if current_chocolate == current_milk:
        prepared_milkshakes += 1
    else:
        milk_cups.append(current_milk)
        chocolate.append(current_chocolate - 5)

if prepared_milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(ch) for ch in chocolate])}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join([str(cup) for cup in milk_cups])}")
else:
    print("Milk: empty")
  
