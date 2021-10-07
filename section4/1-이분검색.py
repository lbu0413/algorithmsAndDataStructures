import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

start = 0
end = len(numbers) - 1

while start <= end:
    mid = (start + end) // 2
    if numbers[mid] == m:
        print(mid + 1)
        break
    elif numbers[mid] > m:
        end = mid - 1
    else:
        start = mid + 1
