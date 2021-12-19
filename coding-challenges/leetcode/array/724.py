def pivotIndex(nums):
    left = 0
    right = sum(nums)

    for i in range(len(nums)):
        num = nums[i]
        right -= num

        if left == right:
            return i
        left += num
    else:
        return -1


# nums = [1, 7, 3, 6, 5, 6]
# nums = [2, 1, -1]
nums = [1, 2, 3]

print(pivotIndex(nums))
