

def merge(nums1, m, nums2, n):
    idx1 = m-1
    idx2 = n-1
    idx = len(nums1)-1

    while 0 <= idx1 and 0 <= idx2:
        if nums1[idx1] >= nums2[idx2]:
            nums1[idx] = nums1[idx1]
            idx -= 1
            idx1 -= 1
        else:
            nums1[idx] = nums2[idx2]
            idx -= 1
            idx2 -= 1

    while 0 <= idx1:
        nums1[idx] = nums1[idx1]
        idx -= 1
        idx1 -= 1

    while 0 <= idx2:
        nums1[idx] = nums2[idx2]
        idx -= 1
        idx2 -= 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))
