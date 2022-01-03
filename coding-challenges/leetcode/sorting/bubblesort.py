from typing import List


def sort(nums: List[int]) -> List[int]:
    for idx in range(0, len(nums)-1):
        for i in range(0, len(nums)-idx-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


print(sort(nums=[9, 3, 5, 7, 1]))
