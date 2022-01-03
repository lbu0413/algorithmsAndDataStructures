

def insertionSort(nums):
    for pIdx in range(1, len(nums)):
        tmp = nums[pIdx]
        idx = pIdx-1
        while 0 <= idx and tmp < nums[idx]:
            nums[idx+1] = nums[idx]
            idx = idx-1
        nums[idx+1] = tmp
    return nums


print(insertionSort(nums=[9, 3, 5, 7, 1]))
