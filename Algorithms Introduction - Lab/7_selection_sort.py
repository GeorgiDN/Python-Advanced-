def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return ' '.join(map(str, arr))


arr = list(map(int, input().split()))
print(selection_sort(arr))


#############################################################
# def selection_sor(nums):
#     for idx in range(len(nums)):
#         min_idx = idx

#         for curr_idx in range(idx + 1, len(nums)):
#             if nums[curr_idx] < nums[min_idx]:
#                 min_idx = curr_idx

#         nums[idx], nums[min_idx] = nums[min_idx], nums[idx]


# nums = list(map(int, input().split()))
# selection_sor(nums)
# print(*nums)
