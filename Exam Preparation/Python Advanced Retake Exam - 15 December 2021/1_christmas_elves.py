from collections import deque

MIN_NEED_ENERGY = 5


def santa_workshop(elfs_energy_input, materials_input):
    elfs_energy = deque(int(x) for x in elfs_energy_input.split())
    materials = deque(int(x) for x in materials_input.split())

    total_energy = 0
    made_toys = 0
    counter = 0

    while elfs_energy and materials:
        curr_elf = elfs_energy.popleft()

        if curr_elf < MIN_NEED_ENERGY:
            continue

        counter += 1
        curr_material = materials.pop()

        if counter % 3 == 0 and counter % 5 == 0:
            required_energy = curr_material * 2
            toys_to_add = 0
        elif counter % 3 == 0:
            required_energy = curr_material * 2
            toys_to_add = 2
        elif counter % 5 == 0:
            required_energy = curr_material
            toys_to_add = 0
        else:
            required_energy = curr_material
            toys_to_add = 1

        if curr_elf >= required_energy:
            total_energy += required_energy
            curr_elf -= required_energy - (1 if toys_to_add > 0 and counter % 5 != 0 else 0)
            made_toys += toys_to_add
        else:
            curr_elf *= 2
            materials.appendleft(curr_material)

        elfs_energy.append(curr_elf)

    print(f"Toys: {made_toys}")
    print(f"Energy: {total_energy}")

    if elfs_energy:
        print(f"Elves left: {', '.join(map(str, elfs_energy))}")
    if materials:
        print(f"Boxes left: {', '.join(map(str, materials))}")


elfs_energy = input()
materials = input()
santa_workshop(elfs_energy, materials)
