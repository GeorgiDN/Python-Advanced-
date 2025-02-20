from collections import deque

potions_to_craft = {
    110: 'Brew of Immortality',
    100: 'Essence of Resilience',
    90: 'Draught of Wisdom',
    80: 'Potion of Agility',
    70: 'Elixir of Strength',
}

crafted_potions = []

substances_collection = list(map(int, input().split(', ')))
crystal_energy = deque(map(int, input().split(', ')))

while substances_collection and crystal_energy:
    if len(crafted_potions) == 5:
        break

    substances = substances_collection.pop()
    crystal = crystal_energy.popleft()

    total_sum = substances + crystal

    if total_sum in potions_to_craft:
        crafted_potions.append(potions_to_craft[total_sum])
        del potions_to_craft[total_sum]

    else:
        find_lower_sum = False
        for energy, p in potions_to_craft.items():
            if total_sum > energy:
                crafted_potions.append(p)
                del potions_to_craft[energy]
                find_lower_sum = True
                break

        if find_lower_sum:
            crystal -= 20
            if crystal > 0:
                crystal_energy.append(crystal)

        else:
            crystal -= 5
            if crystal > 0:
                crystal_energy.append(crystal)

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(map(str, crafted_potions))}")

if substances_collection:
    print(f"Substances: {', '.join(map(str, substances_collection[::-1]))}")

if crystal_energy:
    print(f"Crystals: {', '.join(map(str, crystal_energy))}")
