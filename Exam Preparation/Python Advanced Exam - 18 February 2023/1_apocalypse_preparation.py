from collections import deque

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

healing_items = {30: "Patch", 40: "Bandage", 100: "MedKit"}
produced_healing_items = {}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    total_sum = textile + medicament
    if total_sum in healing_items:
        item = healing_items[total_sum]
        if item not in produced_healing_items:
            produced_healing_items[item] = 0
        produced_healing_items[item] += 1

    elif total_sum > 100:
        if "MedKit" not in produced_healing_items:
            produced_healing_items["MedKit"] = 0
        produced_healing_items["MedKit"] += 1
        total_sum -= 100
        medicaments[-1] += total_sum

    else:
        medicament += 10
        medicaments.append(medicament)

if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

if produced_healing_items:
    sorted_healing_items = dict(sorted(produced_healing_items.items(), key=lambda x: (-x[1], x[0])))

    for produced_item, quantity in sorted_healing_items.items():
        print(f"{produced_item} - {quantity}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, medicaments[::-1]))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
