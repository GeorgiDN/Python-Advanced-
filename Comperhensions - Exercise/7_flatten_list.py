def take_input():
    return input().split("|")


def reversed_nums(nums):
    return [pair for pair in reversed(nums)]


def ordered_nums(rev_nums):
    return [num for sublist in rev_nums for num in sublist.split()]


def print_result(lst):
    return print(*list(map(int, lst)))


numbers = take_input()
numbers_in_reversed = reversed_nums(numbers)
numbers_ordered = ordered_nums(numbers_in_reversed)
print_result(numbers_ordered)







# nums = input().split("|")
# # joined_lists = [pair.strip() for pair in reversed(nums)]
# joined_lists = [pair for pair in reversed(nums)]
# flattened_list = [num for sublist in joined_lists for num in sublist.split()]
# result = list(map(int, flattened_list))
# print(*result)
