def calculate_sum(nums, index):
    if index == len(nums) - 1:
        return nums[index]
    return nums[index] + calculate_sum(nums, index + 1)


list_numbers = [int(x) for x in input().split()]
print(calculate_sum(list_numbers, 0))
