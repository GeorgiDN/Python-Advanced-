from collections import deque

chocolates = list(map(int, input().split(", ")))
cups_of_milks = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolates and cups_of_milks:
    if milkshakes == 5:
        break
    chocolate = chocolates.pop()
    milk = cups_of_milks.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    if chocolate <= 0:
        cups_of_milks.appendleft(milk)
        continue

    if milk <= 0:
        chocolates.append(chocolate)
        continue

    elif chocolate != milk:
        cups_of_milks.append(milk)
        chocolate -= 5
        chocolates.append(chocolate)

    else:
        milkshakes += 1


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_of_milks:
    print(f"Milk: {', '.join(map(str, cups_of_milks))}")
else:
    print("Milk: empty")
    
