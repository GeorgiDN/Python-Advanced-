def set_cover(universe, sets):
    chosen_set = []

    while universe:
        best_set = max(sets, key=lambda s: len(universe.intersection(s)))
        chosen_set.append(best_set)
        universe -= best_set

    return chosen_set


universe = set(map(int, input().split(', ')))
num_of_sets = int(input())
sets = [{int(x) for x in input().split(', ')} for _ in range(num_of_sets)]

result = set_cover(universe, sets)

for i in range(len(result)):
    result[i] = sorted(result[i])

print(f"Sets to take ({len(result)}):")
[print("{ " + f"{', '.join(map(str, s))}" + " }") for s in result]
