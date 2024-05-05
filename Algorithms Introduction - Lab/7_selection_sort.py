def selection_sor(nums):
    for idx in range(len(nums)):
        min_idx = idx

        for curr_idx in range(idx + 1, len(nums)):
            if nums[curr_idx] < nums[min_idx]:
                min_idx = curr_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]


nums = list(map(int, input().split()))
selection_sor(nums)
print(*nums)