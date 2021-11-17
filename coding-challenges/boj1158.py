import sys

n, k = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]
result = []


cnt = 0
for i in range(n):
    cnt += k - 1
    if cnt >= len(nums):
        cnt = cnt % len(nums)
    result.append(str(nums.pop(cnt)))

print(f"<{', '.join(result)}>")
