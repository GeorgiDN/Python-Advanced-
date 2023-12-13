def even_odd(*args):
    *numbers, command = args
    result = []

    if command == "odd":
        [result.append(x) for x in numbers if x % 2 != 0]

    elif command == "even":
        [result.append(x) for x in numbers if x % 2 == 0]

    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
