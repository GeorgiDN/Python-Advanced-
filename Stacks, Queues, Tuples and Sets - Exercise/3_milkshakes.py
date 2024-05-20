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



# from collections import deque


# def process_chocolate_and_milk(choc, milk, chocs, milks):
#     conditions = {
#         (True, True): lambda: None,  # both are <= 0
#         (True, False): lambda: milks.appendleft(milk),  # chocolate <= 0
#         (False, True): lambda: chocs.append(choc),  # milk <= 0
#         (False, False): lambda: None,  # neither are <= 0
#     }
#     conditions[(choc <= 0, milk <= 0)]()


# def make_milkshake(choc, milk, chocs, milks, shakes):
#     if choc == milk:
#         shakes += 1
#     else:
#         milks.append(milk)
#         choc -= 5
#         chocs.append(choc)
#     return shakes


# chocs = [int(x) for x in input().split(", ")]
# milks = deque([int(x) for x in input().split(", ")])

# shakes = 0

# while milks and chocs:
#     if shakes == 5:
#         break
#     choc = chocs.pop()
#     milk = milks.popleft()

#     if choc <= 0 or milk <= 0:
#         process_chocolate_and_milk(choc, milk, chocs, milks)
#         continue

#     shakes = make_milkshake(choc, milk, chocs, milks, shakes)

# print("Great! You made all the chocolate milkshakes needed!") if shakes == 5 else print("Not enough milkshakes.")
# print(f"Chocolate: {', '.join([str(x) for x in chocs])}") if chocs else print("Chocolate: empty")
# print(f"Milk: {', '.join([str(x) for x in milks])}") if milks else print("Milk: empty")


    
