def fill_the_box(*args):
    height, length, width, *rest = args
    cubes = []
    for value in rest:
        if value != "Finish":
            cubes.append(value)
        else:
            break
    box_volume = height * length * width
    while cubes:
        if cubes[0] <= box_volume:
            box_volume -= cubes.pop(0)
        else:
            cubes[0] -= box_volume
            break
    if cubes:
        return f"No more free space! You have {sum(cubes)} more cubes."
    return f"There is free space in the box. You could put {box_volume} more cubes."

# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
