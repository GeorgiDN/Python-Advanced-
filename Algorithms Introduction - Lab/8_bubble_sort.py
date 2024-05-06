def bubble_sort(nums):
    is_sorted = False
    i = 0

    while not is_sorted:
        is_sorted = True

        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                is_sorted = False

        i += 1


nums = list(map(int, input().split()))
bubble_sort(nums)
print(*nums)




# # MEASURE TIME
# import time
#

# def bubble_sort(nums):
#     is_sorted = False
#     i = 0
#
#     while not is_sorted:
#         is_sorted = True
#
#         for j in range(1, len(nums) - i):
#             if nums[j - 1] > nums[j]:
#                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
#                 is_sorted = False
#
#         i += 1
#
#
# nums = list(map(int, input().split()))
#
# start_time = time.time()
#
# bubble_sort(nums)
# print(*nums)
#
# # Calculate and print execution time
# end_time = time.time()
# execution_time = end_time - start_time
# print("Execution time:", execution_time, "seconds")
