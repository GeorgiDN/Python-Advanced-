from collections import deque

working_bees = deque(map(int, input().split()))
nectars = list(map(int, input().split()))
symbols = deque(input().split())
total_honey = 0

while working_bees and nectars:
    bee = working_bees.popleft()
    nectar = nectars.pop()

    if bee > nectar:
        working_bees.appendleft(bee)

    elif bee <= nectar:
        curr_symbol = symbols.popleft()
        if curr_symbol == "/" and nectar == 0:
            continue

        else:
            expression = f"{bee} {curr_symbol} {nectar}"
            result = abs(eval(expression))
            total_honey += result

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if nectars:
    print(f"Nectar left: {', '.join(map(str, nectars))}")





# from collections import deque


# def calculate_honey(matched_bee, matched_nectar, operator):
#     if matched_nectar > 0:
#         return eval(f"{matched_bee}{operator}{matched_nectar}")
#     return 0


# bees = deque(map(int, input().split()))
# nectar_values = list(map(int, input().split()))
# symbols = deque(input().split())
# total_honey = 0

# while bees and nectar_values:
#     bee = bees.popleft()
#     nectar = nectar_values.pop()
#     if nectar >= bee:
#         symbol = symbols.popleft()
#         total_honey += abs(calculate_honey(bee, nectar, symbol))
#     else:
#         bees.appendleft(bee)

# print(f"Total honey made: {total_honey}")
# if bees:
#     print(f"Bees left: {', '.join([str(b) for b in bees])}")
# if nectar_values:
#     print(f"Nectar left: {', '.join([str(n) for n in nectar_values])}")
  
