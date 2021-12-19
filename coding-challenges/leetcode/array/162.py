def findPeak(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left+right)//2
        midNext = mid + 1
        if nums[mid] < nums[midNext]:
            left = mid + 1
        else:
            right = mid

    return left


nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeak(nums))
