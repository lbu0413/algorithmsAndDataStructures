def selectionsort2(nums):
    for idx in range(len(nums)):
        minNum = nums[idx]
        minIdx = idx
        for i in range(idx, len(nums)):
            if nums[i] < minNum:
                minNum = nums[i]
                minIdx = i
        nums[idx], nums[minIdx] = nums[minIdx], nums[idx]
    return nums


print(selectionsort2(nums=[5, 2, 7, 6, 1, 9]))
