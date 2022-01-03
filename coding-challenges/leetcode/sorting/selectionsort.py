
def sort(nums):
    for idx in range(len(nums)):
        minNum = nums[idx]
        minIdx = idx
        for i in range(idx, len(nums)):
            if nums[i] < minNum:
                minNum = nums[i]
                minIdx = i
        nums[idx], nums[minIdx] = nums[minIdx], nums[idx]
    return nums


print(sort(nums=[9, 3, 5, 7, 1]))
