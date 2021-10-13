import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

nums.sort()
for i in range(m):
    print(nums)
    nums[0] += 1
    nums[-1] -= 1
    nums.sort()

print(nums[-1] - nums[0])
