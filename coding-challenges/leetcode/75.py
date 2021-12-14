

def sortColors(nums):
    i0 = 0
    i1 = 0
    i2 = len(nums)-1

    while i1 <= i2:
        if nums[i1] == 0:
            nums[i0], nums[i1] = nums[i1], nums[i0]
            i0 += 1
            i1 += 1
        elif nums[i1] == 2:
            nums[i1], nums[i2] = nums[i2], nums[i1]
            i2 -= 1
        else:
            i1 += 1

    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
