def best_list_pureness(*args):
    my_list, rotate_times = args[0], int(args[1])
    max_sum = 0
    rotation = 0
    for i, num in enumerate(my_list):
        max_sum += (i * num)

    for turn in range(1, rotate_times + 1):
        current_sum = 0
        my_list.insert(0, my_list.pop())
        for idx, num in enumerate(my_list):
            current_sum += (idx * num)
        if current_sum > max_sum:
            max_sum = current_sum
            rotation = turn

    result = f"Best pureness {max_sum} after {rotation} rotations"
    return result


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
