from collections import deque


def add_the_present(crafted_presents, magic_level_required, level):
    current_present = magic_level_required[level]
    if current_present not in crafted_presents:
        crafted_presents[current_present] = 0
    crafted_presents[current_present] += 1

    return crafted_presents


def print_result(crafted_presents, materials, magic_levels):
    if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) \
            or ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")

    if materials:
        materials = materials[::-1]
        print(f"Materials left: {', '.join(map(str, materials))}")

    if magic_levels:
        print(f"Magic left: {', '.join(map(str, magic_levels))}")

    sorted_crafted_presents = dict(sorted(crafted_presents.items()))

    for current_material, count in sorted_crafted_presents.items():
        print(f"{current_material}: {count}")


materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

magic_level_required = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    level = material * magic

    if level in magic_level_required:
        crafted_presents = add_the_present(crafted_presents, magic_level_required, level)

    else:
        if level < 0:
            materials.append(material + magic)
        elif level > 0:
            material += 15
            materials.append(material)

        else:
            if magic == 0 and material == 0:
                continue
            elif magic == 0:
                materials.append(material)
            else:
                magic_levels.appendleft(magic)

print_result(crafted_presents, materials, magic_levels)





####################################################################
# from collections import deque
# 
# materials = list(map(int, input().split()))
# magic_levels = deque(map(int, input().split()))
# 
# magic_level_required = {
#     "Doll": 150,
#     "Wooden train": 250,
#     "Teddy bear": 300,
#     "Bicycle": 400
# }
# 
# crafted_presents = {}
# 
# while materials and magic_levels:
#     material = materials.pop()
#     magic = magic_levels.popleft()
# 
#     if material == 0 and magic == 0:
#         continue
# 
#     if material == 0:
#         magic_levels.appendleft(magic)
#         continue
# 
#     if magic == 0:
#         materials.append(material)
#         continue
# 
#     level = material * magic
# 
#     if level in magic_level_required.values():
#         found_present = [key for key, value in magic_level_required.items() if value == level]
#         curr_present = found_present[0]
#         if curr_present not in crafted_presents:
#             crafted_presents[curr_present] = 0
#         crafted_presents[curr_present] += 1
# 
#     elif level < 0:
#         level = material + magic
#         materials.append(level)
# 
#     else:
#         material += 15
#         materials.append(material)
# 
# if "Doll" in crafted_presents and "Wooden train" in crafted_presents:
#     task_is_done = True
# elif "Teddy bear" in crafted_presents and "Bicycle" in crafted_presents:
#     task_is_done = True
# else:
#     task_is_done = False
# 
# if task_is_done:
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
# 
# if materials:
#     materials = materials[::-1]
#     print(f"Materials left: {', '.join(map(str, materials))}")
# 
# if magic_levels:
#     print(f"Magic left: {', '.join(map(str, magic_levels))}")
# 
# sorted_crafted_presents = dict(sorted(crafted_presents.items()))
# 
# for current_material, count in sorted_crafted_presents.items():
#     print(f"{current_material}: {count}")
