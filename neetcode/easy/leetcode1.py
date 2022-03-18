
def twoSum(nums, target):
    hsh = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hsh:
            return [hsh[diff], i]
        hsh[n] = i


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
