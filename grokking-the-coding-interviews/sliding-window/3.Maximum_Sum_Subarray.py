# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

arr = [2, 1, 5, 1, 3, 2]
k = 3

# bruteforce solution O(N*K) solution


def max_sub_array(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr)-k+1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum


print(max_sub_array(k, arr))

# sliding window O(N) solution


def sliding_window(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


print(sliding_window(k, arr))
