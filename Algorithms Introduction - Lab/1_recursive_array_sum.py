def calculate_sum(nums, index):
    if index == len(nums) - 1:
        return nums[index]
    return nums[index] + calculate_sum(nums, index + 1)


list_numbers = [int(x) for x in input().split()]
print(calculate_sum(list_numbers, 0))



#####################################################
# def calculate_sum(array):
#     if len(array) == 1:
#         return array[0]

#     return array[0] + calculate_sum(array[1:])


# list_numbers = [int(x) for x in input().split()]
# print(calculate_sum(list_numbers))

