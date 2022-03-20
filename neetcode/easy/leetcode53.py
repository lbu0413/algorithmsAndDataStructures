def maxSubArray(nums):
    maxSub = nums[0]
    curSum = 0

    for i in nums:
        if curSum < 0:
            curSum = i
        else:
            curSum += i

        maxSub = max(maxSub, curSum)
    return maxSub


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
