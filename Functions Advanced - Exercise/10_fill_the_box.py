def fill_the_box(*args):
    height, length, width = args[0], args[1], args[2]
    box_volume = height * length * width
    finished_index = args.index("Finish")
    filled_box = sum(args[3:finished_index])
    cubes = abs(box_volume - filled_box)
    if box_volume >= filled_box:
        return f"There is free space in the box. You could put {cubes} more cubes."
    return f"No more free space! You have {cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))





# def fill_the_box(*args):
#     height, length, width, *rest = args
#     cubes = []
#     for value in rest:
#         if value != "Finish":
#             cubes.append(value)
#         else:
#             break
#     box_volume = height * length * width
#     while cubes:
#         if cubes[0] <= box_volume:
#             box_volume -= cubes.pop(0)
#         else:
#             cubes[0] -= box_volume
#             break
#     if cubes:
#         return f"No more free space! You have {sum(cubes)} more cubes."
#     return f"There is free space in the box. You could put {box_volume} more cubes."

# # print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
