nums = input().split("|")
# joined_lists = [pair.strip() for pair in reversed(nums)]
joined_lists = [pair for pair in reversed(nums)]
flattened_list = [num for sublist in joined_lists for num in sublist.split()]
result = list(map(int, flattened_list))
print(*result)
