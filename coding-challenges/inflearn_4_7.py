import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
nums.sort()

for i in range(m):
    nums[0] += 1
    nums[-1] -= 1
    nums.sort()

print(nums[-1] - nums[0])
