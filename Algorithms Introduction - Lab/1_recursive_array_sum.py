def calculate_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calculate_sum(nums, idx + 1)


list_numbers = [int(x) for x in input().split()]
print(calculate_sum(list_numbers, 0))
