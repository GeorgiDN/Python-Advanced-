from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

magic_required = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
presents = {}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    level = material * magic
    if level in magic_required:
        current_present = magic_required[level]
        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1
    else:
        if level < 0:
            materials.append(material + magic)
        elif level > 0:
            materials.append(material + 15)
        else:
            if magic == 0 and material == 0:
                continue
            elif magic == 0:
                materials.append(material)
            else:
                magic_levels.appendleft(magic)

if ("Doll" in presents and "Wooden train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(m) for m in reversed(materials)])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(m) for m in magic_levels])}")
for present in sorted(presents.keys()):
    print(f"{present}: {presents[present]}")
