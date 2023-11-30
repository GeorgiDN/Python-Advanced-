from collections import deque


def calculate_honey(matched_bee, matched_nectar, operator):
    if matched_nectar > 0:
        return eval(f"{matched_bee}{operator}{matched_nectar}")
    return 0


bees = deque(map(int, input().split()))
nectar_values = list(map(int, input().split()))
symbols = deque(input().split())
total_honey = 0

while bees and nectar_values:
    bee = bees.popleft()
    nectar = nectar_values.pop()
    if nectar >= bee:
        symbol = symbols.popleft()
        total_honey += abs(calculate_honey(bee, nectar, symbol))
    else:
        bees.appendleft(bee)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
if nectar_values:
    print(f"Nectar left: {', '.join([str(n) for n in nectar_values])}")
  
