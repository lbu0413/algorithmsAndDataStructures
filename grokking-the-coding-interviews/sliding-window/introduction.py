

# Given an array, find the average of all subarrays of 'K' contiguous elements in it
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

# O(N*K) solution, not efficient


def find_averages(k, arr):
    result = []
    for i in range(len(arr)-k+1):
        _sum = 0
        for j in range(i, i+k):
            _sum += arr[j]
        result.append(_sum/k)
    return result


print(find_averages(k, arr))

# using sliding_windows solution


def using_sliding_windows(k, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result


print(using_sliding_windows(k, arr))
