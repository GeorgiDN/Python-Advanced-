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






# chocolate = list(int(el) for el in input().split(", "))
# cups_of_milk = list(int(el) for el in input().split(", "))


# milk_shakes = 0
# for num1 in reversed(chocolate):
#     if milk_shakes == 5:
#         break
#     for num2 in cups_of_milk:
#         if num1 == num2:
#             chocolate.pop()
#             cups_of_milk.remove(num2)
#             milk_shakes += 1
#             break

#         elif num1 <= 0:
#             chocolate.remove(num1)
#             break
#         elif num2 <= 0:
#             cups_of_milk.remove(num2)
#             break

#         elif num1 != num2:
#             element_to_move = num2
#             cups_of_milk.remove(element_to_move)
#             cups_of_milk.append(element_to_move)
#             index = chocolate.index(num1)
#             chocolate[index] -= 5
#             break

# if milk_shakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# elif milk_shakes < 5:
#     print("Not enough milkshakes.")

# if chocolate:
#     print(f"Chocolate: {', '.join(map(str, chocolate))}")
# else:
#     print("Chocolate: empty")

# if cups_of_milk:
#     print(f"Milk: {', '.join(map(str, cups_of_milk))}")
# else:
#     print("Milk: empty")
  
